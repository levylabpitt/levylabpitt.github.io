[Package]
Name="levylab_lib_newport_stage"
Version="2.0.1.8"
Release=""
ID=ee6dd9c88fed0483c1d7da88d9cab1d0
File Format="vip"
Format Version="2014"
Display Name="Newport Stage"


[Description]
Description="This program allows you to use a joystick to control the Newport Agilis Controller AG-UC8."
Summary=""
License=""
Copyright="Copyright (c) 2014, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Ishan Levy"
Demo="FALSE"
Release Notes="Documented a bit"
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
Requires=""
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
File 0="vi.lib/LevyLab/Newport Stage/config.inf"
File 1="vi.lib/LevyLab/Newport Stage/Create Config File.vi"
File 2="vi.lib/LevyLab/Newport Stage/Main.vi"
File 3="vi.lib/LevyLab/Newport Stage/Sub-VIs/Arrow Key Direction Retrieve.vi"
File 4="vi.lib/LevyLab/Newport Stage/Sub-VIs/Button Movements.vi"
File 5="vi.lib/LevyLab/Newport Stage/Sub-VIs/Direction to Use.vi"
File 6="vi.lib/LevyLab/Newport Stage/Sub-VIs/Find Joystick.vi"
File 7="vi.lib/LevyLab/Newport Stage/Sub-VIs/Get Axis Values.vi"
File 8="vi.lib/LevyLab/Newport Stage/Sub-VIs/Info.ctl"
File 9="vi.lib/LevyLab/Newport Stage/Sub-VIs/Joystick Movements.vi"
File 10="vi.lib/LevyLab/Newport Stage/Sub-VIs/Joystick to Direction.vi"
File 11="vi.lib/LevyLab/Newport Stage/Sub-VIs/Read Button Data.vi"
File 12="vi.lib/LevyLab/Newport Stage/Sub-VIs/Read Joystick Data.vi"
File 13="vi.lib/LevyLab/Newport Stage/Sub-VIs/Remove Unused Buttons.vi"
File 14="vi.lib/LevyLab/Newport Stage/Sub-VIs/Remove Unused Joysticks.vi"
File 15="vi.lib/LevyLab/Newport Stage/Sub-VIs/Used Button Converter.vi"
File 16="vi.lib/LevyLab/Newport Stage/Sub-VIs/Write Button Data.vi"
File 17="vi.lib/LevyLab/Newport Stage/Sub-VIs/Write Joystick Data.vi"
File 18="vi.lib/LevyLab/Newport Stage/Newport AG-UC8/Basic moving.vi"
File 19="vi.lib/LevyLab/Newport Stage/Newport AG-UC8/Case moving.vi"
File 20="vi.lib/LevyLab/Newport Stage/Newport AG-UC8/Feedback moving.vi"
File 21="vi.lib/LevyLab/Newport Stage/Newport AG-UC8/Sequence moving.vi"
File 22="vi.lib/LevyLab/Newport Stage/Newport AG-UC8/Square moving.vi"
File 23="vi.lib/LevyLab/Newport Stage/Newport AG-UC8/LabVIEW 2009/AG-UC2-UC8.lvproj"
File 24="vi.lib/LevyLab/Newport Stage/Newport AG-UC8/LabVIEW 2009/AG-UC2-UC8_Close.vi"
File 25="vi.lib/LevyLab/Newport Stage/Newport AG-UC8/LabVIEW 2009/AG-UC2-UC8_Example.vi"
File 26="vi.lib/LevyLab/Newport Stage/Newport AG-UC8/LabVIEW 2009/AG-UC2-UC8_Open.vi"
File 27="vi.lib/LevyLab/Newport Stage/Newport AG-UC8/LabVIEW 2009/AgilisCmdLib.dll"
File 28="vi.lib/LevyLab/Newport Stage/Newport AG-UC8/LabVIEW 2009/ChooseCorrectInstrument.vi"
File 29="vi.lib/LevyLab/Newport Stage/Newport AG-UC8/LabVIEW 2009/Logging.dll"
File 30="vi.lib/LevyLab/Newport Stage/Newport AG-UC8/LabVIEW 2009/VCPWrap.dll"


[File Group 1]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=4
File 0="_functions_levylab_lib_newport_stage_1.mnu"
File 1="_functions_levylab_lib_newport_stage_2.mnu"
File 2="_functions_levylab_lib_newport_stage_3.mnu"
File 3="functions_LevyLab_lib_Newport_Stage.mnu"


[File Group 2]
Target Dir="<menus>/Controls"
Replace Mode="Always"
Num Files=2
File 0="_controls_levylab_lib_newport_stage_1.mnu"
File 1="controls_LevyLab_lib_Newport_Stage.mnu"
