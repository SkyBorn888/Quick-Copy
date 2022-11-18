import pyside6_main_window
from libs.check_json_module import check_json_module
import sys
import time
import os
import sys


try:
    run = pyside6_main_window 
    check = check_json_module()
    
    check.main()
    run.main()
except KeyboardInterrupt:
    sys.exit()

