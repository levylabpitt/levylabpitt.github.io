[Package]
Name="levylab_lib_build_support_system"
Version="1.8.0.27"
Release=""
ID=af69fc3198287f47e424b5a7e8bcd936
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
Release Notes="[1.8.0]\0A- reorganize folder, libraries, and classes into a more logical structure\0A- update 7zip.bat to better handle missing *.7z files\0A- update and rename build.bat to build_vip.bat, build 7zip is optional and executes only if 7zip.bat exists"
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
File 1="LevyLab/build-support/templates/build_all.bat.template"
File 2="LevyLab/build-support/templates/build_vip.bat.template"
