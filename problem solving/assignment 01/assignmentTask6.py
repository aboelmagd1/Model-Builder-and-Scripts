# -*- coding: utf-8 -*-
import arcpy
input_fc = r"D:\LPAD\Data\GDB\aa0.gdb\Countries"
cursor = arcpy.da.SearchCursor(input_fc, [ "NAME","SHAPE@XY"])
centroid_coords = []
for feature in cursor:
    print("'{}' x={} , y={}".format(feature[0],feature[1][0],feature[1][1]))