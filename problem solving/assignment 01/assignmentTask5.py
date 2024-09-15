# -*- coding: utf-8 -*-
import arcpy , os
arcpy.env.overwriteOutput = True
gdb = r"D:\LPAD\Projects\FramworkProject\FramworkProject.gdb"
fc = r"D:\LPAD\Data\GDB\aa0.gdb\Countries"
outputName = "point1"
feild = "NAME"
value = "Indonesia"
select = arcpy.management.SelectLayerByAttribute(fc, "NEW_SELECTION", "{} = '{}'".format(feild,value), None)
arcpy.management.CreateRandomPoints(gdb, 
                                    outputName, select,"",
                                    300, "500 Meters", "POINT", 2)