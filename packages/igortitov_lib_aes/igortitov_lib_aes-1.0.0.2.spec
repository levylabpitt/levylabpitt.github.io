[Package]
Name="igortitov_lib_aes"
Version="1.0.0.2"
Release=""
ID=8bf35806b3d3be13a22edf17c81f1b25
File Format="vip"
Format Version="2017"
Display Name="AES"


[Description]
Description="This is a native LabVIEW implementation of AES algorithm. It can run on Windows, Mac and Linux operating systems."
Summary=""
License="MIT"
Copyright="Copyright (c) 2021, IgorTitov"
Distribution=""
Vendor="IgorTitov"
URL="https://github.com/IgorTitov/LabVIEW-Advanced-Encryption-Standard"
Packager="IgorTitov"
Demo="FALSE"
Release Notes=""
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
Requires=""
Conflicts=""


[Activation]
License File=""
Licensed Library=""


[Files]
Num File Groups="2"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=26
File 0="vi.lib/IgorTitov/AES/.gitignore"
File 1="vi.lib/IgorTitov/AES/Advanced Encryption Standard (AES).lvlib"
File 2="vi.lib/IgorTitov/AES/Advanced Encryption Standard (AES).lvproj"
File 3="vi.lib/IgorTitov/AES/AES Decrypt.vi"
File 4="vi.lib/IgorTitov/AES/AES Encrypt.vi"
File 5="vi.lib/IgorTitov/AES/CHANGELOG.md"
File 6="vi.lib/IgorTitov/AES/Decrypt with AES.vi"
File 7="vi.lib/IgorTitov/AES/Encrypt with AES.vi"
File 8="vi.lib/IgorTitov/AES/LICENSE"
File 9="vi.lib/IgorTitov/AES/readme.html"
File 10="vi.lib/IgorTitov/AES/README.md"
File 11="vi.lib/IgorTitov/AES/SubVIs/Add Round Key.vi"
File 12="vi.lib/IgorTitov/AES/SubVIs/Base64 to String.vi"
File 13="vi.lib/IgorTitov/AES/SubVIs/Cipher.vi"
File 14="vi.lib/IgorTitov/AES/SubVIs/Expand Key.vi"
File 15="vi.lib/IgorTitov/AES/SubVIs/Mix Columns.vi"
File 16="vi.lib/IgorTitov/AES/SubVIs/Shift Rows.vi"
File 17="vi.lib/IgorTitov/AES/SubVIs/String to Base64.vi"
File 18="vi.lib/IgorTitov/AES/SubVIs/Sub Bytes.vi"
File 19="vi.lib/IgorTitov/AES/Examples/AES Encryption Test.vi"
File 20="vi.lib/IgorTitov/AES/Examples/AES_LabVIEW_image.png"
File 21="vi.lib/IgorTitov/AES/Controls and Typedefs/Cipher Phases Enum (Typedef).ctl"
File 22="vi.lib/IgorTitov/AES/Controls and Typedefs/Decipher Phases Enum (Typedef).ctl"
File 23="vi.lib/IgorTitov/AES/Controls and Typedefs/Decryption Phases Enum (Typedef).ctl"
File 24="vi.lib/IgorTitov/AES/Controls and Typedefs/Encryption Phases Enum (Typedef).ctl"
File 25="vi.lib/IgorTitov/AES/Controls and Typedefs/Mix Bytes Phases Enum (Typedef).ctl"


[File Group 1]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=3
File 0="_functions_igortitov_lib_aes_1.mnu"
File 1="_functions_igortitov_lib_aes_2.mnu"
File 2="functions_IgorTitov_lib_AES.mnu"
