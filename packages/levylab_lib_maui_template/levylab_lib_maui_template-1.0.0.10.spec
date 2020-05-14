[Package]
Name="levylab_lib_maui_template"
Version="1.0.0.10"
Release=""
ID=6f5fd1f2371a27a95b44fcacfddf9dcf
File Format="vip"
Format Version="2017"
Display Name="SMO.UI.MAUI Template (Basic)"


[Description]
Description=""
Summary="A template for the MAUI Framework with two subpanels"
License="BSD-3"
Copyright="Copyright (c) 2020, Levylab"
Distribution=""
Vendor="Levylab"
URL="https://github.com/levylabpitt/MAUI-Template"
Packager="Joseph Albro"
Demo="FALSE"
Release Notes="Dependency Management"
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
Requires="jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.3.0.56,levylab_lib_maui>=1.0.0.22,levylab_lib_embedded_smo_ui>=1.0.0.12"
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
File 0="templates/JKI/JKI SMO/LevyLab/MAUI Template/MauiTemplate.lvproj"
File 1="templates/JKI/JKI SMO/LevyLab/MAUI Template/Process.vi"
File 2="templates/JKI/JKI SMO/LevyLab/MAUI Template/SMO.UI.MAUI.Basic.lvclass"
File 3="templates/JKI/JKI SMO/LevyLab/MAUI Template/SMO.UI.MAUI.Basic.TestLauncher.vi"


[File Group 1]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_MAUI_Template.mnu"
