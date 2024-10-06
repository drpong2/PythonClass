import os
import sys
path=os.path.dirname(sys.executable)
print(path)

print("This is the run script: ")
print(path + '\python.exe -i "$(FULL_CURRENT_PATH)"')

#C:\Users\steve\AppData\Local\Programs\Python\Python312\python.exe -i "$(FULL_CURRENT_PATH)"
#C:\Users\steve\AppData\Local\Programs\Python\Python312 -i "$(FULL_CURRENT_PATH)"