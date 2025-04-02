[Package]
Name="levylab_lib_graph_utilities"
Version="2.1.2.3"
Release=""
ID=eb76c205add41034615ebb72b3d71e59
File Format="vip"
Format Version="2017"
Display Name="Graph Utilities"


[Description]
Description="Misc. graph utilities"
Summary=""
License=""
Copyright="Copyright (c) 2020, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[2.1.2]\0A- Update Control typedefs\0A- Set XY Graph Value: Value is now polymorphic"
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
Requires="levylab_lib_xy_utilities>=1.1.1.10,jki_lib_state_machine>=2018.0.7.45"
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
Num Files=66
File 0="user.lib/LevyLab/Graph Utilities/Graph Utilities Tree.vi"
File 1="user.lib/LevyLab/Graph Utilities/graph_utilities.lvclass"
File 2="user.lib/LevyLab/Graph Utilities/XY Graph/Get XY Graph Plot Names.vi"
File 3="user.lib/LevyLab/Graph Utilities/XY Graph/Get XY Graph Value.vi"
File 4="user.lib/LevyLab/Graph Utilities/XY Graph/Get XY Graph X Label.vi"
File 5="user.lib/LevyLab/Graph Utilities/XY Graph/Get XY Graph X Mapping.vi"
File 6="user.lib/LevyLab/Graph Utilities/XY Graph/Get XY Graph Y Label.vi"
File 7="user.lib/LevyLab/Graph Utilities/XY Graph/Get XY Graph Y Mapping.vi"
File 8="user.lib/LevyLab/Graph Utilities/XY Graph/Offset XY Graph.vi"
File 9="user.lib/LevyLab/Graph Utilities/XY Graph/Set XY Graph Plot Colors.vi"
File 10="user.lib/LevyLab/Graph Utilities/XY Graph/Set XY Graph Plot Names.vi"
File 11="user.lib/LevyLab/Graph Utilities/XY Graph/Set XY Graph Value (array).vi"
File 12="user.lib/LevyLab/Graph Utilities/XY Graph/Set XY Graph Value (single).vi"
File 13="user.lib/LevyLab/Graph Utilities/XY Graph/Set XY Graph Value.vi"
File 14="user.lib/LevyLab/Graph Utilities/XY Graph/Set XY Graph X Label.vi"
File 15="user.lib/LevyLab/Graph Utilities/XY Graph/Set XY Graph X Mapping.vi"
File 16="user.lib/LevyLab/Graph Utilities/XY Graph/Set XY Graph X Range.vi"
File 17="user.lib/LevyLab/Graph Utilities/XY Graph/Set XY Graph Y Label.vi"
File 18="user.lib/LevyLab/Graph Utilities/XY Graph/Set XY Graph Y Mapping.vi"
File 19="user.lib/LevyLab/Graph Utilities/XY Graph/Set XY Graph Y Range.vi"
File 20="user.lib/LevyLab/Graph Utilities/Typedefs/Histogram--Graph.ctl"
File 21="user.lib/LevyLab/Graph Utilities/Typedefs/Histogram--slider.ctl"
File 22="user.lib/LevyLab/Graph Utilities/Typedefs/Intensity Graph.ctl"
File 23="user.lib/LevyLab/Graph Utilities/Typedefs/Scale Mapping --enum.ctl"
File 24="user.lib/LevyLab/Graph Utilities/Typedefs/XY Graph.ctl"
File 25="user.lib/LevyLab/Graph Utilities/subVIs/Array to Offset and Multiplier.vi"
File 26="user.lib/LevyLab/Graph Utilities/subVIs/Create Color Table.vi"
File 27="user.lib/LevyLab/Graph Utilities/subVIs/Normalized Gaussian.vi"
File 28="user.lib/LevyLab/Graph Utilities/subVIs/Offset and Multiplier to Array.vi"
File 29="user.lib/LevyLab/Graph Utilities/subVIs/Variant to 2D Array.vi"
File 30="user.lib/LevyLab/Graph Utilities/subVIs/Variant to XY-Data.vi"
File 31="user.lib/LevyLab/Graph Utilities/Intensity Graph/Get Intensity Graph Cursor (Control).vi"
File 32="user.lib/LevyLab/Graph Utilities/Intensity Graph/Get Intensity Graph Value.vi"
File 33="user.lib/LevyLab/Graph Utilities/Intensity Graph/Get Intensity Graph X Label.vi"
File 34="user.lib/LevyLab/Graph Utilities/Intensity Graph/Get Intensity Graph X Scale.vi"
File 35="user.lib/LevyLab/Graph Utilities/Intensity Graph/Get Intensity Graph Y Label.vi"
File 36="user.lib/LevyLab/Graph Utilities/Intensity Graph/Get Intensity Graph Y Scale.vi"
File 37="user.lib/LevyLab/Graph Utilities/Intensity Graph/Get Intensity Graph Z Label.vi"
File 38="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph Cursor.vi"
File 39="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph Value.vi"
File 40="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph X Label.vi"
File 41="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph X Range.vi"
File 42="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph X Scale Array.vi"
File 43="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph X Scale Min and Max.vi"
File 44="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph Y Label.vi"
File 45="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph Y Range.vi"
File 46="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph Y Scale Array.vi"
File 47="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph Y Scale Min and Max.vi"
File 48="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph Z Color.vi"
File 49="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph Z Label.vi"
File 50="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph Z Range.vi"
File 51="user.lib/LevyLab/Graph Utilities/Histogram/adjust_histogram_cursor.vi"
File 52="user.lib/LevyLab/Graph Utilities/Histogram/calculate_histogram.vi"
File 53="user.lib/LevyLab/Graph Utilities/Histogram/Intensity Graph Histogram Control.vi"
File 54="user.lib/LevyLab/Graph Utilities/API/Intensity Graph Linecut (Horizontal).vi"
File 55="user.lib/LevyLab/Graph Utilities/API/Intensity Graph Linecut (Vertical).vi"
File 56="user.lib/LevyLab/Graph Utilities/API/Intensity Graph to XY Graph (Horizontal).vi"
File 57="user.lib/LevyLab/Graph Utilities/API/Intensity Graph to XY Graph (Vertical).vi"
File 58="user.lib/LevyLab/Graph Utilities/API/XY Graph to Intensity Graph.vi"
File 59="user.lib/LevyLab/Graph Utilities/Accessors/Read Intensity Graph ref.vi"
File 60="user.lib/LevyLab/Graph Utilities/Accessors/Read XY Graph ref.vi"
File 61="user.lib/LevyLab/Graph Utilities/Accessors/Write Intensity Graph ref.vi"
File 62="user.lib/LevyLab/Graph Utilities/Accessors/Write XY Graph ref.vi"
File 63="examples/LevyLab/Graph Utilities/Examples/Histogram.vi"
File 64="examples/LevyLab/Graph Utilities/Examples/Intensity Graph to XY Graph.vi"
File 65="examples/LevyLab/Graph Utilities/Examples/Linecut.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=7
File 0="_functions_levylab_lib_graph_utilities_1.mnu"
File 1="_functions_levylab_lib_graph_utilities_2.mnu"
File 2="_functions_levylab_lib_graph_utilities_3.mnu"
File 3="_functions_levylab_lib_graph_utilities_4.mnu"
File 4="_functions_levylab_lib_graph_utilities_5.mnu"
File 5="_functions_levylab_lib_graph_utilities_6.mnu"
File 6="functions_levylab_lib_graph_utilities.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"


[File Group 3]
Target Dir="<menus>/Controls/LevyLab"
Replace Mode="Always"
Num Files=1
File 0="controls_levylab_lib_graph_utilities.mnu"


[File Group 4]
Target Dir="<menus>/Controls/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
