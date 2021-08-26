[Package]
Name="levylab_lib_data_analysis_template"
Version="1.0.4.5"
Release=""
ID=acc9f814f0ba69edb243fb54c0ffbeab
File Format="vip"
Format Version="2017"
Display Name="Data Analaysis Template"


[Description]
Description="Template for building data analysis programs"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2021, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.0.4]\0D\0A- Update dependencies (Graph Utilities v2.1.7, XY Utilities v1.4.0)\0A- Fix data read example subVI"
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
Requires="jki_lib_state_machine>=2018.0.7.45,levylab_lib_control_vi>=1.3.0.11,levylab_lib_graph_utilities>=2.1.7.10,levylab_lib_xy_utilities>=1.4.0.17,mgi_lib_1d_array>=1.0.2.3,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_string>=5.0.0.25"
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
File 0="user.lib/Levylab/Data Analaysis Template/Data-Analysis.lvproj"
File 1="user.lib/Levylab/Data Analaysis Template/simple-LevyLab Analysis Framework (Template).vi"


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
