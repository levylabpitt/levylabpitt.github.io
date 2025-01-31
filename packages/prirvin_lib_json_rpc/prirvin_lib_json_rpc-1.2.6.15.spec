[Package]
Name="prirvin_lib_json_rpc"
Version="1.2.6.15"
Release=""
ID=7db5900e5d3a21ca08498f9079f5beda
File Format="vip"
Format Version="2017"
Display Name="JSON-RPC"


[Description]
Description="Library for encoding and decoding JSON-RPC 2.0 request and response objects \0A\0Ahttps://www.jsonrpc.org/specification"
Summary="Library for encoding and decoding JSON-RPC 2.0 request and response objects "
License="BSD-3"
Copyright="Copyright (c) 2025, Patrick Irvin"
Distribution=""
Vendor="PRIrvin"
URL="https://github.com/PRIrvin"
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.2.6]\0A- enable 32/64 bit labview"
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
Requires="jdp_science_jsontext>=1.9.0.124,jdp_science_lib_common_utilities>=1.4.1.18,oglib_numeric>=4.1.0.8,prirvin_lib_prirvin_palette>=1.0.0.3"
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
File 0="vi.lib/PRIrvin/JSON-RPC/JSON-RPC.lvlib"
File 1="vi.lib/PRIrvin/JSON-RPC/typedefs/Error--Cluster.ctl"
File 2="vi.lib/PRIrvin/JSON-RPC/typedefs/Request--Cluster.ctl"
File 3="vi.lib/PRIrvin/JSON-RPC/typedefs/Response--Cluster.ctl"
File 4="vi.lib/PRIrvin/JSON-RPC/private/Create Error Object.vi"
File 5="vi.lib/PRIrvin/JSON-RPC/private/Create ID.vi"
File 6="vi.lib/PRIrvin/JSON-RPC/private/Create Request-JSONtext.vi"
File 7="vi.lib/PRIrvin/JSON-RPC/private/Create Response-JSONtext.vi"
File 8="vi.lib/PRIrvin/JSON-RPC/private/Parse Params-JSONtext.vi"
File 9="vi.lib/PRIrvin/JSON-RPC/private/Parse Request-JSONtext.vi"
File 10="vi.lib/PRIrvin/JSON-RPC/private/Parse Response-JSONtext.vi"
File 11="vi.lib/PRIrvin/JSON-RPC/private/Text to UTF-8.vi"
File 12="vi.lib/PRIrvin/JSON-RPC/private/UTF-8 LV80.vi"
File 13="vi.lib/PRIrvin/JSON-RPC/private/UTF-8 to Text.vi"
File 14="vi.lib/PRIrvin/JSON-RPC/private/Variant to JSONRPC params.vi"
File 15="vi.lib/PRIrvin/JSON-RPC/private/Variant to JSONRPC result .vi"
File 16="vi.lib/PRIrvin/JSON-RPC/API/Create Request.vi"
File 17="vi.lib/PRIrvin/JSON-RPC/API/Create Response.vi"
File 18="vi.lib/PRIrvin/JSON-RPC/API/Flatten to String.vim"
File 19="vi.lib/PRIrvin/JSON-RPC/API/JSON to LVtype.vim"
File 20="vi.lib/PRIrvin/JSON-RPC/API/JSON-RPC Errors.vi"
File 21="vi.lib/PRIrvin/JSON-RPC/API/Parse Params.vi"
File 22="vi.lib/PRIrvin/JSON-RPC/API/Parse Request.vi"
File 23="vi.lib/PRIrvin/JSON-RPC/API/Parse Response.vi"
File 24="vi.lib/PRIrvin/JSON-RPC/API/Unflatten from String.vim"
File 25="examples/PRIrvin/JSON-RPC/examples/JSONrpc-Example.vi"
File 26="examples/PRIrvin/JSON-RPC/examples/JSONrpc-Flatten-Example.vi"


[File Group 1]
Target Dir="<vi.lib>/addons/prirvin"
Replace Mode="Always"
Num Files=2
File 0="_functions_prirvin_lib_json_rpc_1.mnu"
File 1="functions_prirvin_lib_json_rpc.mnu"


[File Group 2]
Target Dir="<vi.lib>/addons/prirvin"
Replace Mode="Always"
Num Files=1
File 0="controls_prirvin_lib_json_rpc.mnu"
