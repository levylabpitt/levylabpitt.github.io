[Package]
Name="levylab_lib_build_support_system"
Version="1.11.3.54"
Release=""
ID=e2d5bbac879ef0fd622a84727e7dfc02
File Format="vip"
Format Version="2017"
Display Name="Build Support (System)"


[Description]
Description=" VIs and scripts to help automate package and application builds"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2026, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.11.3]\0D\0A1. Fixed: the 1.11.2 package shipped VIPM.lvlib with six unresolved merge-conflict markers, leaving the library unloadable. It is clean again, and the duplicate VI entries behind the bad merge are gone.\0D\0A\0D\0A2. build.bat can now build a repo that ships more than one product. Give each product its own <name>.cfg in "build support\\" and name it on the command line: build.bat "<repo root>" release build-support. ".cfg" is appended if you leave it off, build.cfg stays the default when no name is given, and naming a config that does not exist lists the ones that do.\0D\0A\0D\0A3. New TAG_PREFIX config key, prepended to the git tag and the GitHub release name, so two products released from one repo no longer collide in a single tag space. Empty by default, which keeps the bare version tag every single-product repo already uses. Avoid a '/' in the prefix for a product that ships the SelfUpdate class: SelfUpdate rebuilds the tag from the last path component of the releases/latest redirect and re-requests releases/tag/<that>, so a slash makes the round-trip 404.\0D\0A\0D\0A4. build.bat takes an optional release/test argument that overrides the config's DO_RELEASE for a single run - "release" runs the git release, "test" builds without touching git. It and the config name are arguments 2 and 3 and may be given in either order.\0D\0A\0D\0A5. The release tag is now pushed as refs/tags/<tag>, so a prefixed tag containing a slash cannot be read as a branch name.\0D\0A\0D\0A6. Fixed a double build-number bump, and moved the bump ahead of the release. The script's own bump now runs only when BUILD_VIP=false; when the package itself is built the bump is left to VIPM's vipBuild rather than being applied twice. Both bumps now happen before the git release, so the release commit carries the bumped vipb instead of leaving it dirty for a manual follow-up commit. The tag and the built artifact keep the version as built.\0D\0A\0D\0A7. Build documentation updated throughout: the config-key table covers TAG_PREFIX, the build steps describe the new arguments, and there is a new section on repos that ship more than one product.\0D\0A\0D\0A8. Fixed: the GitHub release now carries the .vip. The vipb writes the package to its Library_Output_Folder (builds\\Package), but the release step only collected assets from builds\\latest, so no release ever had a .vip attached - and a package-only product, which builds no installer, would have been released with no assets at all. The built package is now staged into builds\\latest and the script says which file it staged, or warns if it found none.\0D\0A\0D\0A9. Fixed: build.bat can now release the repo it lives in. The release step checks out other branches, which rewrote the running script; cmd.exe reads a batch file by byte offset, so execution resumed mid-line and ran unrelated fragments - in one case compiling an Inno installer for a package-only product. When the script detects it is inside the repo being built it now re-runs from a copy in TEMP. Only the build-support repo hits this; the installed copy in %LOCALAPPDATA% was never affected.\0D\0A\0D\0A10. Fixed: every build printed "The filename, directory name, or volume label syntax is incorrect" while archiving the previous release. The guard was "if exist builds\\latest\\*.*", which is true even for an empty directory because the wildcard matches the . and .. entries, so move ran with nothing to move and failed. The guard is now a for wildcard, which matches real files only. Archiving itself always worked when there was something to archive; the message was noise."
System Package="TRUE"
Sub Package="TRUE"
License Agreement="TRUE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"
install into global environment="FALSE"


[Platform]
Exclusive_LabVIEW_Version="LabVIEW>=0"
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
Requires="levylab_lib_progress_bar>=1.0.0.1,wiresmith_technology_lib_g_cli>=3.0.1.98,wiresmith_technology_lib_g_cli_labview_builder>=0.2.0.9,wiresmith_technology_lib_g_cli_vi_package_manager_tools>=0.2.1.15"
Conflicts=""


[Activation]
License File=""
Licensed Library=""


[Files]
Num File Groups="1"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<OS User Application Data>"
Replace Mode="Always"
Num Files=5
File 0="LevyLab/build-support/templates/build.cfg"
File 1="LevyLab/build-support/templates/build_all.bat"
File 2="LevyLab/build-support/templates/Inno.iss"
File 3="LevyLab/build-support/scripts/build.bat"
File 4="LevyLab/build-support/scripts/Setup-BuildMachine.bat"
