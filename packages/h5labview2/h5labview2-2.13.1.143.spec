[Package]
Name="h5labview2"
Version="2.13.1.143"
Release=""
ID=eeb6e9354e56b5370bdbd5613bfcf7de
File Format="vip"
Format Version="2010"
Display Name="Hierarchical Data Format (HDF5)"


[Description]
Description="This library provides a simple interface to read and write data stored in the Heirarchical Data Format (HDF), version 5. This is a multi-lingual cross-platform format permitting storage of data with descriptive meta-data in an object hierarchy within a single file. See http://www.hdfgroup.org/why_hdf/ for more information."
Summary="HDF5 bindings for LabVIEW"
License="BSD-2-Clause"
Copyright="Copyright (c) 2013-2014, Martijn Jasperse"
Distribution=""
Vendor="Martijn Jasperse"
URL="http://h5labview.sourceforge.net/"
Packager="Martijn Jasperse"
Demo="FALSE"
Release Notes="<b>Now supports <u>timestamps and analog waveforms</u></b>\0A\0ARequires <b>HDF5 v1.8.14</b>. You may need to uninstall earlier versions if the installer fails, see the FAQ for more details.\0A\0ASee <i>CHANGES.TXT</i> for a description of changes since the last version."
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


[Platform]
Exclusive_LabVIEW_Version=">=10.0"
Exclusive_LabVIEW_System="ALL"
Exclusive_OS="ALL"


