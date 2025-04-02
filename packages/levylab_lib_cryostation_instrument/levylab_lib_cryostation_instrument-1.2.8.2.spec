[Package]
Name="levylab_lib_cryostation_instrument"
Version="1.2.8.2"
Release=""
ID=c9e40a65fbe9418b4eb588010857538a
File Format="vip"
Format Version="2017"
Display Name="Cryostation"


[Description]
Description="Program for logging Montana Instruments Cryostation status to the SQL DB. Provides a UI and API for getting information from the Cryostation."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2022, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="- update to Instrument Framework v1.12"
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
Requires="levylab_lib_levylab_instruments>=1.12.0.5"
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
Num Files=37
File 0="user.lib/LevyLab/Cryostation/Cryostation Monitor and Control.vi"
File 1="user.lib/LevyLab/Cryostation/Cryostation_inst.lvproj"
File 2="user.lib/LevyLab/Cryostation/instrument.Cryostation UI/Instrument UI.Cryostation.lvclass"
File 3="user.lib/LevyLab/Cryostation/instrument.Cryostation UI/Launch Cryostation UI.vi"
File 4="user.lib/LevyLab/Cryostation/instrument.Cryostation UI/Process.vi"
File 5="user.lib/LevyLab/Cryostation/instrument.Cryostation/instrument.Cryostation.lvclass"
File 6="user.lib/LevyLab/Cryostation/instrument.Cryostation/instrument.Cryostation.TestLauncher.vi"
File 7="user.lib/LevyLab/Cryostation/instrument.Cryostation/Process.vi"
File 8="user.lib/LevyLab/Cryostation/instrument.Cryostation/Typedefs/Cryostation.COM-DBL--combo.ctl"
File 9="user.lib/LevyLab/Cryostation/instrument.Cryostation/Typedefs/Cryostation.COM-STR--combo.ctl"
File 10="user.lib/LevyLab/Cryostation/instrument.Cryostation/Typedefs/Cryostation.Commands--enum.ctl"
File 11="user.lib/LevyLab/Cryostation/instrument.Cryostation/Typedefs/Cryostation.getAll--cluster.ctl"
File 12="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/All Unit Tests.vi"
File 13="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Client.vim"
File 14="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get Chamber Pressure.vi"
File 15="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get DBL (All).vi"
File 16="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get DBL.vi"
File 17="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get Platform Temperature.vi"
File 18="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get Sample Temperature.vi"
File 19="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get Stage 1 Temperature.vi"
File 20="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get Stage 2 Temperature.vi"
File 21="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get STR (All).vi"
File 22="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get STR.vi"
File 23="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Prepend Length.vi"
File 24="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Test Get All.vi"
File 25="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Unit Test.vi"
File 26="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Close Hardware.vi"
File 27="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Get SMO Name.vi"
File 28="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Get SMO PGSQL Log Paths.vi"
File 29="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Get SMO Port.vi"
File 30="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Get SMO Public API.vi"
File 31="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Handle Command.vi"
File 32="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Handle getAll.vi"
File 33="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Open Hardware.vi"
File 34="user.lib/LevyLab/Cryostation/instrument.Cryostation/API/Close.vi"
File 35="user.lib/LevyLab/Cryostation/instrument.Cryostation/API/Get Temperature.vi"
File 36="user.lib/LevyLab/Cryostation/instrument.Cryostation/API/Open.vi"


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
