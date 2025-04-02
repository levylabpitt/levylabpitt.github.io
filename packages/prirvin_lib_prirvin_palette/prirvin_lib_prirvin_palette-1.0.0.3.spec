[Package]
Name="prirvin_lib_prirvin_palette"
Version="1.0.0.3"
Release=""
ID=62b4b53c2fc891868cd4c747b661ef02
File Format="vip"
Format Version="2017"
Display Name="PRIrvin-Palette"


[Description]
Description=""
Summary=""
License=""
Copyright="Copyright (c) 2025, PRIrvin"
Distribution=""
Vendor="PRIrvin"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes=""
System Package="FALSE"
Sub Package="FALSE"
License Agreement="FALSE"


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
Num Files=5
File 0="vi.lib/PRIrvin/PRIrvin-Palette/.gitattributes"
File 1="vi.lib/PRIrvin/PRIrvin-Palette/.gitignore"
File 2="vi.lib/PRIrvin/PRIrvin-Palette/LICENSE"
File 3="vi.lib/PRIrvin/PRIrvin-Palette/icons/g2673.png"
File 4="vi.lib/PRIrvin/PRIrvin-Palette/builds/Package/ciozi137_lib_ciozi137_palette-1.0.0.2.vip"


[File Group 1]
Target Dir="<vi.lib>/addons/prirvin"
Replace Mode="Always"
Num Files=1
File 0="functions_prirvin_lib_prirvin_palette.mnu"


[File Group 2]
Target Dir="<vi.lib>/addons/prirvin"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
