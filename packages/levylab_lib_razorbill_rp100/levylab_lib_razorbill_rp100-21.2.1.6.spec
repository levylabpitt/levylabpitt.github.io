[Package]
Name="levylab_lib_razorbill_rp100"
Version="21.2.1.6"
Release=""
ID=b283b888ed48489219f340ea3c0d237f
File Format="vip"
Format Version="2017"
Display Name="Razorbill RP100"


[Description]
Description="Divers for Razorbill RP100 HV amplifier"
Summary=""
License=""
Copyright="Copyright (c) 2021, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[21.2.1]\0A- Update to  IF 1.10.3"
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
Requires="jki_statemachineobjects>=1.4.0.63,oglib_time>=4.0.1.3,levylab_lib_levylab_instruments>=1.9.1.1"
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
Num Files=34
File 0="user.lib/Levylab/Razorbill RP100/razorbill.lvproj"
File 1="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Process.vi"
File 2="user.lib/Levylab/Razorbill RP100/SMOs/RP100/RP100.lvclass"
File 3="user.lib/Levylab/Razorbill RP100/SMOs/RP100/RP100.TestLauncher.vi"
File 4="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Typedefs/Commands--Enum.ctl"
File 5="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Typedefs/getAll.ctl"
File 6="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Typedefs/Output Channel--Enum.ctl"
File 7="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Typedefs/Output State--Enum.ctl"
File 8="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Typedefs/setLevel--Cluster.ctl"
File 9="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Typedefs/setStrain--Cluster.ctl"
File 10="user.lib/Levylab/Razorbill RP100/SMOs/RP100/private/convert V to d.vi"
File 11="user.lib/Levylab/Razorbill RP100/SMOs/RP100/private/RP100.Remote Client.vim"
File 12="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Methods (Overrides)/Get SMO Name.vi"
File 13="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Methods (Overrides)/Get SMO PGSQL Log Paths.vi"
File 14="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Methods (Overrides)/Get SMO Port.vi"
File 15="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Methods (Overrides)/Get SMO Public API.vi"
File 16="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Methods (Overrides)/Handle Command.vi"
File 17="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Methods (Overrides)/Handle getAll.vi"
File 18="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/RP100.CLS.vi"
File 19="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/RP100.Get Level.vi"
File 20="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/RP100.Get Output State.vi"
File 21="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/RP100.Get Slew.vi"
File 22="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/RP100.IDN.vi"
File 23="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/RP100.Measure Current.vi"
File 24="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/RP100.Measure Voltage.vi"
File 25="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/RP100.RST.vi"
File 26="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/RP100.Set Level.vi"
File 27="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/RP100.Set Output State.vi"
File 28="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/RP100.Set Slew.vi"
File 29="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/subVIs/RP100.VISA RW.vi"
File 30="user.lib/Levylab/Razorbill RP100/SMOs/RP100/API/Get Level.vi"
File 31="user.lib/Levylab/Razorbill RP100/SMOs/RP100/API/Get Strain.vi"
File 32="user.lib/Levylab/Razorbill RP100/SMOs/RP100/API/Set Level.vi"
File 33="user.lib/Levylab/Razorbill RP100/SMOs/RP100/API/Set Strain.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_Razorbill_RP100.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"