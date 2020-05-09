[Package]
Name="levylab_lib_maui_template"
Version="1.0.0.6"
Release=""
ID=b95089fc6d0161bab504e149e1d7d803
File Format="vip"
Format Version="2017"
Display Name="MAUI Template"


[Description]
Description=""
Summary=""
License=""
Copyright="Copyright (c) 2020, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Joseph Albro"
Demo="FALSE"
Release Notes="Changed repository on  disk. Rebuilding package to reflect these changes."
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
Num Files=4
File 0="templates/JKI/JKI SMO/LevyLab/MAUI Template/MauiTemplate.lvclass"
File 1="templates/JKI/JKI SMO/LevyLab/MAUI Template/MauiTemplate.lvproj"
File 2="templates/JKI/JKI SMO/LevyLab/MAUI Template/MauiTemplate.TestLauncher.vi"
File 3="templates/JKI/JKI SMO/LevyLab/MAUI Template/Process.vi"


[File Group 1]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_MAUI_Template.mnu"
