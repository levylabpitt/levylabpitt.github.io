[Package]
Name="levylab_lib_maui"
Version="1.0.0.10"
Release=""
ID=3c610bded4d0a2c5565cf8208348b04e
File Format="vip"
Format Version="2017"
Display Name="MAUI"


[Description]
Description=""
Summary="Main UI for Embedded Framework"
License="BSD-3"
Copyright="Copyright (c) 2020, Levylab"
Distribution=""
Vendor="Levylab"
URL="https://github.com/levylabpitt/Embedded-Main-SMO"
Packager="Joseph Albro"
Demo="FALSE"
Release Notes="Changed repository structure."
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
Num File Groups="10"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=47
File 0="vi.lib/Levylab/MAUI/MAUI.lvclass"
File 1="vi.lib/Levylab/MAUI/Maui.lvproj"
File 2="vi.lib/Levylab/MAUI/MAUI.TestLauncher.vi"
File 3="vi.lib/Levylab/MAUI/Process.vi"
File 4="vi.lib/Levylab/MAUI/Typedefs/EmbeddedNotifier.ctl"
File 5="vi.lib/Levylab/MAUI/Typedefs/PanelData.ctl"
File 6="vi.lib/Levylab/MAUI/Typedefs/PanelDataNotifier.ctl"
File 7="vi.lib/Levylab/MAUI/Typedefs/PrivateEvents--Cluster.ctl"
File 8="vi.lib/Levylab/MAUI/Typedefs/PrivateEvents--MAUI.GetEmbedded.ctl"
File 9="vi.lib/Levylab/MAUI/Typedefs/PrivateEvents--MAUI.GetLeftData.ctl"
File 10="vi.lib/Levylab/MAUI/Typedefs/PrivateEvents--MAUI.GetRightData.ctl"
File 11="vi.lib/Levylab/MAUI/Typedefs/PrivateEvents--MAUI.SetEmbedded.ctl"
File 12="vi.lib/Levylab/MAUI/Typedefs/PrivateEvents--MAUI.SetLeftData.ctl"
File 13="vi.lib/Levylab/MAUI/Typedefs/PrivateEvents--MAUI.SetRightData.ctl"
File 14="vi.lib/Levylab/MAUI/Typedefs/PrivateEvents--MAUI.Update Left Subpanel.ctl"
File 15="vi.lib/Levylab/MAUI/Typedefs/PrivateEvents--MAUI.UpdateRightSubpanel.ctl"
File 16="vi.lib/Levylab/MAUI/Typedefs/PublicEvents--Cluster.ctl"
File 17="vi.lib/Levylab/MAUI/Typedefs/PublicEvents--MAUI.ReadyForInfo .ctl"
File 18="vi.lib/Levylab/MAUI/Private/MAUI.GetEmbedded.vi"
File 19="vi.lib/Levylab/MAUI/Private/MAUI.GetLeftData.vi"
File 20="vi.lib/Levylab/MAUI/Private/MAUI.GetPrivateEvents.vi"
File 21="vi.lib/Levylab/MAUI/Private/MAUI.GetRightData.vi"
File 22="vi.lib/Levylab/MAUI/Private/MAUI.ReadyForInfo.vi"
File 23="vi.lib/Levylab/MAUI/Private/MAUI.SetEmbedded.vi"
File 24="vi.lib/Levylab/MAUI/Private/MAUI.SetLeftData.vi"
File 25="vi.lib/Levylab/MAUI/Private/MAUI.SetRightData.vi"
File 26="vi.lib/Levylab/MAUI/Methods (Overrides)/CreatePrivateEvents.vi"
File 27="vi.lib/Levylab/MAUI/Methods (Overrides)/CreatePublicEvents.vi"
File 28="vi.lib/Levylab/MAUI/Methods (Overrides)/DestroyPrivateEvents.vi"
File 29="vi.lib/Levylab/MAUI/Methods (Overrides)/DestroyPublicEvents.vi"
File 30="vi.lib/Levylab/MAUI/Methods (Overrides)/onProcessStarted.vi"
File 31="vi.lib/Levylab/MAUI/Methods (Overrides)/onStart.vi"
File 32="vi.lib/Levylab/MAUI/Methods (Overrides)/onStop.vi"
File 33="vi.lib/Levylab/MAUI/Methods (Framework)/ChangeLeftSubpanel.vi"
File 34="vi.lib/Levylab/MAUI/Methods (Framework)/ChangeRightSubpanel.vi"
File 35="vi.lib/Levylab/MAUI/Methods (Framework)/GreyLeftRing.vi"
File 36="vi.lib/Levylab/MAUI/Methods (Framework)/GreyRightRing.vi"
File 37="vi.lib/Levylab/MAUI/API/ArrangeFrontPanel.vi"
File 38="vi.lib/Levylab/MAUI/API/MAUI.GetPublicEvents.vi"
File 39="vi.lib/Levylab/MAUI/API/MAUI.UpdateLeftSubpanel.vi"
File 40="vi.lib/Levylab/MAUI/API/MAUI.UpdateRightSubpanel.vi"
File 41="vi.lib/Levylab/MAUI/API/Accessors/ReadEmbedded.vi"
File 42="vi.lib/Levylab/MAUI/API/Accessors/ReadLeftData.vi"
File 43="vi.lib/Levylab/MAUI/API/Accessors/ReadRightData.vi"
File 44="vi.lib/Levylab/MAUI/API/Accessors/WriteEmbedded.vi"
File 45="vi.lib/Levylab/MAUI/API/Accessors/WriteLeftData.vi"
File 46="vi.lib/Levylab/MAUI/API/Accessors/WriteRightData.vi"


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
