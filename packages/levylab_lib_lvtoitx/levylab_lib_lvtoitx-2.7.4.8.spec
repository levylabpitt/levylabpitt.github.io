[Package]
Name="levylab_lib_lvtoitx"
Version="2.7.4.8"
Release=""
ID=ae461d67d8d9455387f26e0e405beba4
File Format="vip"
Format Version="2017"
Display Name="LVtoITX"


[Description]
Description="Collection of VIs to write and read Igor Text Files (*.itx) and text-based spreadsheet data files (*.dat)."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2020, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[2.7.4.8]\0A- add variant to array subVI to TDMS write"
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
Requires="jki_lib_state_machine>=2018.0.7.45,levylab_lib_fileutilities>=1.2.3.9,levylab_lib_graph_utilities>=2.0.0.1,levylab_lib_ibwtolv>=1.0.1.3,oglib_dictionary>=4.0.0.4,oglib_string>=4.1.0.12,oglib_time>=4.0.1.3"
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
Num Files=74
File 0="user.lib/LevyLab/LV to ITX/LV to DAT.vi"
File 1="user.lib/LevyLab/LV to ITX/LV to ITX  Graph.vi"
File 2="user.lib/LevyLab/LV to ITX/LV to ITX  Retrieve Equation.vi"
File 3="user.lib/LevyLab/LV to ITX/LV to ITX  Retrieve.vi"
File 4="user.lib/LevyLab/LV to ITX/LV to ITX 2D AutoPlot.vi"
File 5="user.lib/LevyLab/LV to ITX/LV to ITX XY AutoPlot.vi"
File 6="user.lib/LevyLab/LV to ITX/LV to ITX XY2 AutoPlot.vi"
File 7="user.lib/LevyLab/LV to ITX/LVtoITX.lvclass"
File 8="user.lib/LevyLab/LV to ITX/util/CheckWavenameLength.vi"
File 9="user.lib/LevyLab/LV to ITX/util/LVITX 2D Commands.vi"
File 10="user.lib/LevyLab/LV to ITX/util/LVITX 2D X&Y Commands.vi"
File 11="user.lib/LevyLab/LV to ITX/util/LVITX AddLetter.vi"
File 12="user.lib/LevyLab/LV to ITX/util/LVITX append letter to filename.vi"
File 13="user.lib/LevyLab/LV to ITX/util/LVITX Format 1D.vi"
File 14="user.lib/LevyLab/LV to ITX/util/LVITX Format 2D.vi"
File 15="user.lib/LevyLab/LV to ITX/util/LVITX Format Cmds.vi"
File 16="user.lib/LevyLab/LV to ITX/util/LVITX Format Notes.vi"
File 17="user.lib/LevyLab/LV to ITX/util/LVITX Format Path&Filename TDMS.vi"
File 18="user.lib/LevyLab/LV to ITX/util/LVITX Format Path&Filename.vi"
File 19="user.lib/LevyLab/LV to ITX/util/LVITX Format string 1D.vi"
File 20="user.lib/LevyLab/LV to ITX/util/LVITX Generate Folder Index.vi"
File 21="user.lib/LevyLab/LV to ITX/util/LVITX IBW aperture Commands.vi"
File 22="user.lib/LevyLab/LV to ITX/util/LVITX ITX2 Plot Commands.vi"
File 23="user.lib/LevyLab/LV to ITX/util/LVITX OffsetMult Array.vi"
File 24="user.lib/LevyLab/LV to ITX/util/LVITX R+coord Commands.vi"
File 25="user.lib/LevyLab/LV to ITX/util/LVITX Read Folder Index.vi"
File 26="user.lib/LevyLab/LV to ITX/util/LVITX Remove Illegal Characters from Wavename.vi"
File 27="user.lib/LevyLab/LV to ITX/util/LVITX Rename Illegal Characters to Wavename.vi"
File 28="user.lib/LevyLab/LV to ITX/util/LVITX XY from 2D Commands.vi"
File 29="user.lib/LevyLab/LV to ITX/util/LVITX XY Plot Commands W2D.vi"
File 30="user.lib/LevyLab/LV to ITX/util/LVITX XY Plot Commands.vi"
File 31="user.lib/LevyLab/LV to ITX/util/Parse Comments and Commands.vi"
File 32="user.lib/LevyLab/LV to ITX/util/Variant to Array.vi"
File 33="user.lib/LevyLab/LV to ITX/util/WavenameLengthDialog.vi"
File 34="user.lib/LevyLab/LV to ITX/Typedefs/Dictionary--cluster.ctl"
File 35="user.lib/LevyLab/LV to ITX/Typedefs/Retrieve Data Type.ctl"
File 36="user.lib/LevyLab/LV to ITX/Typedefs/Retrieve Formula Type.ctl"
File 37="user.lib/LevyLab/LV to ITX/Typedefs/Retrieve Index.ctl"
File 38="user.lib/LevyLab/LV to ITX/Typedefs/Retrieve N Results.ctl"
File 39="user.lib/LevyLab/LV to ITX/Tests/Test TDMS Read Speed.vi"
File 40="user.lib/LevyLab/LV to ITX/TDMS/ITX Folder to TDMS.vi"
File 41="user.lib/LevyLab/LV to ITX/TDMS/ITX to TDMS.vi"
File 42="user.lib/LevyLab/LV to ITX/TDMS/Read TDMS Comments.vi"
File 43="user.lib/LevyLab/LV to ITX/TDMS/Read TDMS Wave.vi"
File 44="user.lib/LevyLab/LV to ITX/TDMS/Read TDMS Wavenames.vi"
File 45="user.lib/LevyLab/LV to ITX/TDMS/Read TDMS.vi"
File 46="user.lib/LevyLab/LV to ITX/TDMS/Write TDMS.vi"
File 47="user.lib/LevyLab/LV to ITX/Main/DAT to LV.vi"
File 48="user.lib/LevyLab/LV to ITX/Main/ITX to LV 2.1 1D.vi"
File 49="user.lib/LevyLab/LV to ITX/Main/ITX to LV 2.1.vi"
File 50="user.lib/LevyLab/LV to ITX/Main/ITX to LV 2.2.vi"
File 51="user.lib/LevyLab/LV to ITX/Main/LV to DAT 1D.vi"
File 52="user.lib/LevyLab/LV to ITX/Main/LV to DAT 2D.vi"
File 53="user.lib/LevyLab/LV to ITX/Main/LV to ITX 2.2 1D multi.vi"
File 54="user.lib/LevyLab/LV to ITX/Main/LV to ITX 2.2 1D.vi"
File 55="user.lib/LevyLab/LV to ITX/Main/LV to ITX 2.2 2D w X&Y.vi"
File 56="user.lib/LevyLab/LV to ITX/Main/LV to ITX 2.2 2D.vi"
File 57="user.lib/LevyLab/LV to ITX/Main/LV to ITX 2.2 XY.vi"
File 58="user.lib/LevyLab/LV to ITX/Main/LV to ITX 2.2 XY2.vi"
File 59="user.lib/LevyLab/LV to ITX/Main/LV to ITX R+coord.vi"
File 60="user.lib/LevyLab/LV to ITX/HELP/DAT Example.vi"
File 61="user.lib/LevyLab/LV to ITX/HELP/ITX Example.vi"
File 62="user.lib/LevyLab/LV to ITX/HELP/ITX2 Example.vi"
File 63="user.lib/LevyLab/LV to ITX/HELP/TDMS Read Example.vi"
File 64="user.lib/LevyLab/LV to ITX/API/Append to Data (Dictionary).vi"
File 65="user.lib/LevyLab/LV to ITX/API/Read Comments.vi"
File 66="user.lib/LevyLab/LV to ITX/API/Read Data (Dictionary).vi"
File 67="user.lib/LevyLab/LV to ITX/API/Read Igor Commands.vi"
File 68="user.lib/LevyLab/LV to ITX/API/Read Path.vi"
File 69="user.lib/LevyLab/LV to ITX/API/Read Wavenames.vi"
File 70="user.lib/LevyLab/LV to ITX/API/Write Comments.vi"
File 71="user.lib/LevyLab/LV to ITX/API/Write Data (Dictionary).vi"
File 72="user.lib/LevyLab/LV to ITX/API/Write Igor Commands.vi"
File 73="user.lib/LevyLab/LV to ITX/API/Write Path.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=7
File 0="_functions_levylab_lib_lvtoitx_1.mnu"
File 1="_functions_levylab_lib_lvtoitx_2.mnu"
File 2="_functions_levylab_lib_lvtoitx_3.mnu"
File 3="_functions_levylab_lib_lvtoitx_4.mnu"
File 4="_functions_levylab_lib_lvtoitx_5.mnu"
File 5="_functions_levylab_lib_lvtoitx_6.mnu"
File 6="functions_levylab_lib_lvtoitx.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
