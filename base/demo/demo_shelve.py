import os
import shelve
if not os.path.exists(os.getcwd()+os.path.sep+'shelveFolder'):
    os.makedirs(os.getcwd() + os.path.sep + 'shelveFolder')   #mkdir
    # os.rmdir(os.getcwd()+os.path.sep+'ostestfolder')         #rmdir

os.chdir(os.getcwd()+os.path.sep+'shelveFolder')


shelfile = shelve.open("myData")
cats = ['ketty', 'Jerry']
shelfile['cats'] = cats
shelfile.close()


shelfile = shelve.open("myData")
print(str(type(shelfile)))
print(str(shelfile['cats']))
shelfile.close()