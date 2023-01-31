import sys
import nuke

def getPoolStr():
    sys.path.append(r'I:\script\bin\td\deadline\submit\python_api')
    import deadline_api
    from deadline_api import GetPools
    pool = ['nuke']
    pool2 = GetPools()
    for p in pool2:
        if p == "nuke": continue
        pool.append(p)
    poolString = ""
    for i in pool:
        poolString += " "+i
    return poolString

def DeadlineRenderSelected():
    sys.path.append(r'I:\script\bin\td\deadline\submit\nuke\modules')
    from nuke_deadline_v2 import GetInfoTxt, submit_to_deadline

    pool = getPoolStr()

    selectedNodes = []
    for i in nuke.selectedNodes("Write"):
        selectedNodes.append(i.name())
    selectedNodesStr = ""
    if len(selectedNodes) > 0:
        for i in selectedNodes:
            selectedNodesStr += i + ","
        selectedNodesStr = selectedNodesStr[:len(selectedNodesStr)-1]
    else:
        selectedNodesStr = "REN_EXR"

    p = nuke.Panel('Submit to Deadline')
    p.addEnumerationPulldown('pool', pool)
    p.addSingleLineInput('FrameRange', str(int(nuke.root()['first_frame'].value()))+'-'+str(int(nuke.root()['last_frame'].value())))
    p.addSingleLineInput('ChunkSize', "1")
    p.addSingleLineInput('ExcuteNodes', selectedNodesStr)
    p.addSingleLineInput('priority', "50")
    p.addSingleLineInput('machineLimit', "40")
    p.addBooleanCheckBox('suspend', False)
    ret = p.show()
    
    if not ret: return

    frames = p.value('FrameRange')
    root_name = nuke.Root().name()
    chunkSize = p.value('ChunkSize')
    excuteNodes = p.value('ExcuteNodes')
    pool = p.value('pool')
    priority = p.value('priority')
    machineLimit = p.value('machineLimit')
    initialStatus = 'Active'
    if p.value('suspend'):
        initialStatus = 'Suspended'

    job_info_txt, plugin_info_txt = GetInfoTxt(root_name, frames, chunkSize, excuteNodes, pool, priority, machineLimit, initialStatus)
    nuke.message(job_info_txt+""+plugin_info_txt)
    submit_to_deadline(job_info_txt, plugin_info_txt)
