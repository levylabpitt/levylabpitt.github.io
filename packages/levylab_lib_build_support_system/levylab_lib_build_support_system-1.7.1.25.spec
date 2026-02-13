[Package]
Name="levylab_lib_build_support_system"
Version="1.7.1.25"
Release=""
ID=d48db37e680c9b1e3062a20bd6c39094
File Format="vip"
Format Version="2017"
Display Name="Build Support (System)"


[Description]
Description="Miscellaneous VIs help build applications and packages"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2026, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.7.1]\0D\0A- store *.bat.template files in %localappdata%\\LevyLab\\build-support\\templates\0A- other bug fixes"
System Package="TRUE"
Sub Package="TRUE"
License Agreement="TRUE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"
install into global environment="FALSE"


[Platform]
Exclusive_LabVIEW_Version="LabVIEW>=0"
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
Requires="levylab_lib_progress_bar>=1.0.0.1,wiresmith_technology_lib_g_cli_labview_builder>=0.2.0.9,wiresmith_technology_lib_g_cli_vi_package_manager_tools>=0.2.1.15"
Conflicts=""


[Activation]
License File=""
Licensed Library=""


[Files]
Num File Groups="1"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<OS User Application Data>"
Replace Mode="Always"
Num Files=3
File 0="LevyLab/build-support/templates/7zip.bat.template"
File 1="LevyLab/build-support/templates/build.bat.template"
File 2="LevyLab/build-support/templates/build_all.bat.template"
