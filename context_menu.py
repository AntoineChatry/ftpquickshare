import os
import sys
import winreg as reg

# Get path of current working directory and python.exe
cwd = os.getcwd()
python_exe = sys.executable

# optional hide python terminal in windows
hidden_terminal = "\\".join(python_exe.split("\\")[:-1]) + "\\pythonw.exe"

# Set the paths of the context menu (right-click menu)
key_paths = [
    r"*\shell\SendToNAS",
    r"Directory\shell\SendToFTP",
    r"CompressedFolder\shell\SendToFTP",
]

for key_path in key_paths:
    try:
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path + r"\command")
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path)
    except FileNotFoundError:
        pass

    # Create outer key
    key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
    reg.SetValue(key, "", reg.REG_SZ, "&Send to FTP")

    # create inner key
    key1 = reg.CreateKey(key, r"command")
    reg.SetValue(
        key1,
        "",
        reg.REG_SZ,
        r'yourpythonpath main.pypath "%1"',
    )
