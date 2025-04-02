[Package]
Name="jdp_science_postgresql"
Version="0.3.1.19"
Release=""
ID=2529f7d0dcbc78edf6830c0607489565
File Format="vip"
Format Version="2017"
Display Name="PostgreSQL Library"


[Description]
Description="Wrapping of libPQ for PostgreSQL access.  Higher-level than libPQ itself.  See Examples.\0A\0AFollow this tutorial to install LibPQ on an NI Linux RT target :\0Ahttps://forums.ni.com/t5/NI-Linux-Real-Time-Documents/Tutorial-PostgreSQL-with-LabVIEW/tac-p/4111331\0A\0AMake sure to run VIPM as admin when installing this package."
Summary="Wrapping of libPQ for PostgreSQL access"
License="BSD"
Copyright="Copyright (c) 2016, JDP Science Limited"
Distribution=""
Vendor="JDP Science"
URL="https://www.vipm.io/package/jdp_science_postgresql/"
Packager="JDP Science"
Demo="FALSE"
Release Notes="0.3.1:\0A- add support for COPY (issue #5)\0A- update palette\0A- update Examples\0A\0ANew in 0.3 :\0A- Check if the library was compiled as threadsafe and make library calls according to that.\0A- added Ping Param VI\0A- Gives option to force all calls being made in the UI thread, as in some cases "any thread" calls cause LabVIEW to crash.\0A- included dependency packages into the VIP\0A\0AThanks to contributors Antoine Chalons (@antoinechalons), Patrick Irvin (@ciozi137), and Tom McQuillan"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="FALSE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"


