# -*- coding: utf-8 -*-
import arcpy , os
arcpy.env.overwriteOutput = True
fc = r"D:\LPAD\Data\GDB\a1.gdb\Countries"
allFields = arcpy.ListFields(fc,"*")
for field in allFields:
    if   field.editable:  
        if field.type == "SmallInteger" or field.type == "BigInteger" or field.type == "Integer" :
            expression = 999
            arcpy.management.CalculateField(fc , field.name ,expression ,"PYTHON3", '', "", "NO_ENFORCE_DOMAINS")
        elif field.type == "String":
            if field.length >= len("String"):
                pass
                # expression = '"String"'
                # arcpy.management.CalculateField(fc , field.name , expression ,"PYTHON3", '', "TEXT", "")
                with arcpy.da.UpdateCursor(fc, field.name) as cursor:
                    for row in cursor:
                        row[0]='String'
                        cursor.updateRow(row)
            else:
                print("we cant write 'string' in field:'{}'becouse leanth of char is {}".format(field.name,field.length))
                    
        elif field.type == "Double" or field.type == "Single":
            expression = 33.33
            arcpy.management.CalculateField(fc , field.name ,expression ,"PYTHON3", '', "", "NO_ENFORCE_DOMAINS")
        elif field.type == "Date":
            expression = '"12/12/2012"'
            print(expression)
            arcpy.management.CalculateField(fc , field.name , expression ,"PYTHON3", '', "", "NO_ENFORCE_DOMAINS")
    else:
        print("""field '{}' is not editable""".format(field.name))

