[Package]
Name="jdp_science_postgresql"
Version="0.1.1.10"
Release=""
ID=52e911f7a2e744356d1d4c262bf99e62
File Format="vip"
Format Version="2017"
Display Name="PostgreSQL Library"


[Description]
Description="Wrapping of libPQ for PostgreSQL access.  Higher-level than libPQ itself.  See Examples."
Summary=""
License="BSD-2"
Copyright="Copyright (c) 2016, JDP Science Limited"
Distribution=""
Vendor="JDP Science"
URL=""
Packager="James Powell"
Demo="FALSE"
Release Notes="Allow clusters of parameters to include subcluster structure (which is flattened away before binding) as a conveniance.\0AAdd user and password fields to connection string of examples"
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
Requires=""
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
Num Files=57
File 0="vi.lib/JDP Science/PostgreSQL Library/LICENSE"
File 1="vi.lib/JDP Science/PostgreSQL Library/PQ.lvproj"
File 2="vi.lib/JDP Science/PostgreSQL Library/README.md"
File 3="vi.lib/JDP Science/PostgreSQL Library/Templates/SELECT Template.vi"
File 4="vi.lib/JDP Science/PostgreSQL Library/Support/Connection Status.ctl"
File 5="vi.lib/JDP Science/PostgreSQL Library/Support/Create C-string pointer.vi"
File 6="vi.lib/JDP Science/PostgreSQL Library/Support/Format Error.vi"
File 7="vi.lib/JDP Science/PostgreSQL Library/Support/PQ Support.lvlib"
File 8="vi.lib/JDP Science/PostgreSQL Library/Support/Scan Timestamp.vi"
File 9="vi.lib/JDP Science/PostgreSQL Library/Result/Clear.vi"
File 10="vi.lib/JDP Science/PostgreSQL Library/Result/Error.vi"
File 11="vi.lib/JDP Science/PostgreSQL Library/Result/Format Error.vi"
File 12="vi.lib/JDP Science/PostgreSQL Library/Result/Get all results as 1D strings array.vi"
File 13="vi.lib/JDP Science/PostgreSQL Library/Result/Get all results as 2D strings array.vi"
File 14="vi.lib/JDP Science/PostgreSQL Library/Result/Get Column DBL.vi"
File 15="vi.lib/JDP Science/PostgreSQL Library/Result/Get Column I64.vi"
File 16="vi.lib/JDP Science/PostgreSQL Library/Result/Get Column String.vi"
File 17="vi.lib/JDP Science/PostgreSQL Library/Result/Get Column Timestamp.vi"
File 18="vi.lib/JDP Science/PostgreSQL Library/Result/Number of Columns.vi"
File 19="vi.lib/JDP Science/PostgreSQL Library/Result/Number of Rows.vi"
File 20="vi.lib/JDP Science/PostgreSQL Library/Result/PQ Result.lvclass"
File 21="vi.lib/JDP Science/PostgreSQL Library/Result/Result Status.ctl"
File 22="vi.lib/JDP Science/PostgreSQL Library/Result/Result Status.vi"
File 23="vi.lib/JDP Science/PostgreSQL Library/Result/Write Next Column.vi"
File 24="vi.lib/JDP Science/PostgreSQL Library/Result/Write Next Row (First Column).vi"
File 25="vi.lib/JDP Science/PostgreSQL Library/Result/Write Next Row.vi"
File 26="vi.lib/JDP Science/PostgreSQL Library/Result/Write PGresult.vi"
File 27="vi.lib/JDP Science/PostgreSQL Library/Connection/BEGIN.vi"
File 28="vi.lib/JDP Science/PostgreSQL Library/Connection/Cluster to Array (recursive).vi"
File 29="vi.lib/JDP Science/PostgreSQL Library/Connection/Cluster with subclusters to Flat Array.vi"
File 30="vi.lib/JDP Science/PostgreSQL Library/Connection/COMMIT (ROLLBACK on Error).vi"
File 31="vi.lib/JDP Science/PostgreSQL Library/Connection/Connect.vi"
File 32="vi.lib/JDP Science/PostgreSQL Library/Connection/Disconnect.vi"
File 33="vi.lib/JDP Science/PostgreSQL Library/Connection/Error.vi"
File 34="vi.lib/JDP Science/PostgreSQL Library/Connection/Execute (2D string).vi"
File 35="vi.lib/JDP Science/PostgreSQL Library/Connection/Execute (Multiple result with rows).vi"
File 36="vi.lib/JDP Science/PostgreSQL Library/Connection/Execute (no results).vi"
File 37="vi.lib/JDP Science/PostgreSQL Library/Connection/Execute (Return first result with rows).vi"
File 38="vi.lib/JDP Science/PostgreSQL Library/Connection/Execute Command (1D string results).vi"
File 39="vi.lib/JDP Science/PostgreSQL Library/Connection/Execute Command (2D string results).vi"
File 40="vi.lib/JDP Science/PostgreSQL Library/Connection/Execute Command (No results).vi"
File 41="vi.lib/JDP Science/PostgreSQL Library/Connection/Execute Command (Result).vi"
File 42="vi.lib/JDP Science/PostgreSQL Library/Connection/Execute Single Statement (String Parameters).vi"
File 43="vi.lib/JDP Science/PostgreSQL Library/Connection/Execute.vi"
File 44="vi.lib/JDP Science/PostgreSQL Library/Connection/If Error.vi"
File 45="vi.lib/JDP Science/PostgreSQL Library/Connection/libeay32.dll"
File 46="vi.lib/JDP Science/PostgreSQL Library/Connection/libiconv-2.dll"
File 47="vi.lib/JDP Science/PostgreSQL Library/Connection/libintl-8.dll"
File 48="vi.lib/JDP Science/PostgreSQL Library/Connection/libintl.dll"
File 49="vi.lib/JDP Science/PostgreSQL Library/Connection/libpq.dll"
File 50="vi.lib/JDP Science/PostgreSQL Library/Connection/PQ Connection.lvclass"
File 51="vi.lib/JDP Science/PostgreSQL Library/Connection/Single Command with parameters.vi"
File 52="vi.lib/JDP Science/PostgreSQL Library/Connection/ssleay32.dll"
File 53="examples/JDP Science/PostgreSQL Library/PQ Example Many INSERTs.vi"
File 54="examples/JDP Science/PostgreSQL Library/PQ Example SELECT Clusters.vi"
File 55="examples/JDP Science/PostgreSQL Library/PQ Example SELECT, Parameters.vi"
File 56="examples/JDP Science/PostgreSQL Library/Test MultiValue INSERT.vi"


[File Group 1]
Target Dir="<menus>/Categories/Computer"
Replace Mode="Always"
Num Files=1
File 0="functions_JDP_Science_PostgreSQL.mnu"