[Platform]
Exclusive_LabVIEW_Version="LabVIEW>=17.0"
Exclusive_LabVIEW_System="ALL"
Exclusive_OS="Windows NT,Linux"


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
Requires="oglib_array>=4.1.1.14,oglib_string>=5.0.0.25"
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
Num Files=66
File 0="vi.lib/JDP Science/PostgreSQL Library/PQ.lvproj"
File 1="vi.lib/JDP Science/PostgreSQL Library/Templates/SELECT Template.vi"
File 2="vi.lib/JDP Science/PostgreSQL Library/Support/Connection Status.ctl"
File 3="vi.lib/JDP Science/PostgreSQL Library/Support/Create C-string pointer.vi"
File 4="vi.lib/JDP Science/PostgreSQL Library/Support/Format Error.vi"
File 5="vi.lib/JDP Science/PostgreSQL Library/Support/PQ Support.lvlib"
File 6="vi.lib/JDP Science/PostgreSQL Library/Support/Scan Timestamp.vi"
File 7="vi.lib/JDP Science/PostgreSQL Library/Result/Clear.vi"
File 8="vi.lib/JDP Science/PostgreSQL Library/Result/Error.vi"
File 9="vi.lib/JDP Science/PostgreSQL Library/Result/Format Error.vi"
File 10="vi.lib/JDP Science/PostgreSQL Library/Result/Get all results as 1D strings array.vi"
File 11="vi.lib/JDP Science/PostgreSQL Library/Result/Get all results as 2D strings array.vi"
File 12="vi.lib/JDP Science/PostgreSQL Library/Result/Get Column DBL.vi"
File 13="vi.lib/JDP Science/PostgreSQL Library/Result/Get Column Headers.vi"
File 14="vi.lib/JDP Science/PostgreSQL Library/Result/Get Column I64.vi"
File 15="vi.lib/JDP Science/PostgreSQL Library/Result/Get Column String.vi"
File 16="vi.lib/JDP Science/PostgreSQL Library/Result/Get Column Timestamp.vi"
File 17="vi.lib/JDP Science/PostgreSQL Library/Result/InitResult.vi"
File 18="vi.lib/JDP Science/PostgreSQL Library/Result/Number of Columns.vi"
File 19="vi.lib/JDP Science/PostgreSQL Library/Result/Number of Rows.vi"
File 20="vi.lib/JDP Science/PostgreSQL Library/Result/PQ Result.lvclass"
File 21="vi.lib/JDP Science/PostgreSQL Library/Result/Result Status.ctl"
File 22="vi.lib/JDP Science/PostgreSQL Library/Result/Result Status.vi"
File 23="vi.lib/JDP Science/PostgreSQL Library/Result/Write LibPath.vi"
File 24="vi.lib/JDP Science/PostgreSQL Library/Result/Write Next Column.vi"
File 25="vi.lib/JDP Science/PostgreSQL Library/Result/Write Next Row (First Column).vi"
File 26="vi.lib/JDP Science/PostgreSQL Library/Result/Write Next Row.vi"
File 27="vi.lib/JDP Science/PostgreSQL Library/Result/Write PGresult.vi"
File 28="vi.lib/JDP Science/PostgreSQL Library/Connection/BEGIN.vi"
File 29="vi.lib/JDP Science/PostgreSQL Library/Connection/CheckIfThreadSafe.vi"
File 30="vi.lib/JDP Science/PostgreSQL Library/Connection/Cluster to Array (recursive).vi"
File 31="vi.lib/JDP Science/PostgreSQL Library/Connection/Cluster with subclusters to Flat Array.vi"
File 32="vi.lib/JDP Science/PostgreSQL Library/Connection/COMMIT (ROLLBACK on Error).vi"
File 33="vi.lib/JDP Science/PostgreSQL Library/Connection/Connect.vi"
File 34="vi.lib/JDP Science/PostgreSQL Library/Connection/COPY.vi"
File 35="vi.lib/JDP Science/PostgreSQL Library/Connection/Disconnect.vi"
File 36="vi.lib/JDP Science/PostgreSQL Library/Connection/Error.vi"
File 37="vi.lib/JDP Science/PostgreSQL Library/Connection/Execute (2D string).vi"
File 38="vi.lib/JDP Science/PostgreSQL Library/Connection/Execute (Multiple result with rows).vi"
File 39="vi.lib/JDP Science/PostgreSQL Library/Connection/Execute (no results).vi"
File 40="vi.lib/JDP Science/PostgreSQL Library/Connection/Execute (Return first result with rows).vi"
File 41="vi.lib/JDP Science/PostgreSQL Library/Connection/Execute Command (1D string results).vi"
File 42="vi.lib/JDP Science/PostgreSQL Library/Connection/Execute Command (2D string results).vi"
File 43="vi.lib/JDP Science/PostgreSQL Library/Connection/Execute Command (No results).vi"
File 44="vi.lib/JDP Science/PostgreSQL Library/Connection/Execute Command (Result).vi"
File 45="vi.lib/JDP Science/PostgreSQL Library/Connection/Execute Single Statement (String Parameters).vi"
File 46="vi.lib/JDP Science/PostgreSQL Library/Connection/Execute.vi"
File 47="vi.lib/JDP Science/PostgreSQL Library/Connection/Format SQL COPY.vi"
File 48="vi.lib/JDP Science/PostgreSQL Library/Connection/If Error.vi"
File 49="vi.lib/JDP Science/PostgreSQL Library/Connection/libeay32.dll"
File 50="vi.lib/JDP Science/PostgreSQL Library/Connection/libiconv-2.dll"
File 51="vi.lib/JDP Science/PostgreSQL Library/Connection/libintl-8.dll"
File 52="vi.lib/JDP Science/PostgreSQL Library/Connection/libintl.dll"
File 53="vi.lib/JDP Science/PostgreSQL Library/Connection/libpq.dll"
File 54="vi.lib/JDP Science/PostgreSQL Library/Connection/Ping Params.vi"
File 55="vi.lib/JDP Science/PostgreSQL Library/Connection/pingParam.ctl"
File 56="vi.lib/JDP Science/PostgreSQL Library/Connection/PQ Connection.lvclass"
File 57="vi.lib/JDP Science/PostgreSQL Library/Connection/Single Command with parameters.vi"
File 58="vi.lib/JDP Science/PostgreSQL Library/Connection/ssleay32.dll"
File 59="vi.lib/JDP Science/_PostgreSQL Library_internal_deps/libpq.dll"
File 60="examples/JDP Science/PostgreSQL Library/PQ Example COPY file.vi"
File 61="examples/JDP Science/PostgreSQL Library/PQ Example COPY.vi"
File 62="examples/JDP Science/PostgreSQL Library/PQ Example INSERT Many.vi"
File 63="examples/JDP Science/PostgreSQL Library/PQ Example INSERT MultiValue.vi"
File 64="examples/JDP Science/PostgreSQL Library/PQ Example SELECT Clusters.vi"
File 65="examples/JDP Science/PostgreSQL Library/PQ Example SELECT Parameters.vi"


[File Group 1]
Target Dir="<menus>/Categories/Computer"
Replace Mode="Always"
Num Files=1
File 0="functions_JDP_Science_PostgreSQL.mnu"
