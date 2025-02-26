[app]
# Название приложения
title = Screen Recorder

# Уникальное имя пакета (замени "yourname" на свой ID)
package.name = screenrecorder
package.domain = org.yourname

# Версия приложения
version = 1.0
package.version = 1.0

# Папка с исходным кодом (если код в корне проекта, оставь ".")
source.dir = .

# Основные файлы (главный файл .py)
source.include_exts = py, png, jpg, kv, mp4
source.exclude_exts = spec

# Основные зависимости (Kivy + библиотека для записи экрана)
requirements = python3, kivy, ffpyplayer, android

# Версия Python
python_version = 3

# Полноэкранный режим и ориентация экрана
fullscreen = 1
orientation = portrait

# Иконка приложения (замени на свою)
icon.filename = icon.png

[buildozer]
log_level = 2

[android]
# Версия API (31 = Android 12, можно поменять)
android.api = 31
android.minapi = 21

# Версия NDK (попробуй 23b, если есть проблемы, поменяй на 21)
android.ndk = 23b

# Поддерживаемые архитектуры (если нужна совместимость со старыми устройствами, добавь armeabi-v7a)
android.arch = arm64-v8a

# Разрешения для записи экрана и сохранения файлов
android.permissions = RECORD_AUDIO, SYSTEM_ALERT_WINDOW, INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, FOREGROUND_SERVICE, MEDIA_CONTENT_CONTROL

# Включение OpenGL ES 2.0 (некоторые устройства требуют ES 3.0)
android.opengl_es = 2
android.allow_cleartext = True
android.release = False
android.add_libs_armeabi-v7a = False
android.add_libs_arm64-v8a = False

# Указываем главный `.py` файл (замени "main.py", если другой)
source.entrypoint = main.py
