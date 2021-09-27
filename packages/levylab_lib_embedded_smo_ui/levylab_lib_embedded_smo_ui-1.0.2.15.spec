[Package]
Name="levylab_lib_embedded_smo_ui"
Version="1.0.2.15"
Release=""
ID=ae7c9e85fd4f69c5644e142393d2ed30
File Format="vip"
Format Version="2017"
Display Name="SMO.UI.Embedded"


[Description]
Description="A remake of the embedded example from JKI, using by value SMOs."
Summary="A remake of the embedded example from JKI, using by value SMOs."
License="BSD-3"
Copyright="Copyright (c) 2021, Levylab"
Distribution=""
Vendor="Levylab"
URL="https://github.com/levylabpitt/Embedded-SMO"
Packager="Joe Albro"
Demo="FALSE"
Release Notes="- Change install location (vilib --> userlib)\0A- Include Embedded UI Template"
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
Requires="jki_statemachineobjects>=1.4.0.63,jki_smo_templates>=1.4.0.15"
Conflicts=""


[Activation]
License File=""
Licensed Library=""


[Files]
Num File Groups="12"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=50
File 0="user.lib/Levylab/Embedded UI/EmbeddedSMO.lvproj"
File 1="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Process.vi"
File 2="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/SMO.UI.Embedded.lvclass"
File 3="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/SMO.UI.Embedded.TestLauncher.vi"
File 4="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Typedefs/GetUIStateNotifier.ctl"
File 5="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Typedefs/PrivateEvents--Cluster.ctl"
File 6="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Typedefs/PrivateEvents--SMO.UI.Embedded.Get UI State.ctl"
File 7="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Typedefs/PrivateEvents--SMO.UI.Embedded.GetName.ctl"
File 8="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Typedefs/PrivateEvents--SMO.UI.Embedded.GetSubPanelReference.ctl"
File 9="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Typedefs/PrivateEvents--SMO.UI.Embedded.SetSubpanelReference.ctl"
File 10="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Typedefs/PrivateEvents--SMO.UI.Embedded.SetUIState.ctl"
File 11="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Typedefs/PrivateEvents--SMO.UI.Embedded.WriteName.ctl"
File 12="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Typedefs/PublicEvents--Cluster.ctl"
File 13="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Typedefs/PublicEvents--SMO.UI.Embedded.ReadyForInfo.ctl"
File 14="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Typedefs/PublicEvents--SMO.UI.Embedded.UIState.ctl"
File 15="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Typedefs/UI State.ctl"
File 16="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Private/SMO.UI.Embedded.GetName.vi"
File 17="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Private/SMO.UI.Embedded.GetPrivateEvents.vi"
File 18="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Private/SMO.UI.Embedded.GetSubPanelReference.vi"
File 19="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Private/SMO.UI.Embedded.GetUIState.vi"
File 20="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Private/SMO.UI.Embedded.ReadyForInfo.vi"
File 21="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Private/SMO.UI.Embedded.SetSubpanelReference.vi"
File 22="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Private/SMO.UI.Embedded.SetUIState.vi"
File 23="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Private/SMO.UI.Embedded.UIState.vi"
File 24="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Private/SMO.UI.Embedded.WriteName.vi"
File 25="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Overrides/Get VI Reference.vi"
File 26="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Methods (Overrides)/CreatePrivateEvents.vi"
File 27="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Methods (Overrides)/CreatePublicEvents.vi"
File 28="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Methods (Overrides)/DestroyPrivateEvents.vi"
File 29="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Methods (Overrides)/DestroyPublicEvents.vi"
File 30="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Methods/DeferPanelUpdate.vi"
File 31="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Methods/Embed_Hide.vi"
File 32="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Methods/Embed_Show.vi"
File 33="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Methods/Accessors/Read Name.vi"
File 34="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Methods/Accessors/Read SubPanelReference.vi"
File 35="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Methods/Accessors/Read UI State.vi"
File 36="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Methods/Accessors/Write Name.vi"
File 37="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Methods/Accessors/Write SubPanelReference.vi"
File 38="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/Methods/Accessors/Write UI State.vi"
File 39="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/DataAccessors/GetProcessReference.vi"
File 40="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/API/GetEmbeddedName.vi"
File 41="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/API/GetSubPanelRef.vi"
File 42="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/API/GetUIState.vi"
File 43="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/API/SetEmbeddedName.vi"
File 44="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/API/SetSubPanelRef.vi"
File 45="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/API/SetUIState.vi"
File 46="user.lib/Levylab/Embedded UI/SMO.UI.Embedded/API/SMO.UI.Embedded.GetPublicEvents.vi"
File 47="templates/JKI/JKI SMO/Embedded UI/SMO.UI.Embedded.Template/Process.vi"
File 48="templates/JKI/JKI SMO/Embedded UI/SMO.UI.Embedded.Template/SMO.UI.Embedded.Basic.lvclass"
File 49="templates/JKI/JKI SMO/Embedded UI/SMO.UI.Embedded.Template/SMO.UI.Embedded.Basic.TestLauncher.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_Embedded_SMO_UI.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"


