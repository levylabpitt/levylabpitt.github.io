[Package]
Name="levylab_lib_json_rpc"
Version="1.0.0.1"
Release=""
ID=a27727ae0afd0bb9cb19eaba6f7965a9
File Format="vip"
Format Version="2017"
Display Name="JSON-RPC"


[Description]
Description="Library for encoding and decoding JSON-RPC 2.0 request and response objects \0A\0Ahttps://www.jsonrpc.org/specification"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2023, LevyLab"
Distribution=""
Vendor="LevyLab"
URL="https://github.com/levylabpitt/Instrument-Framework"
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.0.0]\0A- previously was included in Instrument Framework"
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
Requires="jdp_science_jsontext>=1.7.0.118,jdp_science_lib_common_utilities>=1.4.1.18,oglib_numeric>=4.1.0.8,levylab_lib_build_support>=1.2.5.1"
Conflicts="levylab_lib_postgresql>=1.4.0.22"


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
Num Files=19
File 0="user.lib/Levylab/JSON-RPC/JSON-RPC.lvclass"
File 1="user.lib/Levylab/JSON-RPC/typedefs/Error--Cluster.ctl"
File 2="user.lib/Levylab/JSON-RPC/typedefs/Request--Cluster.ctl"
File 3="user.lib/Levylab/JSON-RPC/typedefs/Response--Cluster.ctl"
File 4="user.lib/Levylab/JSON-RPC/private/Create Error Object.vi"
File 5="user.lib/Levylab/JSON-RPC/private/Create ID.vi"
File 6="user.lib/Levylab/JSON-RPC/private/Create Request-JSONtext.vi"
File 7="user.lib/Levylab/JSON-RPC/private/Create Response-JSONtext.vi"
File 8="user.lib/Levylab/JSON-RPC/private/Parse Params-JSONtext.vi"
File 9="user.lib/Levylab/JSON-RPC/private/Parse Request-JSONtext.vi"
File 10="user.lib/Levylab/JSON-RPC/private/Parse Response-JSONtext.vi"
File 11="user.lib/Levylab/JSON-RPC/private/Read ids.vi"
File 12="user.lib/Levylab/JSON-RPC/private/Write ids.vi"
File 13="user.lib/Levylab/JSON-RPC/API/Create Request.vi"
File 14="user.lib/Levylab/JSON-RPC/API/Create Response.vi"
File 15="user.lib/Levylab/JSON-RPC/API/JSON-RPC Errors.vi"
File 16="user.lib/Levylab/JSON-RPC/API/Parse Params.vi"
File 17="user.lib/Levylab/JSON-RPC/API/Parse Request.vi"
File 18="user.lib/Levylab/JSON-RPC/API/Parse Response.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=3
File 0="_functions_levylab_lib_json_rpc_1.mnu"
File 1="_functions_levylab_lib_json_rpc_2.mnu"
File 2="functions_Levylab_lib_json_rpc.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"


[File Group 3]
Target Dir="<menus>/Controls/Levylab"
Replace Mode="Always"
Num Files=2
File 0="_controls_levylab_lib_json_rpc_1.mnu"
File 1="controls_Levylab_lib_json_rpc.mnu"


[File Group 4]
Target Dir="<menus>/Controls/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
