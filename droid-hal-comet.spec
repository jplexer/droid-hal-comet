# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device comet
%define vendor google

%define vendor_pretty Google
%define device_pretty Pixel 9 Pro Fold

%define droid_target_aarch64 1

#define installable_zip 1

%define enable_dtbo_update 1
%define enable_init_boot_update 1
%define enable_vendor_boot_update 1

# On Android 8+ the system partition is (intended to be) mounted on /.
%define makefstab_skip_entries / /odm /product /system /system_ext /vendor

Requires: droid-system

%define straggler_files \
/adb_keys\
/bugreports\
/cache\
/d\
/sdcard\
%{nil}

%define android_config \
#define __availability__(...)\
#define __ANDROID_MIN_SDK_VERSION__ 36\
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

