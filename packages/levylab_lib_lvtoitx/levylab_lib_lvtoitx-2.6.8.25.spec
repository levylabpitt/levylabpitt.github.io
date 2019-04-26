[Package]
Name="levylab_lib_lvtoitx"
Version="2.6.8.25"
Release=""
ID=c74a3dd14eda5dc0e169a71cf042222b
File Format="vip"
Format Version="2017"
Display Name="LVtoITX"


[Description]
Description="Collection of VIs to write and read Igor Text Files (*.itx) and text-based spreadsheet data files (*.dat)."
Summary=""
License=""
Copyright="Copyright (c) 2019, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="bug fixes:\0A- update DAT to LV to better format comments from DAT files"
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
Requires="levylab_lib_colorutillities>=1.0.0.2,levylab_lib_fileutilities>=1.2.1.7,levylab_lib_graph_utilities>=1.0.1.6,levylab_lib_ibwtolv>=1.0.0.2,levylab_lib_control_vi>=1.1.1.4"
Conflicts=""


[Activation]
License File=""
Licensed Library=""


[Files]
Num File Groups="5"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=50
File 0="user.lib/LevyLab/LV to ITX/LV to DAT.vi"
File 1="user.lib/LevyLab/LV to ITX/LV to ITX  Graph.vi"
File 2="user.lib/LevyLab/LV to ITX/LV to ITX  Retrieve Equation.vi"
File 3="user.lib/LevyLab/LV to ITX/LV to ITX  Retrieve.vi"
File 4="user.lib/LevyLab/LV to ITX/LV to ITX 2D AutoPlot.vi"
File 5="user.lib/LevyLab/LV to ITX/LV to ITX XY2 AutoPlot.vi"
File 6="user.lib/LevyLab/LV to ITX/LVtoITX.lvclass"
File 7="user.lib/LevyLab/LV to ITX/util/CheckWavenameLength.vi"
File 8="user.lib/LevyLab/LV to ITX/util/LVITX 2D Commands.vi"
File 9="user.lib/LevyLab/LV to ITX/util/LVITX 2D X&Y Commands.vi"
File 10="user.lib/LevyLab/LV to ITX/util/LVITX AddLetter.vi"
File 11="user.lib/LevyLab/LV to ITX/util/LVITX append letter to filename.vi"
File 12="user.lib/LevyLab/LV to ITX/util/LVITX Format 1D.vi"
File 13="user.lib/LevyLab/LV to ITX/util/LVITX Format 2D.vi"
File 14="user.lib/LevyLab/LV to ITX/util/LVITX Format Cmds.vi"
File 15="user.lib/LevyLab/LV to ITX/util/LVITX Format Notes.vi"
File 16="user.lib/LevyLab/LV to ITX/util/LVITX Format Path&Filename.vi"
File 17="user.lib/LevyLab/LV to ITX/util/LVITX Format string 1D.vi"
File 18="user.lib/LevyLab/LV to ITX/util/LVITX Generate Folder Index.vi"
File 19="user.lib/LevyLab/LV to ITX/util/LVITX IBW aperture Commands.vi"
File 20="user.lib/LevyLab/LV to ITX/util/LVITX ITX2 Plot Commands.vi"
File 21="user.lib/LevyLab/LV to ITX/util/LVITX OffsetMult Array.vi"
File 22="user.lib/LevyLab/LV to ITX/util/LVITX R+coord Commands.vi"
File 23="user.lib/LevyLab/LV to ITX/util/LVITX Read Folder Index.vi"
File 24="user.lib/LevyLab/LV to ITX/util/LVITX Remove Illegal Characters from Wavename.vi"
File 25="user.lib/LevyLab/LV to ITX/util/LVITX Rename Illegal Characters to Wavename.vi"
File 26="user.lib/LevyLab/LV to ITX/util/LVITX XY from 2D Commands.vi"
File 27="user.lib/LevyLab/LV to ITX/util/LVITX XY Plot Commands W2D.vi"
File 28="user.lib/LevyLab/LV to ITX/util/LVITX XY Plot Commands.vi"
File 29="user.lib/LevyLab/LV to ITX/util/WavenameLengthDialog.vi"
File 30="user.lib/LevyLab/LV to ITX/Typedefs/Retrieve Data Type.ctl"
File 31="user.lib/LevyLab/LV to ITX/Typedefs/Retrieve Formula Type.ctl"
File 32="user.lib/LevyLab/LV to ITX/Typedefs/Retrieve Index.ctl"
File 33="user.lib/LevyLab/LV to ITX/Typedefs/Retrieve N Results.ctl"
File 34="user.lib/LevyLab/LV to ITX/Main/DAT to LV.vi"
File 35="user.lib/LevyLab/LV to ITX/Main/ITX to LV 2.1 1D.vi"
File 36="user.lib/LevyLab/LV to ITX/Main/ITX to LV 2.1.vi"
File 37="user.lib/LevyLab/LV to ITX/Main/ITX to LV 2.2.vi"
File 38="user.lib/LevyLab/LV to ITX/Main/LV to ITX 2.2 1D multi.vi"
File 39="user.lib/LevyLab/LV to ITX/Main/LV to ITX 2.2 1D.vi"
File 40="user.lib/LevyLab/LV to ITX/Main/LV to ITX 2.2 2D w X&Y.vi"
File 41="user.lib/LevyLab/LV to ITX/Main/LV to ITX 2.2 2D.vi"
File 42="user.lib/LevyLab/LV to ITX/Main/LV to ITX 2.2 ITX2.vi"
File 43="user.lib/LevyLab/LV to ITX/Main/LV to ITX 2.2 XY.vi"
File 44="user.lib/LevyLab/LV to ITX/Main/LV to ITX R+coord.vi"
File 45="user.lib/LevyLab/LV to ITX/Main/LV to ITX XY AutoPlot.vi"
File 46="user.lib/LevyLab/LV to ITX/HELP/ALL.vi"
File 47="user.lib/LevyLab/LV to ITX/HELP/DAT Example.vi"
File 48="user.lib/LevyLab/LV to ITX/HELP/ITX Example.vi"
File 49="user.lib/LevyLab/LV to ITX/HELP/ITX2 Example.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=4
File 0="_functions_levylab_lib_lvtoitx_1.mnu"
File 1="_functions_levylab_lib_lvtoitx_2.mnu"
File 2="_functions_levylab_lib_lvtoitx_3.mnu"
File 3="functions_levylab_lib_lvtoitx.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"


[File Group 3]
Target Dir="<menus>/Controls/LevyLab"
Replace Mode="Always"
Num Files=2
File 0="_controls_levylab_lib_lvtoitx_1.mnu"
File 1="controls_levylab_lib_lvtoitx.mnu"


[File Group 4]
Target Dir="<menus>/Controls/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
