[Package]
Name="levylab_lib_ppms_instrument"
Version="1.4.4.27"
Release=""
ID=3e10a981488f6c6fe83064ee1f057676
File Format="vip"
Format Version="2017"
Display Name="PPMS Monitor and Control"


[Description]
Description="Program for logging PPMS status to the DSC. Provides a UI and API for controlling the magnet field, temperature, and rotator angle (for PPM2)"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2019, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.4.4.27]\0D\0Aupdate ports:\0A- 29171 (PPMS)\0A- 29172 (PPMS2)"
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
Num File Groups="3"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=87
File 0="user.lib/LevyLab/PPMS Instrument/PPMS Monitor and Control.vi"
File 1="user.lib/LevyLab/PPMS Instrument/PPMS_inst.lvproj"
File 2="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument.dll"
File 3="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument.llx"
File 4="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument_Example.vi"
File 5="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument_Server.exe"
File 6="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/ReleaseNotes.txt"
File 7="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/GetChamber.vi"
File 8="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/GetField.vi"
File 9="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/GetHelium.vi"
File 10="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/GetPosition.vi"
File 11="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/GetTemperature.vi"
File 12="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/OpenQDInstrument.vi"
File 13="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/QDInstrumentExceptionHandler.vi"
File 14="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/SetChamber.vi"
File 15="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/SetField.vi"
File 16="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/SetPosition.vi"
File 17="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/SetTemperature.vi"
File 18="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/QDInstrument/WaitFor.vi"
File 19="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/PPMS/GetPPMSItem.vi"
File 20="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/PPMS/GetPPMSItem_Example.vi"
File 21="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/PPMS/SendPPMSCommand.vi"
File 22="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/PPMS/SendPPMSCommand_Example.vi"
File 23="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/PPMS/SendPPMSCommand_Rotator.vi"
File 24="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/CAN/CAN_Float_Example.vi"
File 25="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_FLT.vi"
File 26="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_S16.vi"
File 27="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_S32.vi"
File 28="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_S8.vi"
File 29="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_STR.vi"
File 30="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_U16.vi"
File 31="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_U32.vi"
File 32="user.lib/LevyLab/PPMS Instrument/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_U8.vi"
File 33="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2 UI/Create UI.vi"
File 34="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2 UI/Instrument.PPMS2 UI.lvclass"
File 35="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2 UI/Launch PPMS2 UI.vi"
File 36="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2 UI/Process.vi"
File 37="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Close Instrument.vi"
File 38="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Create Instrument SMO Name.vi"
File 39="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Get Angle.vi"
File 40="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Get Helium Level.vi"
File 41="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Get Magnet Field.vi"
File 42="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Get Public API.vi"
File 43="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Get Temperature.vi"
File 44="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/getAll.vi"
File 45="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Handle Command.vi"
File 46="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/instrument.PPMS2.lvclass"
File 47="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/instrument.PPMS2.TestLauncher.vi"
File 48="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Open Instrument.vi"
File 49="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/PPMS2 Client.vi"
File 50="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Process.vi"
File 51="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Set Angle.vi"
File 52="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Set Magnet Field.vi"
File 53="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Set Temperature.vi"
File 54="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Typedefs/getAll--PPMS2--cluster.ctl"
File 55="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Typedefs/Magnet Field--PPMS2--cluster.ctl"
File 56="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Typedefs/Magnet Status--PPMS2--cluster.ctl"
File 57="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Typedefs/Magnet Status--PPMS2--ring.ctl"
File 58="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Typedefs/Temperature Status--PPMS2--cluster.ctl"
File 59="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Typedefs/Temperature Status--PPMS2--ring.ctl"
File 60="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Typedefs/Temperature--PPMS2--cluster.ctl"
File 61="user.lib/LevyLab/PPMS Instrument/instrument.PPMS UI/Create UI.vi"
File 62="user.lib/LevyLab/PPMS Instrument/instrument.PPMS UI/Instrument.PPMS UI.lvclass"
File 63="user.lib/LevyLab/PPMS Instrument/instrument.PPMS UI/Launch PPMS UI.vi"
File 64="user.lib/LevyLab/PPMS Instrument/instrument.PPMS UI/Process.vi"
File 65="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Close Instrument.vi"
File 66="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Create Instrument SMO Name.vi"
File 67="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Get Helium Level.vi"
File 68="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Get Magnet Field.vi"
File 69="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Get Public API.vi"
File 70="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Get Temperature.vi"
File 71="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/getAll.vi"
File 72="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Handle Command.vi"
File 73="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/instrument.PPMS.lvclass"
File 74="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/instrument.PPMS.TestLauncher.vi"
File 75="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Open Instrument.vi"
File 76="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/PPMS Client.vi"
File 77="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Process.vi"
File 78="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Set Magnet Field.vi"
File 79="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Set Temperature.vi"
File 80="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/getAll--PPMS--cluster.ctl"
File 81="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/Magnet Field--PPMS--cluster.ctl"
File 82="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/Magnet Status--PPMS--cluster.ctl"
File 83="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/Magnet Status--PPMS--ring.ctl"
File 84="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/Temperature Status--PPMS--cluster.ctl"
File 85="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/Temperature Status--PPMS--ring.ctl"
File 86="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/Temperature--PPMS--cluster.ctl"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=3
File 0="_functions_levylab_lib_ppms_instrument_1.mnu"
File 1="_functions_levylab_lib_ppms_instrument_2.mnu"
File 2="functions_LevyLab_lib_PPMS_Instrument.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
