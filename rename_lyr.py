# -*- coding: utf-8 -*-
# Import arcpy module

import arcpy, os
arcpy.env.overwriteOutput = True

LYR = arcpy.GetParameterAsText(0)
dsc= arcpy.Describe(LYR)


arcpy.Rename_management(LYR, ("ly_"+ str(dsc.name)))