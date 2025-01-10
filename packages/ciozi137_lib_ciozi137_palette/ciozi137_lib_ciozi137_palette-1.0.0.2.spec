[Package]
Name="ciozi137_lib_ciozi137_palette"
Version="1.0.0.2"
Release=""
ID=c070e8880a527bfe7a1d6175361d4ac4
File Format="vip"
Format Version="2017"
Display Name="ciozi137-Palette"


[Description]
Description=""
Summary=""
License=""
Copyright="Copyright (c) 2025, ciozi137"
Distribution=""
Vendor="ciozi137"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes=""
System Package="FALSE"
Sub Package="FALSE"
License Agreement="FALSE"


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
Num Files=4
File 0="vi.lib/ciozi137/ciozi137-Palette/.gitattributes"
File 1="vi.lib/ciozi137/ciozi137-Palette/.gitignore"
File 2="vi.lib/ciozi137/ciozi137-Palette/LICENSE"
File 3="vi.lib/ciozi137/ciozi137-Palette/icons/g2673.png"


[File Group 1]
Target Dir="<vi.lib>/addons/ciozi137"
Replace Mode="Always"
Num Files=1
File 0="functions_ciozi137_lib_ciozi137_Palette.mnu"


[File Group 2]
Target Dir="<vi.lib>/addons/ciozi137"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
