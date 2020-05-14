[Package]
Name="levylab_lib_embedded_smo_ui"
Version="1.0.0.12"
Release=""
ID=93866fef64fcb1a6f405bf6b2515b9b8
File Format="vip"
Format Version="2017"
Display Name="SMO.UI.Embedded"


[Description]
Description=""
Summary="A remake of the embedded example from JKI, using by value SMOs."
License="BSD-3"
Copyright="Copyright (c) 2020, Levylab"
Distribution=""
Vendor="Levylab"
URL="https://github.com/levylabpitt/Embedded-SMO"
Packager="Joseph Albro"
Demo="FALSE"
Release Notes="Changed Class Name"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


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
Requires="jki_smo_templates>=1.4.0.15,jki_statemachineobjects>=1.3.0.56"
Conflicts=""


[Activation]
License File=""
Licensed Library=""


[Files]
Num File Groups="14"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=45
File 0="vi.lib/Levylab/SMO.UI.Embedded/CreatePublicEvents.vi"
File 1="vi.lib/Levylab/SMO.UI.Embedded/DestroyPublicEvents.vi"
File 2="vi.lib/Levylab/SMO.UI.Embedded/EmbeddedSMO.lvproj"
File 3="vi.lib/Levylab/SMO.UI.Embedded/Process.vi"
File 4="vi.lib/Levylab/SMO.UI.Embedded/SMO.UI.Embedded.GetPublicEvents.vi"
File 5="vi.lib/Levylab/SMO.UI.Embedded/SMO.UI.Embedded.lvclass"
File 6="vi.lib/Levylab/SMO.UI.Embedded/SMO.UI.Embedded.ReadyForInfo.vi"
File 7="vi.lib/Levylab/SMO.UI.Embedded/SMO.UI.Embedded.TestLauncher.vi"
File 8="vi.lib/Levylab/SMO.UI.Embedded/Typedefs/GetUIStateNotifier.ctl"
File 9="vi.lib/Levylab/SMO.UI.Embedded/Typedefs/PrivateEvents--Cluster.ctl"
File 10="vi.lib/Levylab/SMO.UI.Embedded/Typedefs/PrivateEvents--SMO.UI.Embedded.Get UI State.ctl"
File 11="vi.lib/Levylab/SMO.UI.Embedded/Typedefs/PrivateEvents--SMO.UI.Embedded.GetName.ctl"
File 12="vi.lib/Levylab/SMO.UI.Embedded/Typedefs/PrivateEvents--SMO.UI.Embedded.GetSubPanelReference.ctl"
File 13="vi.lib/Levylab/SMO.UI.Embedded/Typedefs/PrivateEvents--SMO.UI.Embedded.SetSubpanelReference.ctl"
File 14="vi.lib/Levylab/SMO.UI.Embedded/Typedefs/PrivateEvents--SMO.UI.Embedded.SetUIState.ctl"
File 15="vi.lib/Levylab/SMO.UI.Embedded/Typedefs/PrivateEvents--SMO.UI.Embedded.WriteName.ctl"
File 16="vi.lib/Levylab/SMO.UI.Embedded/Typedefs/PublicEvents--Cluster.ctl"
File 17="vi.lib/Levylab/SMO.UI.Embedded/Typedefs/PublicEvents--SMO.UI.Embedded.ReadyForInfo.ctl"
File 18="vi.lib/Levylab/SMO.UI.Embedded/Typedefs/UI State.ctl"
File 19="vi.lib/Levylab/SMO.UI.Embedded/Private/SMO.UI.Embedded.GetName.vi"
File 20="vi.lib/Levylab/SMO.UI.Embedded/Private/SMO.UI.Embedded.GetPrivateEvents.vi"
File 21="vi.lib/Levylab/SMO.UI.Embedded/Private/SMO.UI.Embedded.GetSubPanelReference.vi"
File 22="vi.lib/Levylab/SMO.UI.Embedded/Private/SMO.UI.Embedded.GetUIState.vi"
File 23="vi.lib/Levylab/SMO.UI.Embedded/Private/SMO.UI.Embedded.SetSubpanelReference.vi"
File 24="vi.lib/Levylab/SMO.UI.Embedded/Private/SMO.UI.Embedded.SetUIState.vi"
File 25="vi.lib/Levylab/SMO.UI.Embedded/Private/SMO.UI.Embedded.WriteName.vi"
File 26="vi.lib/Levylab/SMO.UI.Embedded/Overrides/Get VI Reference.vi"
File 27="vi.lib/Levylab/SMO.UI.Embedded/Methods (Overrides)/CreatePrivateEvents.vi"
File 28="vi.lib/Levylab/SMO.UI.Embedded/Methods (Overrides)/DestroyPrivateEvents.vi"
File 29="vi.lib/Levylab/SMO.UI.Embedded/Methods/DeferPanelUpdate.vi"
File 30="vi.lib/Levylab/SMO.UI.Embedded/Methods/Embed_Hide.vi"
File 31="vi.lib/Levylab/SMO.UI.Embedded/Methods/Embed_Show.vi"
File 32="vi.lib/Levylab/SMO.UI.Embedded/Methods/Accessors/Read Name.vi"
File 33="vi.lib/Levylab/SMO.UI.Embedded/Methods/Accessors/Read SubPanelReference.vi"
File 34="vi.lib/Levylab/SMO.UI.Embedded/Methods/Accessors/Read UI State.vi"
File 35="vi.lib/Levylab/SMO.UI.Embedded/Methods/Accessors/Write Name.vi"
File 36="vi.lib/Levylab/SMO.UI.Embedded/Methods/Accessors/Write SubPanelReference.vi"
File 37="vi.lib/Levylab/SMO.UI.Embedded/Methods/Accessors/Write UI State.vi"
File 38="vi.lib/Levylab/SMO.UI.Embedded/DataAccessors/GetProcessReference.vi"
File 39="vi.lib/Levylab/SMO.UI.Embedded/API/GetEmbeddedName.vi"
File 40="vi.lib/Levylab/SMO.UI.Embedded/API/GetSubPanelRef.vi"
File 41="vi.lib/Levylab/SMO.UI.Embedded/API/GetUIState.vi"
File 42="vi.lib/Levylab/SMO.UI.Embedded/API/SetEmbeddedName.vi"
File 43="vi.lib/Levylab/SMO.UI.Embedded/API/SetSubPanelRef.vi"
File 44="vi.lib/Levylab/SMO.UI.Embedded/API/SetUIState.vi"


