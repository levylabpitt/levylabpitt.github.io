[Package]
Name="levylab_lib_xy_utilities"
Version="1.0.0.1"
Release=""
ID=3aac6ec4b164a3a4c585c3dd8adb6702
File Format="vip"
Format Version="2017"
Display Name="XY Utilities"


[Description]
Description="Utilities for working with XY-data type (Cluster of 1D X and Y arrays).\0A\0ASupported methods:\0A- Arithmetic: Add, Subtract, Multiply, Divide\0A- Array: Sort, Reverse, Decimate, Subset, Sway X and Y, Get X and Y\0A- DSP: Derivative, Average, Interpolate, Resample, FFT Spectrum, FFT Power Spectrum"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2019, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="Initial build"
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
Requires="levylab_lib_control_vi>=1.3.0.11"
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
Num Files=57
File 0="user.lib/LevyLab/XY Uilities/Add.vi"
File 1="user.lib/LevyLab/XY Uilities/Average.vi"
File 2="user.lib/LevyLab/XY Uilities/Decimate.vi"
File 3="user.lib/LevyLab/XY Uilities/Derivative.vi"
File 4="user.lib/LevyLab/XY Uilities/Divide.vi"
File 5="user.lib/LevyLab/XY Uilities/FFT Power Spectrum.vi"
File 6="user.lib/LevyLab/XY Uilities/FFT Spectrum.vi"
File 7="user.lib/LevyLab/XY Uilities/Get X and Y.vi"
File 8="user.lib/LevyLab/XY Uilities/Interpolate.vi"
File 9="user.lib/LevyLab/XY Uilities/Multiply.vi"
File 10="user.lib/LevyLab/XY Uilities/Resample.vi"
File 11="user.lib/LevyLab/XY Uilities/Reverse.vi"
File 12="user.lib/LevyLab/XY Uilities/Sort.vi"
File 13="user.lib/LevyLab/XY Uilities/Subset.vi"
File 14="user.lib/LevyLab/XY Uilities/Subtract.vi"
File 15="user.lib/LevyLab/XY Uilities/Swap X and Y.vi"
File 16="user.lib/LevyLab/XY Uilities/xy_utilities.lvlib"
File 17="user.lib/LevyLab/XY Uilities/xy_utilities.lvproj"
File 18="user.lib/LevyLab/XY Uilities/templates/Template-XY-data (multiple).vit"
File 19="user.lib/LevyLab/XY Uilities/templates/Template-XY-data (single).vit"
File 20="user.lib/LevyLab/XY Uilities/templates/Template-XY-data.vit"
File 21="user.lib/LevyLab/XY Uilities/subVIs/Add float (multiple).vi"
File 22="user.lib/LevyLab/XY Uilities/subVIs/Add float (single).vi"
File 23="user.lib/LevyLab/XY Uilities/subVIs/Add XY (multiple).vi"
File 24="user.lib/LevyLab/XY Uilities/subVIs/Add XY (single).vi"
File 25="user.lib/LevyLab/XY Uilities/subVIs/Decimate (multiple).vi"
File 26="user.lib/LevyLab/XY Uilities/subVIs/Decimate (single).vi"
File 27="user.lib/LevyLab/XY Uilities/subVIs/Derivative (multiple).vi"
File 28="user.lib/LevyLab/XY Uilities/subVIs/Derivative (single).vi"
File 29="user.lib/LevyLab/XY Uilities/subVIs/Divide float (multiple).vi"
File 30="user.lib/LevyLab/XY Uilities/subVIs/Divide float (single).vi"
File 31="user.lib/LevyLab/XY Uilities/subVIs/FFT (multiple).vi"
File 32="user.lib/LevyLab/XY Uilities/subVIs/FFT (single).vi"
File 33="user.lib/LevyLab/XY Uilities/subVIs/Get X and Y (multiple).vi"
File 34="user.lib/LevyLab/XY Uilities/subVIs/Get X and Y (single).vi"
File 35="user.lib/LevyLab/XY Uilities/subVIs/Interpolate (multiple).vi"
File 36="user.lib/LevyLab/XY Uilities/subVIs/Interpolate (single).vi"
File 37="user.lib/LevyLab/XY Uilities/subVIs/Multiply float (multiple).vi"
File 38="user.lib/LevyLab/XY Uilities/subVIs/Multiply float (single).vi"
File 39="user.lib/LevyLab/XY Uilities/subVIs/PS (multiple).vi"
File 40="user.lib/LevyLab/XY Uilities/subVIs/PS (single).vi"
File 41="user.lib/LevyLab/XY Uilities/subVIs/Resample (multiple).vi"
File 42="user.lib/LevyLab/XY Uilities/subVIs/Resample (single).vi"
File 43="user.lib/LevyLab/XY Uilities/subVIs/Reverse (multiple).vi"
File 44="user.lib/LevyLab/XY Uilities/subVIs/Reverse (single).vi"
File 45="user.lib/LevyLab/XY Uilities/subVIs/Sort (multiple).vi"
File 46="user.lib/LevyLab/XY Uilities/subVIs/Sort (single).vi"
File 47="user.lib/LevyLab/XY Uilities/subVIs/Subset (multiple).vi"
File 48="user.lib/LevyLab/XY Uilities/subVIs/Subset (single).vi"
File 49="user.lib/LevyLab/XY Uilities/subVIs/Subtract float (multiple).vi"
File 50="user.lib/LevyLab/XY Uilities/subVIs/Subtract float (single).vi"
File 51="user.lib/LevyLab/XY Uilities/subVIs/Subtract XY (multiple).vi"
File 52="user.lib/LevyLab/XY Uilities/subVIs/Subtract XY (single).vi"
File 53="user.lib/LevyLab/XY Uilities/subVIs/Swap X and Y (multiple).vi"
File 54="user.lib/LevyLab/XY Uilities/subVIs/Swap X and Y (single).vi"
File 55="user.lib/LevyLab/XY Uilities/examples/Test.vi"
File 56="user.lib/LevyLab/XY Uilities/examples/Tree.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=2
File 0="_functions_levylab_lib_xy_utilities_1.mnu"
File 1="functions_LevyLab_lib_XY_Utilities.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
