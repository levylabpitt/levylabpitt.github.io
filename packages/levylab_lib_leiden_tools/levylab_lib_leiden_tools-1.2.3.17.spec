[Package]
Name="levylab_lib_leiden_tools"
Version="1.2.3.17"
Release=""
ID=d8d2770f4415683ac52afdfc0eced7bd
File Format="vip"
Format Version="2017"
Display Name="Leiden Tools"


[Description]
Description="Tools used by LevyLab to interact with Leiden Temperature Control (TC) and Front Panel (FP).\0A\0A[FP to DSC]\0A- Add FP_to_DSC.vi to the FP.vi source code to write data to the DSC. Works for CF or MNK.\0A\0A[TC to DSC]\0A- Add TC_to_DSC.vi to the TC.vi source code to write data to the DSC. Works for CF or MNK.\0A\0A[Instrument.MNK_TC.lvclass]\0A- API that overrides "Get Temperature.vi" method of Instrument.Cryostat.lvclass\0A\0A[Instrument.MNK_FP.lclass]\0A[Instrument.CF_TC.lvclass]\0A[Instrument.CF_FP.lclass]\0A- possible future functions"
Summary=""
License=""
Copyright="Copyright (c) 2020, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.2.3.17]\0A- update to latest Instrument (v1.5.9.71)"
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
Requires="levylab_lib_levylab_instruments>=1.2.5.38"
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
File 0="user.lib/LevyLab/Leiden Tools/Leiden_Tools.lvproj"
File 1="user.lib/LevyLab/Leiden Tools/Leiden to DSC/TC to DSC/TC_to_DSC.vi"
File 2="user.lib/LevyLab/Leiden Tools/Leiden to DSC/TC to DSC/Typedefs/AVSType-enum.ctl"
File 3="user.lib/LevyLab/Leiden Tools/Leiden to DSC/TC to DSC/Typedefs/TC-cluster.ctl"
File 4="user.lib/LevyLab/Leiden Tools/Leiden to DSC/TC to DSC/subVIs/CF_TC_to_DSC.vi"
File 5="user.lib/LevyLab/Leiden Tools/Leiden to DSC/TC to DSC/subVIs/CF_Z_Bridge_to_DSC.vi"
File 6="user.lib/LevyLab/Leiden Tools/Leiden to DSC/TC to DSC/subVIs/CMN_Cali.vi"
File 7="user.lib/LevyLab/Leiden Tools/Leiden to DSC/TC to DSC/subVIs/MNK_TC_to_DSC.vi"
File 8="user.lib/LevyLab/Leiden Tools/Leiden to DSC/TC to DSC/subVIs/MNK_Z_Bridge_to_DSC.vi"
File 9="user.lib/LevyLab/Leiden Tools/Leiden to DSC/TC to DSC/subVIs/TCParseLeidenComputerNames.vi"
File 10="user.lib/LevyLab/Leiden Tools/Leiden to DSC/subVIs/Computer Info.vi"
File 11="user.lib/LevyLab/Leiden Tools/Leiden to DSC/subVIs/GetLocalComputerName.vi"
File 12="user.lib/LevyLab/Leiden Tools/Leiden to DSC/subVIs/NetVarWrite_dbl.vi"
File 13="user.lib/LevyLab/Leiden Tools/Leiden to DSC/subVIs/NetVarWrite_str.vi"
File 14="user.lib/LevyLab/Leiden Tools/Leiden to DSC/FP to DSC/FP_to_DSC.vi"
File 15="user.lib/LevyLab/Leiden Tools/Leiden to DSC/FP to DSC/Typedefs/FP-cluster.ctl"
File 16="user.lib/LevyLab/Leiden Tools/Leiden to DSC/FP to DSC/Typedefs/FPType-enum.ctl"
File 17="user.lib/LevyLab/Leiden Tools/Leiden to DSC/FP to DSC/subVIs/CF_FP_to_DSC.vi"
File 18="user.lib/LevyLab/Leiden Tools/Leiden to DSC/FP to DSC/subVIs/FPParseLeidenComputerNames.vi"
File 19="user.lib/LevyLab/Leiden Tools/Leiden to DSC/FP to DSC/subVIs/MNK_FP_to_DSC.vi"
File 20="user.lib/LevyLab/Leiden Tools/Leiden to DSC/FP to DSC/subVIs/parse_FP_mode.vi"
File 21="user.lib/LevyLab/Leiden Tools/Instrument.MNK_TC/Instrument.MNK_TC.lvclass"
File 22="user.lib/LevyLab/Leiden Tools/Instrument.MNK_TC/Instrument.MNK_TC.TestLauncher.vi"
File 23="user.lib/LevyLab/Leiden Tools/Instrument.MNK_TC/Process.vi"
File 24="user.lib/LevyLab/Leiden Tools/Instrument.MNK_TC/Private/Read_MNK_Temp_from_DSC.vi"
File 25="user.lib/LevyLab/Leiden Tools/Instrument.MNK_TC/API/Get Temperature.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=2
File 0="_functions_levylab_lib_leiden_tools_1.mnu"
File 1="functions_LevyLab_lib_Leiden_Tools.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
