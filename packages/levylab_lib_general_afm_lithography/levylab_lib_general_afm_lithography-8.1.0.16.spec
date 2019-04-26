[Package]
Name="levylab_lib_general_afm_lithography"
Version="8.1.0.16"
Release=""
ID=5da03f17a328eca3f8b9cf71d23e67f9
File Format="vip"
Format Version="2010"
Display Name="General AFM Lithography"


[Description]
Description=""
Summary=""
License=""
Copyright="Copyright (c) 2014, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Shicheng Lu"
Demo="FALSE"
Release Notes="add function generator"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="FALSE"


[Platform]
Exclusive_LabVIEW_Version=">=13.0"
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
Requires="levylab_lib_ibwtolv>=1.0.0.1,levylab_lib_lvtoitx>=2.0.0.10"
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
Num Files=58
File 0="vi.lib/Levylab/General AFM Lithography/Main.vi"
File 1="vi.lib/Levylab/General AFM Lithography/Simulation XY update.vi"
File 2="vi.lib/Levylab/General AFM Lithography/Tip Voltage.vi"
File 3="vi.lib/Levylab/General AFM Lithography/subvi/Votlage wave channel setup.vi"
File 4="vi.lib/Levylab/General AFM Lithography/subvi/toolpath/Arrange Array.vi"
File 5="vi.lib/Levylab/General AFM Lithography/subvi/toolpath/funnels to Commands.vi"
File 6="vi.lib/Levylab/General AFM Lithography/subvi/toolpath/Litho Interpolater.vi"
File 7="vi.lib/Levylab/General AFM Lithography/subvi/toolpath/Paths to Commands_new.vi"
File 8="vi.lib/Levylab/General AFM Lithography/subvi/toolpath/Rectangles to Commands.vi"
File 9="vi.lib/Levylab/General AFM Lithography/subvi/simulator/Global Variables.vi"
File 10="vi.lib/Levylab/General AFM Lithography/subvi/simulator/Open Simulation.vi"
File 11="vi.lib/Levylab/General AFM Lithography/subvi/simulator/Relay Data.vi"
File 12="vi.lib/Levylab/General AFM Lithography/subvi/simulator/Simulator.vi"
File 13="vi.lib/Levylab/General AFM Lithography/subvi/parsing/Check First Character Type.vi"
File 14="vi.lib/Levylab/General AFM Lithography/subvi/parsing/Discard One Character.vi"
File 15="vi.lib/Levylab/General AFM Lithography/subvi/parsing/Get Matrix from Transform.vi"
File 16="vi.lib/Levylab/General AFM Lithography/subvi/parsing/Get Path Commands.vi"
File 17="vi.lib/Levylab/General AFM Lithography/subvi/parsing/Paths Sub-Parser.vi"
File 18="vi.lib/Levylab/General AFM Lithography/subvi/parsing/Rectangle Sub-Parser.vi"
File 19="vi.lib/Levylab/General AFM Lithography/subvi/parsing/SVG Parser.vi"
File 20="vi.lib/Levylab/General AFM Lithography/subvi/parsing/XPath File Sub-Parser.vi"
File 21="vi.lib/Levylab/General AFM Lithography/subvi/parsing/XPath String Sub-Parser.vi"
File 22="vi.lib/Levylab/General AFM Lithography/subvi/mathematics/Bezier curve.vi"
File 23="vi.lib/Levylab/General AFM Lithography/subvi/mathematics/Bezier length.vi"
File 24="vi.lib/Levylab/General AFM Lithography/subvi/mathematics/Estimated Time Required.vi"
File 25="vi.lib/Levylab/General AFM Lithography/subvi/mathematics/Interpolate Points.vi"
File 26="vi.lib/Levylab/General AFM Lithography/subvi/mathematics/Interpolate Points_new.vi"
File 27="vi.lib/Levylab/General AFM Lithography/subvi/mathematics/intersection.vi"
File 28="vi.lib/Levylab/General AFM Lithography/subvi/mathematics/Relative Coordinates.vi"
File 29="vi.lib/Levylab/General AFM Lithography/subvi/mathematics/rotation pattern.vi"
File 30="vi.lib/Levylab/General AFM Lithography/subvi/mathematics/Transform a Point.vi"
File 31="vi.lib/Levylab/General AFM Lithography/subvi/image/Image Processing.vi"
File 32="vi.lib/Levylab/General AFM Lithography/subvi/image/Load IBW File.vi"
File 33="vi.lib/Levylab/General AFM Lithography/subvi/image/Read Scan Size and Offset.vi"
File 34="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/Call Cypher Driver.vi"
File 35="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/Call Cypher Driver_genreal AFM.vi"
File 36="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/Cypher Lithography.vi"
File 37="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/cypher read value.vi"
File 38="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/Cypher XY LVDT Parameters.vi"
File 39="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/Display wave.vi"
File 40="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/igor define command.vi"
File 41="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/interpolate nodes.vi"
File 42="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/Make wave.vi"
File 43="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/move to target point.vi"
File 44="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/Read out  X Sensor.vi"
File 45="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/Read out  Y Sensor.vi"
File 46="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/Send Igor Command.vi"
File 47="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/Send igor command_no return.vi"
File 48="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/Set PIDS loop 0.vi"
File 49="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/Set PIDS loop 1.vi"
File 50="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/Set value.vi"
File 51="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/Stop PIS Loops.vi"
File 52="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/Tip touchdown.vi"
File 53="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/Tip Withdraw.vi"
File 54="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/X sensor convert meter to V.vi"
File 55="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/X sensor convert V to meter.vi"
File 56="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/Y sensor convert meter to V.vi"
File 57="vi.lib/Levylab/General AFM Lithography/subvi/Drivers/Y sensor convert V to meter.vi"


[File Group 1]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=8
File 0="_functions_levylab_lib_general_afm_lithography_1.mnu"
File 1="_functions_levylab_lib_general_afm_lithography_2.mnu"
File 2="_functions_levylab_lib_general_afm_lithography_3.mnu"
File 3="_functions_levylab_lib_general_afm_lithography_4.mnu"
File 4="_functions_levylab_lib_general_afm_lithography_5.mnu"
File 5="_functions_levylab_lib_general_afm_lithography_6.mnu"
File 6="_functions_levylab_lib_general_afm_lithography_7.mnu"
File 7="functions_levylab_lib_general_afm_lithography.mnu"
