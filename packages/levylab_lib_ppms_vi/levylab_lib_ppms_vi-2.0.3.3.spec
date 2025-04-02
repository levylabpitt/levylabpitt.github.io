[Package]
Name="levylab_lib_ppms_vi"
Version="2.0.3.3"
Release=""
ID=ef218f8a2fe541e3d76b9cb1e20dc516
File Format="vip"
Format Version="2010"
Display Name="PPMS VI"


[Description]
Description=""
Summary=""
License=""
Copyright="Copyright (c) 2013, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="voodoo"
Demo="FALSE"
Release Notes=""
System Package="FALSE"


[Platform]
Exclusive_LabVIEW_Version=">=11.0"
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
Requires="levylab_lib_daq_lockin_subvi>=2.0.0.2,levylab_lib_pickering>=4.0.0.7,levylab_lib_ppms_daq_femto>=1.0.0.2,levylab_lib_ppms_remote>=2.0.1.3"
Conflicts=""


[Activation]
License File=""
Licensed Library=""


[Files]
Num File Groups="2"
Sub-Packages=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=33
File 0="user.lib/Levylab/PPMS VI/B_sweep_3ch_DR_v2.1.vi"
File 1="user.lib/Levylab/PPMS VI/B_sweep_versus time_3ch_DR_v2.1.vi"
File 2="user.lib/Levylab/PPMS VI/data2string.vi"
File 3="user.lib/Levylab/PPMS VI/Display.vi"
File 4="user.lib/Levylab/PPMS VI/Filter IV Data-3VoltageAmp.vi"
File 5="user.lib/Levylab/PPMS VI/Four_terminal_IV_3VoltageAmp_3.1.vi"
File 6="user.lib/Levylab/PPMS VI/Get data time.vi"
File 7="user.lib/Levylab/PPMS VI/Get Terminal Name with Device Prefix.vi"
File 8="user.lib/Levylab/PPMS VI/Image Loader.vi"
File 9="user.lib/Levylab/PPMS VI/Lock-in Globles.vi"
File 10="user.lib/Levylab/PPMS VI/Lock-in_dem_mul.vi"
File 11="user.lib/Levylab/PPMS VI/Lockin-4461_3.0.vi"
File 12="user.lib/Levylab/PPMS VI/OSC Waveform.vi"
File 13="user.lib/Levylab/PPMS VI/Read current vs temperature_3ch_2.1.vi"
File 14="user.lib/Levylab/PPMS VI/Read PPMS T and B.vi"
File 15="user.lib/Levylab/PPMS VI/Reference_new version_1.0.vi"
File 16="user.lib/Levylab/PPMS VI/refresh Vbg.vi"
File 17="user.lib/Levylab/PPMS VI/Remote control B.vi"
File 18="user.lib/Levylab/PPMS VI/Remote control T.vi"
File 19="user.lib/Levylab/PPMS VI/Stream IV Data - 3VoltageAmp.vi"
File 20="user.lib/Levylab/PPMS VI/Stream_lock_in_data.vi"
File 21="user.lib/Levylab/PPMS VI/Sweep control.vi"
File 22="user.lib/Levylab/PPMS VI/Vbg_sweep_for_different_configs.vi"
File 23="user.lib/Levylab/PPMS VI/WaitUntilBwithin5Oe.vi"
File 24="user.lib/Levylab/PPMS VI/SubVI/Bias_adjustment.vi"
File 25="user.lib/Levylab/PPMS VI/SubVI/Generate sorted scan parameters.vi"
File 26="user.lib/Levylab/PPMS VI/SubVI/GV.vi"
File 27="user.lib/Levylab/PPMS VI/SubVI/ITX_Global.vi"
File 28="user.lib/Levylab/PPMS VI/SubVI/Post action control.vi"
File 29="user.lib/Levylab/PPMS VI/SubVI/PPMS Dashboard.glb.vi"
File 30="user.lib/Levylab/PPMS VI/SubVI/Scale Voltage.vi"
File 31="user.lib/Levylab/PPMS VI/SubVI/Scan action control.vi"
File 32="user.lib/Levylab/PPMS VI/SubVI/Voltage Update.vi"


[File Group 1]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=2
File 0="_functions_levylab_lib_ppms_vi_1.mnu"
File 1="functions_levylab_lib_ppms_vi.mnu"
