# -*- coding: utf-8 -*-
# Set the necessary product code
import arcpy, os
from zipfile import ZipFile
import os
from os.path import basename
import re

arcpy.env.overwriteOutput = True

GDB = arcpy.GetParameterAsText (0)
GDB_VACIA = arcpy.GetParameterAsText (1)

CARPETA = str(GDB.split("\GDB_COMPILADA.gdb")[0])
nextcloud = r"C:\Users\salgado_maria\Nextcloud2\CAPACIDAD DE ACOGIDA\2022"

#COBERTURA Y USO
COB_USO = arcpy.os.path.join(GDB,"COB_TIERRA","COB_USO_CIUDAD_A") 
arcpy.Frequency_analysis(COB_USO,arcpy.os.path.join(CARPETA,"tabla"),["UGESP_DES","DPA_DESPRO"])

LAYER = arcpy.MakeFeatureLayer_management(COB_USO)
cursor = arcpy.da.SearchCursor(arcpy.os.path.join(CARPETA,"tabla"),["UGESP_DES","DPA_DESPRO"])



def nom_ugesp(abrev):
 if abrev == "BAHIA DE CARAQUEZ":
  return "BAHIA" 

 elif abrev == "SAN VICENTE":
  return "SAN_VICENTE"

 elif abrev == "VELASCO IBARRA (EL EMPALME)":
  return "EL_EMPALME"

 elif abrev == "FLAVIO ALFARO":
  return "FLAVIO_ALFARO"

 elif abrev == "SANTA ANA DE VUELTA LARGA":
  return "SANTA_ANA"

 elif abrev == "SAN JACINTO DE BUENA FE":
  return "BUENA_FE"

 elif abrev == "EL CARMEN":
  return "EL_CARMEN"

 elif abrev == "LA VICTORIA (LAS LAJAS)":
  return "LA_VICTORIA"

 elif abrev == "El SALITRE (LAS RAMAS)":
  return "SALITRE"

 elif abrev == "SANTA LUCIA":
  return "SANTA_LUCIA"

 elif abrev == "GENERAL ANTONIO ELIZALDE (BUCAY)":
  return "BUCAY"

 elif abrev == "ELOY ALFARO (DURAN)":
  return "DURAN" 

 elif abrev == "EL TRIUNFO":
  return "EL_TRIUNFO" 

 elif abrev == "ISIDRO AYORA":
  return "ISIDRO_AYORA" 

 elif abrev == "ALFREDO BAQUERIZO MORENO (JUJAN)":
  return "JUJAN" 

 elif abrev == "LOMAS DE SARGENTILLO":
  return "L_SARGENTILLO" 

 elif abrev == "CORONEL MARCELINO MARIDUEÑA":
  return "MAR_MARIDUENA" 

 elif abrev == "NARCISA DE JESUS (NOBOL)":
  return "NOBOL" 

 elif abrev == "PEDRO CARBO":
  return "PEDRO_CARBO" 

 elif abrev == "PUERTO LOPEZ":
  return "PUERTO_LOPEZ" 

 elif abrev == "SIMON BOLIVAR":
  return "SIMON_BOLIVAR"

 elif abrev == "SAN JACINTO DE YAGUACHI":
  return "YAGUACHI" 

 elif abrev == "LA LIBERTAD":
  return "LA_LIBERTAD" 

 elif abrev == "SIMON BOLIVAR":
  return "SIMON_BOLIVAR" 

 elif abrev == "GENERAL VILLAMIL (PLAYAS)":
  return "PLAYAS" 

 elif abrev == "SANTA ROSA":
  return "SANTA_ROSA" 
 else:
  return abrev

nextcloud = r"C:\Users\salgado_maria\Nextcloud2\CAPACIDAD DE ACOGIDA\2022"

for i in cursor:
 CARPETA = arcpy.os.path.join(nextcloud,str(i[1]),str(nom_ugesp(i[0])),"CARTOGRAF\xc3\x8dA TEM\xc3\x81TICA","COBERTURA Y USO","GDB")
 nom_ugesp(i[0])

 #COBERTURA_USO_TIERRA
 arcpy.Copy_management(GDB_VACIA,arcpy.os.path.join(CARPETA,"GDB_vacia%n%.gdb"))
 arcpy.SelectLayerByAttribute_management(LAYER,"NEW_SELECTION","UGESP_DES="+"'"+str(i[0])+"'")
 arcpy.Append_management(LAYER,arcpy.os.path.join(CARPETA,"GDB_vacia%n%.gdb","COB_TIERRA","COB_USO_CIUDAD_A"),"NO_TEST")
 arcpy.RecalculateFeatureClassExtent_management(arcpy.os.path.join(CARPETA,"GDB_vacia%n%.gdb","COB_TIERRA","COB_USO_CIUDAD_A"))
 arcpy.Delete_management(arcpy.os.path.join(CARPETA,"GDB_vacia%n%.gdb","APT_TIERRAS"))
 arcpy.Delete_management(arcpy.os.path.join(CARPETA,"GDB_vacia%n%.gdb","CONDICIONES_VIDA"))
 arcpy.Delete_management(arcpy.os.path.join(CARPETA,"GDB_vacia%n%.gdb","DEMOGRAFIA"))
 arcpy.Delete_management(arcpy.os.path.join(CARPETA,"GDB_vacia%n%.gdb","DISP_TIERRAS"))
 arcpy.Delete_management(arcpy.os.path.join(CARPETA,"GDB_vacia%n%.gdb","EDAFOLOGIA"))
 arcpy.Delete_management(arcpy.os.path.join(CARPETA,"GDB_vacia%n%.gdb","EDUCACION"))
 arcpy.Delete_management(arcpy.os.path.join(CARPETA,"GDB_vacia%n%.gdb","GEOMORFOLOGIA"))
 arcpy.AddMessage("Ciudad: "+str(i[0]))
 nw= arcpy.os.path.join(CARPETA,"COB_USO_"+str(nom_ugesp(i[0]))+".gdb")
 arcpy.Rename_management(arcpy.os.path.join(CARPETA,"GDB_vacia%n%.gdb"),arcpy.os.path.join(nw))
 cob="COB_USO_"+str(nom_ugesp(i[0]))+"_A"
 arcpy.Rename_management(arcpy.os.path.join(nw,"COB_TIERRA","COB_USO_CIUDAD_A"),arcpy.os.path.join(nw,"COB_TIERRA",cob))
 #arcpy.Copy_management(nw,arcpy.os.path.join(CARPETA,"COB_USO_"+str(nom_ugesp(i[0]))+".gdb"))

 


del i
