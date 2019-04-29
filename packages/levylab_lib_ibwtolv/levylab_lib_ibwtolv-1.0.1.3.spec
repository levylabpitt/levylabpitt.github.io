[Package]
Name="levylab_lib_ibwtolv"
Version="1.0.1.3"
Release=""
ID=dbf3c11b996f0bc289619abf8681cfe4
File Format="vip"
Format Version="2017"
Display Name="IBWtoLV"


[Description]
Description="utilities for opening Igor Binary Wave (IBW) files in Labview"
Summary="utilities for opening Igor Binary Wave (IBW) files in Labview"
License=""
Copyright="Copyright (c) 2019, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="- organize files in a lvproj\0A- remove lvarray2ibw (igorBinV5.llb) (it is now its own, separate package)"
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
Num Files=17
File 0="user.lib/LevyLab/IBWtoLV/IBW to Labview Array 2.0.vi"
File 1="user.lib/LevyLab/IBWtoLV/IBW to Labview Array 2.1.vi"
File 2="user.lib/LevyLab/IBWtoLV/IBW to Labview Array 2.2.vi"
File 3="user.lib/LevyLab/IBWtoLV/IBW to Labview Array 2.3.vi"
File 4="user.lib/LevyLab/IBWtoLV/IBWtoLV.lvproj"
File 5="user.lib/LevyLab/IBWtoLV/utl/dbl-wordswap.vi"
File 6="user.lib/LevyLab/IBWtoLV/utl/IBW_ConvertUnits.vi"
File 7="user.lib/LevyLab/IBWtoLV/utl/IBWtoLV_BinHeader5.vi"
File 8="user.lib/LevyLab/IBWtoLV/utl/IBWtoLV_BinHeader5toDimensionLabels.vi"
File 9="user.lib/LevyLab/IBWtoLV/utl/IBWtoLV_data.vi"
File 10="user.lib/LevyLab/IBWtoLV/utl/IBWtoLV_timestamp.vi"
File 11="user.lib/LevyLab/IBWtoLV/utl/IBWtoLV_WaveHeader5.vi"
File 12="user.lib/LevyLab/IBWtoLV/utl/IBWtoLV_WaveHeader5toDimensionScaling.vi"
File 13="user.lib/LevyLab/IBWtoLV/utl/IBWtoLV_wavename.vi"
File 14="user.lib/LevyLab/IBWtoLV/utl/IBWtoLV_wavenote.vi"
File 15="user.lib/LevyLab/IBWtoLV/utl/PowerSpectrumIBW.vi"
File 16="user.lib/LevyLab/IBWtoLV/utl/sgl-wordswap.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=2
File 0="_functions_levylab_lib_ibwtolv_1.mnu"
File 1="functions_levylab_lib_ibwtolv.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
