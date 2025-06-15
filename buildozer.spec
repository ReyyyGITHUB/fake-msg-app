[app]
title = Spy-Chat
package.name = spychat
package.domain = com.fakemessagerayhan.app

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0
requirements = python3,kivy,cython

# Android specific
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 30
android.minapi = 21
android.ndk = 23b
android.accept_sdk_license = True
android.gradle_dependencies = 
android.add_src = 
android.add_aars = 
android.add_jars = 
android.add_libs_armeabi = 
android.add_libs_armeabi_v7a = 
android.add_libs_arm64_v8a = 
android.add_libs_x86 = 
android.add_libs_mips = 
android.orientation = portrait
android.allow_backup = True
android.private_storage = True
android.add_activites = 
android.add_permissions = 
android.add_features = 
android.ouya.category = 
android.ouya.icon.filename = 
android.entrypoint = org.kivy.android.PythonActivity
android.app_theme = "@android:style/Theme.NoTitleBar"
android.presplash.filename = 
android.icon.filename = 
android.launch_mode = standard
android.wakelock = False

[buildozer]
log_level = 2
warn_on_root = 1
build_dir = ./.buildozer
bin_dir = ./bin
