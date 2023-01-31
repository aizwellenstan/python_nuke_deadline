"""
This script will submit current file to deadline for render
"""

import os
import sys
import subprocess
import os
import json

# https://docs.thinkboxsoftware.com/products/deadline/10.1/1_User%20Manual/manual/manual-submission.html
def job_info(info_txt):
    """
    this function will collect scene file information and write a job file
    :return:
    """
    job_info_file = r'{}\job_info.job'.format(os.getenv('TEMP'))
    with open(job_info_file, 'w') as job_file:
        job_file.write(info_txt)
    return job_info_file

def plugin_info(info_txt):
    """
    this function will collect maya deadline information and write a job file
    """
    plugin_info_file = r'{}\plugin_info.job'.format(os.getenv('TEMP'))
    with open(plugin_info_file, 'w') as job_file:
        job_file.write(info_txt)
    return plugin_info_file

def submit_to_deadline(job_info_txt, plugin_info_txt):
    # Change deadline exe root
    deadline_cmd = r"C:\Program Files\Thinkbox\Deadline10\bin\deadlinecommand.exe"
    job_file = job_info(job_info_txt)
    info_file = plugin_info(plugin_info_txt)
    command = '{deadline_cmd} "{job_file}" "{info_file}"'.format(**vars())
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    lines_iterator = iter(process.stdout.readline, b"")
    #  Lets print the output log to see the Error / Success 
    for line in lines_iterator:
        print(line)
        sys.stdout.flush()
        try:
            with open(f'D:\nuke_deadline_debug.txt', 'w') as f:
                print(line, file=f)
        except:
            pass

def GetInfoTxt(filePath, frames, chunkSize=1, excuteNodes="REN_EXR", pool="nuke", priority=50, machineLimit=30, initialStatus="Active"):
    import socket
    machinename = socket.gethostname()
    import os

    job_info_txt = f"""
    Frames={frames}
    MachineLimit={machineLimit}
    ChunkSize={chunkSize}
    Group=nuke_13
    Name={os.path.basename(filePath)}
    OverrideTaskExtraInfoNames=False
    Plugin=CommandLine
    Pool={pool}
    Priority={priority}
    SecondaryPool=all
    UserName={os.getlogin()}
    MachineName={machinename}
    InitialStatus={initialStatus}
    """

    plugin_info_txt = f"""
    Arguments= -t -x -X {excuteNodes} -- {filePath} <STARTFRAME>,<ENDFRAME>,1
    Executable={os.environ['NUKE_DEADLINE_EXCUTABLE']}
    Shell=default
    ShellExecute=False
    SingleFramesOnly=False
    StartupDirectory=
    """

    return str(job_info_txt.strip()), str(plugin_info_txt)
