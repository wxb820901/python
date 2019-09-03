if __name__=='__main__':
    import csv
    import json
    import os
    import sys
    import json
    import datetime
    import time

    dictValue = {}
    dictEffectiveFrom = {}
    dictEffectiveTo = {}
    dictSystemFrom = {}
    dictSystemTo = {}

    dictRest = {}
    dictRest["data"] = {}

    def readJson(filePath):
        jsonInputFile = open(filePath)
        jsonContent = jsonInputFile.read()
        jsonInputFile.close()
        return jsonContent


    def gekeyName(keyAndVal):
        key_length = len(keyAndVal.split("::"))
        return keyAndVal.split("::")[key_length-1].replace('_L2', '')


    def convertStirngToDate(date_time_str):
        date_time_obj = datetime.datetime.strptime(date_time_str.replace('T', ' ')[:19], '%Y-%m-%d %H:%M:%S')
        return date_time_obj.timetuple()


    def compareStringDate(datetime1, datetime2):
        if datetime1 == 'null' or datetime2 == 'null':
            return False
        return convertStirngToDate(datetime1) > convertStirngToDate(datetime2)

    def fireLeaf(currentElement, keyPlus, CoreInstrumentClass_L2_effectiveFrom, CoreInstrumentClass_L2_effectiveTo, CoreInstrumentClass_L2_systemFrom, CoreInstrumentClass_L2_systemTo):
        print("||||||"+keyPlus+"||||||"+str(currentElement)+"||||||"+CoreInstrumentClass_L2_effectiveFrom+"||||||"+CoreInstrumentClass_L2_effectiveTo+"||||||"+CoreInstrumentClass_L2_systemFrom+"||||||"+CoreInstrumentClass_L2_systemTo)
        if not isExistValue(dictRest, gekeyName(keyPlus)):#new key
            dictRestValues = []
            dictRestValues.append(buildValueBiTempol(str(currentElement), CoreInstrumentClass_L2_effectiveFrom, CoreInstrumentClass_L2_effectiveTo, CoreInstrumentClass_L2_systemFrom, CoreInstrumentClass_L2_systemTo))
            dictRest["data"][gekeyName(keyPlus)] = dictRestValues
        else:#existing key
            isNewValue = True
            valueIndex = -1;
            dictRestValues = dictRest["data"][gekeyName(keyPlus)]
            for dictRestValue in dictRestValues:
                valueIndex+=1
                if dictRestValue['value'] == str(currentElement):
                    isNewValue = False#existing value
                    break;

            if isNewValue:
                dictRest["data"][gekeyName(keyPlus)].append(buildValueBiTempol(str(currentElement), CoreInstrumentClass_L2_effectiveFrom, CoreInstrumentClass_L2_effectiveTo, CoreInstrumentClass_L2_systemFrom, CoreInstrumentClass_L2_systemTo))
            else:#existing value
                if compareStringDate(CoreInstrumentClass_L2_effectiveFrom, dictRestValues[valueIndex]['temporalState']['effectiveFrom']):
                    dictRestValues[valueIndex]['temporalState']['effectiveFrom'] = CoreInstrumentClass_L2_effectiveFrom
                if compareStringDate(CoreInstrumentClass_L2_effectiveTo, dictRestValues[valueIndex]['temporalState']['effectiveTo']):
                    dictRestValues[valueIndex]['temporalState']['effectiveTo'] = CoreInstrumentClass_L2_effectiveTo
                if compareStringDate(CoreInstrumentClass_L2_systemFrom, dictRestValues[valueIndex]['temporalState']['systemFrom']):
                    dictRestValues[valueIndex]['temporalState']['systemFrom'] = CoreInstrumentClass_L2_systemFrom
                if compareStringDate(CoreInstrumentClass_L2_systemTo, dictRestValues[valueIndex]['temporalState']['systemTo']):
                    dictRestValues[valueIndex]['temporalState']['systemTo'] = CoreInstrumentClass_L2_systemTo



    def untilLeaf(currentElement, keyPlus, CoreInstrumentClass_L2_effectiveFrom, CoreInstrumentClass_L2_effectiveTo, CoreInstrumentClass_L2_systemFrom, CoreInstrumentClass_L2_systemTo):
        if isinstance(currentElement, str):
            fireLeaf(currentElement, keyPlus, CoreInstrumentClass_L2_effectiveFrom, CoreInstrumentClass_L2_effectiveTo, CoreInstrumentClass_L2_systemFrom, CoreInstrumentClass_L2_systemTo)
        elif isinstance(currentElement, dict):
            for nextkey in currentElement.keys():#different par from below list
                if isinstance(currentElement[nextkey], str):
                    fireLeaf(currentElement[nextkey], keyPlus+"::"+nextkey, CoreInstrumentClass_L2_effectiveFrom, CoreInstrumentClass_L2_effectiveTo, CoreInstrumentClass_L2_systemFrom, CoreInstrumentClass_L2_systemTo)
                if isinstance(currentElement[nextkey], dict) or isinstance(currentElement[nextkey], list):
                    untilLeaf(currentElement[nextkey], keyPlus+"::"+nextkey, CoreInstrumentClass_L2_effectiveFrom, CoreInstrumentClass_L2_effectiveTo, CoreInstrumentClass_L2_systemFrom, CoreInstrumentClass_L2_systemTo)
        elif isinstance(currentElement, list):
            for nextLayer in currentElement:#different par from above dict
                if isinstance(nextLayer, dict):
                    untilLeaf(nextLayer, keyPlus+"::array", CoreInstrumentClass_L2_effectiveFrom, CoreInstrumentClass_L2_effectiveTo, CoreInstrumentClass_L2_systemFrom, CoreInstrumentClass_L2_systemTo)
                    #without [][*], []['']

    def heapLeafAndFire(filePath):
        CoreInstrumentClass_L2_str = readJson(filePath)
        CoreInstrumentClass_L2_json = json.loads(CoreInstrumentClass_L2_str)
        for CoreInstrumentClass_L2 in CoreInstrumentClass_L2_json:
            untilLeaf(CoreInstrumentClass_L2['CoreInstrumentClass_L2'], 'CoreInstrumentClass_L2', str(getEffectiveFrom(CoreInstrumentClass_L2)), str(getEffectiveTo(CoreInstrumentClass_L2)), str(getSystemFrom(CoreInstrumentClass_L2)), str(getSystemTo(CoreInstrumentClass_L2)))

    def getEffectiveFrom(item):
        return item['effectiveFrom']

    def getEffectiveTo(item):
        return item['effectiveTo']

    def getSystemFrom(item):
        return item['systemFrom']

    def getSystemTo(item):
        return item['systemTo']


    def buildValueBiTempol(value, effectiveFrom, dictEffectiveTo, systemFrom, systemTo):
        dictRestValue = {}
        dictRestValue["temporalState"] = {}
        dictRestValue["temporalState"]["effectiveFrom"] = effectiveFrom
        dictRestValue["temporalState"]["effectiveTo"] = dictEffectiveTo
        dictRestValue["temporalState"]["systemFrom"] = systemFrom
        dictRestValue["temporalState"]["systemTo"] = systemTo
        dictRestValue["value"] = value
        return dictRestValue

    # def getResultLayers():
    #     instruJson = json.loads(jsonContent)
    #     for itemDict in instruJson:
    #         item = itemDict['CoreInstrumentClass_L2']
    #         for key in item.keys():
    #             if isLayer1(item, key):
    #                 parseLayer1(item, key)
    #             elif isLayer2(item, key):
    #                 parseLayer2(item, key)
    #             else :
    #                 parseLayer4(item, key)



    def isExistValue(curentRest, key):
        if key in curentRest["data"]:
            return True
        return False





    heapLeafAndFire(sys.argv[1])
    print(dictRest)






