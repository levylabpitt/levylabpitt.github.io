[Package]
Name="levylab_lib_control_vi"
Version="1.3.0.11"
Release=""
ID=9beaa3d8527536364932ad83c10374f8
File Format="vip"
Format Version="2014"
Display Name="Control VI"


[Description]
Description=""
Summary=""
License=""
Copyright="Copyright (c) 2017, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="- new LevyLab function category"
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
Num File Groups="3"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=13
File 0="user.lib/LevyLab/Control VI/.hgtags"
File 1="user.lib/LevyLab/Control VI/Cartesian_Experiment.vi"
File 2="user.lib/LevyLab/Control VI/Ramp.vi"
File 3="user.lib/LevyLab/Control VI/SubVIs/Generate sorted scan parameters.vi"
File 4="user.lib/LevyLab/Control VI/SubVIs/Max_Min_conversion.vi"
File 5="user.lib/LevyLab/Control VI/Other/Ramp_BackForth_SubVI.vi"
File 6="user.lib/LevyLab/Control VI/Other/Ramp_SubVI.vi"
File 7="user.lib/LevyLab/Control VI/Other/Spiral.vi"
File 8="user.lib/LevyLab/Control VI/Other/Sweep Back and Forth.vi"
File 9="user.lib/LevyLab/Control VI/Action_SubVIs/Set_B.vi"
File 10="user.lib/LevyLab/Control VI/Action_SubVIs/Set_T.vi"
File 11="user.lib/LevyLab/Control VI/Action_SubVIs/Set_Vsg1.vi"
File 12="user.lib/LevyLab/Control VI/Action_SubVIs/Set_Vsg2.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=4
File 0="_functions_levylab_lib_control_vi_1.mnu"
File 1="_functions_levylab_lib_control_vi_2.mnu"
File 2="_functions_levylab_lib_control_vi_3.mnu"
File 3="functions_LevyLab_lib_Control_VI.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
