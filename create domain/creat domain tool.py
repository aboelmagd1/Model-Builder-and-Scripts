import arcpy

#inpute gdb 
gdb = arcpy.GetParameterAsText(0)
arcpy.env.overwriteOutput = True

#inpute  table or feature class
table=arcpy.GetParameterAsText(1)
arcpy.env.overwriteOutput = True

#TheField that you need to make it Domain
TheField = arcpy.GetParameterAsText(2)

#name of domain
domainName = arcpy.GetParameterAsText(3)

# new field to AssignDomain
field_name = arcpy.GetParameterAsText(4)

# type of field
field_domain_type = arcpy.GetParameterAsText(5)

# Create a search cursor based on the shapefile
TheRows=arcpy.SearchCursor(table)
allValues = []

# Loops through each of row to get all values
arcpy.AddMessage("getting all Values...")
for TheRow in TheRows:     
		TheValue=TheRow.getValue(TheField)
		allValues.append(TheValue)
print(allValues)


#get uniqueValues
arcpy.AddMessage("getting uniqueValues...")
uniqueValues = list(set(allValues))
print("you have {allValues} record... \ncount of uniqueValues is {count} record....".format(allValues = len(allValues) , count = len(uniqueValues)))
arcpy.AddMessage("you have {allValues} record... \ncount of uniqueValues is {count} record....".format(allValues = len(allValues) , count = len(uniqueValues)))

"""
for other way
"""
# df = pd.DataFrame(uniqueValues)
# Customize the export settings
# custom_header = ['des']
# Export the DataFrame to an Excel file	
# df.to_excel('output.xlsx', index=True, na_rep='N/A', header= custom_header, index_label='code')
# arcpy.management.TableToDomain(r"output.xlsx\Sheet1$", "code", "des", r"C:\Users\ibrah\OneDrive\?????????\ArcGIS\Projects\New File Geodatabase.gdb", domainName, "APPEND")

# _____________

#create domain
arcpy.AddMessage("creating domain...")
try:
	arcpy.management.CreateDomain(gdb , domainName , "des", field_domain_type, "CODED")
except:
		print("An exception occurred CreateDomain")
		arcpy.AddMessage("you have same name of domain ,it is {domainName}".format(domainName = domainName))
		try:
        		arcpy.management.DeleteDomain(gdb, domainName)
        		arcpy.AddMessage("you are deleted old domain  {domainName} and created a new one ".format(domainName = domainName))
        		arcpy.management.CreateDomain(gdb , domainName, "des", field_domain_type, "CODED")
		except:
				print( "not pass")
				arcpy.AddMessage("you must closed any feature use the {domainName} domain if you want delet".format(domainName = domainName))
#add code and descraption 
for code , des in enumerate (uniqueValues) :
    print(code)        
    print(des)        
    arcpy.management.AddCodedValueToDomain(gdb, domainName , code , des )

print("_"*100)

# creat new field
arcpy.AddMessage("add field...")
allfields =  [fld.name for fld in arcpy.ListFields(table)]

try:
    arcpy.management.AddField(table , field_name, field_domain_type)
    arcpy.AddMessage(">>>>>> Added new field <<<<<<")
except:
    print("An exception occurred AddField")
    arcpy.AddMessage("An exception occurred AddField")
    try:
        print("AddField")
        arcpy.management.DeleteField(table, field_name)
        arcpy.AddMessage("deleted old feild and Added new Field")
        arcpy.management.AddField(table, field_name , field_domain_type)
    except:
        print("not pass")
        arcpy.AddMessage("i cant add new field")


# AssignDomainToField
try:
	arcpy.management.AssignDomainToField(table , field_name , domainName)
except:
    print("An exception occurred AssignDomainToField")
    arcpy.AddMessage("An exception occurred AssignDomainToField")


# add attributes domain to new field 
arcpy.AddMessage("updating Attributs in new field...")
for code , des in enumerate (uniqueValues) :
    expression = "{} = '{}'".format(TheField , des )
    select = arcpy.management.SelectLayerByAttribute(table,"NEW_SELECTION", expression , None)
    arcpy.management.CalculateField(select, field_name, code , "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")

print("_"*50 + "done" + "_"*50)
arcpy.AddMessage("_"*20 + "done" + "_"*20)
