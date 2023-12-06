[Package]
Name="levylab_lib_remote_control_zmq"
Version="1.1.0.3"
Release=""
ID=94d4581b64e94a2e6b031827bf7906e3
File Format="vip"
Format Version="2017"
Display Name="Remote Control.ZMQ"


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
Release Notes="[1.1.0]\0A- Updated to work with JSON-RPC v1.1"
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
Requires="jdp_science_jsontext>=1.8.1.121,jdp_science_lib_common_utilities>=1.4.1.18,jki_lib_caraya>=1.4.2.145,jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.4.0.69,labview-zmq>=3.6.3.113,national_instruments_lib_guid_generator>=1.0.2.3,oglib_appcontrol>=4.1.0.7,oglib_error>=4.2.0.23,oglib_lvdata>=5.0.0.27,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3,levylab_lib_build_support>=1.2.5.1"
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
Num Files=50
File 0="user.lib/Levylab/RemoteControl.ZMQ/Process_donotrun.vi"
File 1="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ.lvclass"
File 2="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ.lvproj"
File 3="user.lib/Levylab/RemoteControl.ZMQ/Typedefs/ZMQ Config.ctl"
File 4="user.lib/Levylab/RemoteControl.ZMQ/Tests/RemoteControl.ZMQ.TestClient.vi"
File 5="user.lib/Levylab/RemoteControl.ZMQ/Tests/RemoteControl.ZMQ.TestServer.vi"
File 6="user.lib/Levylab/RemoteControl.ZMQ/Tests/ZMQ Rep Test.vi"
File 7="user.lib/Levylab/RemoteControl.ZMQ/Tests/ZMQ Req Test.vi"
File 8="user.lib/Levylab/RemoteControl.ZMQ/Tests/ZMQ sandbox.vi"
File 9="user.lib/Levylab/RemoteControl.ZMQ/Tests/Unit Tests/Test Bind REP Socket.vi"
File 10="user.lib/Levylab/RemoteControl.ZMQ/Tests/Unit Tests/Test Connect REQ Socket.vi"
File 11="user.lib/Levylab/RemoteControl.ZMQ/Tests/Unit Tests/Test Context.vi"
File 12="user.lib/Levylab/RemoteControl.ZMQ/Tests/Unit Tests/Test Read.vi"
File 13="user.lib/Levylab/RemoteControl.ZMQ/Tests/Unit Tests/Test REP Socket.vi"
File 14="user.lib/Levylab/RemoteControl.ZMQ/Tests/Unit Tests/Test REQ Socket.vi"
File 15="user.lib/Levylab/RemoteControl.ZMQ/Tests/Unit Tests/Test Write.vi"
File 16="user.lib/Levylab/RemoteControl.ZMQ/private/Build Endpoint.vi"
File 17="user.lib/Levylab/RemoteControl.ZMQ/private/ZMQ.Connect.vi"
File 18="user.lib/Levylab/RemoteControl.ZMQ/private/ZMQ.Handle Error.vi"
File 19="user.lib/Levylab/RemoteControl.ZMQ/Methods (Overrides)/Close Connection.vi"
File 20="user.lib/Levylab/RemoteControl.ZMQ/Methods (Overrides)/Get Connections.vi"
File 21="user.lib/Levylab/RemoteControl.ZMQ/Methods (Overrides)/Open Client Connection.vi"
File 22="user.lib/Levylab/RemoteControl.ZMQ/Methods (Overrides)/Open Server Connection.vi"
File 23="user.lib/Levylab/RemoteControl.ZMQ/Methods (Overrides)/Read Message.vi"
File 24="user.lib/Levylab/RemoteControl.ZMQ/Methods (Overrides)/Send Message.vi"
File 25="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCCreate Error Object.vi"
File 26="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCCreate ID.vi"
File 27="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCCreate Request-JSONtext.vi"
File 28="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCCreate Request.vi"
File 29="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCCreate Response-JSONtext.vi"
File 30="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCCreate Response.vi"
File 31="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCError--Cluster.ctl"
File 32="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCFlatten to String.vim"
File 33="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCJSON to LVtype.vim"
File 34="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCJSON-RPC Errors.vi"
File 35="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCJSON-RPC.lvclass"
File 36="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCParse Params-JSONtext.vi"
File 37="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCParse Params.vi"
File 38="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCParse Request-JSONtext.vi"
File 39="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCParse Request.vi"
File 40="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCParse Response-JSONtext.vi"
File 41="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCParse Response.vi"
File 42="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCRead ids.vi"
File 43="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCRequest--Cluster.ctl"
File 44="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCText to UTF-8.vi"
File 45="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCUnflatten from String.vim"
File 46="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCUTF-8 LV80.vi"
File 47="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCUTF-8 to Text.vi"
File 48="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCVariant to JSON.vi"
File 49="user.lib/Levylab/_RemoteControl_internal_deps/FB2131126572040C6C88AE3D00FB78CCWrite ids.vi"


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
