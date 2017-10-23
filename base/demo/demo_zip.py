import demo_os
import os
import zipfile

if not os.path.exists(os.getcwd()+os.path.sep+'zipFolder'):
    os.makedirs(os.getcwd() + os.path.sep + 'zipFolder')   #mkdir
    # os.rmdir(os.getcwd()+os.path.sep+'ostestfolder')         #rmdir



demo_os.touch(os.getcwd() + os.path.sep + 'zipFolder' + os.path.sep + "zippedFile.txt", '123asd')

if not os.path.exists(os.getcwd() + os.path.sep + 'zipFolder'+os.path.sep+"zippedFile.zip"):
    newZip = zipfile.ZipFile(os.getcwd() + os.path.sep + 'zipFolder'+os.path.sep+"zippedFile.zip", 'w')
    newZip.write(os.getcwd() + os.path.sep + 'zipFolder'+os.path.sep+"zippedFile.txt", compress_type=zipfile.ZIP_DEFLATED)
    newZip.close()



