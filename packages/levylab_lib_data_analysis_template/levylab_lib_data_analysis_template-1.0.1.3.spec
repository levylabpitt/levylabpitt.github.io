[Package]
Name="levylab_lib_data_analysis_template"
Version="1.0.1.3"
Release=""
ID=aee675399db977e8cad08e6836343d82
File Format="vip"
Format Version="2017"
Display Name="Data Analaysis Template"


[Description]
Description="Template for building data analysis programs"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2020, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.0.2.3]\0A- Minor UI changes\0A"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


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
Num Files=2
File 0="user.lib/Levylab/Data-Analysis.lvproj"
File 1="user.lib/Levylab/simple-LevyLab Analysis Framework (Template).vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_Data_Analysis_Template.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
