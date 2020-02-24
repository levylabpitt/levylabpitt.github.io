[Package]
Name="msgpack"
Version="0.10.1.7"
Release=""
ID=a8bbf50744e4ca632ac13ee1ecf00c6c
File Format="vip"
Format Version="2010"
Display Name="msgpack"


[Description]
Description=""
Summary="Implementation of the Message Pack protocol for LabVIEW"
License="LGPL"
Copyright="Copyright (c) 2012, Martijn Jasperse"
Distribution=""
Vendor="Martijn Jasperse"
URL="http://sourceforge.net/p/msgpack-labview/wiki/Home/"
Packager="Martijn Jasperse"
Demo="FALSE"
Release Notes=""
System Package="FALSE"
Sub Package="FALSE"
License Agreement="FALSE"


[Platform]
Exclusive_LabVIEW_Version=">=10.0"
Exclusive_LabVIEW_System="ALL"
Exclusive_OS="Windows NT"


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
Requires="oglib_lvdata>=4.2.0.21"
Conflicts=""


[Activation]
License File=""
Licensed Library=""


[Files]
Num File Groups="2"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=30
File 0="vi.lib/addons/msgpack/copy_packed_data.vi"
File 1="vi.lib/addons/msgpack/create_pack.vi"
File 2="vi.lib/addons/msgpack/create_unpack.vi"
File 3="vi.lib/addons/msgpack/err_handle.vi"
File 4="vi.lib/addons/msgpack/err_id.vi"
File 5="vi.lib/addons/msgpack/free_pack.vi"
File 6="vi.lib/addons/msgpack/free_unpack.vi"
File 7="vi.lib/addons/msgpack/get_packed_data.vi"
File 8="vi.lib/addons/msgpack/get_packed_len.vi"
File 9="vi.lib/addons/msgpack/get_unpack_len.vi"
File 10="vi.lib/addons/msgpack/get_unpack_type.vi"
File 11="vi.lib/addons/msgpack/msgpack.lvlib"
File 12="vi.lib/addons/msgpack/msgpackalt.dll"
File 13="vi.lib/addons/msgpack/msgunpack.lvlib"
File 14="vi.lib/addons/msgpack/pack_array_len.vi"
File 15="vi.lib/addons/msgpack/pack_cluster.vi"
File 16="vi.lib/addons/msgpack/pack_item.vi"
File 17="vi.lib/addons/msgpack/pack_map_len.vi"
File 18="vi.lib/addons/msgpack/pack_raw.vi"
File 19="vi.lib/addons/msgpack/unpack.vi"
File 20="vi.lib/addons/msgpack/unpack_array_len.vi"
File 21="vi.lib/addons/msgpack/unpack_bool.vi"
File 22="vi.lib/addons/msgpack/unpack_dbl.vi"
File 23="vi.lib/addons/msgpack/unpack_int.vi"
File 24="vi.lib/addons/msgpack/unpack_map.vi"
File 25="vi.lib/addons/msgpack/unpack_map_len.vi"
File 26="vi.lib/addons/msgpack/unpack_null.vi"
File 27="vi.lib/addons/msgpack/unpack_object.vi"
File 28="vi.lib/addons/msgpack/unpack_raw.vi"
File 29="vi.lib/addons/msgpack/unpack_uint.vi"


[File Group 1]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=1
File 0="functions_msgpack.mnu"
