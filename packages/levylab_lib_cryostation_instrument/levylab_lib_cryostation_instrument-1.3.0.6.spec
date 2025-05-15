[Package]
Name="levylab_lib_cryostation_instrument"
Version="1.3.0.6"
Release=""
ID=6178a81bd87e6246bc5b21888cbf7036
File Format="vip"
Format Version="2017"
Display Name="Cryostation"


[Description]
Description="Program for logging Montana Instruments Cryostation status to the SQL DB. Provides a UI and API for getting information from the Cryostation."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2025, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="- Update to Instrument Framework v1.15.1"
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
Requires="levylab_lib_levylab_instruments>=1.15.1.34"
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
Num Files=44
File 0="user.lib/LevyLab/Cryostation/Cryostation Monitor and Control.vi"
File 1="user.lib/LevyLab/Cryostation/instrument.Cryostation UI/Instrument UI.Cryostation.lvclass"
File 2="user.lib/LevyLab/Cryostation/instrument.Cryostation UI/Launch Cryostation UI.vi"
File 3="user.lib/LevyLab/Cryostation/instrument.Cryostation UI/Process.vi"
File 4="user.lib/LevyLab/Cryostation/instrument.Cryostation/instrument.Cryostation.lvclass"
File 5="user.lib/LevyLab/Cryostation/instrument.Cryostation/instrument.Cryostation.TestLauncher.vi"
File 6="user.lib/LevyLab/Cryostation/instrument.Cryostation/Process.vi"
File 7="user.lib/LevyLab/Cryostation/instrument.Cryostation/Typedefs/Cryostation.COM-DBL--combo.ctl"
File 8="user.lib/LevyLab/Cryostation/instrument.Cryostation/Typedefs/Cryostation.COM-STR--combo.ctl"
File 9="user.lib/LevyLab/Cryostation/instrument.Cryostation/Typedefs/Cryostation.Commands--enum.ctl"
File 10="user.lib/LevyLab/Cryostation/instrument.Cryostation/Typedefs/Cryostation.getAll--cluster.ctl"
File 11="user.lib/LevyLab/Cryostation/instrument.Cryostation/Typedefs/PublicEvents--Cluster.ctl"
File 12="user.lib/LevyLab/Cryostation/instrument.Cryostation/tests/Test All Drivers.vi"
File 13="user.lib/LevyLab/Cryostation/instrument.Cryostation/tests/Test Each Driver.vi"
File 14="user.lib/LevyLab/Cryostation/instrument.Cryostation/tests/Test Get All.vi"
File 15="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Client.vim"
File 16="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get Chamber Pressure.vi"
File 17="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get DBL (All).vi"
File 18="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get DBL.vi"
File 19="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get Platform Temperature.vi"
File 20="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get Sample Temperature.vi"
File 21="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get Stage 1 Temperature.vi"
File 22="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get Stage 2 Temperature.vi"
File 23="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get STR (All).vi"
File 24="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get STR.vi"
File 25="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.getAll.vi"
File 26="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.GetAlltoStatusString.vi"
File 27="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Prepend Length.vi"
File 28="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.sendMessageFromProcess.vi"
File 29="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Close Hardware.vi"
File 30="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/CreatePublicEvents.vi"
File 31="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Get SMO Database Paths.vi"
File 32="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Get SMO Name.vi"
File 33="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Get SMO Port.vi"
File 34="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Get SMO Public API.vi"
File 35="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Handle Command.vi"
File 36="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Handle getAll.vi"
File 37="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Handle setAllData.vi"
File 38="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Open Hardware.vi"
File 39="user.lib/LevyLab/Cryostation/instrument.Cryostation/API/Close.vi"
File 40="user.lib/LevyLab/Cryostation/instrument.Cryostation/API/Cryostation.GetPublicEvents.vi"
File 41="user.lib/LevyLab/Cryostation/instrument.Cryostation/API/Get Temperature.vi"
File 42="user.lib/LevyLab/Cryostation/instrument.Cryostation/API/getTemperature.vi"
File 43="user.lib/LevyLab/Cryostation/instrument.Cryostation/API/Open.vi"


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
