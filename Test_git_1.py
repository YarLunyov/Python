import platform
import sys

# TODO тестовое сообщение

info = f'OS info is \n{platform.uname()} \n\n Python version is {sys.version}{platform.architecture()}'
print(info)
