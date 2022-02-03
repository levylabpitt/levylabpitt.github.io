[Package]
Name="levylab_lib_ah2500a"
Version="1.1.3.1"
Release=""
ID=c1a963c14f3eafa4db05dce877cc50a7
File Format="vip"
Format Version="2017"
Display Name="AH2500A"


[Description]
Description="LabVIEW drivers for Andeen-Hagerling 2500A capacitance bridge"
Summary=""
License=""
Copyright="Copyright (c) 2022, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="- Update to Instrument Framework v1.11.2.1"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="FALSE"


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
Requires="levylab_lib_levylab_instruments>=1.11.2.1"
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
Num Files=11
File 0="user.lib/Levylab/AH2500A/AH2500A.lvproj"
File 1="user.lib/Levylab/AH2500A/SMOs/AH2500A/AH2500A.lvclass"
File 2="user.lib/Levylab/AH2500A/SMOs/AH2500A/AH2500A.TestLauncher.vi"
File 3="user.lib/Levylab/AH2500A/SMOs/AH2500A/Process.vi"
File 4="user.lib/Levylab/AH2500A/SMOs/AH2500A/Typedefs/AH2500A Measurement--Cluster.ctl"
File 5="user.lib/Levylab/AH2500A/SMOs/AH2500A/drivers/Read Instrument.vi"
File 6="user.lib/Levylab/AH2500A/SMOs/AH2500A/drivers/Set Average Time.vi"
File 7="user.lib/Levylab/AH2500A/SMOs/AH2500A/drivers/Set DC Bias.vi"
File 8="user.lib/Levylab/AH2500A/SMOs/AH2500A/drivers/Set Max AC voltage.vi"
File 9="user.lib/Levylab/AH2500A/SMOs/AH2500A/drivers/Set Units.vi"
File 10="user.lib/Levylab/AH2500A/SMOs/AH2500A/API/Get Capacitance.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_AH2500A.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
