[Package]
Name="prirvin_lib_json_schema"
Version="0.2.0.9"
Release=""
ID=e3efecf3bb8ea97e063876be3a50ce82
File Format="vip"
Format Version="2017"
Display Name="JSON-Schema"


[Description]
Description="Library for converting LV objects into JSON Schema"
Summary="Library for converting LV objects into JSON Schema"
License="BSD-3"
Copyright="Copyright (c) 2025, Patrick Irvin"
Distribution=""
Vendor="PRIrvin"
URL="https://github.com/PRIrvin"
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="#2 fix Creat JSON Schema (Interactive).vi button logic\0A#3 fix schema formatting of cluster and nested clusters\0A#4 fix converting table data to json datatypes (converts to numeric rather than string)\0A- add tools for building and stripping JSON $Path\0A- recursively inspect schema to table and vice versa (useful for nested clusters)"
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
Requires="jdp_science_jsontext>=1.9.1.125,jdp_science_lib_common_utilities>=1.4.2.19,jki_lib_state_machine>=2018.0.7.45,oglib_appcontrol>=4.1.0.7,prirvin_lib_prirvin_palette>=1.0.0.3"
Conflicts=""


[Activation]
License File=""
Licensed Library=""


[Files]
Num File Groups="2"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=28
File 0="vi.lib/PRIrvin/JSON-Schema/JSON-Schema.lvlib"
File 1="vi.lib/PRIrvin/JSON-Schema/Tree.vi"
File 2="vi.lib/PRIrvin/JSON-Schema/typedefs/JSON Schema Dialect--Enum.ctl"
File 3="vi.lib/PRIrvin/JSON-Schema/private/Add enum Type to JSON Schema.vi"
File 4="vi.lib/PRIrvin/JSON-Schema/private/Recursive Find Items.vi"
File 5="vi.lib/PRIrvin/JSON-Schema/private/Recursive Merge.vi"
File 6="vi.lib/PRIrvin/JSON-Schema/develop/Generate Schema $defs From Path.vi"
File 7="vi.lib/PRIrvin/JSON-Schema/develop/Generate Schema $defs.vi"
File 8="vi.lib/PRIrvin/JSON-Schema/develop/Get Object Dependencies.vi"
File 9="vi.lib/PRIrvin/JSON-Schema/develop/Get Object Name.vi"
File 10="vi.lib/PRIrvin/JSON-Schema/develop/Preprocess Variant.vi"
File 11="vi.lib/PRIrvin/JSON-Schema/develop/RecursiveDependenceies.vi"
File 12="vi.lib/PRIrvin/JSON-Schema/API/Add Object to JSON Schema.vi"
File 13="vi.lib/PRIrvin/JSON-Schema/API/Build JSON Path.vi"
File 14="vi.lib/PRIrvin/JSON-Schema/API/Choose JSON Schema Dialect.vi"
File 15="vi.lib/PRIrvin/JSON-Schema/API/Create JSON Schema (Interactive).vi"
File 16="vi.lib/PRIrvin/JSON-Schema/API/Create JSON Schema.vi"
File 17="vi.lib/PRIrvin/JSON-Schema/API/Initialize JSON Schema.vi"
File 18="vi.lib/PRIrvin/JSON-Schema/API/JSON Schema Pretty Print.vi"
File 19="vi.lib/PRIrvin/JSON-Schema/API/JSON Schema to Table.vi"
File 20="vi.lib/PRIrvin/JSON-Schema/API/Read Typedef Description (path).vi"
File 21="vi.lib/PRIrvin/JSON-Schema/API/Read Typedef Description (variant).vi"
File 22="vi.lib/PRIrvin/JSON-Schema/API/Read Typedef Description.vi"
File 23="vi.lib/PRIrvin/JSON-Schema/API/Strip JSON Path.vi"
File 24="vi.lib/PRIrvin/JSON-Schema/API/Table to JSON Schema.vi"
File 25="vi.lib/PRIrvin/JSON-Schema/API/Write Typedef Description (path).vi"
File 26="vi.lib/PRIrvin/JSON-Schema/API/Write Typedef Description (variant).vi"
File 27="vi.lib/PRIrvin/JSON-Schema/API/Write Typedef Description.vi"


[File Group 1]
Target Dir="<vi.lib>/addons/prirvin"
Replace Mode="Always"
Num Files=2
File 0="_functions_prirvin_lib_json_schema_1.mnu"
File 1="functions_prirvin_lib_json_schema.mnu"
