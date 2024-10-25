[Package]
Name="labview-zmq"
Version="3.6.3.113"
Release=""
ID=9294a0f4d8b2f9e213d49d0d744419a0
File Format="vip"
Format Version="2017"
Display Name="ZeroMQ Socket Library"


[Description]
Description="LabVIEW bindings for ZeroMQ, the communication library that provides simple many-many messaging and other topologies."
Summary="ZeroMQ for LabVIEW"
License="BSD 3-clause"
Copyright="Copyright (c) 2012-2021, Martijn Jasperse"
Distribution=""
Vendor="Martijn Jasperse"
URL="http://labview-zmq.sf.net"
Packager="Martijn Jasperse"
Demo="FALSE"
Release Notes="- separate compiled code from all library VIs and classes\0A- disable debugging and automatic error handling in all library VIs\0A- change reentrancy of zmq_recv_multi.vi to "preallocated shared"\0A\0A*This version compiled by Patrick Irvin (ciozi137) with LabVIEW 2019 and VIPM 2022"
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
Exclusive_OS="Windows NT,Linux"


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
Num Files=109
File 0="vi.lib/addons/zeromq/.hgflow"
File 1="vi.lib/addons/zeromq/AUTHORS.txt"
File 2="vi.lib/addons/zeromq/endpoint_proto.ctl"
File 3="vi.lib/addons/zeromq/error_type.ctl"
File 4="vi.lib/addons/zeromq/GPL.txt"
File 5="vi.lib/addons/zeromq/LICENSE.txt"
File 6="vi.lib/addons/zeromq/monitor_event.ctl"
File 7="vi.lib/addons/zeromq/poll_event_data.ctl"
File 8="vi.lib/addons/zeromq/poll_type.ctl"
File 9="vi.lib/addons/zeromq/README.txt"
File 10="vi.lib/addons/zeromq/socket_options.ctl"
File 11="vi.lib/addons/zeromq/socket_type.ctl"
File 12="vi.lib/addons/zeromq/zeromq.lvlib"
File 13="vi.lib/addons/zeromq/zmq_bind.vi"
File 14="vi.lib/addons/zeromq/zmq_bind_random.vi"
File 15="vi.lib/addons/zeromq/zmq_check_term.vi"
File 16="vi.lib/addons/zeromq/zmq_close.vi"
File 17="vi.lib/addons/zeromq/zmq_config_curve.vi"
File 18="vi.lib/addons/zeromq/zmq_connect.vi"
File 19="vi.lib/addons/zeromq/zmq_context.lvclass"
File 20="vi.lib/addons/zeromq/zmq_ctx_check.vi"
File 21="vi.lib/addons/zeromq/zmq_ctx_create.vi"
File 22="vi.lib/addons/zeromq/zmq_ctx_destroy.vi"
File 23="vi.lib/addons/zeromq/zmq_curve_pair.vi"
File 24="vi.lib/addons/zeromq/zmq_disconnect.vi"
File 25="vi.lib/addons/zeromq/zmq_endpoint_build.vi"
File 26="vi.lib/addons/zeromq/zmq_endpoint_split.vi"
File 27="vi.lib/addons/zeromq/zmq_errno.vi"
File 28="vi.lib/addons/zeromq/zmq_get_monitor.vi"
File 29="vi.lib/addons/zeromq/zmq_getsocketopt.vi"
File 30="vi.lib/addons/zeromq/zmq_getsocketopt_binary.vi"
File 31="vi.lib/addons/zeromq/zmq_getsocketopt_int.vi"
File 32="vi.lib/addons/zeromq/zmq_getsocketopt_int64.vi"
File 33="vi.lib/addons/zeromq/zmq_has.vi"
File 34="vi.lib/addons/zeromq/zmq_join.vi"
File 35="vi.lib/addons/zeromq/zmq_leave.vi"
File 36="vi.lib/addons/zeromq/zmq_libpath.vi"
File 37="vi.lib/addons/zeromq/zmq_new_event.vi"
File 38="vi.lib/addons/zeromq/zmq_poll.vi"
File 39="vi.lib/addons/zeromq/zmq_poll_array.vi"
File 40="vi.lib/addons/zeromq/zmq_poll_scalar.vi"
File 41="vi.lib/addons/zeromq/zmq_proxy.vi"
File 42="vi.lib/addons/zeromq/zmq_recv.vi"
File 43="vi.lib/addons/zeromq/zmq_recv_event.vi"
File 44="vi.lib/addons/zeromq/zmq_recv_multi.vi"
File 45="vi.lib/addons/zeromq/zmq_recv_timeout.vi"
File 46="vi.lib/addons/zeromq/zmq_send.vi"
File 47="vi.lib/addons/zeromq/zmq_send_multi.vi"
File 48="vi.lib/addons/zeromq/zmq_setsocketopt.vi"
File 49="vi.lib/addons/zeromq/zmq_socket.lvclass"
File 50="vi.lib/addons/zeromq/zmq_socket.vi"
File 51="vi.lib/addons/zeromq/zmq_socket_check.vi"
File 52="vi.lib/addons/zeromq/zmq_socket_monitor.vi"
File 53="vi.lib/addons/zeromq/zmq_socket_set.vi"
File 54="vi.lib/addons/zeromq/zmq_unbind.vi"
File 55="vi.lib/addons/zeromq/zmq_version.vi"
File 56="vi.lib/addons/zeromq/zmq_z85_decode.vi"
File 57="vi.lib/addons/zeromq/zmq_z85_encode.vi"
File 58="vi.lib/addons/zeromq/zmq_zap_example_globals.vi"
File 59="vi.lib/addons/zeromq/zmq_zap_example_template.vi"
File 60="vi.lib/addons/zeromq/zmq_zap_init.vi"
File 61="vi.lib/addons/zeromq/zmq_zap_thread.vi"
File 62="vi.lib/addons/zeromq/zmq_zap_verify.vi"
File 63="vi.lib/addons/zeromq/tests/test_curve.vi"
File 64="vi.lib/addons/zeromq/tests/test_pubsub.vi"
File 65="vi.lib/addons/zeromq/tests/test_radio.vi"
File 66="vi.lib/addons/zeromq/tests/test_reqrep.vi"
File 67="vi.lib/addons/zeromq/tests/test_term2.vi"
File 68="vi.lib/addons/zeromq/tests/test_z85.vi"
File 69="vi.lib/addons/zeromq/tests/test_zap.vi"
File 70="vi.lib/addons/zeromq/lib/bonzai.c"
File 71="vi.lib/addons/zeromq/lib/bonzai.h"
File 72="vi.lib/addons/zeromq/lib/debug.c"
File 73="vi.lib/addons/zeromq/lib/debug.h"
File 74="vi.lib/addons/zeromq/lib/makefile"
File 75="vi.lib/addons/zeromq/lib/parse_errnos.py"
File 76="vi.lib/addons/zeromq/lib/rename_calls.vi"
File 77="vi.lib/addons/zeromq/lib/rename_lib2.vi"
File 78="vi.lib/addons/zeromq/lib/zmq-errors.txt"
File 79="vi.lib/addons/zeromq/lib/zmq_labview.c"
File 80="vi.lib/addons/zeromq/lib/win64/libsodium.dll"
File 81="vi.lib/addons/zeromq/lib/win64/libzmq-v120-mt-4_3_2.dll"
File 82="vi.lib/addons/zeromq/lib/win64/lvzmq64.dll"
File 83="vi.lib/addons/zeromq/lib/win64/msvcp120.dll"
File 84="vi.lib/addons/zeromq/lib/win64/msvcr120.dll"
File 85="vi.lib/addons/zeromq/lib/win32/libsodium.dll"
File 86="vi.lib/addons/zeromq/lib/win32/libzmq-v120-mt-4_3_2.dll"
File 87="vi.lib/addons/zeromq/lib/win32/lvzmq32.dll"
File 88="vi.lib/addons/zeromq/lib/win32/msvcp120.dll"
File 89="vi.lib/addons/zeromq/lib/win32/msvcr120.dll"
File 90="examples/zeromq/examples/capabilities.vi"
File 91="examples/zeromq/examples/examples.txt"
File 92="examples/zeromq/examples/polling_events.vi"
File 93="examples/zeromq/examples/socket_monitor.vi"
File 94="examples/zeromq/examples/req-rep/trivial_rep.vi"
File 95="examples/zeromq/examples/req-rep/trivial_req.vi"
File 96="examples/zeromq/examples/req-rep/trivial_req.vit"
File 97="examples/zeromq/examples/pub-sub/pub_multipart.vi"
File 98="examples/zeromq/examples/pub-sub/pub_simple.vi"
File 99="examples/zeromq/examples/pub-sub/pub_simple_recv.py"
File 100="examples/zeromq/examples/pub-sub/pub_simple_send.py"
File 101="examples/zeromq/examples/pub-sub/sub_multipart.vi"
File 102="examples/zeromq/examples/pub-sub/zmq_pub.vit"
File 103="examples/zeromq/examples/pub-sub/zmq_sub.vit"
File 104="examples/zeromq/examples/lazy-pirate/lp-client.vi"
File 105="examples/zeromq/examples/lazy-pirate/lp-server-events.vi"
File 106="examples/zeromq/examples/lazy-pirate/lp-server-timeouts.vi"
File 107="examples/zeromq/examples/lazy-pirate/lp-server.vi"
File 108="examples/zeromq/examples/example-app/example-app.lvproj"


[File Group 1]
Target Dir="<vi.lib>/addons"
Replace Mode="Always"
Num Files=1
File 0="functions_labview-zmq.mnu"
