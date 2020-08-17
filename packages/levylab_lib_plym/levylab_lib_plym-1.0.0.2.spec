[Package]
Name="levylab_lib_plym"
Version="1.0.0.2"
Release=""
ID=a33105898332bbd6be7c1264ddf6354c
File Format="vip"
Format Version="2017"
Display Name="PLYM"


[Description]
Description="PLYM (is a) LabVIEW YAML Parser"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2020, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin, Phil Shenk"
Demo="FALSE"
Release Notes="- Build for LV2016"
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
Requires="jdp_science_lib_common_utilities>=1.2.0.11,mgi_lib_string>=1.1.1.5,oglib_dictionary>=4.0.0.4,oglib_string>=4.1.0.12"
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
Num Files=26
File 0="user.lib/LevyLab/PLYM/Flatten to YAML.vi"
File 1="user.lib/LevyLab/PLYM/Unflatten from YAML.vi"
File 2="user.lib/LevyLab/PLYM/YAML.lvclass"
File 3="user.lib/LevyLab/PLYM/yaml_parser_phil.lvproj"
File 4="user.lib/LevyLab/PLYM/Unflatten from YAML/dictionary_nested_references_to_nested_contents.vi"
File 5="user.lib/LevyLab/PLYM/Unflatten from YAML/Extract_Value_from_Patrick's_YAML.vi"
File 6="user.lib/LevyLab/PLYM/Unflatten from YAML/Extract_WaveformShape_from_Patrick's_YAML.vi"
File 7="user.lib/LevyLab/PLYM/Unflatten from YAML/Fix_YAML.vi"
File 8="user.lib/LevyLab/PLYM/Unflatten from YAML/nested_dictionaries_to_populate_tree_ctl.vi"
File 9="user.lib/LevyLab/PLYM/Unflatten from YAML/Parse Comments from CtlExp.vi"
File 10="user.lib/LevyLab/PLYM/Unflatten from YAML/Recursive_core_YAML_parser.vi"
File 11="user.lib/LevyLab/PLYM/Unflatten from YAML/tool/CheckStringEmptySpaces.vi"
File 12="user.lib/LevyLab/PLYM/Unflatten from YAML/tool/CountSpaces.vi"
File 13="user.lib/LevyLab/PLYM/Unflatten from YAML/tool/DetermineArraySize.vi"
File 14="user.lib/LevyLab/PLYM/Unflatten from YAML/tool/DetermineSubdictionaryLength.vi"
File 15="user.lib/LevyLab/PLYM/Unflatten from YAML/tool/IsDashLine.vi"
File 16="user.lib/LevyLab/PLYM/Unflatten from YAML/tool/IsFloatingColon.vi"
File 17="user.lib/LevyLab/PLYM/Unflatten from YAML/tool/IsFloatingColonLine.vi"
File 18="user.lib/LevyLab/PLYM/Unflatten from YAML/tool/string contains expression.vi"
File 19="user.lib/LevyLab/PLYM/Flatten to YAML/YAML.AddSections.vi"
File 20="user.lib/LevyLab/PLYM/Flatten to YAML/YAML.List.vi"
File 21="user.lib/LevyLab/PLYM/Flatten to YAML/YAML.Multiline.vi"
File 22="user.lib/LevyLab/PLYM/Flatten to YAML/YAML.NestedSection.vi"
File 23="user.lib/LevyLab/PLYM/Flatten to YAML/YAML.Scaler.vi"
File 24="examples/LevyLab/PLYM/example/parse and get nested key-val pairs.vi"
File 25="examples/LevyLab/PLYM/example/test_tree_ctl.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=4
File 0="_functions_levylab_lib_plym_1.mnu"
File 1="_functions_levylab_lib_plym_2.mnu"
File 2="_functions_levylab_lib_plym_3.mnu"
File 3="functions_Levylab_lib_PLYM.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
