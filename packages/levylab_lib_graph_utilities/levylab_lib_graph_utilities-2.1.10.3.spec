[Package]
Name="levylab_lib_graph_utilities"
Version="2.1.10.3"
Release=""
ID=86114e42c644c76f99b2980616423998
File Format="vip"
Format Version="2017"
Display Name="Graph Utilities"


[Description]
Description="Misc. graph utilities"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2022, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[2.1.10]\0A- Updated palette and examples install location\0A- Updated package dependencies\0A- Change default intensity graph.ctl color table to viridis"
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
Requires="levylab_lib_xy_utilities>=1.5.1.1,mgi_lib_1d_array>=1.0.2.3,jki_lib_state_machine>=2018.0.7.45"
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
Num Files=76
File 0="user.lib/LevyLab/Graph Utilities/graph_utilities.lvclass"
File 1="user.lib/LevyLab/Graph Utilities/XY Graph/Get XY Graph Plot Names.vi"
File 2="user.lib/LevyLab/Graph Utilities/XY Graph/Get XY Graph Value.vi"
File 3="user.lib/LevyLab/Graph Utilities/XY Graph/Get XY Graph X Label.vi"
File 4="user.lib/LevyLab/Graph Utilities/XY Graph/Get XY Graph X Mapping.vi"
File 5="user.lib/LevyLab/Graph Utilities/XY Graph/Get XY Graph Y Label.vi"
File 6="user.lib/LevyLab/Graph Utilities/XY Graph/Get XY Graph Y Mapping.vi"
File 7="user.lib/LevyLab/Graph Utilities/XY Graph/Offset XY Graph.vi"
File 8="user.lib/LevyLab/Graph Utilities/XY Graph/Set XY Graph Plot Colors.vi"
File 9="user.lib/LevyLab/Graph Utilities/XY Graph/Set XY Graph Plot Names.vi"
File 10="user.lib/LevyLab/Graph Utilities/XY Graph/Set XY Graph Value (array).vi"
File 11="user.lib/LevyLab/Graph Utilities/XY Graph/Set XY Graph Value (single).vi"
File 12="user.lib/LevyLab/Graph Utilities/XY Graph/Set XY Graph Value.vi"
File 13="user.lib/LevyLab/Graph Utilities/XY Graph/Set XY Graph X Label.vi"
File 14="user.lib/LevyLab/Graph Utilities/XY Graph/Set XY Graph X Mapping.vi"
File 15="user.lib/LevyLab/Graph Utilities/XY Graph/Set XY Graph X Range.vi"
File 16="user.lib/LevyLab/Graph Utilities/XY Graph/Set XY Graph Y Label.vi"
File 17="user.lib/LevyLab/Graph Utilities/XY Graph/Set XY Graph Y Mapping.vi"
File 18="user.lib/LevyLab/Graph Utilities/XY Graph/Set XY Graph Y Range.vi"
File 19="user.lib/LevyLab/Graph Utilities/Utilities/Array to Offset and Multiplier.vi"
File 20="user.lib/LevyLab/Graph Utilities/Utilities/Offset and Multiplier to Array.vi"
File 21="user.lib/LevyLab/Graph Utilities/Utilities/Variant to 2D Array.vi"
File 22="user.lib/LevyLab/Graph Utilities/Utilities/Variant to XY-Data.vi"
File 23="user.lib/LevyLab/Graph Utilities/Typedefs/Histogram--Graph.ctl"
File 24="user.lib/LevyLab/Graph Utilities/Typedefs/Histogram--slider.ctl"
File 25="user.lib/LevyLab/Graph Utilities/Typedefs/Intensity Graph.ctl"
File 26="user.lib/LevyLab/Graph Utilities/Typedefs/Scale Mapping --enum.ctl"
File 27="user.lib/LevyLab/Graph Utilities/Typedefs/XY Graph.ctl"
File 28="user.lib/LevyLab/Graph Utilities/subVIs/CETperceptual_ColorTables.vi"
File 29="user.lib/LevyLab/Graph Utilities/subVIs/Create Custom Color Table.vi"
File 30="user.lib/LevyLab/Graph Utilities/subVIs/Interpolate Color V8.vi"
File 31="user.lib/LevyLab/Graph Utilities/subVIs/Normalized Gaussian.vi"
File 32="user.lib/LevyLab/Graph Utilities/subVIs/Step Average.vi"
File 33="user.lib/LevyLab/Graph Utilities/Intensity Graph/Get Intensity Graph Cursor (Control).vi"
File 34="user.lib/LevyLab/Graph Utilities/Intensity Graph/Get Intensity Graph Value.vi"
File 35="user.lib/LevyLab/Graph Utilities/Intensity Graph/Get Intensity Graph X Label.vi"
File 36="user.lib/LevyLab/Graph Utilities/Intensity Graph/Get Intensity Graph X Scale.vi"
File 37="user.lib/LevyLab/Graph Utilities/Intensity Graph/Get Intensity Graph Y Label.vi"
File 38="user.lib/LevyLab/Graph Utilities/Intensity Graph/Get Intensity Graph Y Scale.vi"
File 39="user.lib/LevyLab/Graph Utilities/Intensity Graph/Get Intensity Graph Z Label.vi"
File 40="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph Cursor.vi"
File 41="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph Value.vi"
File 42="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph X Label.vi"
File 43="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph X Range.vi"
File 44="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph X Scale Array.vi"
File 45="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph X Scale Min and Max.vi"
File 46="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph Y Label.vi"
File 47="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph Y Range.vi"
File 48="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph Y Scale Array.vi"
File 49="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph Y Scale Min and Max.vi"
File 50="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph Z Color.vi"
File 51="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph Z Label.vi"
File 52="user.lib/LevyLab/Graph Utilities/Intensity Graph/Set Intensity Graph Z Range.vi"
File 53="user.lib/LevyLab/Graph Utilities/Histogram/adjust_histogram_cursor.vi"
File 54="user.lib/LevyLab/Graph Utilities/Histogram/calculate_histogram.vi"
File 55="user.lib/LevyLab/Graph Utilities/Histogram/Intensity Graph Histogram Control.vi"
File 56="user.lib/LevyLab/Graph Utilities/Examples/Graph Utilities Tree.vi"
File 57="user.lib/LevyLab/Graph Utilities/Examples/Histogram.vi"
File 58="user.lib/LevyLab/Graph Utilities/Examples/Image Color Table.vi"
File 59="user.lib/LevyLab/Graph Utilities/Examples/Intensity Graph to XY Graph.vi"
File 60="user.lib/LevyLab/Graph Utilities/Examples/Linecut.vi"
File 61="user.lib/LevyLab/Graph Utilities/API/Choose Color Table.vi"
File 62="user.lib/LevyLab/Graph Utilities/API/Intensity Graph Linecut (Horizontal) (by val).vi"
File 63="user.lib/LevyLab/Graph Utilities/API/Intensity Graph Linecut (Horizontal).vi"
File 64="user.lib/LevyLab/Graph Utilities/API/Intensity Graph Linecut (Vertical) (by val).vi"
File 65="user.lib/LevyLab/Graph Utilities/API/Intensity Graph Linecut (Vertical).vi"
File 66="user.lib/LevyLab/Graph Utilities/API/Intensity Graph to XY Graph (Horizontal) (by val).vi"
File 67="user.lib/LevyLab/Graph Utilities/API/Intensity Graph to XY Graph (Horizontal).vi"
File 68="user.lib/LevyLab/Graph Utilities/API/Intensity Graph to XY Graph (Vertical) (by val).vi"
File 69="user.lib/LevyLab/Graph Utilities/API/Intensity Graph to XY Graph (Vertical).vi"
File 70="user.lib/LevyLab/Graph Utilities/API/XY Graph to Intensity Graph (by val).vi"
File 71="user.lib/LevyLab/Graph Utilities/API/XY Graph to Intensity Graph.vi"
File 72="user.lib/LevyLab/Graph Utilities/Accessors/Read Intensity Graph ref.vi"
File 73="user.lib/LevyLab/Graph Utilities/Accessors/Read XY Graph ref.vi"
File 74="user.lib/LevyLab/Graph Utilities/Accessors/Write Intensity Graph ref.vi"
File 75="user.lib/LevyLab/Graph Utilities/Accessors/Write XY Graph ref.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=9
File 0="_functions_levylab_lib_graph_utilities_1.mnu"
File 1="_functions_levylab_lib_graph_utilities_2.mnu"
File 2="_functions_levylab_lib_graph_utilities_3.mnu"
File 3="_functions_levylab_lib_graph_utilities_4.mnu"
File 4="_functions_levylab_lib_graph_utilities_5.mnu"
File 5="_functions_levylab_lib_graph_utilities_6.mnu"
File 6="_functions_levylab_lib_graph_utilities_7.mnu"
File 7="_functions_levylab_lib_graph_utilities_8.mnu"
File 8="functions_levylab_lib_graph_utilities.mnu"


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
