[Package]
Name="levylab_lib_razorbill_rp100"
Version="1.2.0.4"
Release=""
ID=80c3a96ae79a264ef19b6f29b2244e83
File Format="vip"
Format Version="2017"
Display Name="Razorbill RP100"


[Description]
Description="Divers for Razorbill RP100 HV amplifier"
Summary=""
License=""
Copyright="Copyright (c) 2020, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.2.0.4]\0A- Inherit from Instrument.Strain.lvclass\0A- Implement Set Strain and Get Strain methods defined by parent class"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="FALSE"


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
Requires="jki_statemachineobjects>=1.3.0.56,oglib_time>=4.0.1.3,levylab_lib_levylab_instruments>=1.4.1.52"
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
Num Files=22
File 0="user.lib/Levylab/Razorbill RP100/razorbill.lvproj"
File 1="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Process.vi"
File 2="user.lib/Levylab/Razorbill RP100/SMOs/RP100/RP100.lvclass"
File 3="user.lib/Levylab/Razorbill RP100/SMOs/RP100/RP100.TestLauncher.vi"
File 4="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Typedefs/Output Channel--Enum.ctl"
File 5="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Typedefs/Output State--Enum.ctl"
File 6="user.lib/Levylab/Razorbill RP100/SMOs/RP100/subVIs/convert V to d.vi"
File 7="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/CLS.vi"
File 8="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/Get Level.vi"
File 9="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/Get Output State.vi"
File 10="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/Get Slew.vi"
File 11="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/IDN.vi"
File 12="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/Measure Current.vi"
File 13="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/Measure Voltage.vi"
File 14="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/Set Level.vi"
File 15="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/Set Output State.vi"
File 16="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/Set Slew.vi"
File 17="user.lib/Levylab/Razorbill RP100/SMOs/RP100/API/Get Strain.vi"
File 18="user.lib/Levylab/Razorbill RP100/SMOs/RP100/API/Set Strain.vi"
File 19="user.lib/Levylab/Razorbill RP100/SMOs/RP100/API/Source V1 and V2.vi"
File 20="user.lib/Levylab/Razorbill RP100/SMOs/RP100/API/Source V1.vi"
File 21="user.lib/Levylab/Razorbill RP100/SMOs/RP100/API/Source V2.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=2
File 0="_functions_levylab_lib_razorbill_rp100_1.mnu"
File 1="functions_Levylab_lib_Razorbill_RP100.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
