[Package]
Name="levylab_lib_remote_control"
Version="1.0.0.1"
Release=""
ID=9aa0a82377b4f5ded595943b88e79c9b
File Format="vip"
Format Version="2017"
Display Name="Remote Control"


[Description]
Description="Parent library for sending messages to programs occupying different application instances, ie, LabVIEW running on different computers, multiple instances of LabVIEW on a single computer, or compiled applications. By itself this library does not implement a specific or even working communication protocol, but provides abstract methods that can be overridden by, for example, ZMQ, MQTT, etc."
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
Requires="jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.4.0.69,national_instruments_lib_guid_generator>=1.0.2.3,oglib_appcontrol>=4.1.0.7,oglib_error>=4.2.0.23,oglib_lvdata>=5.0.0.27,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3,levylab_lib_build_support>=1.2.5.1"
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
Num Files=62
File 0="user.lib/Levylab/RemoteControl/Process.vi"
File 1="user.lib/Levylab/RemoteControl/RemoteControl.lvclass"
File 2="user.lib/Levylab/RemoteControl/RemoteControl.lvproj"
File 3="user.lib/Levylab/RemoteControl/Typedefs/Message--Cluster.ctl"
File 4="user.lib/Levylab/RemoteControl/Typedefs/PrivateEvents--Cluster.ctl"
File 5="user.lib/Levylab/RemoteControl/Typedefs/PrivateEvents--RemoteControl.Configure.ctl"
File 6="user.lib/Levylab/RemoteControl/Typedefs/PrivateEvents--RemoteControl.SendMessageToProcess.ctl"
File 7="user.lib/Levylab/RemoteControl/Typedefs/PublicEvents--Cluster.ctl"
File 8="user.lib/Levylab/RemoteControl/Typedefs/PublicEvents--RemoteControl.SendMessageFromProcess.ctl"
File 9="user.lib/Levylab/RemoteControl/Typedefs/RC Com Type--enum.ctl"
File 10="user.lib/Levylab/RemoteControl/Typedefs/RC Process Type--Enum.ctl"
File 11="user.lib/Levylab/RemoteControl/Tests/RC_Client Client 2.vi"
File 12="user.lib/Levylab/RemoteControl/Tests/RC_Client Client.vi"
File 13="user.lib/Levylab/RemoteControl/Tests/RC_Client N.vi"
File 14="user.lib/Levylab/RemoteControl/Tests/RC_Client.vi"
File 15="user.lib/Levylab/RemoteControl/Tests/RemoteControl.TestLauncher.ConnectionMonitor.vi"
File 16="user.lib/Levylab/RemoteControl/Private/Choose Random Command.vi"
File 17="user.lib/Levylab/RemoteControl/Private/Format Message String.vi"
File 18="user.lib/Levylab/RemoteControl/Private/Message to Display String.vi"
File 19="user.lib/Levylab/RemoteControl/Private/RemoteControl.GetPrivateEvents.vi"
File 20="user.lib/Levylab/RemoteControl/Private/RemoteControl.GlobalVariable.vi"
File 21="user.lib/Levylab/RemoteControl/Private/RemoteControl.SendMessageFromProcess.vi"
File 22="user.lib/Levylab/RemoteControl/Private/State History.vi"
File 23="user.lib/Levylab/RemoteControl/Private/Time Message Events.vi"
File 24="user.lib/Levylab/RemoteControl/Private/Variant to Display String.vi"
File 25="user.lib/Levylab/RemoteControl/Private/VirtualTestInstrument.vi"
File 26="user.lib/Levylab/RemoteControl/Methods (Overrides)/CreatePrivateEvents.vi"
File 27="user.lib/Levylab/RemoteControl/Methods (Overrides)/CreatePublicEvents.vi"
File 28="user.lib/Levylab/RemoteControl/Methods (Overrides)/DestroyPrivateEvents.vi"
File 29="user.lib/Levylab/RemoteControl/Methods (Overrides)/DestroyPublicEvents.vi"
File 30="user.lib/Levylab/RemoteControl/Methods (Framework)/Close Connection.vi"
File 31="user.lib/Levylab/RemoteControl/Methods (Framework)/Get Connections.vi"
File 32="user.lib/Levylab/RemoteControl/Methods (Framework)/Listen.vi"
File 33="user.lib/Levylab/RemoteControl/Methods (Framework)/Open Client Connection.vi"
File 34="user.lib/Levylab/RemoteControl/Methods (Framework)/Open Server Connection.vi"
File 35="user.lib/Levylab/RemoteControl/Methods (Framework)/Read Message.vi"
File 36="user.lib/Levylab/RemoteControl/Methods (Framework)/Send and Receive Message.vi"
File 37="user.lib/Levylab/RemoteControl/Methods (Framework)/Send Message.vi"
File 38="user.lib/Levylab/RemoteControl/Methods (Framework)/Start Listener.vi"
File 39="user.lib/Levylab/RemoteControl/Methods (Framework)/Stop Listener.vi"
File 40="user.lib/Levylab/RemoteControl/API/Connect.vi"
File 41="user.lib/Levylab/RemoteControl/API/Create Server SMO.vi"
File 42="user.lib/Levylab/RemoteControl/API/Disconnect.vi"
File 43="user.lib/Levylab/RemoteControl/API/Read address.vi"
File 44="user.lib/Levylab/RemoteControl/API/Read Commands.vi"
File 45="user.lib/Levylab/RemoteControl/API/Read Connected.vi"
File 46="user.lib/Levylab/RemoteControl/API/Read Message (sent).vi"
File 47="user.lib/Levylab/RemoteControl/API/Read Port.vi"
File 48="user.lib/Levylab/RemoteControl/API/Read RC Process Type.vi"
File 49="user.lib/Levylab/RemoteControl/API/Read timeout.vi"
File 50="user.lib/Levylab/RemoteControl/API/Remote Client.vi"
File 51="user.lib/Levylab/RemoteControl/API/RemoteControl.Configure.vi"
File 52="user.lib/Levylab/RemoteControl/API/RemoteControl.GetPublicEvents.vi"
File 53="user.lib/Levylab/RemoteControl/API/RemoteControl.SendMessageToProcess.vi"
File 54="user.lib/Levylab/RemoteControl/API/Send and Receive.vi"
File 55="user.lib/Levylab/RemoteControl/API/Variant to Data.vim"
File 56="user.lib/Levylab/RemoteControl/API/Write address.vi"
File 57="user.lib/Levylab/RemoteControl/API/Write Commands.vi"
File 58="user.lib/Levylab/RemoteControl/API/Write Debug Mode.vi"
File 59="user.lib/Levylab/RemoteControl/API/Write Message (sent).vi"
File 60="user.lib/Levylab/RemoteControl/API/Write Port.vi"
File 61="user.lib/Levylab/RemoteControl/API/Write Timeout.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=6
File 0="_functions_levylab_lib_remote_control_1.mnu"
File 1="_functions_levylab_lib_remote_control_2.mnu"
File 2="_functions_levylab_lib_remote_control_3.mnu"
File 3="_functions_levylab_lib_remote_control_4.mnu"
File 4="_functions_levylab_lib_remote_control_5.mnu"
File 5="functions_Levylab_lib_remote_control.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
