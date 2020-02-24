[Package]
Name = "levylab_lib_sr830_-_levy_tools"
Version = "1.0.0.2"
Release = ""
ID =7f526bc3c830bd895064d9f975da27ce
File Format = "vip"
Format Version = "2010"
Display Name = "SR830 - Levy Tools"


[Description]
Description = ""
Summary = ""
License = ""
Copyright = "Copyright (c) 2011, LevyLab"
Distribution = ""
Vendor = "LevyLab"
URL = ""
Packager = "voodoo"
Demo = "FALSE"
Release Notes = "These are levylab-coded SR830/810 drivers & utilities."
System Package = "FALSE"


[Platform]
Exclusive_LabVIEW_Version = ">=10.0"
Exclusive_LabVIEW_System = "ALL"
Exclusive_OS = "ALL"


[Script VIs]
PreInstall = ""
PostInstall = ""
PreUninstall = ""
PostUninstall = ""
Verify = ""
PreBuild = ""
PostBuild = ""


[Dependencies]
AutoReqProv = FALSE
Requires = ""
Conflicts = ""


[Activation]
License File = ""
Licensed Library = ""


[Files]
Num File Groups = "3"
Sub-Packages = ""


[File Group 0]
Target Dir = "<application>"
Replace Mode = "Always"
Num Files = 21
File 0 = "instr.lib/LevyLab/SR830 - Levy Tools/RampADCFromCurrentValue.vi"
File 1 = "instr.lib/LevyLab/SR830 - Levy Tools/Read-AUX.vi"
File 2 = "instr.lib/LevyLab/SR830 - Levy Tools/Read-AUX2.vi"
File 3 = "instr.lib/LevyLab/SR830 - Levy Tools/ReadACvolt.vi"
File 4 = "instr.lib/LevyLab/SR830 - Levy Tools/ReadADC.vi"
File 5 = "instr.lib/LevyLab/SR830 - Levy Tools/ReadFREQ.vi"
File 6 = "instr.lib/LevyLab/SR830 - Levy Tools/ReadMAG.vi"
File 7 = "instr.lib/LevyLab/SR830 - Levy Tools/ReadPhase.vi"
File 8 = "instr.lib/LevyLab/SR830 - Levy Tools/ReadSen.vi"
File 9 = "instr.lib/LevyLab/SR830 - Levy Tools/ReadTC.vi"
File 10 = "instr.lib/LevyLab/SR830 - Levy Tools/ReadXY.vi"
File 11 = "instr.lib/LevyLab/SR830 - Levy Tools/SetADC1- voltage.vi"
File 12 = "instr.lib/LevyLab/SR830 - Levy Tools/SetFREQ.vi"
File 13 = "instr.lib/LevyLab/SR830 - Levy Tools/SetHARM.vi"
File 14 = "instr.lib/LevyLab/SR830 - Levy Tools/SetPHASE.vi"
File 15 = "instr.lib/LevyLab/SR830 - Levy Tools/SetSEN.vi"
File 16 = "instr.lib/LevyLab/SR830 - Levy Tools/SetSineAmp.vi"
File 17 = "instr.lib/LevyLab/SR830 - Levy Tools/SetTC.vi"
File 18 = "instr.lib/LevyLab/SR830 - Levy Tools/Snap-SR830.vi"
File 19 = "instr.lib/LevyLab/SR830 - Levy Tools/Snap.ctl"
File 20 = "instr.lib/LevyLab/SR830 - Levy Tools/SR830 Clear.vi"


[File Group 1]
Target Dir = "<user.lib>"
Replace Mode = "Always"
Num Files = 1
File 0 = "functions_levylab_lib_sr830_-_levy_tools.mnu"


[File Group 2]
Target Dir = "<menus>/Controls"
Replace Mode = "Always"
Num Files = 1
File 0 = "controls_levylab_lib_sr830_-_levy_tools.mnu"
