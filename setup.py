import cx_Freeze
import sys
import os 
base = None
if sys.platform == 'win32':
    base = "Win32GUI"
os.environ['TCL_LIBRARY'] = r"E:\Users\Abhimanyu\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"E:\Users\Abhimanyu\AppData\Local\Programs\Python\Python39\tcl\tk8.6"
executables = [cx_Freeze.Executable("qrcode_reader_writer.py", base=base, icon="icon.ico")]
cx_Freeze.setup(
    name = "QR Code Reader/Writer By Abhimanyu Sharma",
    options = {"build_exe": {"packages":["tkinter","os","qrcode","cv2"], "include_files":["icon.ico","tcl86t.dll","tk86t.dll"]}},
    version = "0.01",
    author="Abhimanyu Sharma",
    description = "Create/Read QR Codes With Ease !",
    executables = executables
    )
