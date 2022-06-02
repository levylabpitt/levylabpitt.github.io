[Package]
Name="levylab_lib_relay_box"
Version="1.1.1.2"
Release=""
ID=a453db2e4f0e2fb43f0a17f5a3673cb5
File Format="vip"
Format Version="2017"
Display Name="Relay Box"


[Description]
Description="Software to control resistor relay box"
Summary=""
License=""
Copyright="Copyright (c) 2022, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="John Maier"
Demo="FALSE"
Release Notes="- Update to LV2019\0A- Relink subVIs, FTD LV drivers and dlls\0A--> Major reorganizing of code"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="FALSE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"


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
Requires="jki_lib_state_machine>=2018.0.7.45,oglib_appcontrol>=4.1.0.7"
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
Num Files=91
File 0="user.lib/LevyLab/Relay Box/Relay-Box.lvclass"
File 1="user.lib/LevyLab/Relay Box/RelayBox.lvproj"
File 2="user.lib/LevyLab/Relay Box/Typedefs/Resistor--enum.ctl"
File 3="user.lib/LevyLab/Relay Box/subVIs/Close.vi"
File 4="user.lib/LevyLab/Relay Box/subVIs/Control Relay (256).vi"
File 5="user.lib/LevyLab/Relay Box/subVIs/Control Relay (boolean).vi"
File 6="user.lib/LevyLab/Relay Box/subVIs/Control Relay.vi"
File 7="user.lib/LevyLab/Relay Box/subVIs/Initialize.vi"
File 8="user.lib/LevyLab/Relay Box/subVIs/Port Index Search.vi"
File 9="user.lib/LevyLab/Relay Box/subVIs/Read EEPROM.vi"
File 10="user.lib/LevyLab/Relay Box/subVIs/Read Relay.vi"
File 11="user.lib/LevyLab/Relay Box/D2XX_Functions/D2XX_Functions.lvlib"
File 12="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Clear_DTR.vi"
File 13="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Clear_RTS.vi"
File 14="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Close_Device.vi"
File 15="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Create_Device_Info_List.vi"
File 16="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Cycle_Port.vi"
File 17="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_EEPROM_Read.vi"
File 18="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Erase_EEPROM.vi"
File 19="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Get_Bit_Mode.vi"
File 20="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Get_COM_Port_Number.vi"
File 21="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Get_Device_Description_By_Index.vi"
File 22="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Get_Device_Info.vi"
File 23="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Get_Device_Info_Detail.vi"
File 24="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Get_Device_Info_List.vi"
File 25="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Get_Device_LocationID_By_Index.vi"
File 26="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Get_Device_Serial_Number_By_Index.vi"
File 27="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Get_Driver_Version.vi"
File 28="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Get_EEPROM_User_Area_Size.vi"
File 29="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Get_Event_Status.vi"
File 30="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Get_Latency_Timer.vi"
File 31="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Get_Library_Version.vi"
File 32="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Get_Modem_Status.vi"
File 33="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Get_Number_of_Devices.vi"
File 34="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Get_Queue_Status.vi"
File 35="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Get_Status.vi"
File 36="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Open_Device_By_Description.vi"
File 37="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Open_Device_By_Index.vi"
File 38="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Open_Device_By_Location.vi"
File 39="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Open_Device_By_Serial_Number.vi"
File 40="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Purge.vi"
File 41="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Read_Byte_Data.vi"
File 42="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Read_EEPROM_User_Area.vi"
File 43="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Read_FT2232_EEPROM.vi"
File 44="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Read_FT2232H_EEPROM.vi"
File 45="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Read_FT232-FT245B_EEPROM.vi"
File 46="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Read_FT232-FT245R_EEPROM.vi"
File 47="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Read_FT232H_EEPROM.vi"
File 48="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Read_FT4232H_EEPROM.vi"
File 49="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Read_String_Data.vi"
File 50="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Reload.vi"
File 51="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Rescan.vi"
File 52="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Reset_Device.vi"
File 53="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Reset_Port.vi"
File 54="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Restart_InTask.vi"
File 55="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Set_Baud_Rate.vi"
File 56="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Set_Baud_Rate_Divisor.vi"
File 57="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Set_Bit_Mode.vi"
File 58="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Set_Break_Off.vi"
File 59="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Set_Break_On.vi"
File 60="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Set_Characters.vi"
File 61="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Set_Data_Characteristics.vi"
File 62="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Set_Deadman_Timeout.vi"
File 63="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Set_DTR.vi"
File 64="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Set_Event_Notification.vi"
File 65="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Set_Flow_Control.vi"
File 66="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Set_Latency_Timer.vi"
File 67="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Set_Reset_Pipe_Retry_Count.vi"
File 68="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Set_RTS.vi"
File 69="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Set_Timeouts.vi"
File 70="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Set_USB_Parameters.vi"
File 71="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Stop_InTask.vi"
File 72="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Write_Byte_Data.vi"
File 73="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Write_EEPROM_User_Area.vi"
File 74="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Write_FT2232_EEPROM.vi"
File 75="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Write_FT2232H_EEPROM.vi"
File 76="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Write_FT232-FT245B_EEPROM.vi"
File 77="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Write_FT232-FT245R_EEPROM.vi"
File 78="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Write_FT4232H_EEPROM.vi"
File 79="user.lib/LevyLab/Relay Box/D2XX_Functions/FT_Write_String_Data.vi"
File 80="user.lib/LevyLab/Relay Box/D2XX_Functions/FTDI_Status_Explanation.vi"
File 81="user.lib/LevyLab/Relay Box/D2XX_Functions/i386/ftbusui.dll"
File 82="user.lib/LevyLab/Relay Box/D2XX_Functions/i386/ftcserco.dll"
File 83="user.lib/LevyLab/Relay Box/D2XX_Functions/i386/ftd2xx.dll"
File 84="user.lib/LevyLab/Relay Box/D2XX_Functions/i386/ftd2xx.lib"
File 85="user.lib/LevyLab/Relay Box/D2XX_Functions/i386/ftdibus.sys"
File 86="user.lib/LevyLab/Relay Box/D2XX_Functions/i386/ftlang.dll"
File 87="user.lib/LevyLab/Relay Box/D2XX_Functions/i386/ftser2k.sys"
File 88="user.lib/LevyLab/Relay Box/D2XX_Functions/i386/ftserui2.dll"
File 89="user.lib/LevyLab/Relay Box/API/Read Resistor.vi"
File 90="user.lib/LevyLab/Relay Box/API/Set Resistor.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=1
File 0="functions_LevyLab_lib_Relay_Box.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
