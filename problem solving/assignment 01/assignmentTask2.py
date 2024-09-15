# -*- coding: utf-8 -*-
import arcpy , os
#inputs...
arcpy.env.workspace = "C:\\Users\\ibrah\\Downloads\\Compressed\qc\\split test.gdb\\split test.gdb" 
featureclass = "Land_Parcels_38"

listOfFields = arcpy.ListFields(featureclass)
#list for names of fields ....
listOfFieldsN = [listOfFieldsN.name for listOfFieldsN in listOfFields ]
text = []
FNIN = []
#select null in each field
for nameF in listOfFieldsN :
    expression = "{nameF} IS {null}".format(nameF=nameF , null = "NULL" )
    selectnull = arcpy.management.SelectLayerByAttribute(featureclass,"NEW_SELECTION", expression , None)
    countSelectnull = arcpy.management.GetCount(selectnull)
    if int(countSelectnull.getOutput(0)) != 0 :
        FNIN.append(nameF)
        # print("the field {nameF} have {countSelectnull} record NULL".format(nameF=nameF , countSelectnull=countSelectnull))
        text.append("the field: '{nameF}' Have {countSelectnull} record NULL.\n".format(nameF=nameF , countSelectnull=countSelectnull))
#creat report.....
with open("re1.txt" , "w") as re :
    re.write(f"Totale of fields have NULL is {len(text)} fields and They are {FNIN}.\n")
    for WT in text :
        re.write(WT)
    re.close
os.startfile("re1.txt")