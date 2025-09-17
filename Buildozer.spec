buildozer.spec

[app]
# Title of your application
title = MindMatrix

# Package name
package.name = mindmatrix

# Package domain (unique identifier)
package.domain = org.subhashsaran

# Source code directory
source.dir = .

# Version
version = 1.0.0

# Application requirements
requirements = python3,kivy

# Icon of the application (optional)
icon.filename = %(source.dir)s/icon.png

# Supported orientation
orientation = portrait

# Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
# Android API version
android.api = 33

# Minimum API your APK will support
android.minapi = 21

# Android SDK version
android.sdk = 33

# NDK version
android.ndk = 25b

# Android NDK API level
android.ndk_api = 21

# Use private data storage
android.private_storage = True

