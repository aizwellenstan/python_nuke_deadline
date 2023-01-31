## deadline python api

### main file api
python_api.py

pool setting
```python
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
```

### nuke-ui
deadline.py
