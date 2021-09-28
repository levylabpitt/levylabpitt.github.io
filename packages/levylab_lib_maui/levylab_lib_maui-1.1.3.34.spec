[Package]
Name="levylab_lib_maui"
Version="1.1.3.34"
Release=""
ID=c3a3259c9d728e5f7127df637be5129f
File Format="vip"
Format Version="2017"
Display Name="MAUI"


[Description]
Description="Working Engine for MAUI (Modular Albro UI) Framework."
Summary="Working Engine for MAUI Framework."
License="BSD-3"
Copyright="Copyright (c) 2021, Levylab"
Distribution=""
Vendor="Levylab"
URL="https://github.com/levylabpitt/Embedded-Main-SMO"
Packager="Joe Albro"
Demo="FALSE"
Release Notes="- Improve weakness in default subpanel path"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


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
Requires="jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.4.0.63,oglib_error>=4.2.0.23,oglib_lvdata>=5.0.0.27,oglib_variantconfig>=4.0.0.5,levylab_lib_embedded_smo_ui>=1.0.3.19"
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
Num Files=103
File 0="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/MAUI.lvclass"
File 1="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/MAUI.TestLauncher.vi"
File 2="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Process.vi"
File 3="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Typedefs/DefaultConfiguration.ctl"
File 4="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Typedefs/DefaultSubpanel.ctl"
File 5="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Typedefs/EmbeddedNotifier.ctl"
File 6="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Typedefs/PanelData.ctl"
File 7="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Typedefs/PanelDataNotifier.ctl"
File 8="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Typedefs/PrivateEvents--Cluster.ctl"
File 9="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Typedefs/PrivateEvents--MAUI.GetDefaultSubpanel.ctl"
File 10="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Typedefs/PrivateEvents--MAUI.GetEmbedded.ctl"
File 11="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Typedefs/PrivateEvents--MAUI.GetPanelData.ctl"
File 12="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Typedefs/PrivateEvents--MAUI.OpenSubpanel.ctl"
File 13="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Typedefs/PrivateEvents--MAUI.SetDefaultSubpanel.ctl"
File 14="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Typedefs/PrivateEvents--MAUI.SetEmbedded.ctl"
File 15="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Typedefs/PrivateEvents--MAUI.SetPanelData.ctl"
File 16="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Typedefs/PrivateEvents--MAUI.UpdatePanel.ctl"
File 17="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Typedefs/PublicEvents--Cluster.ctl"
File 18="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Typedefs/PublicEvents--MAUI.ReadyForInfo .ctl"
File 19="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Typedefs/SpecificConfiguration.ctl"
File 20="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Resource/default.json"
File 21="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Private/MAUI.GetDefaultSubpanel.vi"
File 22="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Private/MAUI.GetEmbedded.vi"
File 23="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Private/MAUI.GetPanelData.vi"
File 24="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Private/MAUI.GetPrivateEvents.vi"
File 25="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Private/MAUI.OpenSubpanel.vi"
File 26="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Private/MAUI.ReadyForInfo.vi"
File 27="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Private/MAUI.SetDefaultSubpanel.vi"
File 28="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Private/MAUI.SetEmbedded.vi"
File 29="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Private/MAUI.SetPanelData.vi"
File 30="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Overrides)/CreatePrivateEvents.vi"
File 31="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Overrides)/CreatePublicEvents.vi"
File 32="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Overrides)/DestroyPrivateEvents.vi"
File 33="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Overrides)/DestroyPublicEvents.vi"
File 34="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Overrides)/onProcessStarted.vi"
File 35="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Overrides)/onStart.vi"
File 36="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Overrides)/onStop.vi"
File 37="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/ChangePanel.vi"
File 38="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/CheckIfComposition.vi"
File 39="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/CheckInheritance.vi"
File 40="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/CheckInOpened.vi"
File 41="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/CheckSubpanelDirectory.vi"
File 42="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/DefaultConfigurationLocation.vi"
File 43="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/DetermineCompositionInput.vi"
File 44="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/FindEmptySubpanel.vi"
File 45="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/FindIfActive.vi"
File 46="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/GenerateDefaultSubpanels.vi"
File 47="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/GetAllUIStateChange.vi"
File 48="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/GetCurrentViews.vi"
File 49="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/GetDefaultSubpanelDirectory.vi"
File 50="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/GetFrameworkConfigPath.vi"
File 51="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/GetFrameworkDefaultSubpanelPath.vi"
File 52="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/GetSubpanelPathsFromConfiguration.vi"
File 53="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/GreyRings.vi"
File 54="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/HandleStateChange.vi"
File 55="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/LocateConfigFile.vi"
File 56="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/MatchEmbedByGUID.vi"
File 57="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/OpenSubpanelHandler.vi"
File 58="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/PopulateRings.vi"
File 59="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/ReadDefaultConfigurationFile.vi"
File 60="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/ReadForceSubpanelDir.vi"
File 61="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/ReadSpecificConfigurationFile.vi"
File 62="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/SearchForSubpanelsInDefault.vi"
File 63="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/Methods (Framework)/WriteForceSubpanelDir.vi"
File 64="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/API 2.0/FindSubpanels.Config.vi"
File 65="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/API 2.0/FindSubpanels.PathArray.vi"
File 66="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/API 2.0/FindSubpanels.SMOArray.vi"
File 67="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/API/ArrangeFrontPanel.vi"
File 68="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/API/MAUI.GetPublicEvents.vi"
File 69="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/API/MAUI.UpdatePanel.vi"
File 70="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/API/OpenSubpanel.vi"
File 71="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/API/Accessors/ReadDefaultSubpanel.vi"
File 72="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/API/Accessors/ReadEmbedded.vi"
File 73="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/API/Accessors/ReadPanelData.vi"
File 74="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/API/Accessors/WriteDefaultSubpanel.vi"
File 75="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/API/Accessors/WriteEmbedded.vi"
File 76="user.lib/Levylab/MAUI/Maui 1.0/SMO.UI.MAUI/API/Accessors/WritePanelData.vi"
File 77="user.lib/Levylab/MAUI/Maui 1.0/Maui.Config/Maui.Config.lvclass"
File 78="user.lib/Levylab/MAUI/Maui 1.0/Maui.Config/Private/Maui.Config.GenerateFrameworkPath.vi"
File 79="user.lib/Levylab/MAUI/Maui 1.0/Maui.Config/API/Maui.Config.Create.vi"
File 80="user.lib/Levylab/MAUI/Maui 1.0/Maui.Config/API/Maui.Config.Locate.vi"
File 81="user.lib/Levylab/MAUI/Maui 1.0/Maui.Config/API/Maui.Config.Read.vi"
File 82="user.lib/Levylab/MAUI/Maui 1.0/Maui.Config/API/Maui.Config.ReadFramework.vi"
File 83="user.lib/Levylab/MAUI/Maui 1.0/Maui.Config/Accessors/Maui.Config.ReadApplicationName.vi"
File 84="user.lib/Levylab/MAUI/Maui 1.0/Maui.Config/Accessors/Maui.Config.ReadFrameworkConfigPath.vi"
File 85="user.lib/Levylab/MAUI/Maui 1.0/Maui.Config/Accessors/Maui.Config.ReadFrameworkPath.vi"
File 86="user.lib/Levylab/MAUI/Maui 1.0/Maui.Config/Accessors/Maui.Config.ReadIsComposition.vi"
File 87="user.lib/Levylab/MAUI/Maui 1.0/Maui.Config/Accessors/Maui.Config.ReadOwningClass.vi"
File 88="user.lib/Levylab/MAUI/Maui 1.0/Maui.Config/Accessors/Maui.Config.ReadSpecificConfigPath.vi"
File 89="user.lib/Levylab/MAUI/Maui 1.0/Maui.Config/Accessors/Maui.Config.ReadSubpanelPaths.vi"
File 90="user.lib/Levylab/MAUI/Maui 1.0/Maui.Config/Accessors/Maui.Config.WriteApplicationName.vi"
File 91="user.lib/Levylab/MAUI/Maui 1.0/Maui.Config/Accessors/Maui.Config.WriteFrameworkConfigPath.vi"
File 92="user.lib/Levylab/MAUI/Maui 1.0/Maui.Config/Accessors/Maui.Config.WriteFrameworkPath.vi"
File 93="user.lib/Levylab/MAUI/Maui 1.0/Maui.Config/Accessors/Maui.Config.WriteIsComposition.vi"
File 94="user.lib/Levylab/MAUI/Maui 1.0/Maui.Config/Accessors/Maui.Config.WriteOwningClass.vi"
File 95="user.lib/Levylab/MAUI/Maui 1.0/Maui.Config/Accessors/Maui.Config.WriteSpecificConfigPath.vi"
File 96="user.lib/Levylab/MAUI/Maui 1.0/Maui.Config/Accessors/Maui.Config.WriteSubpanelPaths.vi"
File 97="templates/JKI/JKI SMO/MAUI/Templates/MAUI.SubPanel/MAUI.SubPanel.lvclass"
File 98="templates/JKI/JKI SMO/MAUI/Templates/MAUI.SubPanel/MAUI.SubPanel.TestLauncher.vi"
File 99="templates/JKI/JKI SMO/MAUI/Templates/MAUI.SubPanel/Process.vi"
File 100="templates/JKI/JKI SMO/MAUI/Templates/MAUI.Basic/MAUI.Basic.lvclass"
File 101="templates/JKI/JKI SMO/MAUI/Templates/MAUI.Basic/MAUI.Basic.TestLauncher.vi"
File 102="templates/JKI/JKI SMO/MAUI/Templates/MAUI.Basic/Process.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=15
File 0="_functions_levylab_lib_maui_1.mnu"
File 1="_functions_levylab_lib_maui_10.mnu"
File 2="_functions_levylab_lib_maui_11.mnu"
File 3="_functions_levylab_lib_maui_12.mnu"
File 4="_functions_levylab_lib_maui_13.mnu"
File 5="_functions_levylab_lib_maui_14.mnu"
File 6="_functions_levylab_lib_maui_2.mnu"
File 7="_functions_levylab_lib_maui_3.mnu"
File 8="_functions_levylab_lib_maui_4.mnu"
File 9="_functions_levylab_lib_maui_5.mnu"
File 10="_functions_levylab_lib_maui_6.mnu"
File 11="_functions_levylab_lib_maui_7.mnu"
File 12="_functions_levylab_lib_maui_8.mnu"
File 13="_functions_levylab_lib_maui_9.mnu"
File 14="functions_Levylab_lib_MAUI.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"