[Package]
Name="levylab_lib_cryostation_instrument"
Version="1.1.7.15"
Release=""
ID=41b7e5a0b38e5a6840577dd4735d3016
File Format="vip"
Format Version="2017"
Display Name="Cryostation"


[Description]
Description="Program for logging Montana Instruments Cryostation status to the DSC. Provides a UI and API for getting information from the Cryostation."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2021, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.1.7]\0D\0A- Update to Instrument v1.8.3.102"
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
Requires="jki_lib_caraya>=1.1.0.119,jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.3.0.56,lava_lib_ui_tools>=1.4.1.74,lvh_toolbox>=2.0.0.35,mgi_lib_application_control>=1.1.1.10,mgi_lib_cluster>=1.1.0.1,mgi_lib_error_handling>=1.1.1.3,mgi_lib_error_reporter>=1.0.2.5,mgi_lib_file>=1.1.0.4,mgi_lib_picture_&_image>=1.0.2.1,mgi_lib_read_write_anything>=2.1.4.4,mgi_lib_string>=1.1.1.5,national_instruments_lib_guid_generator>=1.0.2.3,ni_lib_stm>=3.1.0.9,oglib_appcontrol>=4.1.0.7,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=5.0.0.27,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3,oglib_variantconfig>=4.0.0.5,levylab_lib_levylab_instruments>=1.8.3.102"
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
Num Files=31
File 0="user.lib/LevyLab/Cryostation/Cryostation Monitor and Control.vi"
File 1="user.lib/LevyLab/Cryostation/Cryostation_inst.lvproj"
File 2="user.lib/LevyLab/Cryostation/instrument.Cryostation UI/Instrument UI.Cryostation.lvclass"
File 3="user.lib/LevyLab/Cryostation/instrument.Cryostation UI/Launch Cryostation UI.vi"
File 4="user.lib/LevyLab/Cryostation/instrument.Cryostation UI/Process.vi"
File 5="user.lib/LevyLab/Cryostation/instrument.Cryostation/instrument.Cryostation.lvclass"
File 6="user.lib/LevyLab/Cryostation/instrument.Cryostation/instrument.Cryostation.TestLauncher.vi"
File 7="user.lib/LevyLab/Cryostation/instrument.Cryostation/Process.vi"
File 8="user.lib/LevyLab/Cryostation/instrument.Cryostation/Typedefs/Cryostation.Commands--enum.ctl"
File 9="user.lib/LevyLab/Cryostation/instrument.Cryostation/Typedefs/Cryostation.getAll--cluster.ctl"
File 10="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/All Unit Tests.vi"
File 11="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Client.vi"
File 12="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Command Enum to String.vi"
File 13="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get Chamber Pressure.vi"
File 14="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get DBL.vi"
File 15="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get Platform Temperature.vi"
File 16="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get Sample Temperature.vi"
File 17="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get Stage 1 Temperature.vi"
File 18="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get Stage 2 Temperature.vi"
File 19="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Prepend Length.vi"
File 20="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Unit Test.vi"
File 21="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Close Instrument.vi"
File 22="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Get SMO Name.vi"
File 23="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Get SMO PGSQL Log Paths.vi"
File 24="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Get SMO Port.vi"
File 25="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Get SMO Public API.vi"
File 26="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/getAll.vi"
File 27="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Handle Command.vi"
File 28="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Open Instrument.vi"
File 29="user.lib/LevyLab/Cryostation/instrument.Cryostation/API/Get Temperature.vi"
File 30="user.lib/LevyLab/Cryostation/instrument.Cryostation/API/Open.vi"


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
