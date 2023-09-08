import arcpy, os

MAP = arcpy.GetParameterAsText(0)

mxd = arcpy.mapping.MapDocument(MAP)
JPGE = (str(MAP))
arcpy.mapping.ExportToJPEG(mxd,JPGE.replace ('.mxd',''),resolution = 300)

del mxd
