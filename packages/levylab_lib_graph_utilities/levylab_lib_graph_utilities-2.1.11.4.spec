[Package]
Name="levylab_lib_graph_utilities"
Version="2.1.11.4"
Release=""
ID=5227a44cd04c65656cf7d32eb7ecba16
File Format="vip"
Format Version="2017"
Display Name="Graph Utilities"


[Description]
Description="Utilities for working with XY and Intensity graphs"
Summary="Utilities for working with XY and Intensity graphs"
License="BSD-3"
Copyright="Copyright (c) 2025, PRIrvin"
Distribution=""
Vendor="PRIrvin"
URL="https://github.com/PRIrvin"
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[2.1.11]\0A- Updated install location"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"
install into global environment="FALSE"


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
Requires="jki_lib_state_machine>=2018.0.7.45,levylab_lib_xy_utilities>=1.5.5.5,mgi_lib_1d_array>=1.0.2.3,oglib_array>=4.1.1.14,oglib_string>=5.0.0.25"
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
Num Files=76
File 0="vi.lib/prirvin/Graph Utilities/graph_utilities.lvclass"
File 1="vi.lib/prirvin/Graph Utilities/XY Graph/Get XY Graph Plot Names.vi"
File 2="vi.lib/prirvin/Graph Utilities/XY Graph/Get XY Graph Value.vi"
File 3="vi.lib/prirvin/Graph Utilities/XY Graph/Get XY Graph X Label.vi"
File 4="vi.lib/prirvin/Graph Utilities/XY Graph/Get XY Graph X Mapping.vi"
File 5="vi.lib/prirvin/Graph Utilities/XY Graph/Get XY Graph Y Label.vi"
File 6="vi.lib/prirvin/Graph Utilities/XY Graph/Get XY Graph Y Mapping.vi"
File 7="vi.lib/prirvin/Graph Utilities/XY Graph/Offset XY Graph.vi"
File 8="vi.lib/prirvin/Graph Utilities/XY Graph/Set XY Graph Plot Colors.vi"
File 9="vi.lib/prirvin/Graph Utilities/XY Graph/Set XY Graph Plot Names.vi"
File 10="vi.lib/prirvin/Graph Utilities/XY Graph/Set XY Graph Value (array).vi"
File 11="vi.lib/prirvin/Graph Utilities/XY Graph/Set XY Graph Value (single).vi"
File 12="vi.lib/prirvin/Graph Utilities/XY Graph/Set XY Graph Value.vi"
File 13="vi.lib/prirvin/Graph Utilities/XY Graph/Set XY Graph X Label.vi"
File 14="vi.lib/prirvin/Graph Utilities/XY Graph/Set XY Graph X Mapping.vi"
File 15="vi.lib/prirvin/Graph Utilities/XY Graph/Set XY Graph X Range.vi"
File 16="vi.lib/prirvin/Graph Utilities/XY Graph/Set XY Graph Y Label.vi"
File 17="vi.lib/prirvin/Graph Utilities/XY Graph/Set XY Graph Y Mapping.vi"
File 18="vi.lib/prirvin/Graph Utilities/XY Graph/Set XY Graph Y Range.vi"
File 19="vi.lib/prirvin/Graph Utilities/Utilities/Array to Offset and Multiplier.vi"
File 20="vi.lib/prirvin/Graph Utilities/Utilities/Offset and Multiplier to Array.vi"
File 21="vi.lib/prirvin/Graph Utilities/Utilities/Variant to 2D Array.vi"
File 22="vi.lib/prirvin/Graph Utilities/Utilities/Variant to XY-Data.vi"
File 23="vi.lib/prirvin/Graph Utilities/Typedefs/Histogram--Graph.ctl"
File 24="vi.lib/prirvin/Graph Utilities/Typedefs/Histogram--slider.ctl"
File 25="vi.lib/prirvin/Graph Utilities/Typedefs/Intensity Graph.ctl"
File 26="vi.lib/prirvin/Graph Utilities/Typedefs/Scale Mapping --enum.ctl"
File 27="vi.lib/prirvin/Graph Utilities/Typedefs/XY Graph.ctl"
File 28="vi.lib/prirvin/Graph Utilities/subVIs/CETperceptual_ColorTables.vi"
File 29="vi.lib/prirvin/Graph Utilities/subVIs/Create Custom Color Table.vi"
File 30="vi.lib/prirvin/Graph Utilities/subVIs/Interpolate Color V8.vi"
File 31="vi.lib/prirvin/Graph Utilities/subVIs/Normalized Gaussian.vi"
File 32="vi.lib/prirvin/Graph Utilities/subVIs/Step Average.vi"
File 33="vi.lib/prirvin/Graph Utilities/Intensity Graph/Get Intensity Graph Cursor (Control).vi"
File 34="vi.lib/prirvin/Graph Utilities/Intensity Graph/Get Intensity Graph Value.vi"
File 35="vi.lib/prirvin/Graph Utilities/Intensity Graph/Get Intensity Graph X Label.vi"
File 36="vi.lib/prirvin/Graph Utilities/Intensity Graph/Get Intensity Graph X Scale.vi"
File 37="vi.lib/prirvin/Graph Utilities/Intensity Graph/Get Intensity Graph Y Label.vi"
File 38="vi.lib/prirvin/Graph Utilities/Intensity Graph/Get Intensity Graph Y Scale.vi"
File 39="vi.lib/prirvin/Graph Utilities/Intensity Graph/Get Intensity Graph Z Label.vi"
File 40="vi.lib/prirvin/Graph Utilities/Intensity Graph/Set Intensity Graph Cursor.vi"
File 41="vi.lib/prirvin/Graph Utilities/Intensity Graph/Set Intensity Graph Value.vi"
File 42="vi.lib/prirvin/Graph Utilities/Intensity Graph/Set Intensity Graph X Label.vi"
File 43="vi.lib/prirvin/Graph Utilities/Intensity Graph/Set Intensity Graph X Range.vi"
File 44="vi.lib/prirvin/Graph Utilities/Intensity Graph/Set Intensity Graph X Scale Array.vi"
File 45="vi.lib/prirvin/Graph Utilities/Intensity Graph/Set Intensity Graph X Scale Min and Max.vi"
File 46="vi.lib/prirvin/Graph Utilities/Intensity Graph/Set Intensity Graph Y Label.vi"
File 47="vi.lib/prirvin/Graph Utilities/Intensity Graph/Set Intensity Graph Y Range.vi"
File 48="vi.lib/prirvin/Graph Utilities/Intensity Graph/Set Intensity Graph Y Scale Array.vi"
File 49="vi.lib/prirvin/Graph Utilities/Intensity Graph/Set Intensity Graph Y Scale Min and Max.vi"
File 50="vi.lib/prirvin/Graph Utilities/Intensity Graph/Set Intensity Graph Z Color.vi"
File 51="vi.lib/prirvin/Graph Utilities/Intensity Graph/Set Intensity Graph Z Label.vi"
File 52="vi.lib/prirvin/Graph Utilities/Intensity Graph/Set Intensity Graph Z Range.vi"
File 53="vi.lib/prirvin/Graph Utilities/Histogram/adjust_histogram_cursor.vi"
File 54="vi.lib/prirvin/Graph Utilities/Histogram/calculate_histogram.vi"
File 55="vi.lib/prirvin/Graph Utilities/Histogram/Intensity Graph Histogram Control.vi"
File 56="vi.lib/prirvin/Graph Utilities/API/Choose Color Table.vi"
File 57="vi.lib/prirvin/Graph Utilities/API/Intensity Graph Linecut (Horizontal) (by val).vi"
File 58="vi.lib/prirvin/Graph Utilities/API/Intensity Graph Linecut (Horizontal).vi"
File 59="vi.lib/prirvin/Graph Utilities/API/Intensity Graph Linecut (Vertical) (by val).vi"
File 60="vi.lib/prirvin/Graph Utilities/API/Intensity Graph Linecut (Vertical).vi"
File 61="vi.lib/prirvin/Graph Utilities/API/Intensity Graph to XY Graph (Horizontal) (by val).vi"
File 62="vi.lib/prirvin/Graph Utilities/API/Intensity Graph to XY Graph (Horizontal).vi"
File 63="vi.lib/prirvin/Graph Utilities/API/Intensity Graph to XY Graph (Vertical) (by val).vi"
File 64="vi.lib/prirvin/Graph Utilities/API/Intensity Graph to XY Graph (Vertical).vi"
File 65="vi.lib/prirvin/Graph Utilities/API/XY Graph to Intensity Graph (by val).vi"
File 66="vi.lib/prirvin/Graph Utilities/API/XY Graph to Intensity Graph.vi"
File 67="vi.lib/prirvin/Graph Utilities/Accessors/Read Intensity Graph ref.vi"
File 68="vi.lib/prirvin/Graph Utilities/Accessors/Read XY Graph ref.vi"
File 69="vi.lib/prirvin/Graph Utilities/Accessors/Write Intensity Graph ref.vi"
File 70="vi.lib/prirvin/Graph Utilities/Accessors/Write XY Graph ref.vi"
File 71="examples/PRIrvin/Graph Utilities/Graph Utilities Tree.vi"
File 72="examples/PRIrvin/Graph Utilities/Histogram.vi"
File 73="examples/PRIrvin/Graph Utilities/Image Color Table.vi"
File 74="examples/PRIrvin/Graph Utilities/Intensity Graph to XY Graph.vi"
File 75="examples/PRIrvin/Graph Utilities/Linecut.vi"


[File Group 1]
Target Dir="<vi.lib>/addons/prirvin"
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
Target Dir="<vi.lib>/addons/prirvin"
Replace Mode="Always"
Num Files=1
File 0="controls_levylab_lib_graph_utilities.mnu"
