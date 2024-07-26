[Package]
Name="levylab_lib_xeryon_rotator"
Version="1.0.3.6"
Release=""
ID=827b371c0321df5ce4430d0e09dcec22
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
Release Notes="Issue #3\0A- fix shortcut name\0A- change installation directory for configuration settins to %ProgramData%/Xeryon/Settings\0A- change SettingsFileDialog to begin search in above directory"
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
Num Files=97
File 0="user.lib/Levylab/xeryon-rotator/Xeryon-Rotator.lvproj"
File 1="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Documentation.vi"
File 2="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Inst.Xeryon-Rotator.AppLauncher.vi"
File 3="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Inst.Xeryon-Rotator.lvclass"
File 4="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Process.vi"
File 5="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Typedefs/Inst.Xeryon-Rotator.Commands--Enum.ctl"
File 6="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Typedefs/Inst.Xeryon-Rotator.Configuration--Cluster.ctl"
File 7="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Typedefs/Inst.Xeryon-Rotator.getAll--Cluster.ctl"
File 8="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Typedefs/Inst.Xeryon-Rotator.getAngle--Cluster.ctl"
File 9="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Typedefs/Inst.Xeryon-Rotator.ScanState--Enum.ctl"
File 10="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Typedefs/Inst.Xeryon-Rotator.setAngle--Cluster.ctl"
File 11="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Typedefs/PrivateEvents--Cluster.ctl"
File 12="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Typedefs/PrivateEvents--Inst.Xeryon-Rotator.MessageToProcess.ctl"
File 13="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Typedefs/PublicEvents--Cluster.ctl"
File 14="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Typedefs/PublicEvents--Inst.Xeryon-Rotator.MessageFromProcess.ctl"
File 15="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/test/Test Xeryon API.vi"
File 16="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Private/Inst.Xeryon-Rotator.DoSomething.vi"
File 17="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Private/Inst.Xeryon-Rotator.Get Angle.vi"
File 18="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Private/Inst.Xeryon-Rotator.GetAllData.vi"
File 19="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Private/Inst.Xeryon-Rotator.GetPrivateEvents.vi"
File 20="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Private/Inst.Xeryon-Rotator.Set Angle.vi"
File 21="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Private/Inst.Xeryon-Rotator.Set Speed.vi"
File 22="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Private/Inst.Xeryon-Rotator.Set State.vi"
File 23="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Private/Inst.Xeryon-Rotator.Stop.vi"
File 24="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Close Hardware.vi"
File 25="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Configuration Window.vi"
File 26="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/CreatePrivateEvents.vi"
File 27="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/CreatePublicEvents.vi"
File 28="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/DestroyPrivateEvents.vi"
File 29="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/DestroyPublicEvents.vi"
File 30="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Get SMO Address.vi"
File 31="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Get SMO Name.vi"
File 32="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Get SMO PGSQL Log Paths.vi"
File 33="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Get SMO Port.vi"
File 34="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Get SMO Public API.vi"
File 35="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Get SMO RC Type.vi"
File 36="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Handle Command.vi"
File 37="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Handle getAll.vi"
File 38="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Handle setConfiguration.vi"
File 39="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Open Hardware.vi"
File 40="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Read Configuration File.vi"
File 41="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/Overrides/Write Configuration File.vi"
File 42="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/API/Close.vi"
File 43="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/API/Do Something.vi"
File 44="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/API/Get Angle.vi"
File 45="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/API/Inst.Xeryon-Rotator.GetPublicEvents.vi"
File 46="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/API/Inst.Xeryon-Rotator.MessageToProcess.vi"
File 47="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/API/Open.vi"
File 48="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/API/Set Angle.vi"
File 49="user.lib/Levylab/xeryon-rotator/SMOs/Inst.Xeryon-Rotator/API/Set Scan State.vi"
File 50="user.lib/Levylab/xeryon-rotator/SMOs/Inst UI.Xeryon-Rotator/Inst UI.Xeryon-Rotator.lvclass"
File 51="user.lib/Levylab/xeryon-rotator/SMOs/Inst UI.Xeryon-Rotator/Inst UI.Xeryon-Rotator.TestLauncher.vi"
File 52="user.lib/Levylab/xeryon-rotator/SMOs/Inst UI.Xeryon-Rotator/Inst UI.Xeryon-Rotator.UI--Cluster.ctl"
File 53="user.lib/Levylab/xeryon-rotator/SMOs/Inst UI.Xeryon-Rotator/Process.vi"
File 54="user.lib/Levylab/xeryon-rotator/drivers/Xeryon.lvproj"
File 55="user.lib/Levylab/xeryon-rotator/drivers/settings/settings_default_rotate.txt"
File 56="user.lib/Levylab/xeryon-rotator/drivers/settings/settings_default_two_stage_example.txt"
File 57="user.lib/Levylab/xeryon-rotator/drivers/settings/settings_default_xls_two_stage.txt"
File 58="user.lib/Levylab/xeryon-rotator/drivers/examples/Example One Stage.vi"
File 59="user.lib/Levylab/xeryon-rotator/drivers/examples/Example One Stage_Patrick.vi"
File 60="user.lib/Levylab/xeryon-rotator/drivers/examples/Example One Stage_Patrick_JKISM.vi"
File 61="user.lib/Levylab/xeryon-rotator/drivers/examples/Example Three Stage.vi"
File 62="user.lib/Levylab/xeryon-rotator/drivers/examples/Example Two Stages.vi"
File 63="user.lib/Levylab/xeryon-rotator/drivers/Class/Controller/AddAxis.vi"
File 64="user.lib/Levylab/xeryon-rotator/drivers/Class/Controller/Close.vi"
File 65="user.lib/Levylab/xeryon-rotator/drivers/Class/Controller/Controller.lvclass"
File 66="user.lib/Levylab/xeryon-rotator/drivers/Class/Controller/getAxisObject.vi"
File 67="user.lib/Levylab/xeryon-rotator/drivers/Class/Controller/getDataCluster.vi"
File 68="user.lib/Levylab/xeryon-rotator/drivers/Class/Controller/getDposInCurrentUnits.vi"
File 69="user.lib/Levylab/xeryon-rotator/drivers/Class/Controller/getEposInCurrentUnits.vi"
File 70="user.lib/Levylab/xeryon-rotator/drivers/Class/Controller/getStatusBits.vi"
File 71="user.lib/Levylab/xeryon-rotator/drivers/Class/Controller/initialize.vi"
File 72="user.lib/Levylab/xeryon-rotator/drivers/Class/Controller/readSettingsFile.vi"
File 73="user.lib/Levylab/xeryon-rotator/drivers/Class/Controller/receiveData.vi"
File 74="user.lib/Levylab/xeryon-rotator/drivers/Class/Controller/sendCommand.vi"
File 75="user.lib/Levylab/xeryon-rotator/drivers/Class/Controller/setDPOS.vi"
File 76="user.lib/Levylab/xeryon-rotator/drivers/Class/Controller/setSpeed.vi"
File 77="user.lib/Levylab/xeryon-rotator/drivers/Class/Controller/setStep.vi"
File 78="user.lib/Levylab/xeryon-rotator/drivers/Class/Controller/SettingsFileDialog.vi"
File 79="user.lib/Levylab/xeryon-rotator/drivers/Class/Communication/Close.vi"
File 80="user.lib/Levylab/xeryon-rotator/drivers/Class/Communication/Communication.lvclass"
File 81="user.lib/Levylab/xeryon-rotator/drivers/Class/Communication/Initialize.vi"
File 82="user.lib/Levylab/xeryon-rotator/drivers/Class/Communication/ReadData.vi"
File 83="user.lib/Levylab/xeryon-rotator/drivers/Class/Communication/WriteData.vi"
File 84="user.lib/Levylab/xeryon-rotator/drivers/Class/Axis/Axis.lvclass"
File 85="user.lib/Levylab/xeryon-rotator/drivers/Class/Axis/convertCurrentUnitsToEncoderUnits.vi"
File 86="user.lib/Levylab/xeryon-rotator/drivers/Class/Axis/convertEncoderUnitsToCurrentUnits.vi"
File 87="user.lib/Levylab/xeryon-rotator/drivers/Class/Axis/convertMilliMeterToEncoderUnits.vi"
File 88="user.lib/Levylab/xeryon-rotator/drivers/Class/Axis/getAxisLetter.vi"
File 89="user.lib/Levylab/xeryon-rotator/drivers/Class/Axis/getDataCluster.vi"
File 90="user.lib/Levylab/xeryon-rotator/drivers/Class/Axis/getDposInCurrentUnits.vi"
File 91="user.lib/Levylab/xeryon-rotator/drivers/Class/Axis/getEposInCurrentUnits.vi"
File 92="user.lib/Levylab/xeryon-rotator/drivers/Class/Axis/getStatusBits.vi"
File 93="user.lib/Levylab/xeryon-rotator/drivers/Class/Axis/Initialize.vi"
File 94="user.lib/Levylab/xeryon-rotator/drivers/Class/Axis/ReceiveData.vi"
File 95="user.lib/Levylab/xeryon-rotator/drivers/Class/Axis/setData.vi"
File 96="user.lib/Levylab/xeryon-rotator/drivers/Class/Axis/TEMPORARY getReceivedString.vi"


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
