#INICIO PROGRAMA
import arcpy, os

#Variables
FILEGDB= arcpy.GetParameterAsText (0)
path1 = FILEGDB
arcpy.env.workspace = FILEGDB

a = arcpy.ListFeatureClasses()

for i in a:
    count1 = str(arcpy.GetCount_management(i))
    if count1 == "0":
		dirr = os.path.join (path1,i)
		arcpy.Delete_management(dirr)
		arcpy.AddMessage(str(i))
		del dirr


arcpy.AddMessage("====================================================")
arcpy.AddMessage("=============Proceso finalizado=====================")
arcpy.AddMessage("====================================================")

arcpy.AddMessage("********* Elaborado: FERNANDA SALGADO  *************")