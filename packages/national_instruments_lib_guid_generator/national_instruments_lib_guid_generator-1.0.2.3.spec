[Package]
Name="national_instruments_lib_guid_generator"
Version="1.0.2.3"
Release=""
ID=0a172ca970b051c23f00bbc59d01e3c3
File Format="vip"
Format Version="2017"
Display Name="GUID Generator"


[Description]
Description=""
Summary=""
License=""
Copyright="Copyright (c) 2018, National Instruments"
Distribution=""
Vendor="National Instruments"
URL=""
Packager="Elijah Kerry"
Demo="FALSE"
Release Notes="Wraps a .NET call for generating unique IDs in a VI"
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
Num File Groups="2"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=1
File 0="vi.lib/National Instruments/GUID Generator/Guid Generator.vi"


[File Group 1]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=1
File 0="functions_National_Instruments_lib_GUID_Generator.mnu"
