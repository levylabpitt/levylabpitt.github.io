[Package]
Name="levylab_lib_asana_api"
Version="1.4.1.2"
Release=""
ID=daf22191da885988b835651d7bbb989b
File Format="vip"
Format Version="2017"
Display Name="Asana API"


[Description]
Description=""
Summary=""
License=""
Copyright="Copyright (c) 2019, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Aaron Greenberg"
Demo="FALSE"
Release Notes="Input Auth Code handling using JKISM"
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
Requires="i3_json>=1.0.0.10,jki_lib_json_serialization>=1.1.10.37,jki_lib_rest_client>=1.3.2.21"
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
Num Files=38
File 0="user.lib/Levylab/Asana API/Asana API.lvproj"
File 1="user.lib/Levylab/Asana API/Asana Authentication.vi"
File 2="user.lib/Levylab/Asana API/Authenticate.vi"
File 3="user.lib/Levylab/Asana API/Authentication_Header_Handler.vi"
File 4="user.lib/Levylab/Asana API/Build_Auth_URL.vi"
File 5="user.lib/Levylab/Asana API/Build_Request.vi"
File 6="user.lib/Levylab/Asana API/Create Project.vi"
File 7="user.lib/Levylab/Asana API/Create Task.vi"
File 8="user.lib/Levylab/Asana API/Download Attachment.vi"
File 9="user.lib/Levylab/Asana API/Downloader.vi"
File 10="user.lib/Levylab/Asana API/Encode_Base_Info.vi"
File 11="user.lib/Levylab/Asana API/Get Attachment Details.vi"
File 12="user.lib/Levylab/Asana API/Get Attachments.vi"
File 13="user.lib/Levylab/Asana API/Get Custom Fields.vi"
File 14="user.lib/Levylab/Asana API/Get Item Location.vi"
File 15="user.lib/Levylab/Asana API/Get Project Members.vi"
File 16="user.lib/Levylab/Asana API/Get Projects.vi"
File 17="user.lib/Levylab/Asana API/Get Request example.vi"
File 18="user.lib/Levylab/Asana API/Get Tasks.vi"
File 19="user.lib/Levylab/Asana API/Get Teams from User.vi"
File 20="user.lib/Levylab/Asana API/Get Teams.vi"
File 21="user.lib/Levylab/Asana API/Get_Access_Token.vi"
File 22="user.lib/Levylab/Asana API/Get_Auth_Code.vi"
File 23="user.lib/Levylab/Asana API/Get_Timeout.vi"
File 24="user.lib/Levylab/Asana API/Input_Auth_Code.vi"
File 25="user.lib/Levylab/Asana API/levylab_lib_asana_api-1.3.0.2.vip"
File 26="user.lib/Levylab/Asana API/levylab_lib_asana_api-1.3.0.4.vip"
File 27="user.lib/Levylab/Asana API/levylab_lib_asana_api-1.3.0.5.vip"
File 28="user.lib/Levylab/Asana API/levylab_lib_asana_api-1.3.0.6.vip"
File 29="user.lib/Levylab/Asana API/levylab_lib_asana_api-1.4.0.1.vip"
File 30="user.lib/Levylab/Asana API/OAuth.lvclass"
File 31="user.lib/Levylab/Asana API/Post Status Update.vi"
File 32="user.lib/Levylab/Asana API/Post_AuthenticationCode_Request.vi"
File 33="user.lib/Levylab/Asana API/Put Custom Fields.vi"
File 34="user.lib/Levylab/Asana API/Read_Refresh_Token.vi"
File 35="user.lib/Levylab/Asana API/scope_needed.ctl"
File 36="user.lib/Levylab/Asana API/Set_Response_Type.vi"
File 37="user.lib/Levylab/Asana API/User_Get_Auth_Code.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_Asana_API.mnu"
