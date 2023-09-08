#libreries
import arcpy

fc = arcpy.GetParameterAsText (0)
dominio = arcpy.GetParameterAsText (1)
dominio = dominio.split(';')



arcpy.AddMessage(type(dominio))

for h in dominio:
 arcpy.AddMessage ("ESTE DOMINIO ESTA VERIFICANDO:    "+ str(h))
 arcpy.DeleteField_management(fc,str(h))
 if (str(h) == "nug" or h == "dvq" or h== "tds"):
  arcpy.AddField_management(fc,str(h),"TEXT")
 else:
  arcpy.AddField_management(fc,str(h),"LONG")
  arcpy.AddMessage ("else:    "+ str(h))
 cursor = arcpy.da.UpdateCursor(fc,[str(h),str(h)+"1"])
 for i in cursor:
  i[0]=i[1]
  cursor.updateRow(i)
 arcpy.DeleteField_management(fc,str(h)+"1") 