[File Group 3]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_Embedded_SMO_UI.mnu"


[File Group 4]
Target Dir="<menus>/Controls"
Replace Mode="Always"
Num Files=2
File 0="_controls_levylab_lib_embedded_smo_ui_1.mnu"
File 1="controls_Levylab_lib_Embedded_SMO_UI.mnu"


[File Group 5]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=8
File 0="_functions_levylab_lib_embedded_smo_ui_1.mnu"
File 1="_functions_levylab_lib_embedded_smo_ui_2.mnu"
File 2="_functions_levylab_lib_embedded_smo_ui_3.mnu"
File 3="_functions_levylab_lib_embedded_smo_ui_4.mnu"
File 4="_functions_levylab_lib_embedded_smo_ui_5.mnu"
File 5="_functions_levylab_lib_embedded_smo_ui_6.mnu"
File 6="_functions_levylab_lib_embedded_smo_ui_7.mnu"
File 7="functions_Levylab_lib_Embedded_SMO_UI.mnu"


[File Group 6]
Target Dir="<menus>/Controls"
Replace Mode="Always"
Num Files=2
File 0="_controls_levylab_lib_embedded_smo_ui_1.mnu"
File 1="controls_Levylab_lib_Embedded_SMO_UI.mnu"


[File Group 7]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=8
File 0="_functions_levylab_lib_embedded_smo_ui_1.mnu"
File 1="_functions_levylab_lib_embedded_smo_ui_2.mnu"
File 2="_functions_levylab_lib_embedded_smo_ui_3.mnu"
File 3="_functions_levylab_lib_embedded_smo_ui_4.mnu"
File 4="_functions_levylab_lib_embedded_smo_ui_5.mnu"
File 5="_functions_levylab_lib_embedded_smo_ui_6.mnu"
File 6="_functions_levylab_lib_embedded_smo_ui_7.mnu"
File 7="functions_Levylab_lib_Embedded_SMO_UI.mnu"


[File Group 8]
Target Dir="<menus>/Controls"
Replace Mode="Always"
Num Files=2
File 0="_controls_levylab_lib_embedded_smo_ui_1.mnu"
File 1="controls_Levylab_lib_Embedded_SMO_UI.mnu"


[File Group 9]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=2
File 0="_functions_levylab_lib_embedded_smo_ui_1.mnu"
File 1="functions_Levylab_lib_Embedded_SMO_UI.mnu"


[File Group 10]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=8
File 0="_functions_levylab_lib_embedded_smo_ui_1.mnu"
File 1="_functions_levylab_lib_embedded_smo_ui_2.mnu"
File 2="_functions_levylab_lib_embedded_smo_ui_3.mnu"
File 3="_functions_levylab_lib_embedded_smo_ui_4.mnu"
File 4="_functions_levylab_lib_embedded_smo_ui_5.mnu"
File 5="_functions_levylab_lib_embedded_smo_ui_6.mnu"
File 6="_functions_levylab_lib_embedded_smo_ui_7.mnu"
File 7="functions_Levylab_lib_Embedded_SMO_UI.mnu"


[File Group 11]
Target Dir="<menus>/Controls"
Replace Mode="Always"
Num Files=2
File 0="_controls_levylab_lib_embedded_smo_ui_1.mnu"
File 1="controls_Levylab_lib_Embedded_SMO_UI.mnu"
