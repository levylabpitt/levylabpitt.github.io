[Package]
Name="levylab_lib_build_support_system"
Version="1.11.2.50"
Release=""
ID=3f29a5191c391439694c1ddf3d75fffa
File Format="vip"
Format Version="2017"
Display Name="Build Support (System)"


[Description]
Description=" VIs and scripts to help automate package and application builds"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2026, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.11.2]\0D\0A1. Release notes from the vipb - gh release now pulls its body from <Release_Notes> If the vipb has no notes, it falls back to --generate-notes. The old release_notes.txt path is gone.\0A\0A2. Build number always increments on every successful build (after the build/release steps). It writes the bumped version into the vipb but does not commit or push it. DO_RELEASE now gates only the git release (commit/merge/tag/push) + the GitHub release."
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
Requires="levylab_lib_progress_bar>=1.0.0.1,wiresmith_technology_lib_g_cli>=3.0.1.98,wiresmith_technology_lib_g_cli_labview_builder>=0.2.0.9,wiresmith_technology_lib_g_cli_vi_package_manager_tools>=0.2.1.15"
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
Num Files=5
File 0="LevyLab/build-support/templates/build.cfg"
File 1="LevyLab/build-support/templates/build_all.bat"
File 2="LevyLab/build-support/templates/Inno.iss"
File 3="LevyLab/build-support/scripts/build.bat"
File 4="LevyLab/build-support/scripts/Setup-BuildMachine.bat"
