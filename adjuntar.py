
import arcpy, os

#VARIABLES
path1 = arcpy.GetParameterAsText (0)
path2 = arcpy.GetParameterAsText (1)

arcpy.env.workspace = path2
b = arcpy.ListFeatureClasses()
arcpy.env.workspace = path1
a = arcpy.ListFeatureClasses()

#ANEXAR
arcpy.AddMessage("ADJUNTANDO:  ")
for i in a:
	for j in b:
		if i == j:
			dirr = arcpy.os.path.join(path1,j)
			dirr2 = arcpy.os.path.join(path2,i)
	 		arcpy.AddMessage(j)
			arcpy.Append_management(dirr2,dirr,"NO_TEST")
del dirr, dirr2

#ADJUNTAR
arcpy.AddMessage("============================================")
arcpy.AddMessage("FEATURES FALTANTES: ")
for j in b:
     f = j in a
     f = str(f) 
     if f == "False":
         dirr = arcpy.os.path.join (path2,j)
	 arcpy.AddMessage(j)
         arcpy.FeatureClassToFeatureClass_conversion(dirr,path1,j)

arcpy.AddMessage("====================================================")
arcpy.AddMessage("=============Proceso finalizado=====================")
arcpy.AddMessage("====================================================")

arcpy.AddMessage("======= Elaborado POR: FERNANDA SALGADO ============")
