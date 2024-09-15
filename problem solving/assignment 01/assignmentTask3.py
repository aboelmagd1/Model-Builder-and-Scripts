import os , arcpy
arcpy.env.overwriteOutput = True
mainFc = "D:\\LPAD\\Data\\GDB"
fc="D:\\LPAD\\Data\\GDB\\a1.gdb"
fileGDB = arcpy.CreateFileGDB_management(mainFc,"backup")
arcpy.env.workspace = fc
dateSet = arcpy.ListDatasets()
path = []
namedataset=[]
outputeTextlist = []
outputeText = "report.txt"
try:
    if dateSet:
        allFeatures = arcpy.ListFeatureClasses("*p*")
        for n in allFeatures :
            # path.append("{0}\\{1}".format(fc,n))
            in_features = "{0}\\{1}".format(fc,n)
            out_feature_class = "{0}\\{1}".format(fileGDB,n)
            typeF = arcpy.Describe(in_features).shapeType
            referenceF = arcpy.Describe(in_features).spatialReference.Name
            outputeTextlist.append("the featureclass name is: {n} , type is: {typeF} , spatialReference is: {referenceF} , backup path is: {out_feature_class}\n".format(n=n,typeF=typeF,referenceF=referenceF,out_feature_class=out_feature_class))
            # print(in_features)
            # print(out_feature_class)
            arcpy.analysis.Select(in_features, out_feature_class)
        for nameSet in dateSet:
            fcDetaSet = "{0}\\{1}".format(fc,nameSet)
            arcpy.env.workspace = fcDetaSet
            for nameInDetaset in arcpy.ListFeatureClasses("*p*"):
                # allFeatures.append("{0}_{1}".format(nameSet,nameInDetaset))
                # path.append("{0}\\{1}\\{2}".format(fc,nameSet,nameInDetaset))
                in_features = "{0}\\{1}\\{2}".format(fc,nameSet,nameInDetaset)
                typeF = arcpy.Describe(in_features).shapeType
                referenceF = arcpy.Describe(in_features).spatialReference.Name
                # print(typeF)
                out_feature_class = "{0}\\{1}_{2}".format(fileGDB,nameSet,nameInDetaset)
                # print(in_features)
                # print(out_feature_class)
                outputeTextlist.append("the featureclass name is: {n} , type is: {typeF} , spatialReference is: {referenceF} , backup path is: {out_feature_class}\n".format(n=n,typeF=typeF,referenceF=referenceF,out_feature_class=out_feature_class))  
                arcpy.analysis.Select(in_features, out_feature_class)    
    else:
        allFeatures = arcpy.ListFeatureClasses("*p*")
        for n in allFeatures :
            # path.append("{0}\\{1}".format(fc,n))
            in_features = "{0}\\{1}".format(fc,n)
            out_feature_class = "{0}\\{1}".format(fileGDB,n)
            typeF = arcpy.Describe(in_features).shapeType
            referenceF = arcpy.Describe(in_features).spatialReference.Name
            outputeTextlist.append("the featureclass name is: {n} , type is: {typeF} , spatialReference is: {referenceF} , backup path is: {out_feature_class}\n".format(n=n,typeF=typeF,referenceF=referenceF,out_feature_class=out_feature_class))
            # print(in_features)
            # print(out_feature_class)
            arcpy.analysis.Select(in_features, out_feature_class)
    with open(outputeText ,"w") as wText:
        for t in outputeTextlist:
            wText.write(t)
        wText.write("count of all featurclasses is: {0}".format(len(outputeTextlist)))
        wText.read
        wText.close         
    os.startfile("report.txt")
except:
    with open(outputeText ,"w") as wText:
        wText.write("no featureclasses")
        wText.read
        wText.close
