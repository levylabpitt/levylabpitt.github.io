[Package]
Name="levylab_lib_data_analysis_template"
Version="1.0.8.3"
Release=""
ID=32a9aa087f72974a89404948b8070563
File Format="vip"
Format Version="2017"
Display Name="Data Analysis Template"


[Description]
Description="Template for building data analysis programs"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2022, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.0.8]\0A\0DBug fixes:\0A- add support for TDMS groups\0A- automatically call XY: Subset\0A- disable XY to intensity pre-processed\0A- add simple help instructions"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"


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
Requires="jki_lib_json_serialization>=1.1.10.37,jki_lib_serialization>=1.0.1.14,jki_lib_state_machine>=2018.0.7.45,levylab_lib_control_vi>=1.3.0.11,levylab_lib_fileutilities>=1.2.6.13,levylab_lib_graph_utilities>=2.1.10.2,levylab_lib_lvtoitx>=3.4.1.2,levylab_lib_xy_utilities>=1.5.1.1,mgi_lib_1d_array>=1.0.2.3,mgi_lib_numeric>=1.1.0.2,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_dictionary>=4.0.0.4,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=5.0.0.27,oglib_lvzip>=4.0.1,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3"
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
File 0="user.lib/Levylab/Data Analysis Template/Data-Analysis.lvproj"
File 1="user.lib/Levylab/Data Analysis Template/simple-LevyLab Analysis Framework (Template).vi"


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
