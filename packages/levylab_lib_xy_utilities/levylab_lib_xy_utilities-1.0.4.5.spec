[Package]
Name="levylab_lib_xy_utilities"
Version="1.0.4.5"
Release=""
ID=a986f5f54f9764391e586d17e4867195
File Format="vip"
Format Version="2017"
Display Name="XY Utilities"


[Description]
Description="Utilities for working with XY-data type (Cluster of 1D X and Y arrays).\0A\0ASupported methods:\0A- Arithmetic: Add, Subtract, Multiply, Divide\0A- Array: Sort, Reverse, Decimate, Subset, Sway X and Y, Get X and Y, Append, Waveform to XY\0A- DSP: Derivative, Average, Interpolate, Resample, FFT Spectrum, FFT Power Spectrum"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2020, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.0.4.5]\0ANew method:\0A- XY to Waveform.vi\0ABug Fixes"
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
Requires="jki_lib_state_machine>=2018.0.7.45,levylab_lib_control_vi>=1.3.0.11,oglib_string>=4.1.0.12"
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
File 0="user.lib/LevyLab/XY Uilities/Add.vi"
File 1="user.lib/LevyLab/XY Uilities/Append.vi"
File 2="user.lib/LevyLab/XY Uilities/Average.vi"
File 3="user.lib/LevyLab/XY Uilities/Decimate.vi"
File 4="user.lib/LevyLab/XY Uilities/Derivative.vi"
File 5="user.lib/LevyLab/XY Uilities/Divide.vi"
File 6="user.lib/LevyLab/XY Uilities/FFT Power Spectrum.vi"
File 7="user.lib/LevyLab/XY Uilities/FFT Spectrum.vi"
File 8="user.lib/LevyLab/XY Uilities/Get X and Y.vi"
File 9="user.lib/LevyLab/XY Uilities/Interpolate.vi"
File 10="user.lib/LevyLab/XY Uilities/Multiply.vi"
File 11="user.lib/LevyLab/XY Uilities/Resample.vi"
File 12="user.lib/LevyLab/XY Uilities/Reverse.vi"
File 13="user.lib/LevyLab/XY Uilities/Sort.vi"
File 14="user.lib/LevyLab/XY Uilities/Square.vi"
File 15="user.lib/LevyLab/XY Uilities/Subset.vi"
File 16="user.lib/LevyLab/XY Uilities/Subtract.vi"
File 17="user.lib/LevyLab/XY Uilities/Swap X and Y.vi"
File 18="user.lib/LevyLab/XY Uilities/Symmetrize.vi"
File 19="user.lib/LevyLab/XY Uilities/Waveform to XY.vi"
File 20="user.lib/LevyLab/XY Uilities/XY to Waveform.vi"
File 21="user.lib/LevyLab/XY Uilities/xy_utilities.lvlib"
File 22="user.lib/LevyLab/XY Uilities/xy_utilities.lvproj"
File 23="user.lib/LevyLab/XY Uilities/Typedefs/Interpolation Configuration--cluster.ctl"
File 24="user.lib/LevyLab/XY Uilities/templates/Template-XY-data (multiple).vit"
File 25="user.lib/LevyLab/XY Uilities/templates/Template-XY-data (single).vit"
File 26="user.lib/LevyLab/XY Uilities/subVIs/Add float (multiple).vi"
File 27="user.lib/LevyLab/XY Uilities/subVIs/Add float (single).vi"
File 28="user.lib/LevyLab/XY Uilities/subVIs/Add XY (multiple).vi"
File 29="user.lib/LevyLab/XY Uilities/subVIs/Add XY (single).vi"
File 30="user.lib/LevyLab/XY Uilities/subVIs/Append (multiple).vi"
File 31="user.lib/LevyLab/XY Uilities/subVIs/Append (single).vi"
File 32="user.lib/LevyLab/XY Uilities/subVIs/Decimate (multiple).vi"
File 33="user.lib/LevyLab/XY Uilities/subVIs/Decimate (single).vi"
File 34="user.lib/LevyLab/XY Uilities/subVIs/Derivative (multiple).vi"
File 35="user.lib/LevyLab/XY Uilities/subVIs/Derivative (single).vi"
File 36="user.lib/LevyLab/XY Uilities/subVIs/Divide float (multiple).vi"
File 37="user.lib/LevyLab/XY Uilities/subVIs/Divide float (single).vi"
File 38="user.lib/LevyLab/XY Uilities/subVIs/Divide XY (multiple).vi"
File 39="user.lib/LevyLab/XY Uilities/subVIs/Divide XY (single).vi"
File 40="user.lib/LevyLab/XY Uilities/subVIs/FFT (multiple).vi"
File 41="user.lib/LevyLab/XY Uilities/subVIs/FFT (single).vi"
File 42="user.lib/LevyLab/XY Uilities/subVIs/Get X and Y (multiple).vi"
File 43="user.lib/LevyLab/XY Uilities/subVIs/Get X and Y (single).vi"
File 44="user.lib/LevyLab/XY Uilities/subVIs/Interpolate (multiple).vi"
File 45="user.lib/LevyLab/XY Uilities/subVIs/Interpolate (single).vi"
File 46="user.lib/LevyLab/XY Uilities/subVIs/Multiply float (multiple).vi"
File 47="user.lib/LevyLab/XY Uilities/subVIs/Multiply float (single).vi"
File 48="user.lib/LevyLab/XY Uilities/subVIs/Multiply XY (multiple).vi"
File 49="user.lib/LevyLab/XY Uilities/subVIs/Multiply XY (single).vi"
File 50="user.lib/LevyLab/XY Uilities/subVIs/PS (multiple).vi"
File 51="user.lib/LevyLab/XY Uilities/subVIs/PS (single).vi"
File 52="user.lib/LevyLab/XY Uilities/subVIs/Resample (multiple).vi"
File 53="user.lib/LevyLab/XY Uilities/subVIs/Resample (single).vi"
File 54="user.lib/LevyLab/XY Uilities/subVIs/Reverse (multiple).vi"
File 55="user.lib/LevyLab/XY Uilities/subVIs/Reverse (single).vi"
File 56="user.lib/LevyLab/XY Uilities/subVIs/Sort (multiple).vi"
File 57="user.lib/LevyLab/XY Uilities/subVIs/Sort (single).vi"
File 58="user.lib/LevyLab/XY Uilities/subVIs/Square (multiple).vi"
File 59="user.lib/LevyLab/XY Uilities/subVIs/Square (single).vi"
File 60="user.lib/LevyLab/XY Uilities/subVIs/Subset (multiple).vi"
File 61="user.lib/LevyLab/XY Uilities/subVIs/Subset (single).vi"
File 62="user.lib/LevyLab/XY Uilities/subVIs/Subtract float (multiple).vi"
File 63="user.lib/LevyLab/XY Uilities/subVIs/Subtract float (single).vi"
File 64="user.lib/LevyLab/XY Uilities/subVIs/Subtract XY (multiple).vi"
File 65="user.lib/LevyLab/XY Uilities/subVIs/Subtract XY (single).vi"
File 66="user.lib/LevyLab/XY Uilities/subVIs/Swap X and Y (multiple).vi"
File 67="user.lib/LevyLab/XY Uilities/subVIs/Swap X and Y (single).vi"
File 68="user.lib/LevyLab/XY Uilities/subVIs/Symmetrize (multiple).vi"
File 69="user.lib/LevyLab/XY Uilities/subVIs/Symmetrize (single).vi"
File 70="user.lib/LevyLab/XY Uilities/subVIs/Waveform to XY (multiple).vi"
File 71="user.lib/LevyLab/XY Uilities/subVIs/Waveform to XY (single).vi"
File 72="user.lib/LevyLab/XY Uilities/subVIs/XY to Waveform (multiple).vi"
File 73="user.lib/LevyLab/XY Uilities/subVIs/XY to Waveform (single).vi"
File 74="user.lib/LevyLab/XY Uilities/examples/Test.vi"
File 75="user.lib/LevyLab/XY Uilities/examples/Tree.vi"


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
