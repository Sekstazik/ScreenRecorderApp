[app]
# Название приложения
title = Screen Recorder

# Уникальное имя пакета (замени "yourname" на свой ID)
package.name = screenrecorder
package.domain = org.yourname

# Версия приложения
version = 1.0
package.version = 1.0

# Основные файлы (главный файл .py)
source.include_exts = py, png, jpg, kv, mp4
source.exclude_exts = spec

# Основные зависимости (Kivy + библиотека для записи экрана)
requirements = python3, kivy, ffpyplayer, android

# Python версии
python_version = 3

# Язык интерфейса
fullscreen = 1
orientation = portrait

# Включаем иконку (замени на свою)
icon.filename = icon.png

[buildozer]
log_level = 2

[android]
# Версия API (31 = Android 12)
android.api = 31
android.minapi = 21

# Версия NDK (иногда требуется изменить)
android.ndk = 23b

# Поддерживаемая архитектура
android.arch = arm64-v8a

# Разрешения для записи экрана
android.permissions = RECORD_AUDIO, SYSTEM_ALERT_WINDOW, INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, FOREGROUND_SERVICE

# Используем OpenGL ES 2.0 для графики
android.opengl_es = 2
