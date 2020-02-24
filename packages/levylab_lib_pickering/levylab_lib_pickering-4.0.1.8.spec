[Package]
Name="levylab_lib_pickering"
Version="4.0.1.8"
Release=""
ID=0a704e8b8582fbe7d4ece01ec530452d
File Format="vip"
Format Version="2017"
Display Name="Pickering"


[Description]
Description="VIs for controlling Pickering matrix switch"
Summary=""
License=""
Copyright="Copyright (c) 2018, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick"
Demo="FALSE"
Release Notes="- reorganize code\0A- experimental release"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="FALSE"


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
Requires=""
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
Num Files=27
File 0="user.lib/Levylab/Pickering/Pickering 4 wire PPMS DR.vi"
File 1="user.lib/Levylab/Pickering/Pickering 4 wire PPMS Puck.vi"
File 2="user.lib/Levylab/Pickering/Pickering 4 wire.vi"
File 3="user.lib/Levylab/Pickering/Pickering action.vi"
File 4="user.lib/Levylab/Pickering/pickering.lvclass"
File 5="user.lib/Levylab/Pickering/pickering.lvproj"
File 6="user.lib/Levylab/Pickering/pickering.TestLauncher.vi"
File 7="user.lib/Levylab/Pickering/Process.vi"
File 8="user.lib/Levylab/Pickering/Typedefs/Channel-Cluster.ctl"
File 9="user.lib/Levylab/Pickering/Typedefs/Channels-Array.ctl"
File 10="user.lib/Levylab/Pickering/Typedefs/ChannelX-ComboBox.ctl"
File 11="user.lib/Levylab/Pickering/Typedefs/ChannelY-ComboBox.ctl"
File 12="user.lib/Levylab/Pickering/Typedefs/PickeringConfig-Cluster.ctl"
File 13="user.lib/Levylab/Pickering/Typedefs/PickeringXConfig-Cluster.ctl"
File 14="user.lib/Levylab/Pickering/Typedefs/PickeringYConfig-Cluster.ctl"
File 15="user.lib/Levylab/Pickering/subVI/Array difference.vi"
File 16="user.lib/Levylab/Pickering/subVI/Array_Remove duplicates.vi"
File 17="user.lib/Levylab/Pickering/subVI/Assign switches.vi"
File 18="user.lib/Levylab/Pickering/subVI/ConvertChannelsArrayToString.vi"
File 19="user.lib/Levylab/Pickering/subVI/ReadPickeringConfig.vi"
File 20="user.lib/Levylab/Pickering/subVI/StringToChannelsArray.vi"
File 21="user.lib/Levylab/Pickering/subVI/Switch status IO - Human Readable.vi"
File 22="user.lib/Levylab/Pickering/subVI/Switch status IO - Human Readable_3voltageamp.vi"
File 23="user.lib/Levylab/Pickering/subVI/Switch status IO.vi"
File 24="user.lib/Levylab/Pickering/subVI/WritePickeringConfig.vi"
File 25="user.lib/Levylab/Pickering/old/Crosspoint_x.vi"
File 26="user.lib/Levylab/Pickering/old/Crosspoint_y.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=3
File 0="_functions_levylab_lib_pickering_1.mnu"
File 1="_functions_levylab_lib_pickering_2.mnu"
File 2="functions_levylab_lib_pickering.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
