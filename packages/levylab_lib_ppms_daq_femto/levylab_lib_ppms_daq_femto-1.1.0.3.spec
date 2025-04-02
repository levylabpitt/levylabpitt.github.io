[Package]
Name="levylab_lib_ppms_daq_femto"
Version="1.1.0.3"
Release=""
ID=cfc7276cb5ac3d47bd91cd47216da20f
File Format="vip"
Format Version="2014"
Display Name="PPMS DAQ Femto"


[Description]
Description="Control VIs for 4 Femto amplifiers in QD PPMS DAQ breakout box.  There are two main VIs:\0A"PPMS_Femto_GUI.vi" is a "GUI" style VI for interacting with amplifiers to check which gain setting is correct, which amplifier has which address, etc.\0A"PPMS_Femto_SetAll.vi" simply sets all parameters for all of the amplifiers and can be called as a subVI."
Summary="Femto controls for PPMS breakout box "
License=""
Copyright="Copyright (c) 2016, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="patrick irvin"
Demo="FALSE"
Release Notes="- added drivers into this project (in \\drivers\\ sub directory\0A- added a file for reading the gain files\0A- added a "functional global variable" for reading/writng the gains instead of the txt file"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="FALSE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"


[Platform]
Exclusive_LabVIEW_Version="LabVIEW>=13.0"
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
Num Files=64
File 0="user.lib/LevyLab/PPMS DAQ Femto/PPMS_Femto_GUI.vi"
File 1="user.lib/LevyLab/PPMS DAQ Femto/PPMS_Femto_SetAll.vi"
File 2="user.lib/LevyLab/PPMS DAQ Femto/subVIs/ConvertDDPCAGainIndex.vi"
File 3="user.lib/LevyLab/PPMS DAQ Femto/subVIs/ConvertDLPVAGainIndex.vi"
File 4="user.lib/LevyLab/PPMS DAQ Femto/subVIs/ConvertDLPVAGainStages.vi"
File 5="user.lib/LevyLab/PPMS DAQ Femto/subVIs/ConvertDLPVAGainStages_to_dB.vi"
File 6="user.lib/LevyLab/PPMS DAQ Femto/subVIs/DLPVA_3_ReadAll.vi"
File 7="user.lib/LevyLab/PPMS DAQ Femto/subVIs/DLPVA_3_WriteAll.vi"
File 8="user.lib/LevyLab/PPMS DAQ Femto/subVIs/DLPVA_4_ReadAll.vi"
File 9="user.lib/LevyLab/PPMS DAQ Femto/subVIs/DLPVA_4_WriteAll.vi"
File 10="user.lib/LevyLab/PPMS DAQ Femto/subVIs/Femto Gain_FGV.vi"
File 11="user.lib/LevyLab/PPMS DAQ Femto/subVIs/FemtoGain_ReadAll.vi"
File 12="user.lib/LevyLab/PPMS DAQ Femto/subVIs/PPMS_Femto_TXT_Global.vi.txt"
File 13="user.lib/LevyLab/PPMS DAQ Femto/subVIs/PPMS_Femto_TXT_Global_READ.vi"
File 14="user.lib/LevyLab/PPMS DAQ Femto/subVIs/PPMS_Femto_TXT_Global_WRITE.vi"
File 15="user.lib/LevyLab/PPMS DAQ Femto/instruments/DDPCA-300.vi"
File 16="user.lib/LevyLab/PPMS DAQ Femto/instruments/DDPCA-300_Set.vi"
File 17="user.lib/LevyLab/PPMS DAQ Femto/instruments/DLPVA-100-B_&_F.vi"
File 18="user.lib/LevyLab/PPMS DAQ Femto/instruments/DLPVA-100-B_&_F_Set.vi"
File 19="user.lib/LevyLab/PPMS DAQ Femto/driver/FEMTO_LUCI-10.lvlib"
File 20="user.lib/LevyLab/PPMS DAQ Femto/driver/LUCI_10.dll"
File 21="user.lib/LevyLab/PPMS DAQ Femto/driver/LUCI_10.h"
File 22="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Adapter_ID_to_Index.vi"
File 23="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Bit_Shifter.vi"
File 24="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Choose_Device.vi"
File 25="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/dir.mnu"
File 26="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Init_UCI.vi"
File 27="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Read._Overload.vi"
File 28="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Reset_Device.vi"
File 29="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Rotate_Bit.vi"
File 30="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Set_Bandwidth.vi"
File 31="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Set_Bandwidth_DHPCA-100.vi"
File 32="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Set_Bandwidth_DHPVA-100.vi"
File 33="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Set_Bandwidth_DHPVA-200.vi"
File 34="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Set_Bandwidth_DLPVA-Series.vi"
File 35="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Set_Coupling.vi"
File 36="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Set_Gain.vi"
File 37="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Set_Gain_DDPCA-300.vi"
File 38="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Set_Gain_DHPCA-100.vi"
File 39="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Set_Gain_DHPVA_Series.vi"
File 40="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Set_Gain_DLPCA-200.vi"
File 41="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Set_Gain_DLPVA-100-B&F_Series.vi"
File 42="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Set_Gain_DLPVA-100-BLN-S.vi"
File 43="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Set_Gain_DLPVA-100-BUN-S.vi"
File 44="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Set_Gain_DUPVA-1-60.vi"
File 45="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Set_Gain_DUPVA-1-70.vi"
File 46="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Set_Gain_OE-200.vi"
File 47="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Set_Mode.vi"
File 48="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/User_Info.vi"
File 49="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Lock-In/dir.mnu"
File 50="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Lock-In/LIA-MV-150.vi"
File 51="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Lock-In/LIA-MVx-200-L.vi"
File 52="user.lib/LevyLab/PPMS DAQ Femto/driver/Control/Lock-In/Read_Unlocked.vi"
File 53="user.lib/LevyLab/PPMS DAQ Femto/driver/Advanced/dir.mnu"
File 54="user.lib/LevyLab/PPMS DAQ Femto/driver/Advanced/Enumerate Usb Devices.vi"
File 55="user.lib/LevyLab/PPMS DAQ Femto/driver/Advanced/Get Product String.vi"
File 56="user.lib/LevyLab/PPMS DAQ Femto/driver/Advanced/Get Status Pin5.vi"
File 57="user.lib/LevyLab/PPMS DAQ Femto/driver/Advanced/Get Status Pin6.vi"
File 58="user.lib/LevyLab/PPMS DAQ Femto/driver/Advanced/Get Status Pin7.vi"
File 59="user.lib/LevyLab/PPMS DAQ Femto/driver/Advanced/Led Off.vi"
File 60="user.lib/LevyLab/PPMS DAQ Femto/driver/Advanced/Led On.vi"
File 61="user.lib/LevyLab/PPMS DAQ Femto/driver/Advanced/Read Adapter ID.vi"
File 62="user.lib/LevyLab/PPMS DAQ Femto/driver/Advanced/Write Adapter ID.vi"
File 63="user.lib/LevyLab/PPMS DAQ Femto/driver/Advanced/Write Data.vi"


[File Group 1]
Target Dir="<user.lib>"
Replace Mode="Always"
Num Files=7
File 0="_functions_levylab_lib_ppms_daq_femto_1.mnu"
File 1="_functions_levylab_lib_ppms_daq_femto_2.mnu"
File 2="_functions_levylab_lib_ppms_daq_femto_3.mnu"
File 3="_functions_levylab_lib_ppms_daq_femto_4.mnu"
File 4="_functions_levylab_lib_ppms_daq_femto_5.mnu"
File 5="_functions_levylab_lib_ppms_daq_femto_6.mnu"
File 6="functions_levylab_lib_ppms_daq_femto.mnu"
