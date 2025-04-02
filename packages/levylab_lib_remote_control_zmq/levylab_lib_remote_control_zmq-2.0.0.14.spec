[Package]
Name="levylab_lib_remote_control_zmq"
Version="2.0.0.14"
Release=""
ID=6db7154476ccdab2229a8b2f755f1ee7
File Format="vip"
Format Version="2017"
Display Name="RemoteControl.ZMQ"


[Description]
Description="Override library implementing ZMQ lazy pirate reliable request reply (RRR) protocal using RemoteControl SMO framework."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2025, LevyLab"
Distribution=""
Vendor="LevyLab"
URL="https://github.com/levylabpitt/Instrument-Framework"
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[2.0.0]\0A- update to SMO v2.0 lvlib"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"
install into global environment="FALSE"


[Platform]
Exclusive_LabVIEW_Version="LabVIEW>=19.0"
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
Requires="jdp_science_jsontext>=1.9.0.124,jdp_science_lib_common_utilities>=1.4.1.18,jki_lib_caraya>=1.4.3.147,jki_lib_state_machine>=2018.0.7.45,labview-zmq>=3.6.3.113,national_instruments_lib_guid_generator>=1.0.2.3,oglib_appcontrol>=4.1.0.7,oglib_error>=4.2.0.23,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3,prirvin_lib_json_rpc>=1.2.5.14"
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
Num Files=24
File 0="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ.lvlib"
File 1="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/RemoteControl.ZMQ.lvclass"
File 2="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/Typedefs/ZMQ Config.ctl"
File 3="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/Tests/RemoteControl.ZMQ.TestClient.vi"
File 4="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/Tests/RemoteControl.ZMQ.TestServer.vi"
File 5="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/Tests/ZMQ Rep Test.vi"
File 6="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/Tests/ZMQ Req Test.vi"
File 7="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/Tests/ZMQ sandbox.vi"
File 8="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/Tests/Unit Tests/Test Bind REP Socket.vi"
File 9="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/Tests/Unit Tests/Test Connect REQ Socket.vi"
File 10="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/Tests/Unit Tests/Test Context.vi"
File 11="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/Tests/Unit Tests/Test Read.vi"
File 12="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/Tests/Unit Tests/Test REP Socket.vi"
File 13="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/Tests/Unit Tests/Test REQ Socket.vi"
File 14="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/Tests/Unit Tests/Test Write.vi"
File 15="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/private/Build Endpoint.vi"
File 16="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/private/ZMQ.Connect.vi"
File 17="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/private/ZMQ.Handle Error.vi"
File 18="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/Methods (Overrides)/Close Connection.vi"
File 19="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/Methods (Overrides)/Get Connections.vi"
File 20="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/Methods (Overrides)/Open Client Connection.vi"
File 21="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/Methods (Overrides)/Open Server Connection.vi"
File 22="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/Methods (Overrides)/Read Message.vi"
File 23="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ/Methods (Overrides)/Send Message.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab/RemoteControl"
Replace Mode="Always"
Num Files=6
File 0="_functions_levylab_lib_remote_control_zmq_1.mnu"
File 1="_functions_levylab_lib_remote_control_zmq_2.mnu"
File 2="_functions_levylab_lib_remote_control_zmq_3.mnu"
File 3="_functions_levylab_lib_remote_control_zmq_4.mnu"
File 4="_functions_levylab_lib_remote_control_zmq_5.mnu"
File 5="functions_Levylab_lib_remote_control_zmq.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab/RemoteControl"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
