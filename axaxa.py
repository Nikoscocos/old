import subprocess
from pexpect import popen_spawn


user = 'Nikoscocos'
password = 'fursiNik0819'

cmd = "cd C:\\Users\\User\\Desktop\\NikoBot\\NikoSite\\nikosite.github.io"
returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix

cmd = "git add ." 
subprocess.call(cmd, shell=True)

cmd = 'git commit -m "python project update"'
subprocess.call(cmd, shell=True)

cmd = "git remote set-url origin https://github.com/Nikoscocos/nikosite.github.io"
subprocess.call(cmd, shell=True)

cmd = "git push -u origin main"
subprocess.call(cmd, shell=True)

print('end of commands')