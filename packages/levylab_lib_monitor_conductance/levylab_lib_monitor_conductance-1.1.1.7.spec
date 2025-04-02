[Package]
Name="levylab_lib_monitor_conductance"
Version="1.1.1.7"
Release=""
ID=192c4ca758106359487350d8e7711b42
File Format="vip"
Format Version="2014"
Display Name="Monitor Conductance"


[Description]
Description=""
Summary=""
License=""
Copyright="Copyright (c) 2014, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Ishan Levy"
Demo="FALSE"
Release Notes="Shicheng version with visual modification"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="FALSE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"


[Platform]
Exclusive_LabVIEW_Version="LabVIEW>=13.0"
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
Requires="levylab_lib_linecut_linefit>=2.1.4.21,levylab_lib_lvtoitx>=2.4.1.7"
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
Num Files=75
File 0="vi.lib/LevyLab/Monitor Conductance/DefinedSignal.lvm"
File 1="vi.lib/LevyLab/Monitor Conductance/DirExists-NoThenCreate.vi"
File 2="vi.lib/LevyLab/Monitor Conductance/Domain Finder.vi"
File 3="vi.lib/LevyLab/Monitor Conductance/Format number_123456.vi"
File 4="vi.lib/LevyLab/Monitor Conductance/increment filename.vi"
File 5="vi.lib/LevyLab/Monitor Conductance/Linecut Linefit.vi"
File 6="vi.lib/LevyLab/Monitor Conductance/LV to ITX 2.2 ITX2.vi"
File 7="vi.lib/LevyLab/Monitor Conductance/LV to ITX AutoPlot.vi"
File 8="vi.lib/LevyLab/Monitor Conductance/LVITX append letter to filename.vi"
File 9="vi.lib/LevyLab/Monitor Conductance/LVITX Format Path&Filename.vi"
File 10="vi.lib/LevyLab/Monitor Conductance/LVITX ITX2 Plot Commands.vi"
File 11="vi.lib/LevyLab/Monitor Conductance/Monitor Conductance - 4Terminal.vi"
File 12="vi.lib/LevyLab/Monitor Conductance/Monitor Conductance.vi"
File 13="vi.lib/LevyLab/Monitor Conductance/Restrict X Domain of Graph.vi"
File 14="vi.lib/LevyLab/Monitor Conductance/sfpCore Hue to RGB.vi"
File 15="vi.lib/LevyLab/Monitor Conductance/SR5302 Configure DAC Voltages"
File 16="vi.lib/LevyLab/Monitor Conductance/SR5302 Configure Reference Channel"
File 17="vi.lib/LevyLab/Monitor Conductance/SR5302 VISA Write-Read"
File 18="vi.lib/LevyLab/Monitor Conductance/SR830 Monitor.vi"
File 19="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Stanford Research 830 Readme.html"
File 20="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Stanford Research 830.lvlib"
File 21="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Stanford Research 830.lvproj"
File 22="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Close.vi"
File 23="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/dir.mnu"
File 24="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Initialize.vi"
File 25="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/VI Tree.vi"
File 26="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Utility/Error Query.vi"
File 27="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Utility/Reset.vi"
File 28="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Utility/Revision Query.vi"
File 29="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Utility/Utility.mnu"
File 30="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Data/Data.mnu"
File 31="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Data/Read (1 Parameter).vi"
File 32="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Data/Read (All Parameters).vi"
File 33="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Data/Read (Multiple Points).vi"
File 34="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Data/Read.vi"
File 35="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Data/Low Level/Abort.vi"
File 36="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Data/Low Level/Data_Low Level.mnu"
File 37="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Data/Low Level/Fetch Buffer.vi"
File 38="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Data/Low Level/Pause.vi"
File 39="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Data/Low Level/Send Software Trigger.vi"
File 40="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Data/Low Level/Start.vi"
File 41="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Data/Low Level/Wait for Acquisition Complete.vi"
File 42="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Configure/Configure Acquisition.vi"
File 43="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Configure/Configure Aux Ouput.vi"
File 44="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Configure/Configure Channel Display.vi"
File 45="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Configure/Configure Channel Expand and Offset.vi"
File 46="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Configure/Configure Channel Output.vi"
File 47="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Configure/Configure Filter.vi"
File 48="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Configure/Configure Input Signal.vi"
File 49="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Configure/Configure Reference.vi"
File 50="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Configure/Configure Sensitivity and Reserve.vi"
File 51="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Configure/Configure.mnu"
File 52="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Configure/Low Level/Configure Trigger.vi"
File 53="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Configure/Low Level/Configure_Low Level.mnu"
File 54="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Action-Status/Action-Status.mnu"
File 55="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Public/Action-Status/Save Recall Setup.vi"
File 56="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Private/Default Instrument Setup.vi"
File 57="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Private/Query Error Status.vi"
File 58="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Private/Query Lock In Amplifier Status.vi"
File 59="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Private/Query Standard Event Status.vi"
File 60="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Examples/Stanford Research 830 Acquire Measurement - 1 Parameter.vi"
File 61="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Examples/Stanford Research 830 Acquire Measurement - All Parameters.vi"
File 62="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Examples/Stanford Research 830 Acquire Measurement - Multiple Points - SW Triggered.vi"
File 63="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Examples/Stanford Research 830 Acquire Measurement - Multiple Points.vi"
File 64="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Examples/Stanford Research 830 Expand Offset and Output Channel.vi"
File 65="vi.lib/LevyLab/Monitor Conductance/Stanford Research 830/Examples/Stanford Research 830.bin3"
File 66="vi.lib/LevyLab/Monitor Conductance/Four Terminal Characterization/AnalyzeIV_ITX_MFP3D.vi"
File 67="vi.lib/LevyLab/Monitor Conductance/Four Terminal Characterization/Four Terminal Characterization.lvproj"
File 68="vi.lib/LevyLab/Monitor Conductance/Four Terminal Characterization/IV_sweep AC amp.vi"
File 69="vi.lib/LevyLab/Monitor Conductance/Four Terminal Characterization/IV_sweep DC amp.vi"
File 70="vi.lib/LevyLab/Monitor Conductance/Four Terminal Characterization/Monitor_Conductance.vi"
File 71="vi.lib/LevyLab/Monitor Conductance/Four Terminal Characterization/Monitor_Conductance_1.1.vi"
File 72="vi.lib/LevyLab/Monitor Conductance/Four Terminal Characterization/Read_DAQ_1CH.vi"
File 73="vi.lib/LevyLab/Monitor Conductance/Four Terminal Characterization/Read_DAQ_2CH.vi"
File 74="vi.lib/LevyLab/Monitor Conductance/Four Terminal Characterization/Two CH Acq.vi"


[File Group 1]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=2
File 0="_functions_levylab_lib_monitor_conductance_1.mnu"
File 1="functions_LevyLab_lib_Monitor_Conductance.mnu"


[File Group 2]
Target Dir="<menus>/Controls"
Replace Mode="Always"
Num Files=1
File 0="controls_LevyLab_lib_Monitor_Conductance.mnu"
