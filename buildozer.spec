[app]

# Название приложения
title = QR Pass

# Имя пакета (английскими буквами)
package.name = qrpass
package.domain = org.example

# Версия
version = 1.0.0

# Главный файл
source.dir = .
source.include_exts = py,png,kv,atlas

# Библиотеки Python
requirements = python3,kivy,kivymd,requests,qrcode,pillow

# Ориентация
orientation = portrait

# Фуллскрин (0 = нет, 1 = да)
fullscreen = 0

# Минимальный и целевой API
android.api = 34
android.minapi = 21
android.build_tools_version = 34.0.0

# Разрешения
android.permissions = INTERNET

# Иконка (можешь заменить на свою картинку)
# icon.filename = %(source.dir)s/data/icon.png


[buildozer]

# Лог в консоли
log_level = 2

# Папка для сборки
build_dir = ./.buildozer

# Автоматическая компиляция requirements
warn_on_root = 1
