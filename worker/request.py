#!/usr/bin/env python3

import os
import argparse
import io
import tarfile
import json
import requests
import logging



# Wrapper for the RP2paths script that takes the same input (results.csv) as the original script but returns
# the out_paths.csv so as to be compliant with Galaxy


def process_params(params):

    multipart_form_data = {}
    data = {}

    for key in params:
        if key.startswith("_file_"):
            multipart_form_data[key] = open(params[key], 'rb')
        else:
            data[key] = params[key]

    multipart_form_data['data'] = ('data.json', json.dumps(data))

    return multipart_form_data,data


def format_params_standalone(multipart_form_data, data):
    args = {}
    for key in multipart_form_data:
        if key.startswith("_file_"):
            args[key] = multipart_form_data[key].read()
    args.update(data)
    return args


def request(params):

    multipart_form_data,data = process_params(params)

    if(params['server_url']=="standalone"):

        args = format_params_standalone(multipart_form_data, data)
        from worker import run as rest_run
        result = rest_run(args)

    else:

        try:

            r = requests.post(params['server_url'], files=multipart_form_data)

        except requests.exceptions.HTTPError as err:
            logging.error(err)
            logging.error(r.text)
            return False

        if (r.status_code==400):
            logging.error(r.text)
            return False

        result = r.content

    return result

#
#
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser('Python wrapper for the python RP2paths script')
#     parser.add_argument('-_file_rp2_pathways', type=str)
#     parser.add_argument('-rp2paths_pathways', type=str)
#     parser.add_argument('-rp2paths_compounds', type=str)
#     parser.add_argument('-timeout', type=int)
#     parser.add_argument('-server_url', type=str)
#     parser.add_argument('-galaxy', type=str)
#     params = parser.parse_args()
#
#     if (params.timeout < 0):
#         logging.error('Time out cannot be less than 0: '+str(params.timeout))
#         exit(1)
#
#     request(vars(params))
