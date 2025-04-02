[Package]
Name="levylab_lib_ppms_data_analysis"
Version="3.2.0.16"
Release=""
ID=1d5fd7af658b363691a723d0fcbe6887
File Format="vip"
Format Version="2010"
Display Name="PPMS Data Analysis"


[Description]
Description=""
Summary=""
License=""
Copyright="Copyright (c) 2013, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Guanglei"
Demo="FALSE"
Release Notes="This is a collection of analysis VIs for PPMS gating experiments. \0AThis version: Save the retrieved data to disk so that it does not save on the front panel, which may crashes labview if the data size is too large.\0A\0A1.2 added line cuts. Placed a stop button in retrieve mode so that the read is only read from the hard disk once. \0A\0AV1.3\0Aa, Write data (including comments) to a single file instead of 4 files, and some front panel data. In this case all the retrieved data can be opened by a master program.\0Ab, Put an option in retrieved data whether we want to apply filtering or not. In the mean time put an option of filtering in the visualizing the data part. \0Ac, Added random telegraph signal analysis VIs. \0Ad, added line cuts for 4 terminal intensity plot\0Ae, replaced the temperal "LV ITX retrieve" with Patrick's new version.\0A\0Av1.4\0Aa, Save only two terminal and Four terminal IV to disk. dI/dV curves are calculated in visualization part.\0Ab, Retrieve data via two different decimation axis, current and voltage. Both retrieved data is saved to disk. The size of dat file does not increase since dI/dV curves are not saved. \0Ac, Added plot log scale function.\0Av1.5\0Aa, added offset to compensate instrumental offset\0Ab, better UI\0Ac, wire additional comments and data retrieval condition to dat file\0Ad, corrected codes for matching the cursor position\0Ae, auto adjust Y scale of the intensity graphs. \0AV1.5.1\0AMinor fix\0AV2.0\0A1, Change the method for dI/dV. Now find derivative vs time. \0A2, Add new tabs for dV/dI\0A3, Restructured the block diagram so that it has cleaner block diagram and executes faster.\0A4, Add Curve analysis VIs for analyzing IV curves. It accormadates with 3 types of XY graphs. No need to convert between each other!\0A5, Put version 1.6 in subVI foler in order to use old extracted dat files. \0A\0AV2.1\0A1) Increased running speed\0A2) Fixed memory overloading after repeated run\0Aver3.0\0Ause New data reference and in place element structure to optimize the memory use\0A\0AV3.1\0A1) insert fake points in region there is no experimental data\0A2) fixed 2T R vs I tab\0A\0AV3.2\0A1) Experimental release...added "3D" data sliicing tab"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="FALSE"


[Platform]
Exclusive_LabVIEW_Version=">=11.0"
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
Num Files=16
File 0="user.lib/LevyLab/PPMS Data Analysis/Curve analysis.vi"
File 1="user.lib/LevyLab/PPMS Data Analysis/Data retrieve engine.vi"
File 2="user.lib/LevyLab/PPMS Data Analysis/GenerateLineCuts.vi"
File 3="user.lib/LevyLab/PPMS Data Analysis/Read_90_configs_ITX.vi"
File 4="user.lib/LevyLab/PPMS Data Analysis/Retrieve and visualize telegraph signal.vi"
File 5="user.lib/LevyLab/PPMS Data Analysis/Retrieve and visulize data.vi"
File 6="user.lib/LevyLab/PPMS Data Analysis/subVI/Average and decimate multiple XY graphs curves.vi"
File 7="user.lib/LevyLab/PPMS Data Analysis/subVI/Data retrieve engine1.6.vi"
File 8="user.lib/LevyLab/PPMS Data Analysis/subVI/Decimate_VS_X_Value.vi"
File 9="user.lib/LevyLab/PPMS Data Analysis/subVI/differential.vi"
File 10="user.lib/LevyLab/PPMS Data Analysis/subVI/Extract Parameters from Comments.vi"
File 11="user.lib/LevyLab/PPMS Data Analysis/subVI/Remove XY graph end points.vi"
File 12="user.lib/LevyLab/PPMS Data Analysis/subVI/Retrieve and visulize data1.6.vi"
File 13="user.lib/LevyLab/PPMS Data Analysis/subVI/Scale Voltage.vi"
File 14="user.lib/LevyLab/PPMS Data Analysis/subVI/Take_portion_of_data.vi"
File 15="user.lib/LevyLab/PPMS Data Analysis/subVI/Telegraph signal analysis.vi"


[File Group 1]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=2
File 0="_functions_levylab_lib_ppms_data_analysis_1.mnu"
File 1="functions_levylab_lib_ppms_data_analysis.mnu"
