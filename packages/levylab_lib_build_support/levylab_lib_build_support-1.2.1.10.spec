[Package]
Name="levylab_lib_build_support"
Version="1.2.1.10"
Release=""
ID=04c0a6d976f4c3e2ddf405a2885471e6
File Format="vip"
Format Version="2017"
Display Name="Build Support"


[Description]
Description="Miscellaneous VIs help build applications and packages"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2021, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.2.1]\0D\0A- Update rename UI default values"
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
Requires="jki_lib_rest_client>=1.3.3.25,jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.4.0.63,mgi_lib_1d_array>=1.0.2.3,mgi_lib_file>=1.1.0.4,mgi_lib_numeric>=1.1.0.2,mgi_lib_timing>=1.1.0.2,mgi_lib_user_interface>=1.0.1.11,oglib_appcontrol>=4.1.0.7,oglib_file>=4.0.1.22,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3,wireflow_ab_lib_wf_progressbar>=1.0.2.56"
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
Num Files=57
File 0="user.lib/Levylab/Build Support/build-support.lvproj"
File 1="user.lib/Levylab/Build Support/Templates/Post-Build Custom Action.vit"
File 2="user.lib/Levylab/Build Support/Templates/Post-Install Custom Action.vit"
File 3="user.lib/Levylab/Build Support/Templates/Pre-Build Custom Action.vit"
File 4="user.lib/Levylab/Build Support/SelfUpdate/SelfUpdate.lvclass"
File 5="user.lib/Levylab/Build Support/SelfUpdate/private/Default Repo.vi"
File 6="user.lib/Levylab/Build Support/SelfUpdate/private/Default User.vi"
File 7="user.lib/Levylab/Build Support/SelfUpdate/private/Update Dialog.vi"
File 8="user.lib/Levylab/Build Support/SelfUpdate/example/Self Update Example.vi"
File 9="user.lib/Levylab/Build Support/SelfUpdate/API/Dialog.vi"
File 10="user.lib/Levylab/Build Support/SelfUpdate/API/Download and Run Installer.vi"
File 11="user.lib/Levylab/Build Support/SelfUpdate/API/Get Latest Release Version.vi"
File 12="user.lib/Levylab/Build Support/SelfUpdate/API/Get Path to Latest Installer.vi"
File 13="user.lib/Levylab/Build Support/SelfUpdate/API/Set User and Repository.vi"
File 14="user.lib/Levylab/Build Support/ProjectItem/ProjectItem.lvclass"
File 15="user.lib/Levylab/Build Support/ProjectItem/Typedefs/ClassData--Cluster.ctl"
File 16="user.lib/Levylab/Build Support/ProjectItem/Protected/Close.vi"
File 17="user.lib/Levylab/Build Support/ProjectItem/Protected/Delete Empty Folders.vi"
File 18="user.lib/Levylab/Build Support/ProjectItem/Protected/Initialize.vi"
File 19="user.lib/Levylab/Build Support/ProjectItem/Protected/List Classes.vi"
File 20="user.lib/Levylab/Build Support/ProjectItem/Protected/List Controls.vi"
File 21="user.lib/Levylab/Build Support/ProjectItem/Protected/List Project.vi"
File 22="user.lib/Levylab/Build Support/ProjectItem/Protected/List VIs.vi"
File 23="user.lib/Levylab/Build Support/ProjectItem/Protected/Rename Classes.vi"
File 24="user.lib/Levylab/Build Support/ProjectItem/Protected/Rename Controls.vi"
File 25="user.lib/Levylab/Build Support/ProjectItem/Protected/Rename Project.vi"
File 26="user.lib/Levylab/Build Support/ProjectItem/Protected/Rename VIs.vi"
File 27="user.lib/Levylab/Build Support/ProjectItem/Protected/Save All.vi"
File 28="user.lib/Levylab/Build Support/ProjectItem/Protected/Update Class Icon.vi"
File 29="user.lib/Levylab/Build Support/ProjectItem/Protected/Update Icon Preview.vi"
File 30="user.lib/Levylab/Build Support/ProjectItem/Protected/Write Icon Data.vi"
File 31="user.lib/Levylab/Build Support/ProjectItem/Private/Delete File and Folder.vi"
File 32="user.lib/Levylab/Build Support/ProjectItem/Private/Escape Brackets.vi"
File 33="user.lib/Levylab/Build Support/ProjectItem/Private/Is UI.vi"
File 34="user.lib/Levylab/Build Support/ProjectItem/Private/Update Path.vi"
File 35="user.lib/Levylab/Build Support/ProjectItem/API/Instrument Name and Icon UI.vi"
File 36="user.lib/Levylab/Build Support/ProjectItem/API/Rename items.vi"
File 37="user.lib/Levylab/Build Support/PreBuildSupport/rename to VIPT.vi"
File 38="user.lib/Levylab/Build Support/PreBuildSupport/VIPT to rename.vi"
File 39="user.lib/Levylab/Build Support/PreBuildSupport/subVI/Find File By Name.vi"
File 40="user.lib/Levylab/Build Support/PostBuildSupport/PostBuildSupport.lvclass"
File 41="user.lib/Levylab/Build Support/PostBuildSupport/Test/Test 7z.bat.vi"
File 42="user.lib/Levylab/Build Support/PostBuildSupport/Private/7zSD.sfx"
File 43="user.lib/Levylab/Build Support/PostBuildSupport/Private/Auto Build Script.vi"
File 44="user.lib/Levylab/Build Support/PostBuildSupport/Private/Build Application with API.vi"
File 45="user.lib/Levylab/Build Support/PostBuildSupport/Private/Build Application.vi"
File 46="user.lib/Levylab/Build Support/PostBuildSupport/Private/Build Installer with API.vi"
File 47="user.lib/Levylab/Build Support/PostBuildSupport/Private/Build Installer.vi"
File 48="user.lib/Levylab/Build Support/PostBuildSupport/Private/Copy 7zSD.SFX.vi"
File 49="user.lib/Levylab/Build Support/PostBuildSupport/Private/Copy Package.vi"
File 50="user.lib/Levylab/Build Support/PostBuildSupport/Private/Create Folders.vi"
File 51="user.lib/Levylab/Build Support/PostBuildSupport/Private/Execute 7z bat.vi"
File 52="user.lib/Levylab/Build Support/PostBuildSupport/Private/Update Build Version.vi"
File 53="user.lib/Levylab/Build Support/PostBuildSupport/Private/Write 7z config.vi"
File 54="user.lib/Levylab/Build Support/PostBuildSupport/Private/Write 7z.bat.vi"
File 55="user.lib/Levylab/Build Support/PostBuildSupport/API/Post Build Script (auto build).vi"
File 56="user.lib/Levylab/Build Support/PostBuildSupport/API/Post Build Script (manual build).vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=16
File 0="_functions_levylab_lib_build_support_1.mnu"
File 1="_functions_levylab_lib_build_support_10.mnu"
File 2="_functions_levylab_lib_build_support_11.mnu"
File 3="_functions_levylab_lib_build_support_12.mnu"
File 4="_functions_levylab_lib_build_support_13.mnu"
File 5="_functions_levylab_lib_build_support_14.mnu"
File 6="_functions_levylab_lib_build_support_15.mnu"
File 7="_functions_levylab_lib_build_support_2.mnu"
File 8="_functions_levylab_lib_build_support_3.mnu"
File 9="_functions_levylab_lib_build_support_4.mnu"
File 10="_functions_levylab_lib_build_support_5.mnu"
File 11="_functions_levylab_lib_build_support_6.mnu"
File 12="_functions_levylab_lib_build_support_7.mnu"
File 13="_functions_levylab_lib_build_support_8.mnu"
File 14="_functions_levylab_lib_build_support_9.mnu"
File 15="functions_Levylab_lib_Build_Support.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
