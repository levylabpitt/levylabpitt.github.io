[Package]
Name="oxford_lib_mercury_ixx_system"
Version="2.0.0.6"
Release=""
ID=ef184446e47a1e2bf969b519bd3d6690
File Format="vip"
Format Version="2017"
Display Name="Mercury iXX (System)"


[Description]
Description="A library of  VIs for NI LabVIEW used to built simple application to communicate with Mercury system or complex graphical interfaces to take advantage of full system functionality."
Summary=""
License=""
Copyright="Copyright (c) 2016, Oxford"
Distribution=""
Vendor="Oxford"
URL="https://mymercurysupport.com"
Packager="Oxford Instruments"
Demo="FALSE"
Release Notes="An updated revision of the Mercury LabVIEW function library containing new features, many new examples and many bug fixes.  It can be used with LV 13.0f2 or later and Mercury firmware 2.0 or later. "
System Package="TRUE"
Sub Package="TRUE"
License Agreement="FALSE"


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
Requires=""
Conflicts=""


[Activation]
License File=""
Licensed Library=""


[Files]
Num File Groups="1"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<temp>"
Replace Mode="Always"
Num Files=3
File 0="Mercury iXX/Mercury iXX.zip"
File 1="Mercury iXX/Post-Install Custom Action.vi"
File 2="Mercury iXX/Unzip-Mercury-iXX.vi"
