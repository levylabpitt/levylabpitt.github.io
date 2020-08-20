[Package]
Name="levylab_lib_lockin_multichannel"
Version="2.11.7.33"
Release=""
ID=6ecac4bfa4f9d9e4f55a1fd618115e69
File Format="vip"
Format Version="2017"
Display Name="Multichannel Lockin"


[Description]
Description="Multichannel Lockin for National Instruments' Dynamic Signal Acquisition hardware (4431, 4461, 4462). This version is configured to handle multiple cards (up to 16) for simultaneous, synchronized AI/AO. You can configure a number of analog outputs (up to 32) to output sine, square, sawtooth, or triangle functions with DC offsets. Each of the analog inputs (up to 32) can be demodulated at multiple frequencies."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2020, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[2.11.7]\0A- Build with Instrument Framework v1.5.17\0A- Build for LV 2016\0A- Note: This release includes only the LabVIEW API, not the lockin application.\0A- To get the lockin application, go to: https://github.com/levylabpitt/Multichannel-Lockin/releases/latest"
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
Requires="jki_lib_json_serialization>=1.1.10.37,jki_lib_serialization>=1.0.1.14,jki_lib_state_machine>=2018.0.7.45,jki_lib_unicode>=1.0.0.7,jki_statemachineobjects>=1.3.0.56,lava_lib_ui_tools>=1.4.1.74,levylab_lib_control_vi>=1.3.0.11,levylab_lib_fileutilities>=1.2.5.12,levylab_lib_lvtoitx>=2.8.2.13,levylab_lib_voltage_update>=1.0.3.5,levylab_lib_xy_utilities>=1.1.1.10,mgi_lib_application_control>=1.1.1.10,mgi_lib_cluster>=1.1.0.1,mgi_lib_error_handling>=1.1.1.3,mgi_lib_error_reporter>=1.0.2.5,mgi_lib_file>=1.1.0.4,mgi_lib_numeric>=1.1.0.2,mgi_lib_picture_&_image>=1.0.2.1,mgi_lib_read_write_anything>=2.1.4.4,mgi_lib_string>=1.1.1.5,mgi_lib_timing>=1.1.0.2,national_instruments_lib_guid_generator>=1.0.2.3,ni_lib_stm>=3.1.0.9,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_dictionary>=4.0.0.4,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=4.2.0.21,oglib_numeric>=4.1.0.8,oglib_string>=4.1.0.12,oglib_time>=4.0.1.3,oglib_variantconfig>=4.0.0.5,wireflow_ab_lib_wf_progressbar>=1.0.2.56,labview-zmq>=3.5.1.109,levylab_lib_levylab_instruments>=1.5.15.77"
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
File 0="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getAI.vi"
File 1="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getAO.vi"
File 2="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getAOconfig.vi"
File 3="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getAutoSampling.vi"
File 4="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getAUX.vi"
File 5="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getGain.vi"
File 6="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getIVmode.vi"
File 7="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getIVSweepResults.vi"
File 8="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getREFconfig.vi"
File 9="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getRefreshTime.vi"
File 10="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getResults.vi"
File 11="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getSampling.vi"
File 12="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getStatus.vi"
File 13="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getSweepResults.vi"
File 14="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getTrigger.vi"
File 15="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/Open.vi"
File 16="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/reset.vi"
File 17="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setAIDAQ.vi"
File 18="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setAO.vi"
File 19="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setAO_Amp.vi"
File 20="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setAO_DC.vi"
File 21="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setAO_f.vi"
File 22="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setAO_function.vi"
File 23="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setAO_phi.vi"
File 24="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setAODAQ.vi"
File 25="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setAutoSampling.vi"
File 26="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setAUX.vi"
File 27="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setGain.vi"
File 28="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setIVmodeConfig.vi"
File 29="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setREF.vi"
File 30="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setREF_f.vi"
File 31="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setREF_phi.vi"
File 32="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setSampling.vi"
File 33="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setSweepConfiguration.vi"
File 34="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/startIVAndWait.vi"
File 35="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/startIVSweepAndWait.vi"
File 36="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/startSweep.vi"
File 37="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/startSweepAndWait.vi"
File 38="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/stopSweep.vi"
File 39="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/trigger.vi"
File 40="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/waitForNewResults.vi"
File 41="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/waitForNewWaveforms.vi"
File 42="examples/LevyLab/Multichannel Lockin/Examples/Example_IV_Curves.vi"
File 43="examples/LevyLab/Multichannel Lockin/Examples/Example_Lockin.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=2
File 0="_functions_levylab_lib_lockin_multichannel_1.mnu"
File 1="functions_LevyLab_lib_Lockin_Multichannel.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
