[Package]
Name="levylab_lib_maui"
Version="1.0.0.22"
Release=""
ID=9afccf3f491e1f82b6bc5e1e38f443ae
File Format="vip"
Format Version="2017"
Display Name="SMO.UI.MAUI"


[Description]
Description=""
Summary="Working Engine for MAUI Framework."
License="BSD-3"
Copyright="Copyright (c) 2020, Levylab"
Distribution=""
Vendor="Levylab"
URL="https://github.com/levylabpitt/Embedded-Main-SMO"
Packager="Joseph Albro"
Demo="FALSE"
Release Notes="Changed Names\0AFixed dependencies on old names of Embedded Engine and Embedded Template"
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
Requires="jki_statemachineobjects>=1.3.0.56,levylab_lib_embedded_smo_ui>=1.0.0.12,levylab_lib_smo_embeddedui>=1.0.0.10"
Conflicts=""


[Activation]
License File=""
Licensed Library=""


[Files]
Num File Groups="18"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=38
File 0="vi.lib/Levylab/SMO.UI.MAUI/Maui.lvproj"
File 1="vi.lib/Levylab/SMO.UI.MAUI/Process.vi"
File 2="vi.lib/Levylab/SMO.UI.MAUI/SMO.UI.MAUI.lvclass"
File 3="vi.lib/Levylab/SMO.UI.MAUI/SMO.UI.MAUI.TestLauncher.vi"
File 4="vi.lib/Levylab/SMO.UI.MAUI/Typedefs/EmbeddedNotifier.ctl"
File 5="vi.lib/Levylab/SMO.UI.MAUI/Typedefs/PanelData.ctl"
File 6="vi.lib/Levylab/SMO.UI.MAUI/Typedefs/PanelDataNotifier.ctl"
File 7="vi.lib/Levylab/SMO.UI.MAUI/Typedefs/PrivateEvents--Cluster.ctl"
File 8="vi.lib/Levylab/SMO.UI.MAUI/Typedefs/PrivateEvents--SMO.UI.MAUI.GetEmbedded.ctl"
File 9="vi.lib/Levylab/SMO.UI.MAUI/Typedefs/PrivateEvents--SMO.UI.MAUI.GetPanelData.ctl"
File 10="vi.lib/Levylab/SMO.UI.MAUI/Typedefs/PrivateEvents--SMO.UI.MAUI.SetEmbedded.ctl"
File 11="vi.lib/Levylab/SMO.UI.MAUI/Typedefs/PrivateEvents--SMO.UI.MAUI.SetPanelData.ctl"
File 12="vi.lib/Levylab/SMO.UI.MAUI/Typedefs/PrivateEvents--SMO.UI.MAUI.UpdatePanel.ctl"
File 13="vi.lib/Levylab/SMO.UI.MAUI/Typedefs/PublicEvents--Cluster.ctl"
File 14="vi.lib/Levylab/SMO.UI.MAUI/Typedefs/PublicEvents--SMO.UI.MAUI.ReadyForInfo .ctl"
File 15="vi.lib/Levylab/SMO.UI.MAUI/Private/SMO.UI.MAUI.GetEmbedded.vi"
File 16="vi.lib/Levylab/SMO.UI.MAUI/Private/SMO.UI.MAUI.GetPanelData.vi"
File 17="vi.lib/Levylab/SMO.UI.MAUI/Private/SMO.UI.MAUI.GetPrivateEvents.vi"
File 18="vi.lib/Levylab/SMO.UI.MAUI/Private/SMO.UI.MAUI.ReadyForInfo.vi"
File 19="vi.lib/Levylab/SMO.UI.MAUI/Private/SMO.UI.MAUI.SetEmbedded.vi"
File 20="vi.lib/Levylab/SMO.UI.MAUI/Private/SMO.UI.MAUI.SetPanelData.vi"
File 21="vi.lib/Levylab/SMO.UI.MAUI/Methods (Overrides)/CreatePrivateEvents.vi"
File 22="vi.lib/Levylab/SMO.UI.MAUI/Methods (Overrides)/CreatePublicEvents.vi"
File 23="vi.lib/Levylab/SMO.UI.MAUI/Methods (Overrides)/DestroyPrivateEvents.vi"
File 24="vi.lib/Levylab/SMO.UI.MAUI/Methods (Overrides)/DestroyPublicEvents.vi"
File 25="vi.lib/Levylab/SMO.UI.MAUI/Methods (Overrides)/onProcessStarted.vi"
File 26="vi.lib/Levylab/SMO.UI.MAUI/Methods (Overrides)/onStart.vi"
File 27="vi.lib/Levylab/SMO.UI.MAUI/Methods (Overrides)/onStop.vi"
File 28="vi.lib/Levylab/SMO.UI.MAUI/Methods (Framework)/ChangePanel.vi"
File 29="vi.lib/Levylab/SMO.UI.MAUI/Methods (Framework)/GreyRings.vi"
File 30="vi.lib/Levylab/SMO.UI.MAUI/Methods (Framework)/PopulateRings.vi"
File 31="vi.lib/Levylab/SMO.UI.MAUI/API/ArrangeFrontPanel.vi"
File 32="vi.lib/Levylab/SMO.UI.MAUI/API/SMO.UI.MAUI.GetPublicEvents.vi"
File 33="vi.lib/Levylab/SMO.UI.MAUI/API/SMO.UI.MAUI.UpdatePanel.vi"
File 34="vi.lib/Levylab/SMO.UI.MAUI/API/Accessors/ReadEmbedded.vi"
File 35="vi.lib/Levylab/SMO.UI.MAUI/API/Accessors/ReadPanelData.vi"
File 36="vi.lib/Levylab/SMO.UI.MAUI/API/Accessors/WriteEmbedded.vi"
File 37="vi.lib/Levylab/SMO.UI.MAUI/API/Accessors/WritePanelData.vi"


