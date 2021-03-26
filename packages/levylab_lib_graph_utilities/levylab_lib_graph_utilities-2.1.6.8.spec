[Package]
Name="levylab_lib_graph_utilities"
Version="2.1.6.8"
Release=""
ID=40caa6b9bd940bb19f49c166121a5fc7
File Format="vip"
Format Version="2017"
Display Name="Graph Utilities"


[Description]
Description="Misc. graph utilities"
Summary=""
License=""
Copyright="Copyright (c) 2021, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[2.1.6]\0A- Add Number control to "Choose Color Table""
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
Requires="levylab_lib_xy_utilities>=1.4.0.17,jki_lib_state_machine>=2018.0.7.45"
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
Num Files=136
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
File 20="user.lib/LevyLab/Graph Utilities/Utilities/Array to Offset and Multiplier.vi"
File 21="user.lib/LevyLab/Graph Utilities/Utilities/Offset and Multiplier to Array.vi"
File 22="user.lib/LevyLab/Graph Utilities/Utilities/Variant to 2D Array.vi"
File 23="user.lib/LevyLab/Graph Utilities/Utilities/Variant to XY-Data.vi"
File 24="user.lib/LevyLab/Graph Utilities/Typedefs/Histogram--Graph.ctl"
File 25="user.lib/LevyLab/Graph Utilities/Typedefs/Histogram--slider.ctl"
File 26="user.lib/LevyLab/Graph Utilities/Typedefs/Intensity Graph.ctl"
File 27="user.lib/LevyLab/Graph Utilities/Typedefs/Scale Mapping --enum.ctl"
File 28="user.lib/LevyLab/Graph Utilities/Typedefs/XY Graph.ctl"
File 29="user.lib/LevyLab/Graph Utilities/subVIs/CETperceptual_ColorTables.vi"
File 30="user.lib/LevyLab/Graph Utilities/subVIs/Create Custom Color Table.vi"
File 31="user.lib/LevyLab/Graph Utilities/subVIs/Interpolate Color V8.vi"
File 32="user.lib/LevyLab/Graph Utilities/subVIs/Normalized Gaussian.vi"
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
File 56="user.lib/LevyLab/Graph Utilities/API/Choose Color Table.vi"
File 57="user.lib/LevyLab/Graph Utilities/API/Intensity Graph Linecut (Horizontal).vi"
File 58="user.lib/LevyLab/Graph Utilities/API/Intensity Graph Linecut (Vertical).vi"
File 59="user.lib/LevyLab/Graph Utilities/API/Intensity Graph to XY Graph (Horizontal).vi"
File 60="user.lib/LevyLab/Graph Utilities/API/Intensity Graph to XY Graph (Vertical).vi"
File 61="user.lib/LevyLab/Graph Utilities/API/XY Graph to Intensity Graph.vi"
File 62="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Project-Documentation.adoc"
File 63="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/broadcast.png"
File 64="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/empty.png"
File 65="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_adjust_histogram_cursor.vi__.png"
File 66="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Array_to_Offset_and_Multiplier.vi__.png"
File 67="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_calculate_histogram.vi__.png"
File 68="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Create_Color_Table.vi__.png"
File 69="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Get_Intensity_Graph_Cursor_(Control).vi__.png"
File 70="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Get_Intensity_Graph_Value.vi__.png"
File 71="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Get_Intensity_Graph_X_Label.vi__.png"
File 72="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Get_Intensity_Graph_X_Scale.vi__.png"
File 73="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Get_Intensity_Graph_Y_Label.vi__.png"
File 74="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Get_Intensity_Graph_Y_Scale.vi__.png"
File 75="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Get_Intensity_Graph_Z_Label.vi__.png"
File 76="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Get_XY_Graph_Plot_Names.vi__.png"
File 77="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Get_XY_Graph_Value.vi__.png"
File 78="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Get_XY_Graph_X_Label.vi__.png"
File 79="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Get_XY_Graph_X_Mapping.vi__.png"
File 80="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Get_XY_Graph_Y_Label.vi__.png"
File 81="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Get_XY_Graph_Y_Mapping.vi__.png"
File 82="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Intensity_Graph_Histogram_Control.vi__.png"
File 83="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Intensity_Graph_Linecut_(Horizontal).vi__.png"
File 84="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Intensity_Graph_Linecut_(Vertical).vi__.png"
File 85="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Intensity_Graph_to_XY_Graph_(Horizontal).vi__.png"
File 86="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Intensity_Graph_to_XY_Graph_(Vertical).vi__.png"
File 87="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Normalized_Gaussian.vi__.png"
File 88="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Offset_and_Multiplier_to_Array.vi__.png"
File 89="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Offset_XY_Graph.vi__.png"
File 90="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Read_Intensity_Graph_ref.vi__.png"
File 91="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Read_XY_Graph_ref.vi__.png"
File 92="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_Intensity_Graph_Cursor.vi__.png"
File 93="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_Intensity_Graph_Value.vi__.png"
File 94="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_Intensity_Graph_X_Label.vi__.png"
File 95="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_Intensity_Graph_X_Range.vi__.png"
File 96="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_Intensity_Graph_X_Scale_Array.vi__.png"
File 97="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_Intensity_Graph_X_Scale_Min_and_Max.vi__.png"
File 98="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_Intensity_Graph_Y_Label.vi__.png"
File 99="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_Intensity_Graph_Y_Range.vi__.png"
File 100="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_Intensity_Graph_Y_Scale_Array.vi__.png"
File 101="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_Intensity_Graph_Y_Scale_Min_and_Max.vi__.png"
File 102="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_Intensity_Graph_Z_Color.vi__.png"
File 103="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_Intensity_Graph_Z_Label.vi__.png"
File 104="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_Intensity_Graph_Z_Range.vi__.png"
File 105="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_XY_Graph_Plot_Colors.vi__.png"
File 106="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_XY_Graph_Plot_Names.vi__.png"
File 107="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_XY_Graph_Value_(array).vi__.png"
File 108="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_XY_Graph_Value_(single).vi__.png"
File 109="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_XY_Graph_X_Label.vi__.png"
File 110="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_XY_Graph_X_Mapping.vi__.png"
File 111="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_XY_Graph_X_Range.vi__.png"
File 112="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_XY_Graph_Y_Label.vi__.png"
File 113="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_XY_Graph_Y_Mapping.vi__.png"
File 114="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Set_XY_Graph_Y_Range.vi__.png"
File 115="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Variant_to_2D_Array.vi__.png"
File 116="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Variant_to_XY_Data.vi__.png"
File 117="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Write_Intensity_Graph_ref.vi__.png"
File 118="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_Write_XY_Graph_ref.vi__.png"
File 119="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/graph_utilities.lvclass_XY_Graph_to_Intensity_Graph.vi__.png"
File 120="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/inlined.png"
File 121="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/reentrancy-preallocated.png"
File 122="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/reentrancy-shared.png"
File 123="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/request-and-wait-for-reply.png"
File 124="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/request.png"
File 125="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/scope-community.png"
File 126="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/scope-private.png"
File 127="user.lib/LevyLab/Graph Utilities/Antidoc-Output/Images/scope-protected.png"
File 128="user.lib/LevyLab/Graph Utilities/Accessors/Read Intensity Graph ref.vi"
File 129="user.lib/LevyLab/Graph Utilities/Accessors/Read XY Graph ref.vi"
File 130="user.lib/LevyLab/Graph Utilities/Accessors/Write Intensity Graph ref.vi"
File 131="user.lib/LevyLab/Graph Utilities/Accessors/Write XY Graph ref.vi"
File 132="examples/LevyLab/Graph Utilities/Examples/Histogram.vi"
File 133="examples/LevyLab/Graph Utilities/Examples/Image Color Table.vi"
File 134="examples/LevyLab/Graph Utilities/Examples/Intensity Graph to XY Graph.vi"
File 135="examples/LevyLab/Graph Utilities/Examples/Linecut.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=8
File 0="_functions_levylab_lib_graph_utilities_1.mnu"
File 1="_functions_levylab_lib_graph_utilities_2.mnu"
File 2="_functions_levylab_lib_graph_utilities_3.mnu"
File 3="_functions_levylab_lib_graph_utilities_4.mnu"
File 4="_functions_levylab_lib_graph_utilities_5.mnu"
File 5="_functions_levylab_lib_graph_utilities_6.mnu"
File 6="_functions_levylab_lib_graph_utilities_7.mnu"
File 7="functions_levylab_lib_graph_utilities.mnu"


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