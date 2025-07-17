[Package]
Name="ftdi_lib_d2xx"
Version="1.3.0.8"
Release=""
ID=a58e67d7d7392d31c0ccf3dfafed2bb6
File Format="vip"
Format Version="2017"
Display Name="D2XX"


[Description]
Description="Communicate with FTDI devices using D2XX drivers. This package organizes files provided by FTDI into a LV library and adds support for 64 bit LabVIEW."
Summary="Communicate with FTDI devices using D2XX drivers"
License="FTDI"
Copyright="Copyright (c) 2025, FTDI"
Distribution=""
Vendor="FTDI"
URL="https://ftdichip.com/software-examples/code-examples/labview-examples/"
Packager="FTDI / Patrick Irvin"
Demo="FALSE"
Release Notes="Issue #5\0A- Updated installation location (instr.lib/_D2XX/...)\0A- Reorganize palette\0A- Package requires Windows OS"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


[LabVIEW]
close labview before install="TRUE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"
install into global environment="FALSE"


[Platform]
Exclusive_LabVIEW_Version="LabVIEW>=19.0"
Exclusive_LabVIEW_System="ALL"
Exclusive_OS="Windows NT"


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
Num Files=94
File 0="instr.lib/_D2XX/D2XX/D2XX.lvlib"
File 1="instr.lib/_D2XX/D2XX/FT_Clear_DTR.vi"
File 2="instr.lib/_D2XX/D2XX/FT_Clear_RTS.vi"
File 3="instr.lib/_D2XX/D2XX/FT_Close_Device.vi"
File 4="instr.lib/_D2XX/D2XX/FT_Create_Device_Info_List.vi"
File 5="instr.lib/_D2XX/D2XX/FT_Cycle_Port.vi"
File 6="instr.lib/_D2XX/D2XX/FT_Erase_EEPROM.vi"
File 7="instr.lib/_D2XX/D2XX/FT_Get_Bit_Mode.vi"
File 8="instr.lib/_D2XX/D2XX/FT_Get_COM_Port_Number.vi"
File 9="instr.lib/_D2XX/D2XX/FT_Get_Device_Description_By_Index.vi"
File 10="instr.lib/_D2XX/D2XX/FT_Get_Device_Info.vi"
File 11="instr.lib/_D2XX/D2XX/FT_Get_Device_Info_Detail.vi"
File 12="instr.lib/_D2XX/D2XX/FT_Get_Device_Info_List.vi"
File 13="instr.lib/_D2XX/D2XX/FT_Get_Device_LocationID_By_Index.vi"
File 14="instr.lib/_D2XX/D2XX/FT_Get_Device_Serial_Number_By_Index.vi"
File 15="instr.lib/_D2XX/D2XX/FT_Get_Driver_Version.vi"
File 16="instr.lib/_D2XX/D2XX/FT_Get_EEPROM_User_Area_Size.vi"
File 17="instr.lib/_D2XX/D2XX/FT_Get_Event_Status.vi"
File 18="instr.lib/_D2XX/D2XX/FT_Get_Latency_Timer.vi"
File 19="instr.lib/_D2XX/D2XX/FT_Get_Library_Version.vi"
File 20="instr.lib/_D2XX/D2XX/FT_Get_Modem_Status.vi"
File 21="instr.lib/_D2XX/D2XX/FT_Get_Number_of_Devices.vi"
File 22="instr.lib/_D2XX/D2XX/FT_Get_Queue_Status.vi"
File 23="instr.lib/_D2XX/D2XX/FT_Get_Queue_Status_Ex.vi"
File 24="instr.lib/_D2XX/D2XX/FT_Get_Status.vi"
File 25="instr.lib/_D2XX/D2XX/FT_Open_Device_By_Description.vi"
File 26="instr.lib/_D2XX/D2XX/FT_Open_Device_By_Index.vi"
File 27="instr.lib/_D2XX/D2XX/FT_Open_Device_By_Location.vi"
File 28="instr.lib/_D2XX/D2XX/FT_Open_Device_By_Serial_Number.vi"
File 29="instr.lib/_D2XX/D2XX/FT_Purge.vi"
File 30="instr.lib/_D2XX/D2XX/FT_Read_Byte_Data.vi"
File 31="instr.lib/_D2XX/D2XX/FT_Read_EEPROM_User_Area.vi"
File 32="instr.lib/_D2XX/D2XX/FT_Read_FT2232_EEPROM.vi"
File 33="instr.lib/_D2XX/D2XX/FT_Read_FT2232H_EEPROM.vi"
File 34="instr.lib/_D2XX/D2XX/FT_Read_FT232-FT245B_EEPROM.vi"
File 35="instr.lib/_D2XX/D2XX/FT_Read_FT232-FT245R_EEPROM.vi"
File 36="instr.lib/_D2XX/D2XX/FT_Read_FT232H_EEPROM.vi"
File 37="instr.lib/_D2XX/D2XX/FT_Read_FT4232H_EEPROM.vi"
File 38="instr.lib/_D2XX/D2XX/FT_Read_String_Data.vi"
File 39="instr.lib/_D2XX/D2XX/FT_Reload.vi"
File 40="instr.lib/_D2XX/D2XX/FT_Rescan.vi"
File 41="instr.lib/_D2XX/D2XX/FT_Reset_Device.vi"
File 42="instr.lib/_D2XX/D2XX/FT_Reset_Port.vi"
File 43="instr.lib/_D2XX/D2XX/FT_Restart_InTask.vi"
File 44="instr.lib/_D2XX/D2XX/FT_Set_Baud_Rate.vi"
File 45="instr.lib/_D2XX/D2XX/FT_Set_Baud_Rate_Divisor.vi"
File 46="instr.lib/_D2XX/D2XX/FT_Set_Bit_Mode.vi"
File 47="instr.lib/_D2XX/D2XX/FT_Set_Break_Off.vi"
File 48="instr.lib/_D2XX/D2XX/FT_Set_Break_On.vi"
File 49="instr.lib/_D2XX/D2XX/FT_Set_Characters.vi"
File 50="instr.lib/_D2XX/D2XX/FT_Set_Data_Characteristics.vi"
File 51="instr.lib/_D2XX/D2XX/FT_Set_Deadman_Timeout.vi"
File 52="instr.lib/_D2XX/D2XX/FT_Set_DTR.vi"
File 53="instr.lib/_D2XX/D2XX/FT_Set_Event_Notification.vi"
File 54="instr.lib/_D2XX/D2XX/FT_Set_Flow_Control.vi"
File 55="instr.lib/_D2XX/D2XX/FT_Set_Latency_Timer.vi"
File 56="instr.lib/_D2XX/D2XX/FT_Set_Reset_Pipe_Retry_Count.vi"
File 57="instr.lib/_D2XX/D2XX/FT_Set_RTS.vi"
File 58="instr.lib/_D2XX/D2XX/FT_Set_Timeouts.vi"
File 59="instr.lib/_D2XX/D2XX/FT_Set_USB_Parameters.vi"
File 60="instr.lib/_D2XX/D2XX/FT_Stop_InTask.vi"
File 61="instr.lib/_D2XX/D2XX/FT_Write_Byte_Data.vi"
File 62="instr.lib/_D2XX/D2XX/FT_Write_EEPROM_User_Area.vi"
File 63="instr.lib/_D2XX/D2XX/FT_Write_FT2232_EEPROM.vi"
File 64="instr.lib/_D2XX/D2XX/FT_Write_FT2232H_EEPROM.vi"
File 65="instr.lib/_D2XX/D2XX/FT_Write_FT232-FT245B_EEPROM.vi"
File 66="instr.lib/_D2XX/D2XX/FT_Write_FT232-FT245R_EEPROM.vi"
File 67="instr.lib/_D2XX/D2XX/FT_Write_FT232H_EEPROM.vi"
File 68="instr.lib/_D2XX/D2XX/FT_Write_FT4232H_EEPROM.vi"
File 69="instr.lib/_D2XX/D2XX/FT_Write_String_Data.vi"
File 70="instr.lib/_D2XX/D2XX/FTDI_Status_Explanation.vi"
File 71="instr.lib/_D2XX/D2XX/lib/path.vi"
File 72="instr.lib/_D2XX/D2XX/lib/i386/ftbusui.dll"
File 73="instr.lib/_D2XX/D2XX/lib/i386/ftcserco.dll"
File 74="instr.lib/_D2XX/D2XX/lib/i386/ftd2xx.dll"
File 75="instr.lib/_D2XX/D2XX/lib/i386/ftd2xx.lib"
File 76="instr.lib/_D2XX/D2XX/lib/i386/ftdibus.sys"
File 77="instr.lib/_D2XX/D2XX/lib/i386/ftlang.dll"
File 78="instr.lib/_D2XX/D2XX/lib/i386/ftser2k.sys"
File 79="instr.lib/_D2XX/D2XX/lib/i386/ftserui2.dll"
File 80="instr.lib/_D2XX/D2XX/lib/i386/i386.lvclass"
File 81="instr.lib/_D2XX/D2XX/lib/i386/path.i386.vi"
File 82="instr.lib/_D2XX/D2XX/lib/amd64/amd64.lvclass"
File 83="instr.lib/_D2XX/D2XX/lib/amd64/ftbusui.dll"
File 84="instr.lib/_D2XX/D2XX/lib/amd64/ftcserco.dll"
File 85="instr.lib/_D2XX/D2XX/lib/amd64/ftd2xx.lib"
File 86="instr.lib/_D2XX/D2XX/lib/amd64/ftd2xx64.dll"
File 87="instr.lib/_D2XX/D2XX/lib/amd64/ftdibus.sys"
File 88="instr.lib/_D2XX/D2XX/lib/amd64/ftlang.dll"
File 89="instr.lib/_D2XX/D2XX/lib/amd64/ftser2k.sys"
File 90="instr.lib/_D2XX/D2XX/lib/amd64/ftserui2.dll"
File 91="instr.lib/_D2XX/D2XX/lib/amd64/path.amd64.vi"
File 92="examples/D2XX/D2XX/Write-Read Byte Array Demo.vi"
File 93="examples/D2XX/D2XX/Write-Read String Demo.vi"


[File Group 1]
Target Dir="<instr.lib>/D2XX"
Replace Mode="Always"
Num Files=4
File 0="_functions_ftdi_lib_d2xx_1.mnu"
File 1="_functions_ftdi_lib_d2xx_2.mnu"
File 2="_functions_ftdi_lib_d2xx_3.mnu"
File 3="functions_FTDI_lib_D2XX.mnu"


[File Group 2]
Target Dir="<instr.lib>/D2XX"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