[File Group 1]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=6
File 0="_functions_levylab_lib_maui_1.mnu"
File 1="_functions_levylab_lib_maui_2.mnu"
File 2="_functions_levylab_lib_maui_3.mnu"
File 3="_functions_levylab_lib_maui_4.mnu"
File 4="_functions_levylab_lib_maui_5.mnu"
File 5="functions_Levylab_lib_MAUI.mnu"


[File Group 2]
Target Dir="<menus>/Controls"
Replace Mode="Always"
Num Files=2
File 0="_controls_levylab_lib_maui_1.mnu"
File 1="controls_Levylab_lib_MAUI.mnu"


[File Group 3]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=6
File 0="_functions_levylab_lib_maui_1.mnu"
File 1="_functions_levylab_lib_maui_2.mnu"
File 2="_functions_levylab_lib_maui_3.mnu"
File 3="_functions_levylab_lib_maui_4.mnu"
File 4="_functions_levylab_lib_maui_5.mnu"
File 5="functions_Levylab_lib_MAUI.mnu"


[File Group 4]
Target Dir="<menus>/Controls"
Replace Mode="Always"
Num Files=2
File 0="_controls_levylab_lib_maui_1.mnu"
File 1="controls_Levylab_lib_MAUI.mnu"


[File Group 5]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=6
File 0="_functions_levylab_lib_maui_1.mnu"
File 1="_functions_levylab_lib_maui_2.mnu"
File 2="_functions_levylab_lib_maui_3.mnu"
File 3="_functions_levylab_lib_maui_4.mnu"
File 4="_functions_levylab_lib_maui_5.mnu"
File 5="functions_Levylab_lib_MAUI.mnu"


[File Group 6]
Target Dir="<menus>/Controls"
Replace Mode="Always"
Num Files=2
File 0="_controls_levylab_lib_maui_1.mnu"
File 1="controls_Levylab_lib_MAUI.mnu"


[File Group 7]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=6
File 0="_functions_levylab_lib_maui_1.mnu"
File 1="_functions_levylab_lib_maui_2.mnu"
File 2="_functions_levylab_lib_maui_3.mnu"
File 3="_functions_levylab_lib_maui_4.mnu"
File 4="_functions_levylab_lib_maui_5.mnu"
File 5="functions_Levylab_lib_MAUI.mnu"


[File Group 8]
Target Dir="<menus>/Controls"
Replace Mode="Always"
Num Files=2
File 0="_controls_levylab_lib_maui_1.mnu"
File 1="controls_Levylab_lib_MAUI.mnu"


[File Group 9]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=3
File 0="_functions_levylab_lib_maui_1.mnu"
File 1="_functions_levylab_lib_maui_2.mnu"
File 2="functions_Levylab_lib_MAUI.mnu"


[File Group 10]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=6
File 0="_functions_levylab_lib_maui_1.mnu"
File 1="_functions_levylab_lib_maui_2.mnu"
File 2="_functions_levylab_lib_maui_3.mnu"
File 3="_functions_levylab_lib_maui_4.mnu"
File 4="_functions_levylab_lib_maui_5.mnu"
File 5="functions_Levylab_lib_MAUI.mnu"


[File Group 11]
Target Dir="<menus>/Controls"
Replace Mode="Always"
Num Files=2
File 0="_controls_levylab_lib_maui_1.mnu"
File 1="controls_Levylab_lib_MAUI.mnu"


[File Group 12]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=2
File 0="_functions_levylab_lib_maui_1.mnu"
File 1="functions_Levylab_lib_MAUI.mnu"


[File Group 13]
Target Dir="<menus>/Controls"
Replace Mode="Always"
Num Files=2
File 0="_controls_levylab_lib_maui_1.mnu"
File 1="controls_Levylab_lib_MAUI.mnu"


[File Group 14]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=3
File 0="_functions_levylab_lib_maui_1.mnu"
File 1="_functions_levylab_lib_maui_2.mnu"
File 2="functions_Levylab_lib_MAUI.mnu"


[File Group 15]
Target Dir="<menus>/Controls"
Replace Mode="Always"
Num Files=2
File 0="_controls_levylab_lib_maui_1.mnu"
File 1="controls_Levylab_lib_MAUI.mnu"


[File Group 16]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=6
File 0="_functions_levylab_lib_maui_1.mnu"
File 1="_functions_levylab_lib_maui_2.mnu"
File 2="_functions_levylab_lib_maui_3.mnu"
File 3="_functions_levylab_lib_maui_4.mnu"
File 4="_functions_levylab_lib_maui_5.mnu"
File 5="functions_Levylab_lib_MAUI.mnu"


[File Group 17]
Target Dir="<menus>/Controls"
Replace Mode="Always"
Num Files=2
File 0="_controls_levylab_lib_maui_1.mnu"
File 1="controls_Levylab_lib_MAUI.mnu"
