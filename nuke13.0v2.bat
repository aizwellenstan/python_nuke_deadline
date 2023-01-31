@echo off

set NUKE_PATH=C:\Users\%USERNAME%\.nuke
set NUKE_PATH=D:\gizmos_customMenu;D:\nuke

set OPTICAL_FLARES_LICENSE_PATH=C:\Program Files\Nuke13.0v2
set OPTICAL_FLARES_PATH=C:\Program Files\Common Files\Nuke\13.0\plugins
set OPTICAL_FLARES_PRESET_PATH=C:\Program Files\Common Files\Nuke\13.0\plugins\OpticalFlares_Nuke_13.0_Node-Locked_1.0.86\Textures-And-Presets
set peregrinel_LICENSE=license@license

set OCIO=D:\proj\config.ocio

@REM excutable path for deadline
set NUKE_DEADLINE_EXCUTABLE=I:\script\bin\td\bin\vd2_nuke13.0v2.bat

call "C:\Program Files\Nuke13.0v2\Nuke13.0.exe" %*
