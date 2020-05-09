[Package]
Name="levylab_lib_embedded_smo_ui"
Version="1.0.0.10"
Release=""
ID=2387098d48204b76ded978aee48a1a4c
File Format="vip"
Format Version="2017"
Display Name="Embedded SMO UI"


[Description]
Description=""
Summary="A remake of the embedded example from JKI, using by value SMOs."
License="BSD 3"
Copyright="Copyright (c) 2020, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Joseph Albro"
Demo="FALSE"
Release Notes="Fixed default naming functionality to remove ".lvclass""
System Package="FALSE"
Sub Package="FALSE"
License Agreement="FALSE"


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
Requires=""
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
Num Files=45
File 0="vi.lib/Levylab/Embedded SMO UI/CreatePublicEvents.vi"
File 1="vi.lib/Levylab/Embedded SMO UI/DestroyPublicEvents.vi"
File 2="vi.lib/Levylab/Embedded SMO UI/EmbeddedSMO.GetPublicEvents.vi"
File 3="vi.lib/Levylab/Embedded SMO UI/EmbeddedSMO.lvclass"
File 4="vi.lib/Levylab/Embedded SMO UI/EmbeddedSMO.lvproj"
File 5="vi.lib/Levylab/Embedded SMO UI/EmbeddedSMO.ReadyForInfo.vi"
File 6="vi.lib/Levylab/Embedded SMO UI/EmbeddedSMO.TestLauncher.vi"
File 7="vi.lib/Levylab/Embedded SMO UI/Process.vi"
File 8="vi.lib/Levylab/Embedded SMO UI/Typedefs/GetUIStateNotifier.ctl"
File 9="vi.lib/Levylab/Embedded SMO UI/Typedefs/PrivateEvents--Cluster.ctl"
File 10="vi.lib/Levylab/Embedded SMO UI/Typedefs/PrivateEvents--EmbeddedSMO.Get UI State.ctl"
File 11="vi.lib/Levylab/Embedded SMO UI/Typedefs/PrivateEvents--EmbeddedSMO.GetName.ctl"
File 12="vi.lib/Levylab/Embedded SMO UI/Typedefs/PrivateEvents--EmbeddedSMO.GetSubPanelReference.ctl"
File 13="vi.lib/Levylab/Embedded SMO UI/Typedefs/PrivateEvents--EmbeddedSMO.SetSubpanelReference.ctl"
File 14="vi.lib/Levylab/Embedded SMO UI/Typedefs/PrivateEvents--EmbeddedSMO.SetUIState.ctl"
File 15="vi.lib/Levylab/Embedded SMO UI/Typedefs/PrivateEvents--EmbeddedSMO.WriteName.ctl"
File 16="vi.lib/Levylab/Embedded SMO UI/Typedefs/PublicEvents--Cluster.ctl"
File 17="vi.lib/Levylab/Embedded SMO UI/Typedefs/PublicEvents--EmbeddedSMO.ReadyForInfo.ctl"
File 18="vi.lib/Levylab/Embedded SMO UI/Typedefs/UI State.ctl"
File 19="vi.lib/Levylab/Embedded SMO UI/Private/EmbeddedSMO.GetName.vi"
File 20="vi.lib/Levylab/Embedded SMO UI/Private/EmbeddedSMO.GetPrivateEvents.vi"
File 21="vi.lib/Levylab/Embedded SMO UI/Private/EmbeddedSMO.GetSubPanelReference.vi"
File 22="vi.lib/Levylab/Embedded SMO UI/Private/EmbeddedSMO.GetUIState.vi"
File 23="vi.lib/Levylab/Embedded SMO UI/Private/EmbeddedSMO.SetSubpanelReference.vi"
File 24="vi.lib/Levylab/Embedded SMO UI/Private/EmbeddedSMO.SetUIState.vi"
File 25="vi.lib/Levylab/Embedded SMO UI/Private/EmbeddedSMO.WriteName.vi"
File 26="vi.lib/Levylab/Embedded SMO UI/Overrides/Get VI Reference.vi"
File 27="vi.lib/Levylab/Embedded SMO UI/Methods (Overrides)/CreatePrivateEvents.vi"
File 28="vi.lib/Levylab/Embedded SMO UI/Methods (Overrides)/DestroyPrivateEvents.vi"
File 29="vi.lib/Levylab/Embedded SMO UI/Methods/DeferPanelUpdate.vi"
File 30="vi.lib/Levylab/Embedded SMO UI/Methods/Embed_Hide.vi"
File 31="vi.lib/Levylab/Embedded SMO UI/Methods/Embed_Show.vi"
File 32="vi.lib/Levylab/Embedded SMO UI/Methods/Accessors/Read Name.vi"
File 33="vi.lib/Levylab/Embedded SMO UI/Methods/Accessors/Read SubPanelReference.vi"
File 34="vi.lib/Levylab/Embedded SMO UI/Methods/Accessors/Read UI State.vi"
File 35="vi.lib/Levylab/Embedded SMO UI/Methods/Accessors/Write Name.vi"
File 36="vi.lib/Levylab/Embedded SMO UI/Methods/Accessors/Write SubPanelReference.vi"
File 37="vi.lib/Levylab/Embedded SMO UI/Methods/Accessors/Write UI State.vi"
File 38="vi.lib/Levylab/Embedded SMO UI/DataAccessors/GetProcessReference.vi"
File 39="vi.lib/Levylab/Embedded SMO UI/API/GetEmbeddedName.vi"
File 40="vi.lib/Levylab/Embedded SMO UI/API/GetSubPanelRef.vi"
File 41="vi.lib/Levylab/Embedded SMO UI/API/GetUIState.vi"
File 42="vi.lib/Levylab/Embedded SMO UI/API/SetEmbeddedName.vi"
File 43="vi.lib/Levylab/Embedded SMO UI/API/SetSubPanelRef.vi"
File 44="vi.lib/Levylab/Embedded SMO UI/API/SetUIState.vi"


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
