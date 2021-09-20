# file mover application using python
# import OS module
import os
# import shutil module
import  shutil



# source path
sourcePath = r"C:\Users\rajit\OneDrive\Pictures\iCloud Photos\Downloads"

# destination path
destinationDir = 'D:\Gallery\Pictures\Backup'

#import datetime
from datetime import datetime
now = datetime.now()
date_time = now.strftime("%Y-%m-%d")
print("date and time:",date_time)


print(date_time)

destinationPath = os.path.join(destinationDir, date_time)

print(destinationPath)

#destinationPath = destinationDir + "\" + today

# list down all the files in the source directory
print("-- list down all the files in " + sourcePath)
print(os.listdir(sourcePath))


shutil.move(sourcePath, destinationPath)