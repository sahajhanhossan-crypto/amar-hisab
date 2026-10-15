[app]

# (string) Title of your application
title = Amar Hisab

# (string) Package name
package.name = amarhisab

# (string) Package domain (needed for android package name)
package.domain = com.boss

# (string) Source code directory where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (string) Application version
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.3.1

# (str) Supported orientations
orientation = portrait

# (bool) Use fullscreen mode or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (list) Architecture to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup
android.allow_backup = True
