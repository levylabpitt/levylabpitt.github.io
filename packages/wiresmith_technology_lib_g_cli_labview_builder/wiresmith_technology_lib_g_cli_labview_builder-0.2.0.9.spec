[Package]
Name="wiresmith_technology_lib_g_cli_labview_builder"
Version="0.2.0.9"
Release=""
ID=712064b34b80da74ae62c831d7dedfb7
File Format="vip"
Format Version="2017"
Display Name="G CLI LabVIEW Builder"


[Description]
Description="Provides a G CLI tool to automate build specifications in LabVIEW"
Summary="Provides a G CLI tool to automate build specifications in LabVIEW"
License="MIT"
Copyright="Copyright (c) 2025, Wiresmith Technology"
Distribution=""
Vendor="Wiresmith Technology"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="* First Release"
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
Requires="wiresmith_technology_lib_g_cli>=2.1.0.1520"
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
Num Files=6
File 0="vi.lib/Wiresmith Technology/G CLI LabVIEW Builder/G CLI LvBuild.lvlib"
File 1="vi.lib/Wiresmith Technology/G CLI LabVIEW Builder/lvBuild SubVIs/Calculate Common Root.vi"
File 2="vi.lib/Wiresmith Technology/G CLI LabVIEW Builder/lvBuild SubVIs/CONSTANT - lvBuild Version.vi"
File 3="vi.lib/Wiresmith Technology/G CLI LabVIEW Builder/lvBuild SubVIs/Version Updates.vi"
File 4="vi.lib/Wiresmith Technology/G CLI LabVIEW Builder/lvBuild SubVIs/Zip Output.vi"
File 5="vi.lib/G CLI Tools/lvBuild.vi"
