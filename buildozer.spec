[app]

title = Candy.flood
package.name = candyflood
package.domain = org.candyflood

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json

version = 1.0

requirements = python3,kivy

android.accept_sdk_license = True

orientation = portrait

fullscreen = 0

android.debug_artifact = apk
android.release_artifact = aab

[buildozer]

log_level = 2
warn_on_root = 1
