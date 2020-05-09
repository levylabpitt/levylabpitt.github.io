[Package]
Name="levylab_lib_smo_embeddedui"
Version="1.0.0.7"
Release=""
ID=c035480c16fcd0641959a757f85746df
File Format="vip"
Format Version="2017"
Display Name="SMO.EmbeddedUI"


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
Release Notes="Moved on disk. Rebuilding to reflect those changes."
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
Num Files=3
File 0="templates/JKI/JKI SMO/LevyLab/Process.vi"
File 1="templates/JKI/JKI SMO/LevyLab/SMO.EmbeddedUI.lvclass"
File 2="templates/JKI/JKI SMO/LevyLab/SMO.EmbeddedUI.TestLauncher.vi"


[File Group 1]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_SMO_EmbeddedUI.mnu"
