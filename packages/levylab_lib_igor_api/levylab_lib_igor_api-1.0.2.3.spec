[Package]
Name="levylab_lib_igor_api"
Version="1.0.2.3"
Release=""
ID=cbaa26ccfefd46886f4d49483fc4a680
File Format="vip"
Format Version="2017"
Display Name="Igor API"


[Description]
Description="LabVIEW wrapper to facilitate the use of the text-based Igor Pro ActiveX API."
Summary="LabVIEW wrapper to control Igor Pro with ActiveX"
License="BSD-3"
Copyright="Copyright (c) 2025, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin, Joe Albro"
Demo="FALSE"
Release Notes="[1.0.2.3]\0D\0A- project organization to reduce package depeendencies (move tests into own project)"
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
Requires="oglib_error>=4.2.0.23,oglib_time>=4.0.1.3"
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
Num Files=12
File 0="user.lib/Levylab/Igor API/private/DebugModeSingleton.vi"
File 1="user.lib/Levylab/Igor API/private/Igor_EnsureIgorStringFormat.vi"
File 2="user.lib/Levylab/Igor API/private/Igor_NumericArraytoIgorWave.vi"
File 3="user.lib/Levylab/Igor API/private/Igor_StringArraytoIgorWave.vi"
File 4="user.lib/Levylab/Igor API/API/Igor_ArraytoIgorWave.vi"
File 5="user.lib/Levylab/Igor API/API/Igor_CloseRefnum.vi"
File 6="user.lib/Levylab/Igor API/API/Igor_LoadLargeWaveUsingFile.vi"
File 7="user.lib/Levylab/Igor API/API/Igor_LoadWaveFromFile.vi"
File 8="user.lib/Levylab/Igor API/API/Igor_OpenRefnum.vi"
File 9="user.lib/Levylab/Igor API/API/Igor_SaveArrayToFile.vi"
File 10="user.lib/Levylab/Igor API/API/Igor_SaveWavesToFile.vi"
File 11="user.lib/Levylab/Igor API/API/Igor_SendCommand.vi"


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
