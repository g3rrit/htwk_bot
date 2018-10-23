import os
import sys
import git
import subprocess

'''
def restart_program():
   #Restarts the current program, with file objects and descriptors 

   try:
       p = psutil.Process(os.getpid())
       for handler in p.open_files() + p.connections():
           os.close(handler.fd)
   except Exception as e:
       logging.error(e)

   python = sys.executable
   os.execl(python, python, *sys.argv)
'''

def restart_program():
    g = git.Git(".")
    g.pull("origin", "master")

    os.execv(sys.executable, ["python3"] + sys.argv)


def install(package):
    try:
        subprocess.call(["python3",  "-m pip3", "install", package])
    except Exception as e:
        raise e
