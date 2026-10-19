[app]

# ───────────────────────────────
#  App identity
# ───────────────────────────────
title = ListApp
package.name = listapp
package.domain = org.yourname
version = 0.1

# ───────────────────────────────
#  Source files
# ───────────────────────────────
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# ───────────────────────────────
#  Requirements
# ───────────────────────────────
requirements = python3,kivy

# ───────────────────────────────
#  Display
# ───────────────────────────────
orientation = portrait
fullscreen = 0

# ───────────────────────────────
#  Android settings
# ───────────────────────────────
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True


[buildozer]

# Log level: 0 = errors only, 1 = info, 2 = debug
log_level = 1
warn_on_root = 1
