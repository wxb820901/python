import csv,  os, demo_os, json


if not os.path.exists(os.getcwd()+os.path.sep+'csvjsonfolder'):
    os.makedirs(os.getcwd() + os.path.sep + 'csvjsonfolder')   #mkdir


if not os.path.exists(os.getcwd()+os.path.sep+"csvjsonfolder"+os.path.sep+"csv.txt"):
    demo_os.touch(os.getcwd()+os.path.sep+"csvjsonfolder"+os.path.sep+"csv.txt",
                  "1,2,3\n4,5,6\n7,8,9")


def getCsvContent(filePath):
    csvContent = open(filePath)
    csvReader = csv.reader(csvContent)
    csvData = list(csvReader)
    csvContent.close()
    return csvData


print(str(getCsvContent(os.getcwd() + os.path.sep + "csvjsonfolder" + os.path.sep + "csv.txt")))
print("------------------------------")

def writeCsvContent(filePath, content):
    csvContent = open(filePath, 'w')
    csvWriter = csv.writer(csvContent)
    for i in range(len(content)):
        csvWriter.writerow(content[i])
    csvContent.close()


writeCsvContent(os.getcwd() + os.path.sep + "csvjsonfolder" + os.path.sep + "csv.txt", [['a','b','c'],['a','b','c']])
print(str(getCsvContent(os.getcwd() + os.path.sep + "csvjsonfolder" + os.path.sep + "csv.txt")))
print("------------------------------")

#content = ['a','b','c']
jsonstr='{"name":"bill","gender":"male","age":"35"}'
jsonData = json.loads(jsonstr)#string to dictionary
print(str(jsonData))
print(json.dumps(jsonData))#dictionary to string