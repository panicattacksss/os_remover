# main.py

from os_remover.os_selector import choose_os
from os_remover.mode_selector import choose_mode
from os_remover.linux import linux_delete
from os_remover.windows import windows_delete
from os_remover.macos import macos_delete

def main():
    os_choice = choose_os()
    mode_choice = choose_mode()
    if os_choice == "windows":
        windows_delete(mode_choice)
    elif os_choice == "linux":
        linux_delete(mode_choice)
    elif os_choice == "macos":
        macos_delete(mode_choice)

if __name__ == "__main__":
    main()
