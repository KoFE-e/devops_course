import subprocess

def check_output():
    print('date and ls linux commands')
    print(subprocess.check_output('date && ls -la', text=True, shell=True))

check_output()