[Script VIs]
PreInstall=""
PostInstall="<OS Boot Volume Root>\\dev\\projs\\labview\\h5labview\\lib\\post-install.vi"
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
Num File Groups="1"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=246
File 0="vi.lib/addons/h5labview2/CHANGES.txt"
File 1="vi.lib/addons/h5labview2/dir.mnu"
File 2="vi.lib/addons/h5labview2/LICENSE"
File 3="vi.lib/addons/h5labview2/README"
File 4="vi.lib/addons/h5labview2/type/H5T.lvlib"
File 5="vi.lib/addons/h5labview2/type/H5Tclose.vi"
File 6="vi.lib/addons/h5labview2/type/H5Tcreate.vi"
File 7="vi.lib/addons/h5labview2/type/H5Tcreate_compound.vi"
File 8="vi.lib/addons/h5labview2/type/H5Tget_members.vi"
File 9="vi.lib/addons/h5labview2/type/H5Tget_size.vi"
File 10="vi.lib/addons/h5labview2/type/H5Tget_type.vi"
File 11="vi.lib/addons/h5labview2/type/H5Tquery.vi"
File 12="vi.lib/addons/h5labview2/tests/test_suite.vi"
File 13="vi.lib/addons/h5labview2/tests/waveform_append_array.vi"
File 14="vi.lib/addons/h5labview2/tests/waveform_variant.vi"
File 15="vi.lib/addons/h5labview2/tests/test_suite/array_cluster.vi"
File 16="vi.lib/addons/h5labview2/tests/test_suite/array_empty.vi"
File 17="vi.lib/addons/h5labview2/tests/test_suite/array_fixstr.vi"
File 18="vi.lib/addons/h5labview2/tests/test_suite/array_int.vi"
File 19="vi.lib/addons/h5labview2/tests/test_suite/array_stride.vi"
File 20="vi.lib/addons/h5labview2/tests/test_suite/array_timestamp.vi"
File 21="vi.lib/addons/h5labview2/tests/test_suite/array_units.vi"
File 22="vi.lib/addons/h5labview2/tests/test_suite/array_varstr.vi"
File 23="vi.lib/addons/h5labview2/tests/test_suite/attrib_obj.vi"
File 24="vi.lib/addons/h5labview2/tests/test_suite/attrib_obj_direct.vi"
File 25="vi.lib/addons/h5labview2/tests/test_suite/bigdata_2d.vi"
File 26="vi.lib/addons/h5labview2/tests/test_suite/bigdata_2d_filesp.vi"
File 27="vi.lib/addons/h5labview2/tests/test_suite/bigdata_3d.vi"
File 28="vi.lib/addons/h5labview2/tests/test_suite/boolean.vi"
File 29="vi.lib/addons/h5labview2/tests/test_suite/cluster1.vi"
File 30="vi.lib/addons/h5labview2/tests/test_suite/cluster2.vi"
File 31="vi.lib/addons/h5labview2/tests/test_suite/cluster_nested.vi"
File 32="vi.lib/addons/h5labview2/tests/test_suite/numeric_basic.vi"
File 33="vi.lib/addons/h5labview2/tests/test_suite/numeric_cluster.vi"
File 34="vi.lib/addons/h5labview2/tests/test_suite/numeric_dblarr.vi"
File 35="vi.lib/addons/h5labview2/tests/test_suite/numeric_extarr.vi"
File 36="vi.lib/addons/h5labview2/tests/test_suite/string_fix32.vi"
File 37="vi.lib/addons/h5labview2/tests/test_suite/string_fix6.vi"
File 38="vi.lib/addons/h5labview2/tests/test_suite/string_fixnull.vi"
File 39="vi.lib/addons/h5labview2/tests/test_suite/string_varlen.vi"
File 40="vi.lib/addons/h5labview2/tests/test_suite/string_varnull.vi"
File 41="vi.lib/addons/h5labview2/tests/test_suite/test_data.ctl"
File 42="vi.lib/addons/h5labview2/tests/test_suite/timestamp.vi"
File 43="vi.lib/addons/h5labview2/tests/test_suite/units.vi"
File 44="vi.lib/addons/h5labview2/tests/test_suite/variant_empty.vi"
File 45="vi.lib/addons/h5labview2/tests/test_suite/variant_read.vi"
File 46="vi.lib/addons/h5labview2/tests/test_suite/variant_write.vi"
File 47="vi.lib/addons/h5labview2/space/H5S.lvlib"
File 48="vi.lib/addons/h5labview2/space/H5Sclose.vi"
File 49="vi.lib/addons/h5labview2/space/H5Screate_simple.vi"
File 50="vi.lib/addons/h5labview2/space/H5Sget_dims.vi"
File 51="vi.lib/addons/h5labview2/space/H5Sget_npoints.vi"
File 52="vi.lib/addons/h5labview2/space/H5Sget_space.vi"
File 53="vi.lib/addons/h5labview2/space/H5Squery.vi"
File 54="vi.lib/addons/h5labview2/space/H5Sselect_hyperslab.vi"
File 55="vi.lib/addons/h5labview2/space/H5Sselect_simple.vi"
File 56="vi.lib/addons/h5labview2/props/H5P.lvlib"
File 57="vi.lib/addons/h5labview2/props/H5Pclose.vi"
File 58="vi.lib/addons/h5labview2/props/H5Pcreate.vi"
File 59="vi.lib/addons/h5labview2/props/H5Pget_chunk.vi"
File 60="vi.lib/addons/h5labview2/props/H5Pget_chunk_cache.vi"
File 61="vi.lib/addons/h5labview2/props/H5Pget_userblock.vi"
File 62="vi.lib/addons/h5labview2/props/H5Pset_chunk.vi"
File 63="vi.lib/addons/h5labview2/props/H5Pset_chunk_cache.vi"
File 64="vi.lib/addons/h5labview2/props/H5Pset_deflate.vi"
File 65="vi.lib/addons/h5labview2/props/H5Pset_scaleoffset.vi"
File 66="vi.lib/addons/h5labview2/props/H5Pset_userblock.vi"
File 67="vi.lib/addons/h5labview2/mnu/h5labview2_A.mnu"
File 68="vi.lib/addons/h5labview2/mnu/h5labview2_D.mnu"
File 69="vi.lib/addons/h5labview2/mnu/h5labview2_F.mnu"
File 70="vi.lib/addons/h5labview2/mnu/h5labview2_O.mnu"
File 71="vi.lib/addons/h5labview2/mnu/h5labview2_P.mnu"
File 72="vi.lib/addons/h5labview2/mnu/h5labview2_S.mnu"
File 73="vi.lib/addons/h5labview2/mnu/h5labview2_T.mnu"
File 74="vi.lib/addons/h5labview2/lib/bonzai.c"
File 75="vi.lib/addons/h5labview2/lib/bonzai.h"
File 76="vi.lib/addons/h5labview2/lib/clean.bat"
File 77="vi.lib/addons/h5labview2/lib/converters.c"
File 78="vi.lib/addons/h5labview2/lib/debug.c"
File 79="vi.lib/addons/h5labview2/lib/debug.h"
File 80="vi.lib/addons/h5labview2/lib/err_codes.c"
File 81="vi.lib/addons/h5labview2/lib/get_stats.py"
File 82="vi.lib/addons/h5labview2/lib/H5err.txt"
File 83="vi.lib/addons/h5labview2/lib/h5labview-errors.txt"
File 84="vi.lib/addons/h5labview2/lib/h5labview.c"
File 85="vi.lib/addons/h5labview2/lib/h5labview.h"
File 86="vi.lib/addons/h5labview2/lib/h5labview32.dll"
File 87="vi.lib/addons/h5labview2/lib/h5labview32.so"
File 88="vi.lib/addons/h5labview2/lib/h5labview64.dll"
File 89="vi.lib/addons/h5labview2/lib/hdf5dll.def"
File 90="vi.lib/addons/h5labview2/lib/MAINTAINER_NOTES"
File 91="vi.lib/addons/h5labview2/lib/makefile"
File 92="vi.lib/addons/h5labview2/lib/makefile.win"
File 93="vi.lib/addons/h5labview2/lib/ms_stdint.h"
File 94="vi.lib/addons/h5labview2/lib/palmanip.vi"
File 95="vi.lib/addons/h5labview2/lib/post-install.vi"
File 96="vi.lib/addons/h5labview2/lib/proc_h5e.awk"
File 97="vi.lib/addons/h5labview2/lib/proc_h5e.vi"
File 98="vi.lib/addons/h5labview2/lib/readwrite.c"
File 99="vi.lib/addons/h5labview2/lib/stdint.h"
File 100="vi.lib/addons/h5labview2/lib/testlib"
File 101="vi.lib/addons/h5labview2/lib/testlib.c"
File 102="vi.lib/addons/h5labview2/lib/typeconv.c"
File 103="vi.lib/addons/h5labview2/lib/version.h"
File 104="vi.lib/addons/h5labview2/lib/version.rc"
File 105="vi.lib/addons/h5labview2/lib/vi_tree.vi"
File 106="vi.lib/addons/h5labview2/lib/waveforms.c"
File 107="vi.lib/addons/h5labview2/lib/xptest.c"
File 108="vi.lib/addons/h5labview2/group/H5G.lvlib"
File 109="vi.lib/addons/h5labview2/group/H5Gclose.vi"
File 110="vi.lib/addons/h5labview2/group/H5Gdelete.vi"
File 111="vi.lib/addons/h5labview2/group/H5Glist.vi"
File 112="vi.lib/addons/h5labview2/group/H5Gopen.vi"
File 113="vi.lib/addons/h5labview2/group/H5Ocopy.vi"
File 114="vi.lib/addons/h5labview2/group/H5Oquery.vi"
File 115="vi.lib/addons/h5labview2/file/H5F.lvlib"
File 116="vi.lib/addons/h5labview2/file/H5Fclose.vi"
File 117="vi.lib/addons/h5labview2/file/H5Fflush.vi"
File 118="vi.lib/addons/h5labview2/file/H5Fget_image.vi"
File 119="vi.lib/addons/h5labview2/file/H5Fget_name.vi"
File 120="vi.lib/addons/h5labview2/file/H5Fget_size.vi"
File 121="vi.lib/addons/h5labview2/file/H5Fis_hdf.vi"
File 122="vi.lib/addons/h5labview2/file/H5Fmode.ctl"
File 123="vi.lib/addons/h5labview2/file/H5Fopen.vi"
File 124="vi.lib/addons/h5labview2/file/H5Fopen_core.vi"
File 125="vi.lib/addons/h5labview2/dataset/H5D.lvlib"
File 126="vi.lib/addons/h5labview2/dataset/H5Dappend.vi"
File 127="vi.lib/addons/h5labview2/dataset/H5Dclose.vi"
File 128="vi.lib/addons/h5labview2/dataset/H5Dcreate.vi"
File 129="vi.lib/addons/h5labview2/dataset/H5Dcreate_simple.vi"
File 130="vi.lib/addons/h5labview2/dataset/H5Dget_space.vi"
File 131="vi.lib/addons/h5labview2/dataset/H5Dget_type.vi"
File 132="vi.lib/addons/h5labview2/dataset/H5Dopen.vi"
File 133="vi.lib/addons/h5labview2/dataset/H5Dprepare_append.vi"
File 134="vi.lib/addons/h5labview2/dataset/H5Dread_var.vi"
File 135="vi.lib/addons/h5labview2/dataset/H5Dset_extent.vi"
File 136="vi.lib/addons/h5labview2/dataset/H5Dset_image.vi"
File 137="vi.lib/addons/h5labview2/dataset/H5Dwrite_pixmap.vi"
File 138="vi.lib/addons/h5labview2/dataset/H5Dwrite_var.vi"
File 139="vi.lib/addons/h5labview2/dataset/H5Dwrite.llb/H5Dwrite.xnode"
File 140="vi.lib/addons/h5labview2/dataset/H5Dwrite.llb/H5Dwrite__code.vi"
File 141="vi.lib/addons/h5labview2/dataset/H5Dwrite.llb/H5Dwrite_AdaptToInputs.vi"
File 142="vi.lib/addons/h5labview2/dataset/H5Dwrite.llb/H5Dwrite_base.vi"
File 143="vi.lib/addons/h5labview2/dataset/H5Dwrite.llb/H5Dwrite_Bounds.vi"
File 144="vi.lib/addons/h5labview2/dataset/H5Dwrite.llb/H5Dwrite_BuildMenu3.vi"
File 145="vi.lib/addons/h5labview2/dataset/H5Dwrite.llb/H5Dwrite_GenerateCode.vi"
File 146="vi.lib/addons/h5labview2/dataset/H5Dwrite.llb/H5Dwrite_GetTerms3.vi"
File 147="vi.lib/addons/h5labview2/dataset/H5Dwrite.llb/H5Dwrite_Help.vi"
File 148="vi.lib/addons/h5labview2/dataset/H5Dwrite.llb/H5Dwrite_Image.vi"
File 149="vi.lib/addons/h5labview2/dataset/H5Dwrite.llb/H5Dwrite_SelectMenu3.vi"
File 150="vi.lib/addons/h5labview2/dataset/H5Dwrite.llb/H5Dwrite_State.ctl"
File 151="vi.lib/addons/h5labview2/dataset/H5Dwrite.llb/H5Dwrite_UpdateStateWithRef.vi"
File 152="vi.lib/addons/h5labview2/dataset/H5Dread.llb/H5Dread.xnode"
File 153="vi.lib/addons/h5labview2/dataset/H5Dread.llb/H5Dread__code.vi"
File 154="vi.lib/addons/h5labview2/dataset/H5Dread.llb/H5Dread_AdaptToInputs.vi"
File 155="vi.lib/addons/h5labview2/dataset/H5Dread.llb/H5Dread_base.vi"
File 156="vi.lib/addons/h5labview2/dataset/H5Dread.llb/H5Dread_Bounds.vi"
File 157="vi.lib/addons/h5labview2/dataset/H5Dread.llb/H5Dread_BuildMenu3.vi"
File 158="vi.lib/addons/h5labview2/dataset/H5Dread.llb/H5Dread_GenerateCode.vi"
File 159="vi.lib/addons/h5labview2/dataset/H5Dread.llb/H5Dread_GetTerms3.vi"
File 160="vi.lib/addons/h5labview2/dataset/H5Dread.llb/H5Dread_Help.vi"
File 161="vi.lib/addons/h5labview2/dataset/H5Dread.llb/H5Dread_Image.vi"
File 162="vi.lib/addons/h5labview2/dataset/H5Dread.llb/H5Dread_SelectMenu3.vi"
File 163="vi.lib/addons/h5labview2/dataset/H5Dread.llb/H5Dread_State.ctl"
File 164="vi.lib/addons/h5labview2/dataset/H5Dread.llb/H5Dread_UpdateStateWithRef.vi"
File 165="vi.lib/addons/h5labview2/base/H5Equery.vi"
File 166="vi.lib/addons/h5labview2/base/h5err.ctl"
File 167="vi.lib/addons/h5labview2/base/H5get_libversion.vi"
File 168="vi.lib/addons/h5labview2/base/H5get_type.vi"
File 169="vi.lib/addons/h5labview2/base/H5Ldelete.vi"
File 170="vi.lib/addons/h5labview2/base/H5Lexists.vi"
File 171="vi.lib/addons/h5labview2/base/h5o_type.ctl"
File 172="vi.lib/addons/h5labview2/base/H5restart.vi"
File 173="vi.lib/addons/h5labview2/base/hclass_t.ctl"
File 174="vi.lib/addons/h5labview2/base/hid_t.ctl"
File 175="vi.lib/addons/h5labview2/base/lib_path.vi"
File 176="vi.lib/addons/h5labview2/base/ref_to_int.vi"
File 177="vi.lib/addons/h5labview2/base/rel_path.vi"
File 178="vi.lib/addons/h5labview2/base/ts_from_iso8601.vi"
File 179="vi.lib/addons/h5labview2/base/ts_to_iso8601.vi"
File 180="vi.lib/addons/h5labview2/base/validator.vi"
File 181="vi.lib/addons/h5labview2/attrib/H5A.lvlib"
File 182="vi.lib/addons/h5labview2/attrib/H5Aclose.vi"
File 183="vi.lib/addons/h5labview2/attrib/H5Acopy.vi"
File 184="vi.lib/addons/h5labview2/attrib/H5Acopy_multi.vi"
File 185="vi.lib/addons/h5labview2/attrib/H5Adelete.vi"
File 186="vi.lib/addons/h5labview2/attrib/H5Aexists.vi"
File 187="vi.lib/addons/h5labview2/attrib/H5Aget_space.vi"
File 188="vi.lib/addons/h5labview2/attrib/H5Aget_type.vi"
File 189="vi.lib/addons/h5labview2/attrib/H5Alist.vi"
File 190="vi.lib/addons/h5labview2/attrib/H5Aopen.vi"
File 191="vi.lib/addons/h5labview2/attrib/H5Aread_multi.vi"
File 192="vi.lib/addons/h5labview2/attrib/H5Aread_var.vi"
File 193="vi.lib/addons/h5labview2/attrib/H5Awrite_multi.vi"
File 194="vi.lib/addons/h5labview2/attrib/H5Awrite_var.vi"
File 195="vi.lib/addons/h5labview2/attrib/H5Awrite.llb/H5Awrite.xnode"
File 196="vi.lib/addons/h5labview2/attrib/H5Awrite.llb/H5Awrite__code.vi"
File 197="vi.lib/addons/h5labview2/attrib/H5Awrite.llb/H5Awrite_AdaptToInputs.vi"
File 198="vi.lib/addons/h5labview2/attrib/H5Awrite.llb/H5Awrite_base.vi"
File 199="vi.lib/addons/h5labview2/attrib/H5Awrite.llb/H5Awrite_Bounds.vi"
File 200="vi.lib/addons/h5labview2/attrib/H5Awrite.llb/H5Awrite_BuildMenu3.vi"
File 201="vi.lib/addons/h5labview2/attrib/H5Awrite.llb/H5Awrite_GenerateCode.vi"
File 202="vi.lib/addons/h5labview2/attrib/H5Awrite.llb/H5Awrite_GetTerms3.vi"
File 203="vi.lib/addons/h5labview2/attrib/H5Awrite.llb/H5Awrite_Help.vi"
File 204="vi.lib/addons/h5labview2/attrib/H5Awrite.llb/H5Awrite_Image.vi"
File 205="vi.lib/addons/h5labview2/attrib/H5Awrite.llb/H5Awrite_SelectMenu3.vi"
File 206="vi.lib/addons/h5labview2/attrib/H5Awrite.llb/H5Awrite_State.ctl"
File 207="vi.lib/addons/h5labview2/attrib/H5Awrite.llb/H5Awrite_UpdateStateWithRef.vi"
File 208="vi.lib/addons/h5labview2/attrib/H5Aread.llb/H5Aread.xnode"
File 209="vi.lib/addons/h5labview2/attrib/H5Aread.llb/H5Aread__code.vi"
File 210="vi.lib/addons/h5labview2/attrib/H5Aread.llb/H5Aread_AdaptToInputs.vi"
File 211="vi.lib/addons/h5labview2/attrib/H5Aread.llb/H5Aread_base.vi"
File 212="vi.lib/addons/h5labview2/attrib/H5Aread.llb/H5Aread_Bounds.vi"
File 213="vi.lib/addons/h5labview2/attrib/H5Aread.llb/H5Aread_BuildMenu3.vi"
File 214="vi.lib/addons/h5labview2/attrib/H5Aread.llb/H5Aread_GenerateCode.vi"
File 215="vi.lib/addons/h5labview2/attrib/H5Aread.llb/H5Aread_GetTerms3.vi"
File 216="vi.lib/addons/h5labview2/attrib/H5Aread.llb/H5Aread_Help.vi"
File 217="vi.lib/addons/h5labview2/attrib/H5Aread.llb/H5Aread_Image.vi"
File 218="vi.lib/addons/h5labview2/attrib/H5Aread.llb/H5Aread_SelectMenu3.vi"
File 219="vi.lib/addons/h5labview2/attrib/H5Aread.llb/H5Aread_State.ctl"
File 220="vi.lib/addons/h5labview2/attrib/H5Aread.llb/H5Aread_UpdateStateWithRef.vi"
File 221="examples/h5labview2/examples/append-dataset-2D.vi"
File 222="examples/h5labview2/examples/append-dataset.vi"
File 223="examples/h5labview2/examples/partial-read.vi"
File 224="examples/h5labview2/examples/partial-write.vi"
File 225="examples/h5labview2/examples/repack-h5.vi"
File 226="examples/h5labview2/examples/save-image-multi.vi"
File 227="examples/h5labview2/examples/save-image.vi"
File 228="examples/h5labview2/examples/simple-cluster.vi"
File 229="examples/h5labview2/examples/simple-read.vi"
File 230="examples/h5labview2/examples/simple-write.vi"
File 231="examples/h5labview2/examples/string-types.vi"
File 232="examples/h5labview2/examples/test-pic.jpg"
File 233="examples/h5labview2/examples/variant-io.vi"
File 234="examples/h5labview2/examples/waveform.vi"
File 235="examples/h5labview2/examples/waveform_append.vi"
File 236="examples/h5labview2/examples/waveform_array.vi"
File 237="examples/h5labview2/examples/zipped-dataset.vi"
File 238="examples/h5labview2/examples/treeview/treeview-item.vi"
File 239="examples/h5labview2/examples/treeview/treeview-recurse.vi"
File 240="examples/h5labview2/examples/treeview/treeview.vi"
File 241="examples/h5labview2/examples/matlab/matlab_create.vi"
File 242="examples/h5labview2/examples/matlab/matlab_example.vi"
File 243="examples/h5labview2/examples/matlab/matlab_locale.vi"
File 244="examples/h5labview2/examples/matlab/matlab_readme.txt"
File 245="examples/h5labview2/examples/matlab/matlab_write.vi"