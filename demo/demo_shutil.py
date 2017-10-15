import shutil, os
if not os.path.exists(os.getcwd()+os.path.sep+'shutilFolder'):
    os.makedirs(os.getcwd() + os.path.sep + 'shutilFolder')   #mkdir
    # os.rmdir(os.getcwd()+os.path.sep+'ostestfolder')         #rmdir



if not os.path.exists(os.getcwd()+os.path.sep+'shutilFolder'+os.path.sep+"new1.txt"):
    new1 = open(os.getcwd()+os.path.sep+'shutilFolder'+os.path.sep+"new1.txt",'w')
    new1.close()
if not os.path.exists(os.getcwd()+os.path.sep+'shutilFolder'+os.path.sep+"new2.txt"):
    new2 = open(os.getcwd()+os.path.sep+'shutilFolder'+os.path.sep+"new2.txt",'w')
    new2.close()

# if not os.path.exists(os.getcwd()+os.path.sep+'shutilFolder'+os.path.sep+'shutilSubFolder'):
#     os.makedirs(os.getcwd()+os.path.sep+'shutilFolder'+os.path.sep+'shutilSubFolder')  # mkdir

shutil.copytree(os.getcwd()+os.path.sep+'shutilFolder',os.getcwd()+os.path.sep+'shutilFolder'+os.path.sep+'shutilSubFolder')
for filename in os.listdir('.'):
    print(filename + "===>" + str(os.path.getsize(filename)) + "===>" + str(os.path.getctime(filename)))
print('-----------------------------------------------')
shutil.move(os.getcwd()+os.path.sep+'shutilFolder'+os.path.sep+'shutilSubFolder',os.getcwd()+os.path.sep+'shutilFolder'+os.path.sep+'shutilSubFolder2')
for filename in os.listdir('.'):
    print(filename + "===>" + str(os.path.getsize(filename)) + "===>" + str(os.path.getctime(filename)))


shutil.rmtree(os.getcwd()+os.path.sep+'shutilFolder')
