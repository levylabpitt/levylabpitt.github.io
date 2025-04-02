[Package]
Name="pybywire"
Version="1.2.3.5"
Release=""
ID=c5d636230bd32364ea9a9820837b07b0
File Format="vip"
Format Version="2010"
Display Name="PyByWire"


[Description]
Description=""
Summary=""
License="BSD 2-clause"
Copyright="Copyright (c) 2013, Martijn Jasperse"
Distribution=""
Vendor="Monash University"
URL="http://pybywire.sf.net"
Packager="Martijn Jasperse"
Demo="FALSE"
Release Notes=""
System Package="FALSE"
Sub Package="FALSE"
License Agreement="FALSE"


[Platform]
Exclusive_LabVIEW_Version=">=10.0"
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
Requires="labview-zmq>=1.4.5.78,msgpack>=0.9.4.3"
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
Num Files=11
File 0="vi.lib/PyByWire/functions.py"
File 1="vi.lib/PyByWire/pbw_cluster_to_str.vi"
File 2="vi.lib/PyByWire/pbw_connect.vi"
File 3="vi.lib/PyByWire/pbw_get_result.vi"
File 4="vi.lib/PyByWire/pbw_host_path.vi"
File 5="vi.lib/PyByWire/pbw_rebuild.vi"
File 6="vi.lib/PyByWire/pbw_send_cmd.vi"
File 7="vi.lib/PyByWire/pbw_send_frame.vi"
File 8="vi.lib/PyByWire/pbw_tcode_to_dtype.vi"
File 9="vi.lib/PyByWire/pbw_to_ctrl.vi"
File 10="vi.lib/PyByWire/pybywire.py"


[File Group 1]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=1
File 0="functions_pybywire.mnu"
