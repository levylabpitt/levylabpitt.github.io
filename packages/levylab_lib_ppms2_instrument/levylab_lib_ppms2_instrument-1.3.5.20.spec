[Package]
Name="levylab_lib_ppms2_instrument"
Version="1.3.5.20"
Release=""
ID=996a4c159403b28003747b8caf821a77
File Format="vip"
Format Version="2017"
Display Name="PPMS2 Monitor and Control"


[Description]
Description="Files for controlling PPMS2 Angle, Field, Temperature, etc. and logging to DSC"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2019, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.3.5.20]\0A- rearrange front panel\0A- use new build scripts to build package and exe installer"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"


[Platform]
Exclusive_LabVIEW_Version="LabVIEW>=16.0"
Exclusive_LabVIEW_System="ALL"
Exclusive_OS="ALL"


[Script VIs]
PreInstall=""
PostInstall=""
PreUninstall=""
PostUninstall=""
Verify=""
PreBuild=""
PostBuild=""


[Dependencies]
AutoReqProv=FALSE
Requires="jki_statemachineobjects>=1.3.0.56,oglib_appcontrol>=4.1.0.7,oglib_time>=4.0.1.3,levylab_lib_levylab_instruments>=1.2.4.37"
Conflicts=""


[Activation]
License File=""
Licensed Library=""


[Files]
Num File Groups="3"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=61
File 0="user.lib/LevyLab/PPMS2 Instrument/PPMS2_inst.lvproj"
File 1="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/QDInstrument.dll"
File 2="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/QDInstrument.llx"
File 3="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/QDInstrument_Example.vi"
File 4="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/QDInstrument_Server.exe"
File 5="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/ReleaseNotes.txt"
File 6="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/QDInstrument/GetChamber.vi"
File 7="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/QDInstrument/GetField.vi"
File 8="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/QDInstrument/GetHelium.vi"
File 9="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/QDInstrument/GetPosition.vi"
File 10="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/QDInstrument/GetTemperature.vi"
File 11="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/QDInstrument/OpenQDInstrument.vi"
File 12="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/QDInstrument/QDInstrumentExceptionHandler.vi"
File 13="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/QDInstrument/SetChamber.vi"
File 14="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/QDInstrument/SetField.vi"
File 15="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/QDInstrument/SetPosition.vi"
File 16="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/QDInstrument/SetTemperature.vi"
File 17="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/QDInstrument/WaitFor.vi"
File 18="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/PPMS/GetPPMSItem.vi"
File 19="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/PPMS/GetPPMSItem_Example.vi"
File 20="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/PPMS/SendPPMSCommand.vi"
File 21="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/PPMS/SendPPMSCommand_Example.vi"
File 22="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/PPMS/SendPPMSCommand_Rotator.vi"
File 23="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/CAN/CAN_Float_Example.vi"
File 24="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_FLT.vi"
File 25="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_S16.vi"
File 26="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_S32.vi"
File 27="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_S8.vi"
File 28="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_STR.vi"
File 29="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_U16.vi"
File 30="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_U32.vi"
File 31="user.lib/LevyLab/PPMS2 Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_U8.vi"
File 32="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2 UI/Create UI.vi"
File 33="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2 UI/Instrument.PPMS2 UI.lvclass"
File 34="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2 UI/Launch PPMS2 UI.vi"
File 35="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2 UI/Process.vi"
File 36="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/Close Instrument.vi"
File 37="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/Create Instrument SMO Name.vi"
File 38="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/Get Angle.vi"
File 39="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/Get Helium Level.vi"
File 40="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/Get Magnet Field.vi"
File 41="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/Get Public API.vi"
File 42="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/Get Temperature.vi"
File 43="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/getAll.vi"
File 44="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/Handle Command.vi"
File 45="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/instrument.PPMS2.lvclass"
File 46="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/instrument.PPMS2.TestLauncher.vi"
File 47="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/Open Instrument.vi"
File 48="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/PPMS Monitor and Control.vi"
File 49="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/PPMS2 Client.vi"
File 50="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/Process.vi"
File 51="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/Set Angle.vi"
File 52="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/Set Magnet Field.vi"
File 53="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/Set Temperature.vi"
File 54="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/Typedefs/getAll--PPMS2--cluster.ctl"
File 55="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/Typedefs/Magnet Field--PPMS2--cluster.ctl"
File 56="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/Typedefs/Magnet Status--PPMS2--cluster.ctl"
File 57="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/Typedefs/Magnet Status--PPMS2--ring.ctl"
File 58="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/Typedefs/Temperature Status--PPMS2--cluster.ctl"
File 59="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/Typedefs/Temperature Status--PPMS2--ring.ctl"
File 60="user.lib/LevyLab/PPMS2 Instrument/instrument.PPMS2/Typedefs/Temperature--PPMS2--cluster.ctl"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=1
File 0="functions_LevyLab_lib_PPMS2_Instrument.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
