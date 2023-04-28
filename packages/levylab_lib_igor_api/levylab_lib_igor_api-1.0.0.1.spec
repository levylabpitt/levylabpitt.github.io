[Package]
Name="levylab_lib_igor_api"
Version="1.0.0.1"
Release=""
ID=bb279f57224e0ef55f7e6c69cf067399
File Format="vip"
Format Version="2017"
Display Name="Igor API"


[Description]
Description="LabVIEW wrapper meant to facilitate the use of the text-based Igor Pro ActiveX API."
Summary="LabVIEW wrapper to control Igor Pro with ActiveX"
License="BSD-3"
Copyright="Copyright (c) 2023, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin, Joe Albro"
Demo="FALSE"
Release Notes="[1.0.0.1]\0A- initial build\0A- This packages is based on Asylum-API v1.0.0.5, AFM Lithography f108670, LV-Data v3.5.2.3"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"
install into global environment="FALSE"


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
Requires="jki_lib_caraya>=1.3.0.137,labview_open_source_lib_epoch_datetime>=1.1.0.5,oglib_array>=4.1.1.14,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=5.0.0.27,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3"
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
Num Files=15
File 0="user.lib/Levylab/Igor API/Igor_API.lvproj"
File 1="user.lib/Levylab/Igor API/Tests/TestArraytoWave.vi"
File 2="user.lib/Levylab/Igor API/Tests/TestEnsureIgorStringFormat.vi"
File 3="user.lib/Levylab/Igor API/private/DebugModeSingleton.vi"
File 4="user.lib/Levylab/Igor API/private/Igor_EnsureIgorStringFormat.vi"
File 5="user.lib/Levylab/Igor API/private/Igor_NumericArraytoIgorWave.vi"
File 6="user.lib/Levylab/Igor API/private/Igor_StringArraytoIgorWave.vi"
File 7="user.lib/Levylab/Igor API/API/Igor_ArraytoIgorWave.vi"
File 8="user.lib/Levylab/Igor API/API/Igor_CloseRefnum.vi"
File 9="user.lib/Levylab/Igor API/API/Igor_LoadLargeWaveUsingFile.vi"
File 10="user.lib/Levylab/Igor API/API/Igor_LoadWaveFromFile.vi"
File 11="user.lib/Levylab/Igor API/API/Igor_OpenRefnum.vi"
File 12="user.lib/Levylab/Igor API/API/Igor_SaveArrayToFile.vi"
File 13="user.lib/Levylab/Igor API/API/Igor_SaveWavesToFile.vi"
File 14="user.lib/Levylab/Igor API/API/Igor_SendCommand.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_Igor_API.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
