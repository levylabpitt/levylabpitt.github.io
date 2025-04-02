[Package]
Name="ftdi_lib_d2xx"
Version="1.0.0.2"
Release=""
ID=83bd401af63f674b00763ef549307da4
File Format="vip"
Format Version="2017"
Display Name="D2XX"


[Description]
Description="examples of communicating with FTDI devices through the D2XX drivers and FTD2XX.DLL using LabVIEW. This package organizes files provided by FTDI into a LV library"
Summary="examples of communicating with FTDI devices through the D2XX drivers and FTD2XX.DLL using LabVIEW. "
License="FTDI"
Copyright="Copyright (c) 2024, FTDI"
Distribution=""
Vendor="FTDI"
URL="https://ftdichip.com/software-examples/code-examples/labview-examples/"
Packager="FTDI / Patrick Irvin"
Demo="FALSE"
Release Notes="initial release"
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
Num Files=73
File 0="instr.lib/FTDI/D2XX/D2XX.lvlib"
File 1="instr.lib/FTDI/D2XX/FT_Clear_DTR.vi"
File 2="instr.lib/FTDI/D2XX/FT_Clear_RTS.vi"
File 3="instr.lib/FTDI/D2XX/FT_Close_Device.vi"
File 4="instr.lib/FTDI/D2XX/FT_Create_Device_Info_List.vi"
File 5="instr.lib/FTDI/D2XX/FT_Cycle_Port.vi"
File 6="instr.lib/FTDI/D2XX/FT_Erase_EEPROM.vi"
File 7="instr.lib/FTDI/D2XX/FT_Get_Bit_Mode.vi"
File 8="instr.lib/FTDI/D2XX/FT_Get_COM_Port_Number.vi"
File 9="instr.lib/FTDI/D2XX/FT_Get_Device_Description_By_Index.vi"
File 10="instr.lib/FTDI/D2XX/FT_Get_Device_Info.vi"
File 11="instr.lib/FTDI/D2XX/FT_Get_Device_Info_Detail.vi"
File 12="instr.lib/FTDI/D2XX/FT_Get_Device_Info_List.vi"
File 13="instr.lib/FTDI/D2XX/FT_Get_Device_LocationID_By_Index.vi"
File 14="instr.lib/FTDI/D2XX/FT_Get_Device_Serial_Number_By_Index.vi"
File 15="instr.lib/FTDI/D2XX/FT_Get_Driver_Version.vi"
File 16="instr.lib/FTDI/D2XX/FT_Get_EEPROM_User_Area_Size.vi"
File 17="instr.lib/FTDI/D2XX/FT_Get_Event_Status.vi"
File 18="instr.lib/FTDI/D2XX/FT_Get_Latency_Timer.vi"
File 19="instr.lib/FTDI/D2XX/FT_Get_Library_Version.vi"
File 20="instr.lib/FTDI/D2XX/FT_Get_Modem_Status.vi"
File 21="instr.lib/FTDI/D2XX/FT_Get_Number_of_Devices.vi"
File 22="instr.lib/FTDI/D2XX/FT_Get_Queue_Status.vi"
File 23="instr.lib/FTDI/D2XX/FT_Get_Queue_Status_Ex.vi"
File 24="instr.lib/FTDI/D2XX/FT_Get_Status.vi"
File 25="instr.lib/FTDI/D2XX/FT_Open_Device_By_Description.vi"
File 26="instr.lib/FTDI/D2XX/FT_Open_Device_By_Index.vi"
File 27="instr.lib/FTDI/D2XX/FT_Open_Device_By_Location.vi"
File 28="instr.lib/FTDI/D2XX/FT_Open_Device_By_Serial_Number.vi"
File 29="instr.lib/FTDI/D2XX/FT_Purge.vi"
File 30="instr.lib/FTDI/D2XX/FT_Read_Byte_Data.vi"
File 31="instr.lib/FTDI/D2XX/FT_Read_EEPROM_User_Area.vi"
File 32="instr.lib/FTDI/D2XX/FT_Read_FT2232_EEPROM.vi"
File 33="instr.lib/FTDI/D2XX/FT_Read_FT2232H_EEPROM.vi"
File 34="instr.lib/FTDI/D2XX/FT_Read_FT232-FT245B_EEPROM.vi"
File 35="instr.lib/FTDI/D2XX/FT_Read_FT232-FT245R_EEPROM.vi"
File 36="instr.lib/FTDI/D2XX/FT_Read_FT232H_EEPROM.vi"
File 37="instr.lib/FTDI/D2XX/FT_Read_FT4232H_EEPROM.vi"
File 38="instr.lib/FTDI/D2XX/FT_Read_String_Data.vi"
File 39="instr.lib/FTDI/D2XX/FT_Reload.vi"
File 40="instr.lib/FTDI/D2XX/FT_Rescan.vi"
File 41="instr.lib/FTDI/D2XX/FT_Reset_Device.vi"
File 42="instr.lib/FTDI/D2XX/FT_Reset_Port.vi"
File 43="instr.lib/FTDI/D2XX/FT_Restart_InTask.vi"
File 44="instr.lib/FTDI/D2XX/FT_Set_Baud_Rate.vi"
File 45="instr.lib/FTDI/D2XX/FT_Set_Baud_Rate_Divisor.vi"
File 46="instr.lib/FTDI/D2XX/FT_Set_Bit_Mode.vi"
File 47="instr.lib/FTDI/D2XX/FT_Set_Break_Off.vi"
File 48="instr.lib/FTDI/D2XX/FT_Set_Break_On.vi"
File 49="instr.lib/FTDI/D2XX/FT_Set_Characters.vi"
File 50="instr.lib/FTDI/D2XX/FT_Set_Data_Characteristics.vi"
File 51="instr.lib/FTDI/D2XX/FT_Set_Deadman_Timeout.vi"
File 52="instr.lib/FTDI/D2XX/FT_Set_DTR.vi"
File 53="instr.lib/FTDI/D2XX/FT_Set_Event_Notification.vi"
File 54="instr.lib/FTDI/D2XX/FT_Set_Flow_Control.vi"
File 55="instr.lib/FTDI/D2XX/FT_Set_Latency_Timer.vi"
File 56="instr.lib/FTDI/D2XX/FT_Set_Reset_Pipe_Retry_Count.vi"
File 57="instr.lib/FTDI/D2XX/FT_Set_RTS.vi"
File 58="instr.lib/FTDI/D2XX/FT_Set_Timeouts.vi"
File 59="instr.lib/FTDI/D2XX/FT_Set_USB_Parameters.vi"
File 60="instr.lib/FTDI/D2XX/FT_Stop_InTask.vi"
File 61="instr.lib/FTDI/D2XX/FT_Write_Byte_Data.vi"
File 62="instr.lib/FTDI/D2XX/FT_Write_EEPROM_User_Area.vi"
File 63="instr.lib/FTDI/D2XX/FT_Write_FT2232_EEPROM.vi"
File 64="instr.lib/FTDI/D2XX/FT_Write_FT2232H_EEPROM.vi"
File 65="instr.lib/FTDI/D2XX/FT_Write_FT232-FT245B_EEPROM.vi"
File 66="instr.lib/FTDI/D2XX/FT_Write_FT232-FT245R_EEPROM.vi"
File 67="instr.lib/FTDI/D2XX/FT_Write_FT232H_EEPROM.vi"
File 68="instr.lib/FTDI/D2XX/FT_Write_FT4232H_EEPROM.vi"
File 69="instr.lib/FTDI/D2XX/FT_Write_String_Data.vi"
File 70="instr.lib/FTDI/D2XX/FTDI_Status_Explanation.vi"
File 71="examples/FTDI/D2XX/Write-Read Byte Array Demo.vi"
File 72="examples/FTDI/D2XX/Write-Read String Demo.vi"


[File Group 1]
Target Dir="<instr.lib>/FTDI"
Replace Mode="Always"
Num Files=2
File 0="_functions_ftdi_lib_d2xx_1.mnu"
File 1="functions_FTDI_lib_D2XX.mnu"


[File Group 2]
Target Dir="<instr.lib>/FTDI"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
