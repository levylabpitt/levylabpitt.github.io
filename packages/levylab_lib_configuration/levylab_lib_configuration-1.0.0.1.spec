[Package]
Name="levylab_lib_configuration"
Version="1.0.0.1"
Release=""
ID=5e05fefb7612075159924392b74e2470
File Format="vip"
Format Version="2017"
Display Name="Configuration"


[Description]
Description="Library for reading and writing configuration files"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2023, LevyLab"
Distribution=""
Vendor="LevyLab"
URL="https://github.com/levylabpitt/Instrument-Framework"
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.0.0]\0A- First build as stand-along package (previously included in Instrument Framework)\0A- Add Read Configuration.vim malleable VI as an alternative to Read Configuration + Variant to Data"
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
Requires="oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=5.0.0.27,oglib_string>=5.0.0.25,oglib_variantconfig>=4.0.0.5,levylab_lib_build_support>=1.2.5.1"
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
Num Files=13
File 0="user.lib/Levylab/Configuration/Configuration.lvclass"
File 1="user.lib/Levylab/Configuration/Configuration.lvproj"
File 2="user.lib/Levylab/Configuration/Default Path.vi"
File 3="user.lib/Levylab/Configuration/Handle Missing Sections.vi"
File 4="user.lib/Levylab/Configuration/Read Configuration (FrameworkTemplate).vi"
File 5="user.lib/Levylab/Configuration/Read Configuration.vi"
File 6="user.lib/Levylab/Configuration/Read Configuration.vim"
File 7="user.lib/Levylab/Configuration/Read Path.vi"
File 8="user.lib/Levylab/Configuration/Read Section.vi"
File 9="user.lib/Levylab/Configuration/Show Configuration.vi"
File 10="user.lib/Levylab/Configuration/Write Configuration.vi"
File 11="user.lib/Levylab/Configuration/Write Path.vi"
File 12="user.lib/Levylab/Configuration/Write Section.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_configuration.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
