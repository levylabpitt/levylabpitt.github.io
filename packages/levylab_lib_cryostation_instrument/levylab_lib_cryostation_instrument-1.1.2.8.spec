[Package]
Name="levylab_lib_cryostation_instrument"
Version="1.1.2.8"
Release=""
ID=d05fc5a8c1d546a2119a31b2735dcdab
File Format="vip"
Format Version="2017"
Display Name="Cryostation"


[Description]
Description="Program for logging Montana Instruments Cryostation status to the DSC. Provides a UI and API for getting information from the Cryostation."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2020, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.1.2.8]\0A- update to work with Instrument v1.5.8.70"
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
Requires="levylab_lib_levylab_instruments>=1.4.1.52"
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
Num Files=29
File 0="user.lib/LevyLab/Cryostation/Cryostation Monitor and Control.vi"
File 1="user.lib/LevyLab/Cryostation/Cryostation_inst.lvproj"
File 2="user.lib/LevyLab/Cryostation/instrument.Cryostation UI/Instrument.Cryostation UI.lvclass"
File 3="user.lib/LevyLab/Cryostation/instrument.Cryostation UI/Launch Cryostation UI.vi"
File 4="user.lib/LevyLab/Cryostation/instrument.Cryostation UI/Process.vi"
File 5="user.lib/LevyLab/Cryostation/instrument.Cryostation/Close Instrument.vi"
File 6="user.lib/LevyLab/Cryostation/instrument.Cryostation/Get SMO Name.vi"
File 7="user.lib/LevyLab/Cryostation/instrument.Cryostation/Get SMO Port.vi"
File 8="user.lib/LevyLab/Cryostation/instrument.Cryostation/Get SMO Public API.vi"
File 9="user.lib/LevyLab/Cryostation/instrument.Cryostation/Get Temperature.vi"
File 10="user.lib/LevyLab/Cryostation/instrument.Cryostation/getAll.vi"
File 11="user.lib/LevyLab/Cryostation/instrument.Cryostation/Handle Command.vi"
File 12="user.lib/LevyLab/Cryostation/instrument.Cryostation/Instrument.Cryostation.getAll.vi"
File 13="user.lib/LevyLab/Cryostation/instrument.Cryostation/instrument.Cryostation.lvclass"
File 14="user.lib/LevyLab/Cryostation/instrument.Cryostation/instrument.Cryostation.TestLauncher.vi"
File 15="user.lib/LevyLab/Cryostation/instrument.Cryostation/Open Instrument.vi"
File 16="user.lib/LevyLab/Cryostation/instrument.Cryostation/Process.vi"
File 17="user.lib/LevyLab/Cryostation/instrument.Cryostation/Typedefs/Commands-enum.ctl"
File 18="user.lib/LevyLab/Cryostation/instrument.Cryostation/Typedefs/getAll--Cryostation--cluster.ctl"
File 19="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/instrument.Cryostation.Client.vi"
File 20="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/MI.Get Chamber Pressure.vi"
File 21="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/MI.Get DBL.vi"
File 22="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/MI.Get Platform Temperature.vi"
File 23="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/MI.Get Sample Temperature.vi"
File 24="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/MI.Get Stage 1 Temperature.vi"
File 25="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/MI.Get Stage 2 Temperature.vi"
File 26="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/MI.PrependLength.vi"
File 27="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Test.vi"
File 28="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Unit Tests.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=1
File 0="functions_LevyLab_lib_Cryostation_Instrument.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
