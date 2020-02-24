[Package]
Name="levylab_lib_linecut_linefit"
Version="2.1.4.21"
Release=""
ID=fad69e2a2bf666cbba904f978d295cdd
File Format="vip"
Format Version="2014"
Display Name="Linecut Linefit"


[Description]
Description="Best fit Levenburg-Marquardt method to XY data. Typically used to determine width of lithography wire by fitting to data obtained during cutting of a wire. User enters XY data and cutting rate, as well as estimates of initial parameters for the fit.\0A\0AThe included "Simple Graph Converter - Multi to XY.vi" converts a multiplot (from Lock-in current monitor) into XY plot (input format for the linecut vi)."
Summary=""
License=""
Copyright="Copyright (c) 2014, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Ishan Levy"
Demo="FALSE"
Release Notes="Fixed bug where the off option for autofit wasn't working within the program itself because it scaled to the whole data"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="FALSE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"


[Platform]
Exclusive_LabVIEW_Version="LabVIEW>=13.0"
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
Num Files=4
File 0="user.lib/Levylab/Linecut Linefit/Domain Finder.vi"
File 1="user.lib/Levylab/Linecut Linefit/Linecut Linefit.vi"
File 2="user.lib/Levylab/Linecut Linefit/Restrict X Domain of Graph.vi"
File 3="user.lib/Levylab/Linecut Linefit/Simple Graph Converter - Multi to XY.vi"


[File Group 1]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=1
File 0="functions_levylab_lib_linecut_linefit.mnu"
