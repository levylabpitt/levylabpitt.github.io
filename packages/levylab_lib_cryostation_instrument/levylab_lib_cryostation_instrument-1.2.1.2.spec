[Package]
Name="levylab_lib_cryostation_instrument"
Version="1.2.1.2"
Release=""
ID=55099bfbe19526e4887529112b9c669e
File Format="vip"
Format Version="2017"
Display Name="Cryostation"


[Description]
Description="Program for logging Montana Instruments Cryostation status to the SQL DB. Provides a UI and API for getting information from the Cryostation."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2021, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.2.1]\0A- Update Instrument Framework v1.9.2\0A"
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
Requires="jdp_science_jsontext>=1.6.5.105,jdp_science_lib_common_utilities>=1.3.0.14,jdp_science_postgresql>=0.3.4.22,jki_lib_caraya>=1.2.1.131,jki_lib_json_serialization>=1.1.10.37,jki_lib_serialization>=1.0.1.14,jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.4.0.63,labview-zmq>=3.6.1.111,lava_lib_ui_tools>=1.4.1.74,levylab_lib_fileutilities>=1.2.6.13,levylab_lib_graph_utilities>=2.1.7.10,levylab_lib_lvtoitx>=3.1.0.1,levylab_lib_xy_utilities>=1.4.0.17,lvh_toolbox>=2.0.0.35,mgi_lib_1d_array>=1.0.2.3,mgi_lib_application_control>=1.1.1.10,mgi_lib_cluster>=1.1.0.1,mgi_lib_error_handling>=1.1.1.3,mgi_lib_error_reporter>=1.0.2.5,mgi_lib_file>=1.1.0.4,mgi_lib_numeric>=1.1.0.2,mgi_lib_picture_&_image>=1.0.2.1,mgi_lib_read_write_anything>=2.1.4.4,mgi_lib_string>=1.1.1.5,national_instruments_lib_guid_generator>=1.0.2.3,ni_lib_stm>=3.1.0.9,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_dictionary>=4.0.0.4,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=5.0.0.27,oglib_lvzip>=4.0.1,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3,oglib_variantconfig>=4.0.0.5,levylab_lib_levylab_instruments>=1.9.2.1"
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
Num Files=35
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
File 15="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get DBL.vi"
File 16="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get Platform Temperature.vi"
File 17="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get Sample Temperature.vi"
File 18="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get Stage 1 Temperature.vi"
File 19="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get Stage 2 Temperature.vi"
File 20="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Get STR.vi"
File 21="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Cryostation.Prepend Length.vi"
File 22="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Test Get All.vi"
File 23="user.lib/LevyLab/Cryostation/instrument.Cryostation/private/Unit Test.vi"
File 24="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Close Instrument.vi"
File 25="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Get SMO Name.vi"
File 26="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Get SMO PGSQL Log Paths.vi"
File 27="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Get SMO Port.vi"
File 28="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Get SMO Public API.vi"
File 29="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/getAll.vi"
File 30="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Handle Command.vi"
File 31="user.lib/LevyLab/Cryostation/instrument.Cryostation/Overrides/Open Instrument.vi"
File 32="user.lib/LevyLab/Cryostation/instrument.Cryostation/API/Cryostation.GET ALL.vi"
File 33="user.lib/LevyLab/Cryostation/instrument.Cryostation/API/Get Temperature.vi"
File 34="user.lib/LevyLab/Cryostation/instrument.Cryostation/API/Open.vi"


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
