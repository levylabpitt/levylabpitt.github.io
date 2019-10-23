[Package]
Name="levylab_lib_ppms_instrument"
Version="1.0.2.8"
Release=""
ID=b82e194c836ee61110f2dc21b17f9678
File Format="vip"
Format Version="2017"
Display Name="PPMS Monitor and Control"


[Description]
Description="Files for controlling the PPMS Magnet , Temperature, etc. and logging to the DSC."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2019, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.0.2.8]\0A- remove angle set/get from front panel"
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
Requires="levylab_lib_levylab_instruments>=1.2.4.37"
Conflicts=""


[Activation]
License File=""
Licensed Library=""


[Files]
Num File Groups="5"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=59
File 0="user.lib/LevyLab/PPMS Instrument/PPMS_inst.lvproj"
File 1="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument.dll"
File 2="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument.llx"
File 3="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument_Example.vi"
File 4="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument_Server.exe"
File 5="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/ReleaseNotes.txt"
File 6="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/GetChamber.vi"
File 7="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/GetField.vi"
File 8="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/GetHelium.vi"
File 9="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/GetPosition.vi"
File 10="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/GetTemperature.vi"
File 11="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/OpenQDInstrument.vi"
File 12="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/QDInstrumentExceptionHandler.vi"
File 13="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/SetChamber.vi"
File 14="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/SetField.vi"
File 15="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/SetPosition.vi"
File 16="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/SetTemperature.vi"
File 17="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/WaitFor.vi"
File 18="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/PPMS/GetPPMSItem.vi"
File 19="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/PPMS/GetPPMSItem_Example.vi"
File 20="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/PPMS/SendPPMSCommand.vi"
File 21="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/PPMS/SendPPMSCommand_Example.vi"
File 22="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/PPMS/SendPPMSCommand_Rotator.vi"
File 23="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/CAN/CAN_Float_Example.vi"
File 24="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_FLT.vi"
File 25="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_S16.vi"
File 26="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_S32.vi"
File 27="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_S8.vi"
File 28="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_STR.vi"
File 29="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_U16.vi"
File 30="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_U32.vi"
File 31="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_U8.vi"
File 32="user.lib/LevyLab/PPMS Instrument/instrument.PPMS UI/Create UI.vi"
File 33="user.lib/LevyLab/PPMS Instrument/instrument.PPMS UI/Instrument.PPMS UI.lvclass"
File 34="user.lib/LevyLab/PPMS Instrument/instrument.PPMS UI/Launch PPMS UI.vi"
File 35="user.lib/LevyLab/PPMS Instrument/instrument.PPMS UI/Process.vi"
File 36="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Close Instrument.vi"
File 37="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Create Instrument SMO Name.vi"
File 38="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Get Helium Level.vi"
File 39="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Get Magnet Field.vi"
File 40="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Get Public API.vi"
File 41="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Get Temperature.vi"
File 42="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/getAll.vi"
File 43="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Handle Command.vi"
File 44="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/instrument.PPMS.lvclass"
File 45="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/instrument.PPMS.TestLauncher.vi"
File 46="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Open Instrument.vi"
File 47="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/PPMS Client.vi"
File 48="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/PPMS Monitor and Control.vi"
File 49="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Process.vi"
File 50="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Set Magnet Field.vi"
File 51="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Set Temperature.vi"
File 52="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/getAll--PPMS--cluster.ctl"
File 53="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/Magnet Field--PPMS--cluster.ctl"
File 54="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/Magnet Status--PPMS--cluster.ctl"
File 55="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/Magnet Status--PPMS--ring.ctl"
File 56="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/Temperature Status--PPMS--cluster.ctl"
File 57="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/Temperature Status--PPMS--ring.ctl"
File 58="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/Temperature--PPMS--cluster.ctl"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=1
File 0="functions_LevyLab_lib_PPMS_Instrument.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"


[File Group 3]
Target Dir="<menus>/Controls/LevyLab"
Replace Mode="Always"
Num Files=3
File 0="_controls_levylab_lib_ppms_instrument_1.mnu"
File 1="_controls_levylab_lib_ppms_instrument_2.mnu"
File 2="controls_LevyLab_lib_PPMS_Instrument.mnu"


[File Group 4]
Target Dir="<menus>/Controls/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