[File Group 1]
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


[File Group 2]
Target Dir="<menus>/Controls"
Replace Mode="Always"
Num Files=2
File 0="_controls_levylab_lib_embedded_smo_ui_1.mnu"
File 1="controls_Levylab_lib_Embedded_SMO_UI.mnu"


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
Num Files=1
File 0="functions_Levylab_lib_Embedded_SMO_UI.mnu"


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
Num Files=8
File 0="_functions_levylab_lib_embedded_smo_ui_1.mnu"
File 1="_functions_levylab_lib_embedded_smo_ui_2.mnu"
File 2="_functions_levylab_lib_embedded_smo_ui_3.mnu"
File 3="_functions_levylab_lib_embedded_smo_ui_4.mnu"
File 4="_functions_levylab_lib_embedded_smo_ui_5.mnu"
File 5="_functions_levylab_lib_embedded_smo_ui_6.mnu"
File 6="_functions_levylab_lib_embedded_smo_ui_7.mnu"
File 7="functions_Levylab_lib_Embedded_SMO_UI.mnu"


[File Group 10]
Target Dir="<menus>/Controls"
Replace Mode="Always"
Num Files=2
File 0="_controls_levylab_lib_embedded_smo_ui_1.mnu"
File 1="controls_Levylab_lib_Embedded_SMO_UI.mnu"


[File Group 11]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=2
File 0="_functions_levylab_lib_embedded_smo_ui_1.mnu"
File 1="functions_Levylab_lib_Embedded_SMO_UI.mnu"


[File Group 12]
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


[File Group 13]
Target Dir="<menus>/Controls"
Replace Mode="Always"
Num Files=2
File 0="_controls_levylab_lib_embedded_smo_ui_1.mnu"
File 1="controls_Levylab_lib_Embedded_SMO_UI.mnu"
