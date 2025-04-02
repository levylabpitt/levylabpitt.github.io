[Package]
Name="levylab_lib_remote_control_zmq"
Version="1.0.0.1"
Release=""
ID=1f0eea3caeefd9c6a26617b865f83269
File Format="vip"
Format Version="2017"
Display Name="RemoteControl.ZMQ"


[Description]
Description="Override library implementing ZMQ lazy pirate reliable request reply (RRR) protocal using RemoteControl SMO framework."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2023, LevyLab"
Distribution=""
Vendor="LevyLab"
URL="https://github.com/levylabpitt/Instrument-Framework"
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.0.0]\0A- First build as stand-alone package"
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
Requires="jdp_science_jsontext>=1.7.0.118,jdp_science_lib_common_utilities>=1.4.1.18,jki_lib_caraya>=1.4.2.145,jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.4.0.69,labview-zmq>=3.6.3.113,national_instruments_lib_guid_generator>=1.0.2.3,oglib_appcontrol>=4.1.0.7,oglib_error>=4.2.0.23,oglib_lvdata>=5.0.0.27,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3,levylab_lib_build_support>=1.2.5.1"
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
Num Files=25
File 0="user.lib/Levylab/RemoteControl/Process_donotrun.vi"
File 1="user.lib/Levylab/RemoteControl/RemoteControl.ZMQ.lvclass"
File 2="user.lib/Levylab/RemoteControl/RemoteControl.ZMQ.lvproj"
File 3="user.lib/Levylab/RemoteControl/Typedefs/ZMQ Config.ctl"
File 4="user.lib/Levylab/RemoteControl/Tests/RemoteControl.ZMQ.TestClient.vi"
File 5="user.lib/Levylab/RemoteControl/Tests/RemoteControl.ZMQ.TestServer.vi"
File 6="user.lib/Levylab/RemoteControl/Tests/ZMQ Rep Test.vi"
File 7="user.lib/Levylab/RemoteControl/Tests/ZMQ Req Test.vi"
File 8="user.lib/Levylab/RemoteControl/Tests/ZMQ sandbox.vi"
File 9="user.lib/Levylab/RemoteControl/Tests/Unit Tests/Test Bind REP Socket.vi"
File 10="user.lib/Levylab/RemoteControl/Tests/Unit Tests/Test Connect REQ Socket.vi"
File 11="user.lib/Levylab/RemoteControl/Tests/Unit Tests/Test Context.vi"
File 12="user.lib/Levylab/RemoteControl/Tests/Unit Tests/Test Read.vi"
File 13="user.lib/Levylab/RemoteControl/Tests/Unit Tests/Test REP Socket.vi"
File 14="user.lib/Levylab/RemoteControl/Tests/Unit Tests/Test REQ Socket.vi"
File 15="user.lib/Levylab/RemoteControl/Tests/Unit Tests/Test Write.vi"
File 16="user.lib/Levylab/RemoteControl/private/Build Endpoint.vi"
File 17="user.lib/Levylab/RemoteControl/private/ZMQ.Connect.vi"
File 18="user.lib/Levylab/RemoteControl/private/ZMQ.Handle Error.vi"
File 19="user.lib/Levylab/RemoteControl/Methods (Overrides)/Close Connection.vi"
File 20="user.lib/Levylab/RemoteControl/Methods (Overrides)/Get Connections.vi"
File 21="user.lib/Levylab/RemoteControl/Methods (Overrides)/Open Client Connection.vi"
File 22="user.lib/Levylab/RemoteControl/Methods (Overrides)/Open Server Connection.vi"
File 23="user.lib/Levylab/RemoteControl/Methods (Overrides)/Read Message.vi"
File 24="user.lib/Levylab/RemoteControl/Methods (Overrides)/Send Message.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=5
File 0="_functions_levylab_lib_remote_control_zmq_1.mnu"
File 1="_functions_levylab_lib_remote_control_zmq_2.mnu"
File 2="_functions_levylab_lib_remote_control_zmq_3.mnu"
File 3="_functions_levylab_lib_remote_control_zmq_4.mnu"
File 4="functions_Levylab_lib_remote_control_zmq.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
