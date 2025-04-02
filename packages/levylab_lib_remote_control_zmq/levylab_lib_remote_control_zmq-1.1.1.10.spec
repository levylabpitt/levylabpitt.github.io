[Package]
Name="levylab_lib_remote_control_zmq"
Version="1.1.1.10"
Release=""
ID=81127b43574011bfe33ab883acb329fa
File Format="vip"
Format Version="2017"
Display Name="RemoteControl.ZMQ"


[Description]
Description="Override library implementing ZMQ lazy pirate reliable request reply (RRR) protocal using RemoteControl SMO framework."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2024, LevyLab"
Distribution=""
Vendor="LevyLab"
URL="https://github.com/levylabpitt/Instrument-Framework"
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.1.1]\0A- Update install location\0A- Update default timeout for ZMQ read"
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
Requires="jdp_science_jsontext>=1.8.2.122,jdp_science_lib_common_utilities>=1.4.1.18,jki_lib_caraya>=1.4.3.147,jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.4.0.69,labview-zmq>=3.6.3.113,national_instruments_lib_guid_generator>=1.0.2.3,oglib_appcontrol>=4.1.0.7,oglib_error>=4.2.0.23,oglib_lvdata>=5.0.0.27,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3,levylab_lib_build_support>=1.2.5.1"
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
Num Files=85
File 0="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ.lvclass"
File 1="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ.lvproj"
File 2="user.lib/Levylab/RemoteControl.ZMQ/Typedefs/ZMQ Config.ctl"
File 3="user.lib/Levylab/RemoteControl.ZMQ/Tests/RemoteControl.ZMQ.TestClient.vi"
File 4="user.lib/Levylab/RemoteControl.ZMQ/Tests/RemoteControl.ZMQ.TestServer.vi"
File 5="user.lib/Levylab/RemoteControl.ZMQ/Tests/ZMQ Rep Test.vi"
File 6="user.lib/Levylab/RemoteControl.ZMQ/Tests/ZMQ Req Test.vi"
File 7="user.lib/Levylab/RemoteControl.ZMQ/Tests/ZMQ sandbox.vi"
File 8="user.lib/Levylab/RemoteControl.ZMQ/Tests/Unit Tests/Test Bind REP Socket.vi"
File 9="user.lib/Levylab/RemoteControl.ZMQ/Tests/Unit Tests/Test Connect REQ Socket.vi"
File 10="user.lib/Levylab/RemoteControl.ZMQ/Tests/Unit Tests/Test Context.vi"
File 11="user.lib/Levylab/RemoteControl.ZMQ/Tests/Unit Tests/Test Read.vi"
File 12="user.lib/Levylab/RemoteControl.ZMQ/Tests/Unit Tests/Test REP Socket.vi"
File 13="user.lib/Levylab/RemoteControl.ZMQ/Tests/Unit Tests/Test REQ Socket.vi"
File 14="user.lib/Levylab/RemoteControl.ZMQ/Tests/Unit Tests/Test Write.vi"
File 15="user.lib/Levylab/RemoteControl.ZMQ/private/Build Endpoint.vi"
File 16="user.lib/Levylab/RemoteControl.ZMQ/private/ZMQ.Connect.vi"
File 17="user.lib/Levylab/RemoteControl.ZMQ/private/ZMQ.Handle Error.vi"
File 18="user.lib/Levylab/RemoteControl.ZMQ/Methods (Overrides)/Close Connection.vi"
File 19="user.lib/Levylab/RemoteControl.ZMQ/Methods (Overrides)/Get Connections.vi"
File 20="user.lib/Levylab/RemoteControl.ZMQ/Methods (Overrides)/Open Client Connection.vi"
File 21="user.lib/Levylab/RemoteControl.ZMQ/Methods (Overrides)/Open Server Connection.vi"
File 22="user.lib/Levylab/RemoteControl.ZMQ/Methods (Overrides)/Read Message.vi"
File 23="user.lib/Levylab/RemoteControl.ZMQ/Methods (Overrides)/Send Message.vi"
File 24="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Choose Random Command.vi"
File 25="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Close Connection.vi"
File 26="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Connect.vi"
File 27="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Create Server SMO.vi"
File 28="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6CreatePrivateEvents.vi"
File 29="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6CreatePublicEvents.vi"
File 30="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6DestroyPrivateEvents.vi"
File 31="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6DestroyPublicEvents.vi"
File 32="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Disconnect.vi"
File 33="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Format Message String.vi"
File 34="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Get Connections.vi"
File 35="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Listen.vi"
File 36="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Message to Display String.vi"
File 37="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Message--Cluster.ctl"
File 38="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Open Client Connection.vi"
File 39="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Open Server Connection.vi"
File 40="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6PrivateEvents--Cluster.ctl"
File 41="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6PrivateEvents--RemoteControl.Configure.ctl"
File 42="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6PrivateEvents--RemoteControl.SendMessageToProcess.ctl"
File 43="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Process.vi"
File 44="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6PublicEvents--Cluster.ctl"
File 45="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6PublicEvents--RemoteControl.SendMessageFromProcess.ctl"
File 46="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6RC Com Type--enum.ctl"
File 47="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6RC Process Type--Enum.ctl"
File 48="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6RC_Client Client 2.vi"
File 49="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6RC_Client Client.vi"
File 50="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6RC_Client N.vi"
File 51="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6RC_Client.vi"
File 52="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Read address.vi"
File 53="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Read Commands.vi"
File 54="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Read Connected.vi"
File 55="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Read Message (sent).vi"
File 56="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Read Message.vi"
File 57="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Read Port.vi"
File 58="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Read RC Process Type.vi"
File 59="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Read timeout.vi"
File 60="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6RemoteControl.Configure.vi"
File 61="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6RemoteControl.GetPrivateEvents.vi"
File 62="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6RemoteControl.GetPublicEvents.vi"
File 63="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6RemoteControl.GlobalVariable.vi"
File 64="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6RemoteControl.lvclass"
File 65="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6RemoteControl.Remote Client.vi"
File 66="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6RemoteControl.SendMessageFromProcess.vi"
File 67="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6RemoteControl.SendMessageToProcess.vi"
File 68="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6RemoteControl.TestLauncher.ConnectionMonitor.vi"
File 69="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6RemoteControl.Variant to Data.vim"
File 70="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Send and Receive Message.vi"
File 71="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Send and Receive.vi"
File 72="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Send Message.vi"
File 73="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Start Listener.vi"
File 74="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6State History.vi"
File 75="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Stop Listener.vi"
File 76="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Time Message Events.vi"
File 77="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Variant to Display String.vi"
File 78="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6VirtualTestInstrument.vi"
File 79="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Write address.vi"
File 80="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Write Commands.vi"
File 81="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Write Debug Mode.vi"
File 82="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Write Message (sent).vi"
File 83="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Write Port.vi"
File 84="user.lib/Levylab/_RemoteControl_internal_deps/0216792C2718E3EEB6E13FC952486FA6Write Timeout.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab/RemoteControl"
Replace Mode="Always"
Num Files=5
File 0="_functions_levylab_lib_remote_control_zmq_1.mnu"
File 1="_functions_levylab_lib_remote_control_zmq_2.mnu"
File 2="_functions_levylab_lib_remote_control_zmq_3.mnu"
File 3="_functions_levylab_lib_remote_control_zmq_4.mnu"
File 4="functions_Levylab_lib_remote_control_zmq.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab/RemoteControl"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
