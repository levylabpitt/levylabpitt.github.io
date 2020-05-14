[Package]
Name="levylab_lib_smo_embeddedui"
Version="1.0.0.10"
Release=""
ID=1a2c8c62c46337ecc63f671032fb690e
File Format="vip"
Format Version="2017"
Display Name="SMO.UI.Embedded Template (Basic)"


[Description]
Description=""
Summary="Embedded SMO Template"
License="BSD-3"
Copyright="Copyright (c) 2020, Levylab"
Distribution=""
Vendor="Levylab"
URL="https://github.com/levylabpitt/Embedded-Template-SMO"
Packager="Joseph Albro"
Demo="FALSE"
Release Notes="Dependencies management and configuration"
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
Requires="jki_statemachineobjects>=1.3.0.56,levylab_lib_embedded_smo_ui>=1.0.0.12,oglib_appcontrol>=4.1.0.7"
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
Num Files=3
File 0="templates/JKI/JKI SMO/LevyLab/Process.vi"
File 1="templates/JKI/JKI SMO/LevyLab/SMO.UI.Embedded.Basic.lvclass"
File 2="templates/JKI/JKI SMO/LevyLab/SMO.UI.Embedded.Basic.TestLauncher.vi"


[File Group 1]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_SMO_EmbeddedUI.mnu"
