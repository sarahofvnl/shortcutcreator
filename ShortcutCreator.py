import os
import sys
import winshell
from win32com.client import Dispatch

def create_shortcut(target, shortcut_name, description="", working_dir=None):
    """
    Creates a desktop shortcut.

    Parameters:
    - target: The path to the file or URL for which the shortcut is to be created.
    - shortcut_name: The name of the shortcut to be created.
    - description: A brief description of the shortcut.
    - working_dir: The working directory for the shortcut.
    """
    desktop = winshell.desktop()
    path = os.path.join(desktop, f"{shortcut_name}.lnk")
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = working_dir if working_dir else os.path.dirname(target)
    shortcut.Description = description
    shortcut.save()

def main():
    print("Shortcut Creator")
    target = input("Enter the file path or URL for the shortcut: ")
    shortcut_name = input("Enter the name for the shortcut: ")
    description = input("Enter a description for the shortcut (optional): ")
    working_dir = input("Enter the working directory (optional): ")

    try:
        create_shortcut(target, shortcut_name, description, working_dir)
        print(f"Shortcut '{shortcut_name}' created successfully on your desktop.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()