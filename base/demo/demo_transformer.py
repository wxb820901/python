if __name__=='__main__':
    import csv
    import json
    import os
    import sys
    import json
    import datetime
    import time

    def readJson(filePath):
        jsonInputFile = open(filePath)
        jsonCOntent = jsonInputFile.read()
        jsonInputFile.close()
        return jsonCOntent

    def convertStirngToDate(date_time_str):
        date_time_obj = datetime.datetime.strptime(date_time_str.replace('T', ' ').replace('+0000', ''), '%Y-%m-%d %H:%M:%S')
        return date_time_obj.timetuple()

    def compareStringDate(datetime1, datetime2):
        return convertStirngToDate(datetime1) > convertStirngToDate(datetime2)

    def getEffectiveFrom(element):
        return element['effectiveFrom']

    def getEffectiveTo(element):
        return element['effectiveTo']

    def getDictFormJson(jsonContent):
        # jsonStructure = json.loads("{\"body\"="+jsonContent+"}")v
        instruJson = json.loads(jsonContent)
        dictValue = {}
        dictEffectiveFrom = {}
        dictEffectiveTo = {}
        for itemDict in instruJson:
            item = itemDict['CoreInstrumentClass_L2']
            for key in item.keys():

                if isinstance(dictValue[key], str) and not isNotCaredField(key) and not item[key] == "null":
                    keyAndVal = key+"::"+ item[key]
                    if keyAndVal not in dictValue.keys():
                        dictValue[keyAndVal] = item[key]
                        dictEffectiveFrom[keyAndVal] = getEffectiveFrom(itemDict)
                        dictEffectiveTo[keyAndVal] = getEffectiveTo(itemDict)
                    else:
                        if compareStringDate(dictEffectiveFrom[keyAndVal], getEffectiveFrom(itemDict)):
                            dictEffectiveFrom[keyAndVal] = getEffectiveFrom(itemDict)
                        if not compareStringDate(dictEffectiveTo[keyAndVal], getEffectiveFrom(itemDict)):
                            dictEffectiveFrom[keyAndVal] = getEffectiveFrom(itemDict)
                elif isinstance(dictValue[key], dict):
                    '''
                    'classifications_L2':{  #===============================> dictValue[key]
                    'ActiveStatusClass_L2':{   #===============================> dictValue[key]
                    '''
                    for subElement in dictValue[key].keys():
                        if isinstance(dictValue[key][subElement], list):
                            """
                                                "classifications_L2":{  
                                                   "ClassificationClass_L2":[ #=========================>dictValue[key].keys()===>subElement
                                                      {  
                                                         "classification_L2":"1002662342",  #===========>subItemKey:subItem[subItemKey]
                                                         "classificationType_L2":"classification_1" #===>
                                                      }
                                                   ]
                                                },
                                                """
                            for subItem in subElement:
                                for subItemKey in subItem.keys:
                                    keyAndVal = key + "::"+subElement+"::"+subItemKey+"::"+subItem[subItemKey]
                                    print(keyAndVal)
                                    if keyAndVal not in dictValue.keys():
                                        dictValue[keyAndVal] = subItem[subItemKey]
                                        dictEffectiveFrom[keyAndVal] = getEffectiveFrom(itemDict)
                                        dictEffectiveTo[keyAndVal] = getEffectiveTo(itemDict)
                                    else:
                                        if compareStringDate(dictEffectiveFrom[keyAndVal], getEffectiveFrom(itemDict)):
                                            dictEffectiveFrom[keyAndVal] = getEffectiveFrom(itemDict)
                                        if not compareStringDate(dictEffectiveTo[keyAndVal], getEffectiveFrom(itemDict)):
                                            dictEffectiveFrom[keyAndVal] = getEffectiveFrom(itemDict)
                        elif isinstance(dictValue[key][subElement], str):
                            """
                                             "ActiveStatusClass_L2":{  
                                                   "status_L2":"Deactive",#=========================>dictValue[key].keys()===>subElement
                                                   "reason_L2":"Merged"
                                                },
                                               """

                            keyAndVal = key + "::" + subElement + "::" + dictValue[key][subElement]
                            print(keyAndVal)
                            if keyAndVal not in dictValue.keys():
                                dictValue[keyAndVal] = dictValue[key][subElement]
                                dictEffectiveFrom[keyAndVal] = getEffectiveFrom(itemDict)
                                dictEffectiveTo[keyAndVal] = getEffectiveTo(itemDict)
                            else:
                                if compareStringDate(dictEffectiveFrom[keyAndVal], getEffectiveFrom(itemDict)):
                                    dictEffectiveFrom[keyAndVal] = getEffectiveFrom(itemDict)
                                if not compareStringDate(dictEffectiveTo[keyAndVal], getEffectiveFrom(itemDict)):
                                    dictEffectiveFrom[keyAndVal] = getEffectiveFrom(itemDict)





        buildResult(dictValue, dictEffectiveFrom, dictEffectiveTo)


    def buildResult(dictValue, dictEffectiveFrom, dictEffectiveTo):
        dictRest = {}
        dictRest["data"] = {}
        for key in dictValue.keys():
            print("===>" + str(type(dictValue[key]))+"==>"+str(isinstance(dictValue[key], str)))
            if isinstance(dictValue[key], str):
                if not isExistValue(dictRest, gekeyName(key)):
                    dictRestValues = []
                    dictRestValues.append(buildValueBiTempol(key, dictValue, dictEffectiveFrom, dictEffectiveTo))
                    dictRest["data"][gekeyName(key)] = dictRestValues
                else:
                    dictRestValues = dictRest["data"][gekeyName(key)]
                    dictRestValues.append(buildValueBiTempol(key, dictValue, dictEffectiveFrom, dictEffectiveTo))
            elif isinstance(dictValue[key], dist):
                if not isExistValue(dictRest, gekeyName(key)):
                    dictRestValues = []
                    dictRestValues.append(buildValueBiTempol(key, dictValue, dictEffectiveFrom, dictEffectiveTo))
                    dictRest["data"][gekeyName(key)] = dictRestValues
                else:
                    dictRestValues = dictRest["data"][gekeyName(key)]
                    dictRestValues.append(buildValueBiTempol(key, dictValue, dictEffectiveFrom, dictEffectiveTo))


        print(dictRest)

    def buildValueBiTempol(key, dictValue, dictEffectiveFrom, dictEffectiveTo):
        dictRestValue = {}
        dictRestValue["temporalState"] = {}
        dictRestValue["temporalState"]["effectiveFrom"] = dictEffectiveFrom[key]
        dictRestValue["temporalState"]["effectiveTo"] = dictEffectiveTo[key]
        dictRestValue["value"] = dictValue[key]
        return dictRestValue

    def isExistValue(curentRest, key):
        if key in curentRest["data"]:
            return True
        return False

    def gekeyName(keyAndVal):
        return keyAndVal.split("::")[0].replace('_L2', '')

    def isNotCaredField(fieldName):
        return "effectiveFrom" in fieldName or "effectiveTo" in fieldName or "systemFrom" in fieldName or "systemTo" in fieldName



    getDictFormJson(readJson(sys.argv[1]))