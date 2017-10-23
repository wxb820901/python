import os
# orginPath = os.getcwd()  #pwd
# print(orginPath)
# os.chdir("C:\\")        #cd
# print(os.getcwd())
# os.chdir(orginPath)
# print(os.getcwd())
# print('-----------------------------------------------')
# if not os.path.exists(os.getcwd()+os.path.sep+'ostestfolder'):
#     os.makedirs(os.getcwd() + os.path.sep + 'ostestfolder')   #mkdir
#     # os.rmdir(os.getcwd()+os.path.sep+'ostestfolder')         #rmdir
#
#
# for filename in os.listdir('.'):
#     print(filename + "===>" + str(os.path.getsize(filename)) + "===>" + str(os.path.getctime(filename)))
#
#
# if os.path.exists(os.getcwd()+os.path.sep+'ostestfolder'+os.path.sep+'nf.txt'):
#     os.remove(os.getcwd()+os.path.sep+'ostestfolder'+os.path.sep+'nf.txt')     #rm
#
# if os.path.exists(os.getcwd()+os.path.sep+'ostestfolder') : # 123abc > nf.txt
#     os.chdir(os.getcwd()+os.path.sep+'ostestfolder')
#     newFile = open('nf.txt','w')
#     newFile.write('123abc')
#     newFile.close();
#
# oldFile = open('nf.txt')
# print(oldFile.read())
# oldFile.close()
#
# os.chdir(orginPath)

def touch(filename, content = 'null'):
    newFile = open(str(filename), 'w')
    newFile.write(str(content))
    newFile.close();
