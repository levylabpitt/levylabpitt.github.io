[Package]
Name="andreas_wirsing_lib_lvarray2ibw"
Version="1.0.0.1"
Release=""
ID=135e0e936bf29305974d3b2018ba3619
File Format="vip"
Format Version="2017"
Display Name="lvarray2ibw"


[Description]
Description="igorBinV5.llb\0A\0ALabVIEW library to store arrays as Igor Binary Waves on disk.\0AMost of the features of IGOR Binary Waves are supported.\0AThe waves are stored in IGOR Binary Wave file version 5 even if this is not required.\0ABecause IGOR Binary Wave file version 5 was introduced in IGOR 3.0 the ibw files cannot be read with earlier versions of IGOR.\0A\0ARestrictions:\0AThe library was developed under LabVIEW 7.1 on a Windows 2000 machine. It will not run on LabVIEW versions below 7.1.\0AIt is also successfully tested on a Win XP machine and LV 7.1.\0AIt is neither known if Mac LV versions nor if LV version higher than 7.1 are supported.\0AUp to now it is not possible to read IGOR Binary Wave files into LV arrays.\0A\0AUsage:\0AThe library contains - among many other VIs - a VI called Array2ibw.vi. This is a Polymorphic VI, that chooses the the right sub VI depending on the data type that is connected to 'array in'. So only this VI is actually needed.\0ACopy the library to the user.lib directory inside the LabVIEW 7.1 directory to make the VI accessable via the User Libraries entry of the palletteMenu.\0A\0AIMPORTANT: THERE IS A SIGNIFICANT DIFFERENCE HOW DIMENSION INDECES ARE HANDLED IN IGOR AND LABVIEW!\0AIN LABVIEW THE HIGHEST DIMENSION IS STATED FIRST WHEREAS IN IGOR THE FIRST DIMENSION IS THE ROW DIMENSION.\0A\0AExample: If you concatenate two 1-dimensional waves of the same length (and without the /NP flag) in IGOR you'll get an 2-dimensional wave. Using IGOR's DimSize function to reveal the dimension size you get for dimNumber 0 the number of points of the two original waves and for dimNumber 1 DimSize returns 2. Doing the same in LabVIEW with two 1-dimensional arrays and the Build Array VI and using the Array Size VI to reveal the dimension size, you get a 2 point array whose first entry is 2 and the second contains the number of points of the original arrays.\0AThis VI considers this difference. An 2-dimensional array created via the Build Array VI as explained above can simply be connected to this VI, for arrays created via the Initialize Array VI for example, one has to pay particular attention on this difference. If not an IGOR binary file is created that does not reflect the data in the original LabVIEW array.\0A\0AThanks:\0AGary W. Johnson for his great work on the first version of such a LabVIEW library several years ago.\0A_______________\0A\0AIf you find any bugs or have comments or feature requests, contact me or make a request on the IgorExchange site.\0A\0AAndreas Wirsing, FU Berlin\0Aawirsing@zedat.fu-berlin.de\0AOktober 2010"
Summary="LabVIEW library to store arrays as Igor Binary Waves on disk."
License=""
Copyright="Copyright (c) 20, Andreas Wirsing"
Distribution=""
Vendor="Andreas Wirsing"
URL="https://www.wavemetrics.com/project-releases/1129"
Packager="Andreas Wirsing"
Demo="FALSE"
Release Notes="initial build of _only_ lvarray2ibw.llb (was previously part of IBWtoLV package)"
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
Num File Groups="3"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=3
File 0="user.lib/Andreas Wirsing/lvarray2ibw/igorBinV5.llb"
File 1="user.lib/Andreas Wirsing/lvarray2ibw/lvarray2ibw.lvproj"
File 2="user.lib/Andreas Wirsing/lvarray2ibw/README.txt"


[File Group 1]
Target Dir="<menus>/Categories/Andreas Wirsing"
Replace Mode="Always"
Num Files=2
File 0="_functions_andreas_wirsing_lib_lvarray2ibw_1.mnu"
File 1="functions_Andreas_Wirsing_lib_lvarray2ibw.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Andreas Wirsing"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
