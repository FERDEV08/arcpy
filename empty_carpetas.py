#INICIO PROGRAMA
import arcpy, os

#Variables
carpeta= arcpy.GetParameterAsText (0)
path1 = carpeta
arcpy.env.workspace = carpeta

a = arcpy.ListFiles()
arcpy.AddMessage(a)
for j in a:
	arcpy.env.workspace = os.path.join(path1,j)
        b= arcpy.ListFeatureClasses()
        arcpy.AddMessage('carpeta: ' +str(j)+'  '+str(b))
	for i in b:
         d = os.path.join (path1,j,i)
         arcpy.AddMessage(str(d))
    	 count1 = str(arcpy.GetCount_management(d))
         arcpy.AddMessage(count1)
    	 if count1 == "0":
			dirr = os.path.join (path1,j,i)
			arcpy.Delete_management(dirr)
			arcpy.AddMessage(str(i))
			del dirr
        del i


arcpy.AddMessage("====================================================")
arcpy.AddMessage("=============Proceso finalizado=====================")
arcpy.AddMessage("====================================================")

arcpy.AddMessage("********* Elaborado: FERNANDA SALGADO  *************")