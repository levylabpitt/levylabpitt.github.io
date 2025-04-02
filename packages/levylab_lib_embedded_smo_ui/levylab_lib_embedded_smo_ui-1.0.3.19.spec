[Package]
Name="levylab_lib_embedded_smo_ui"
Version="1.0.3.19"
Release=""
ID=cd6abb5a1482dbfc7dbea73229225fc7
File Format="vip"
Format Version="2017"
Display Name="Embedded UI"


[Description]
Description="A remake of the JKI Embedded UI example using by-value SMOs."
Summary="A remake of the embedded example from JKI using by value SMOs."
License="BSD-3"
Copyright="Copyright (c) 2021, LevyLab"
Distribution=""
Vendor="LevyLab"
URL="https://github.com/levylabpitt/Embedded-SMO"
Packager="Joe Albro"
Demo="FALSE"
Release Notes="- Update class names"
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
Requires="jki_statemachineobjects>=1.4.0.63,oglib_appcontrol>=4.1.0.7,jki_lib_smo_editor>=2.0.2.5,jki_smo_templates>=1.4.0.15"
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
Num Files=49
File 0="user.lib/Levylab/Embedded UI/Embedded UI/Embedded UI.lvclass"
File 1="user.lib/Levylab/Embedded UI/Embedded UI/Embedded UI.TestLauncher.vi"
File 2="user.lib/Levylab/Embedded UI/Embedded UI/Process.vi"
File 3="user.lib/Levylab/Embedded UI/Embedded UI/Typedefs/GetUIStateNotifier.ctl"
File 4="user.lib/Levylab/Embedded UI/Embedded UI/Typedefs/PrivateEvents--Cluster.ctl"
File 5="user.lib/Levylab/Embedded UI/Embedded UI/Typedefs/PrivateEvents--Embedded UI.Get UI State.ctl"
File 6="user.lib/Levylab/Embedded UI/Embedded UI/Typedefs/PrivateEvents--Embedded UI.GetName.ctl"
File 7="user.lib/Levylab/Embedded UI/Embedded UI/Typedefs/PrivateEvents--Embedded UI.GetSubPanelReference.ctl"
File 8="user.lib/Levylab/Embedded UI/Embedded UI/Typedefs/PrivateEvents--Embedded UI.SetSubpanelReference.ctl"
File 9="user.lib/Levylab/Embedded UI/Embedded UI/Typedefs/PrivateEvents--Embedded UI.SetUIState.ctl"
File 10="user.lib/Levylab/Embedded UI/Embedded UI/Typedefs/PrivateEvents--Embedded UI.WriteName.ctl"
File 11="user.lib/Levylab/Embedded UI/Embedded UI/Typedefs/PublicEvents--Cluster.ctl"
File 12="user.lib/Levylab/Embedded UI/Embedded UI/Typedefs/PublicEvents--Embedded UI.ReadyForInfo.ctl"
File 13="user.lib/Levylab/Embedded UI/Embedded UI/Typedefs/PublicEvents--Embedded UI.UIState.ctl"
File 14="user.lib/Levylab/Embedded UI/Embedded UI/Typedefs/UI State.ctl"
File 15="user.lib/Levylab/Embedded UI/Embedded UI/Private/Embedded UI.GetName.vi"
File 16="user.lib/Levylab/Embedded UI/Embedded UI/Private/Embedded UI.GetPrivateEvents.vi"
File 17="user.lib/Levylab/Embedded UI/Embedded UI/Private/Embedded UI.GetSubPanelReference.vi"
File 18="user.lib/Levylab/Embedded UI/Embedded UI/Private/Embedded UI.GetUIState.vi"
File 19="user.lib/Levylab/Embedded UI/Embedded UI/Private/Embedded UI.ReadyForInfo.vi"
File 20="user.lib/Levylab/Embedded UI/Embedded UI/Private/Embedded UI.SetSubpanelReference.vi"
File 21="user.lib/Levylab/Embedded UI/Embedded UI/Private/Embedded UI.SetUIState.vi"
File 22="user.lib/Levylab/Embedded UI/Embedded UI/Private/Embedded UI.UIState.vi"
File 23="user.lib/Levylab/Embedded UI/Embedded UI/Private/Embedded UI.WriteName.vi"
File 24="user.lib/Levylab/Embedded UI/Embedded UI/Overrides/Get VI Reference.vi"
File 25="user.lib/Levylab/Embedded UI/Embedded UI/Methods (Overrides)/CreatePrivateEvents.vi"
File 26="user.lib/Levylab/Embedded UI/Embedded UI/Methods (Overrides)/CreatePublicEvents.vi"
File 27="user.lib/Levylab/Embedded UI/Embedded UI/Methods (Overrides)/DestroyPrivateEvents.vi"
File 28="user.lib/Levylab/Embedded UI/Embedded UI/Methods (Overrides)/DestroyPublicEvents.vi"
File 29="user.lib/Levylab/Embedded UI/Embedded UI/Methods/DeferPanelUpdate.vi"
File 30="user.lib/Levylab/Embedded UI/Embedded UI/Methods/Embed_Hide.vi"
File 31="user.lib/Levylab/Embedded UI/Embedded UI/Methods/Embed_Show.vi"
File 32="user.lib/Levylab/Embedded UI/Embedded UI/Methods/Accessors/Read Name.vi"
File 33="user.lib/Levylab/Embedded UI/Embedded UI/Methods/Accessors/Read SubPanelReference.vi"
File 34="user.lib/Levylab/Embedded UI/Embedded UI/Methods/Accessors/Read UI State.vi"
File 35="user.lib/Levylab/Embedded UI/Embedded UI/Methods/Accessors/Write Name.vi"
File 36="user.lib/Levylab/Embedded UI/Embedded UI/Methods/Accessors/Write SubPanelReference.vi"
File 37="user.lib/Levylab/Embedded UI/Embedded UI/Methods/Accessors/Write UI State.vi"
File 38="user.lib/Levylab/Embedded UI/Embedded UI/DataAccessors/GetProcessReference.vi"
File 39="user.lib/Levylab/Embedded UI/Embedded UI/API/Embedded UI.GetPublicEvents.vi"
File 40="user.lib/Levylab/Embedded UI/Embedded UI/API/GetEmbeddedName.vi"
File 41="user.lib/Levylab/Embedded UI/Embedded UI/API/GetSubPanelRef.vi"
File 42="user.lib/Levylab/Embedded UI/Embedded UI/API/GetUIState.vi"
File 43="user.lib/Levylab/Embedded UI/Embedded UI/API/SetEmbeddedName.vi"
File 44="user.lib/Levylab/Embedded UI/Embedded UI/API/SetSubPanelRef.vi"
File 45="user.lib/Levylab/Embedded UI/Embedded UI/API/SetUIState.vi"
File 46="templates/JKI/JKI SMO/Embedded UI/Embedded UI.BasicTemplate/Embedded UI.BasicTemplate.lvclass"
File 47="templates/JKI/JKI SMO/Embedded UI/Embedded UI.BasicTemplate/Embedded UI.BasicTemplate.TestLauncher.vi"
File 48="templates/JKI/JKI SMO/Embedded UI/Embedded UI.BasicTemplate/Process.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=10
File 0="_functions_levylab_lib_embedded_smo_ui_1.mnu"
File 1="_functions_levylab_lib_embedded_smo_ui_2.mnu"
File 2="_functions_levylab_lib_embedded_smo_ui_3.mnu"
File 3="_functions_levylab_lib_embedded_smo_ui_4.mnu"
File 4="_functions_levylab_lib_embedded_smo_ui_5.mnu"
File 5="_functions_levylab_lib_embedded_smo_ui_6.mnu"
File 6="_functions_levylab_lib_embedded_smo_ui_7.mnu"
File 7="_functions_levylab_lib_embedded_smo_ui_8.mnu"
File 8="_functions_levylab_lib_embedded_smo_ui_9.mnu"
File 9="functions_Levylab_lib_Embedded_SMO_UI.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
