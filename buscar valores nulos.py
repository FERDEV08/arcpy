
# Script arguments
GDB = arcpy.GetParameterAsText(0)



#Valor de la capa

arcpy.env.workspace = GDB
datasets = arcpy.ListDatasets()
#FUNCION:
def xxx(fc1,DS):
 for h in fc1:
  count2 = 0
  if (DS == 0):
   f_classes = arcpy.os.path.join(h)
  else:
   f_classes = arcpy.os.path.join(DS,h)
  nam = arcpy.Describe(f_classes)
  if (nam.shapeType == "Polygon" or nam.shapeType =="Polyline" or nam.shapeType == "Point"):
   fc1 = f_classes #CAPA
   field_names = [f.name for f in arcpy.ListFields(fc1)]
   for i in field_names:
    count = 0
    with arcpy.da.SearchCursor(fc1,i) as cursor:
     for row in cursor:
      if None in row:
       count = count +1
     if count > 0: 
      arcpy.AddWarning("   En feature class: " + str(h)+ " hay " + str(count) + " Null Value, en: "+ str(i))
    if count > 0:
     count2 = count2 +1
  if count2 == 0:
   arcpy.AddMessage ("No hay NULL VALUES en: "+ str(h.lower()))

#EMPIEZA EL CALCULO
arcpy.AddMessage("______________________________________________")
for j in datasets:
 DATASET = arcpy.os.path.join(GDB,j)
 arcpy.env.workspace = DATASET
 arcpy.AddMessage("DATASET: "+ j)
 fc = arcpy.ListFeatureClasses()
 xxx(fc,DATASET)
 arcpy.AddMessage("______________________________________________")
arcpy.env.workspace = GDB
fc_1 = arcpy.ListFeatureClasses()
xxx(fc_1, 0)