[Package]
Name="levylab_lib_xeryon_rotator"
Version="1.0.0.1"
Release=""
ID=634ec4e421993849ae1a61d38ba939f3
File Format="vip"
Format Version="2017"
Display Name="Xeryon-Rotator"


[Description]
Description="instrument framework smo for controlling xeryon rotation stage. initializes communication, monitors rotator status, logs status, and exposed api to for other labview vis to set and get the angle"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2024, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
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
Num Files=98
File 0="instr.lib/Levylab/xeryon-rotator/Xeryon-Rotator.lvproj"
File 1="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Documentation.vi"
File 2="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Inst.Xeryon-Rotator.AppLauncher.vi"
File 3="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Inst.Xeryon-Rotator.lvclass"
File 4="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Process.vi"
File 5="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Typedefs/Inst.Xeryon-Rotator.Commands--Enum.ctl"
File 6="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Typedefs/Inst.Xeryon-Rotator.Configuration--Cluster.ctl"
File 7="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Typedefs/Inst.Xeryon-Rotator.getAll--Cluster.ctl"
File 8="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Typedefs/Inst.Xeryon-Rotator.getAngle--Cluster.ctl"
File 9="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Typedefs/Inst.Xeryon-Rotator.ScanState--Enum.ctl"
File 10="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Typedefs/Inst.Xeryon-Rotator.setAngle--Cluster.ctl"
File 11="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Typedefs/PrivateEvents--Cluster.ctl"
File 12="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Typedefs/PrivateEvents--Inst.Xeryon-Rotator.MessageToProcess.ctl"
File 13="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Typedefs/PublicEvents--Cluster.ctl"
File 14="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Typedefs/PublicEvents--Inst.Xeryon-Rotator.MessageFromProcess.ctl"
File 15="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/test/Test Xeryon API.vi"
File 16="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Private/Inst.Xeryon-Rotator.DoSomething.vi"
File 17="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Private/Inst.Xeryon-Rotator.Get Angle.vi"
File 18="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Private/Inst.Xeryon-Rotator.GetAllData.vi"
File 19="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Private/Inst.Xeryon-Rotator.GetPrivateEvents.vi"
File 20="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Private/Inst.Xeryon-Rotator.Set Angle.vi"
File 21="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Private/Inst.Xeryon-Rotator.Set Speed.vi"
File 22="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Private/Inst.Xeryon-Rotator.Set State.vi"
File 23="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Private/Inst.Xeryon-Rotator.Stop.vi"
File 24="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Close Hardware.vi"
File 25="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Configuration Window.vi"
File 26="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/CreatePrivateEvents.vi"
File 27="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/CreatePublicEvents.vi"
File 28="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/DestroyPrivateEvents.vi"
File 29="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/DestroyPublicEvents.vi"
File 30="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Get SMO Address.vi"
File 31="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Get SMO Name.vi"
File 32="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Get SMO PGSQL Log Paths.vi"
File 33="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Get SMO Port.vi"
File 34="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Get SMO Public API.vi"
File 35="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Get SMO RC Type.vi"
File 36="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Handle Command.vi"
File 37="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Handle getAll.vi"
File 38="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Handle setConfiguration.vi"
File 39="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Open Hardware.vi"
File 40="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Read Configuration File.vi"
File 41="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Write Configuration File.vi"
File 42="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/API/Close.vi"
File 43="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/API/Do Something.vi"
File 44="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/API/Get Angle.vi"
File 45="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/API/Inst.Xeryon-Rotator.GetPublicEvents.vi"
File 46="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/API/Inst.Xeryon-Rotator.MessageToProcess.vi"
File 47="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/API/Open.vi"
File 48="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/API/Set Angle.vi"
File 49="instr.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/API/Set Scan State.vi"
File 50="instr.lib/Levylab/xeryon-rotator/SMOs/Inst UI.Xeryon-Rotator/Inst UI.Xeryon-Rotator.lvclass"
File 51="instr.lib/Levylab/xeryon-rotator/SMOs/Inst UI.Xeryon-Rotator/Inst UI.Xeryon-Rotator.TestLauncher.vi"
File 52="instr.lib/Levylab/xeryon-rotator/SMOs/Inst UI.Xeryon-Rotator/Inst UI.Xeryon-Rotator.UI--Cluster.ctl"
File 53="instr.lib/Levylab/xeryon-rotator/SMOs/Inst UI.Xeryon-Rotator/Process.vi"
File 54="instr.lib/Levylab/xeryon-rotator/drivers/settings_default.txt"
File 55="instr.lib/Levylab/xeryon-rotator/drivers/settings_default_backup.txt"
File 56="instr.lib/Levylab/xeryon-rotator/drivers/settings_default_rotate.txt"
File 57="instr.lib/Levylab/xeryon-rotator/drivers/settings_default_two_stage_example.txt"
File 58="instr.lib/Levylab/xeryon-rotator/drivers/settings_default_xls.txt"
File 59="instr.lib/Levylab/xeryon-rotator/drivers/Xeryon.lvproj"
File 60="instr.lib/Levylab/xeryon-rotator/drivers/examples/Example One Stage.vi"
File 61="instr.lib/Levylab/xeryon-rotator/drivers/examples/Example One Stage_Patrick.vi"
File 62="instr.lib/Levylab/xeryon-rotator/drivers/examples/Example One Stage_Patrick_JKISM.vi"
File 63="instr.lib/Levylab/xeryon-rotator/drivers/examples/Example Three Stage.vi"
File 64="instr.lib/Levylab/xeryon-rotator/drivers/examples/Example Two Stages.vi"
File 65="instr.lib/Levylab/xeryon-rotator/drivers/Class/Controller/AddAxis.vi"
File 66="instr.lib/Levylab/xeryon-rotator/drivers/Class/Controller/Close.vi"
File 67="instr.lib/Levylab/xeryon-rotator/drivers/Class/Controller/Controller.lvclass"
File 68="instr.lib/Levylab/xeryon-rotator/drivers/Class/Controller/getAxisObject.vi"
File 69="instr.lib/Levylab/xeryon-rotator/drivers/Class/Controller/getDataCluster.vi"
File 70="instr.lib/Levylab/xeryon-rotator/drivers/Class/Controller/getDposInCurrentUnits.vi"
File 71="instr.lib/Levylab/xeryon-rotator/drivers/Class/Controller/getEposInCurrentUnits.vi"
File 72="instr.lib/Levylab/xeryon-rotator/drivers/Class/Controller/getStatusBits.vi"
File 73="instr.lib/Levylab/xeryon-rotator/drivers/Class/Controller/initialize.vi"
File 74="instr.lib/Levylab/xeryon-rotator/drivers/Class/Controller/readSettingsFile.vi"
File 75="instr.lib/Levylab/xeryon-rotator/drivers/Class/Controller/receiveData.vi"
File 76="instr.lib/Levylab/xeryon-rotator/drivers/Class/Controller/sendCommand.vi"
File 77="instr.lib/Levylab/xeryon-rotator/drivers/Class/Controller/setDPOS.vi"
File 78="instr.lib/Levylab/xeryon-rotator/drivers/Class/Controller/setSpeed.vi"
File 79="instr.lib/Levylab/xeryon-rotator/drivers/Class/Controller/setStep.vi"
File 80="instr.lib/Levylab/xeryon-rotator/drivers/Class/Communication/Close.vi"
File 81="instr.lib/Levylab/xeryon-rotator/drivers/Class/Communication/Communication.lvclass"
File 82="instr.lib/Levylab/xeryon-rotator/drivers/Class/Communication/Initialize.vi"
File 83="instr.lib/Levylab/xeryon-rotator/drivers/Class/Communication/ReadData.vi"
File 84="instr.lib/Levylab/xeryon-rotator/drivers/Class/Communication/WriteData.vi"
File 85="instr.lib/Levylab/xeryon-rotator/drivers/Class/Axis/Axis.lvclass"
File 86="instr.lib/Levylab/xeryon-rotator/drivers/Class/Axis/convertCurrentUnitsToEncoderUnits.vi"
File 87="instr.lib/Levylab/xeryon-rotator/drivers/Class/Axis/convertEncoderUnitsToCurrentUnits.vi"
File 88="instr.lib/Levylab/xeryon-rotator/drivers/Class/Axis/convertMilliMeterToEncoderUnits.vi"
File 89="instr.lib/Levylab/xeryon-rotator/drivers/Class/Axis/getAxisLetter.vi"
File 90="instr.lib/Levylab/xeryon-rotator/drivers/Class/Axis/getDataCluster.vi"
File 91="instr.lib/Levylab/xeryon-rotator/drivers/Class/Axis/getDposInCurrentUnits.vi"
File 92="instr.lib/Levylab/xeryon-rotator/drivers/Class/Axis/getEposInCurrentUnits.vi"
File 93="instr.lib/Levylab/xeryon-rotator/drivers/Class/Axis/getStatusBits.vi"
File 94="instr.lib/Levylab/xeryon-rotator/drivers/Class/Axis/Initialize.vi"
File 95="instr.lib/Levylab/xeryon-rotator/drivers/Class/Axis/ReceiveData.vi"
File 96="instr.lib/Levylab/xeryon-rotator/drivers/Class/Axis/setData.vi"
File 97="instr.lib/Levylab/xeryon-rotator/drivers/Class/Axis/TEMPORARY getReceivedString.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_Xeryon_Rotator.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
