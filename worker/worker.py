"""
Created on March 7 2019

@author: Melchior du Lac, Joan Hérisson
@description: RESTful version of RP2paths. Returns bytes of compressed results archive

"""
from tempfile import TemporaryDirectory
import logging
# import resource
# import glob

MAX_VIRTUAL_MEMORY = 20000 * 1024 * 1024 # 20GB -- define what is the best
#MAX_VIRTUAL_MEMORY = 20 * 1024 * 1024 # 20GB -- define what is the best

##
#
#
def limit_virtual_memory():
    resource.setrlimit(resource.RLIMIT_AS, (MAX_VIRTUAL_MEMORY, resource.RLIM_INFINITY))

from io import BytesIO as io_BytesIO
from tarfile import open as tarfile_open
def tar_cz_relative(*path):
    """tar_cz(*path) -> bytes
    Compress a sequence of files or directories in memory.
    The resulting string could be stored as a .tgz file."""
    file_out = io_BytesIO()
    tar = tarfile_open(mode = "w:gz", fileobj = file_out)
    for p in path:
        tar.add(p, arcname='./')
    tar.close()
    return file_out.getvalue()



def process_params(args, out_folder):

    # Process input files
    files = {}
    for key in args:
        if key.startswith("_file_"):
            # remove _file_
            files[key[6:]] = out_folder+'/'+key+'.csv'
            with open(files[key[6:]], 'wb') as outfi:
                outfi.write(args[key])

    tool_process_params = getattr(import_module("tool"), "process_params")
    return tool_process_params(args, files, out_folder)


from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.dirname(os_path.abspath(__file__)))
sys_path.append(os_path.dirname(os_path.abspath(__file__))+"/src")
from importlib import import_module
def run(args):
#    if logger==None:

    # if data['logger']==None:
    #     logging.basicConfig(level=logging.DEBUG)
    #     logger = logging.getLogger(__name__)

    with TemporaryDirectory() as tmpOutputFolder:

        params = process_params(args, tmpOutputFolder)

        tool_entrypoint = getattr(
            import_module("."+args['module'], "src"),
            "entrypoint"
            )
        tool_entrypoint(params)


        ### Return a compressed archive of result files ###
        try:

            result_bytes = tar_cz_relative(tmpOutputFolder)
            return result_bytes

        except FileNotFoundError as e:
            logger.error('Cannot find the output folder'+tmpOutputFolder)
            return b'', b'', b'filenotfounderror', str.encode('Command: '+str(rp2paths_command)+'\n Error: '+str(e)+'\n tmpOutputFolder: '+str(glob.glob(tmpOutputFolder+'/*')))

        except ValueError as e:
            logger.error('Cannot set the RAM usage limit')
            return b'', b'', b'valueerror', str.encode('Command: '+str(rp2paths_command)+'\n Error: '+str(e)+'\n tmpOutputFolder: '+str(glob.glob(tmpOutputFolder+'/*')))
