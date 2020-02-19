[Package]
Name="levylab_lib_build_support"
Version="1.0.0.1"
Release=""
ID=9c99761c54730b0dda975bd3d10a1ce2
File Format="vip"
Format Version="2017"
Display Name="Build Support"


[Description]
Description="Miscellanious VIs help build applications and packages"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2020, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="first build"
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
Requires="mgi_lib_file>=1.1.0.4,mgi_lib_timing>=1.1.0.2,oglib_appcontrol>=4.1.0.7,oglib_file>=4.0.1.22,oglib_time>=4.0.1.3,wireflow_ab_lib_wf_progressbar>=1.0.2.56"
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
Num Files=28
File 0="user.lib/Levylab/build-support.lvproj"
File 1="user.lib/Levylab/Templates/buildspec-template.vipt.rename"
File 2="user.lib/Levylab/Templates/Post-Build Custom Action.vit"
File 3="user.lib/Levylab/Templates/Post-Install Custom Action.vit"
File 4="user.lib/Levylab/Templates/Pre-Build Custom Action.vit"
File 5="user.lib/Levylab/subVIs/Find File By Name.vi"
File 6="user.lib/Levylab/PreBuildSupport/rename to VIPT.vi"
File 7="user.lib/Levylab/PreBuildSupport/VIPT to rename.vi"
File 8="user.lib/Levylab/PostBuildSupport/7zSD.sfx"
File 9="user.lib/Levylab/PostBuildSupport/Build Application with API.vi"
File 10="user.lib/Levylab/PostBuildSupport/Build Application.vi"
File 11="user.lib/Levylab/PostBuildSupport/Build Installer with API.vi"
File 12="user.lib/Levylab/PostBuildSupport/Build Installer.vi"
File 13="user.lib/Levylab/PostBuildSupport/Copy 7zSD.SFX.vi"
File 14="user.lib/Levylab/PostBuildSupport/Copy Package.vi"
File 15="user.lib/Levylab/PostBuildSupport/Create Folders.vi"
File 16="user.lib/Levylab/PostBuildSupport/Execute 7z bat.vi"
File 17="user.lib/Levylab/PostBuildSupport/Post Build Script.vi"
File 18="user.lib/Levylab/PostBuildSupport/PostBuildSupport.lvclass"
File 19="user.lib/Levylab/PostBuildSupport/Test 7z.bat.vi"
File 20="user.lib/Levylab/PostBuildSupport/Test Script.vi"
File 21="user.lib/Levylab/PostBuildSupport/Update Build Version.vi"
File 22="user.lib/Levylab/PostBuildSupport/Write 7z config.vi"
File 23="user.lib/Levylab/PostBuildSupport/Write 7z.bat.vi"
File 24="user.lib/Levylab/PostBuildSupport/Write Output Package File Path.vi"
File 25="user.lib/Levylab/PostBuildSupport/Write Package Source Folder.vi"
File 26="user.lib/Levylab/PostBuildSupport/Write Package Version.vi"
File 27="user.lib/Levylab/PostBuildSupport/Write Product Name.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=5
File 0="_functions_levylab_lib_build_support_1.mnu"
File 1="_functions_levylab_lib_build_support_2.mnu"
File 2="_functions_levylab_lib_build_support_3.mnu"
File 3="_functions_levylab_lib_build_support_4.mnu"
File 4="functions_Levylab_lib_Build_Support.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
