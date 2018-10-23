import os
import sys
import git

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


