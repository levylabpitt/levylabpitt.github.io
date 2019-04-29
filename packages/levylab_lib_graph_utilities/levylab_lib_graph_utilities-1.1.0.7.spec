[Package]
Name="levylab_lib_graph_utilities"
Version="1.1.0.7"
Release=""
ID=75026fe347ff240a167b62dc79ebc180
File Format="vip"
Format Version="2017"
Display Name="Graph Utilities"


[Description]
Description="Misc. graph utilities"
Summary=""
License=""
Copyright="Copyright (c) 2019, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick"
Demo="FALSE"
Release Notes="- organize in project.\0A- new algorithm for interpolating color table"
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
Num Files=12
File 0="user.lib/LevyLab/Graph Utilities/Average xy graphs.vi"
File 1="user.lib/LevyLab/Graph Utilities/BuildXYGraph.vi"
File 2="user.lib/LevyLab/Graph Utilities/Convert XY to polar graph.vi"
File 3="user.lib/LevyLab/Graph Utilities/Example Graph utls.vi"
File 4="user.lib/LevyLab/Graph Utilities/Graph Utilities.lvproj"
File 5="user.lib/LevyLab/Graph Utilities/IntensityScales.vi"
File 6="user.lib/LevyLab/Graph Utilities/IntensityScales_v2.vi"
File 7="user.lib/LevyLab/Graph Utilities/Make Color Table.vi"
File 8="user.lib/LevyLab/Graph Utilities/OffsetMultiplier.vi"
File 9="user.lib/LevyLab/Graph Utilities/View Complex Impedance.vi"
File 10="user.lib/LevyLab/Graph Utilities/XYArray from OffsetMultiplier.vi"
File 11="user.lib/LevyLab/Graph Utilities/XYGraphAddScaler.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=1
File 0="functions_levylab_lib_graph_utilities.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
