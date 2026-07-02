[Package]
Name="wiresmith_technology_lib_g_cli_vi_package_manager_tools"
Version="0.2.1.15"
Release=""
ID=691f654c6df2cd4f35e3eac1c8f4e6dc
File Format="vip"
Format Version="2017"
Display Name="G CLI VI Package Manager Tools"


[Description]
Description="Contains a series of tools for automating VI package manager from the command line including:\0D\0A\0D\0A*vipBuild - Build a package from a VIPB file.\0D\0A* vipcApply - Apply a VIPC file.\0D\0A\0D\0AThis requires VI Package Manager Pro in order to have access to the API."
Summary="G CLI Tools for VI Package Manager Automation."
License="MIT"
Copyright="Copyright (c) 2026, Wiresmith Technology"
Distribution=""
Vendor="Wiresmith Technology"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="* VIPBuild now returns path VIP file as 'BUILD_OUTPUT=""'"
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
Requires="jki_lib_vipm_api>=2017.0.0.55,wiresmith_technology_lib_g_cli>=2.1.0.1520"
Conflicts=""


[Activation]
License File=""
Licensed Library=""


[Files]
Num File Groups="1"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=9
File 0="vi.lib/Wiresmith Technology/G CLI VI Package Manager Tools/G CLI VIP.lvlib"
File 1="vi.lib/Wiresmith Technology/G CLI VI Package Manager Tools/VIP SubVIs/CONSTANT - VIP API Version.vi"
File 2="vi.lib/Wiresmith Technology/G CLI VI Package Manager Tools/VIP SubVIs/Get VIP Builder Config.vi"
File 3="vi.lib/Wiresmith Technology/G CLI VI Package Manager Tools/VIP SubVIs/Package List to Files and Library Package List.vi"
File 4="vi.lib/Wiresmith Technology/G CLI VI Package Manager Tools/VIP SubVIs/Update VIPB Version.vi"
File 5="vi.lib/Wiresmith Technology/G CLI VI Package Manager Tools/VIP SubVIs/Version information to VIP API Version.vi"
File 6="vi.lib/G CLI Tools/VIPBuild.vi"
File 7="vi.lib/G CLI Tools/VIPCApply.vi"
File 8="vi.lib/G CLI Tools/VIPInstall.vi"
