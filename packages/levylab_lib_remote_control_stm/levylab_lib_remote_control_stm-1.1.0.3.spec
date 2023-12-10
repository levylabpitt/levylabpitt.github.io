[Package]
Name="levylab_lib_remote_control_stm"
Version="1.1.0.3"
Release=""
ID=1cff1f1301e66c19d4d61173baee3aad
File Format="vip"
Format Version="2017"
Display Name="RemoteControl.STM"


[Description]
Description="Remote Control override implementing STM (LabVIEW Simple Messaging)"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2023, LevyLab"
Distribution=""
Vendor="LevyLab"
URL="https://github.com/levylabpitt/Instrument-Framework"
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.0.1]\0A- Update palette location"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"
install into global environment="FALSE"


[Platform]
Exclusive_LabVIEW_Version="LabVIEW x86>=19.0"
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
Requires="jdp_science_jsontext>=1.8.1.121,jdp_science_lib_common_utilities>=1.4.1.18,jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.4.0.69,national_instruments_lib_guid_generator>=1.0.2.3,ni_lib_stm>=3.1.0.9,oglib_appcontrol>=4.1.0.7,oglib_error>=4.2.0.23,oglib_lvdata>=5.0.0.27,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3,levylab_lib_build_support>=1.2.5.1"
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
Num Files=18
File 0="user.lib/Levylab/RemoteControl.STM/RemoteControl.STM.lvclass"
File 1="user.lib/Levylab/RemoteControl.STM/RemoteControl.STM.lvproj"
File 2="user.lib/Levylab/RemoteControl.STM/Tests/RC_STM_Server.vi"
File 3="user.lib/Levylab/RemoteControl.STM/Tests/Test Variant Flatten Unflatten.vi"
File 4="user.lib/Levylab/RemoteControl.STM/Tests/simple/STM_Client.vi"
File 5="user.lib/Levylab/RemoteControl.STM/Tests/simple/STM_Server.vi"
File 6="user.lib/Levylab/RemoteControl.STM/Tests/simple/subVI/PRI Counts Since Last Reset.vi"
File 7="user.lib/Levylab/RemoteControl.STM/Private/Choose Connection.vi"
File 8="user.lib/Levylab/RemoteControl.STM/Private/Find STM connection by ID.vi"
File 9="user.lib/Levylab/RemoteControl.STM/Methods (Overrides)/Close Connection.vi"
File 10="user.lib/Levylab/RemoteControl.STM/Methods (Overrides)/Get Connections.vi"
File 11="user.lib/Levylab/RemoteControl.STM/Methods (Overrides)/Handle Error.vi"
File 12="user.lib/Levylab/RemoteControl.STM/Methods (Overrides)/Listen.vi"
File 13="user.lib/Levylab/RemoteControl.STM/Methods (Overrides)/Open Client Connection.vi"
File 14="user.lib/Levylab/RemoteControl.STM/Methods (Overrides)/Read Message.vi"
File 15="user.lib/Levylab/RemoteControl.STM/Methods (Overrides)/Send Message.vi"
File 16="user.lib/Levylab/RemoteControl.STM/Methods (Overrides)/Start Listener.vi"
File 17="user.lib/Levylab/RemoteControl.STM/Methods (Overrides)/Stop Listener.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab/RemoteControl"
Replace Mode="Always"
Num Files=6
File 0="_functions_levylab_lib_remote_control_stm_1.mnu"
File 1="_functions_levylab_lib_remote_control_stm_2.mnu"
File 2="_functions_levylab_lib_remote_control_stm_3.mnu"
File 3="_functions_levylab_lib_remote_control_stm_4.mnu"
File 4="_functions_levylab_lib_remote_control_stm_5.mnu"
File 5="functions_Levylab_lib_remote_control_stm.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab/RemoteControl"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
