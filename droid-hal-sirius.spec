%define device sirius
%define vendor sony
%define vendor_pretty Sony
%define device_pretty Xperia Z2
%define installable_zip 1

%define straggler_files\
/selinux_version\
/service_contexts\
%{nil}

%include rpm/dhd/droid-hal-device.inc
