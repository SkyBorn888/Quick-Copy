import QuickCopy_PyInstaller.pyside6_main_window
from QuickCopy_PyInstaller.libs.check_json_module import check_json_module
import sys
import time
import os
import sys


try:
    run = QuickCopy_PyInstaller.pyside6_main_window 
    check = check_json_module()
    
    check.main()
    run.main()
except KeyboardInterrupt:
    sys.exit()

