import arcpy

#VARIABLES
BB = arcpy.GetParameterAsText (0)
BV = arcpy.GetParameterAsText (1)
LAYER = arcpy.GetParameterAsText (2)
base = arcpy.GetParameterAsText (3)
CARPETA = arcpy.GetParameterAsText (4)

LAYER = arcpy.MakeFeatureLayer_management(LAYER)


def nom(c):
 if c == "BAHIA DE CARAQUEZ":
  return "BAHIA"
 elif c =="SAN VICENTE":
  return "SAN_VICENTE"
 elif c =="VELASCO IBARRA (EL EMPALME)":
  return "EL_EMPALME"
 elif c =="FLAVIO ALFARO":
  return "FLAVIO_ALFARO"
 elif c =="SANTA ANA DE VUELTA LARGA":
  return "SANTA_ANA"
 elif c =="SAN JACINTO DE BUENA FE":
  return "BUENA_FE"
 elif c =="EL CARMEN":
  return "EL_CARMEN"
 elif c =="LA VICTORIA (LAS LAJAS)":
  return "LA_VICTORIA"
 elif c =="SALITRE (LAS RAMAS)":
  return "SALITRE"
 elif c =="SANTA LUCIA":
  return "SANTA_LUCIA"
 elif c =="GENERAL ANTONIO ELIZALDE (BUCAY)":
  return "BUCAY"
 elif c =="EL TRIUNFO":
  return "EL_TRIUNFO"
 elif c =="ISIDRO AYORA":
  return "ISIDRO_AYORA"
 elif c =="ALFREDO BAQUERIZO MORENO (JUJAN)":
  return "JUJAN"
 elif c =="LOMAS DE SARGENTILLO":
  return "L_SARGENTILLO"
 elif c =="CORONEL MARCELINO MARIDUEÑA":
  return "MAR_MARIDUENA"
 elif c =="NARCISA DE JESUS (NOBOL)":
  return "NOBOL"
 elif c =="PEDRO CARBO":
  return "PEDRO_CARBO"
 elif c =="PUERTO LOPEZ":
  return "PUERTO_LOPEZ"
 elif c =="SIMON BOLIVAR":
  return "SIMON_BOLIVAR"
 elif c =="SAN JACINTO DE YAGUACHI":
  return "YAGUACHI"
 elif c =="LA LIBERTAD":
  return "LA_LIBERTAD"
 elif c =="GENERAL VILLAMIL (PLAYAS)":
  return "PLAYAS"
 elif c =="SANTA ROSA":
  return "SANTA_ROSA"
 elif c =="ELOY ALFARO (DURAN)":
  return "DURAN"
 elif c =="EL GUABO":
  return "EL_GUABO"
 else:
  return c



j = arcpy.da.SearchCursor(base,"UGESP_DES")
for i in j:
    BN = arcpy.os.path.join(CARPETA,"COB_USO_"+nom(i[0])+".gdb")
    arcpy.Copy_management(BV,BN)
    arcpy.SelectLayerByAttribute_management(LAYER,"NEW_SELECTION","UGESP_DES ="+"'"+i[0]+"'")
    arcpy.Append_management(LAYER,arcpy.os.path.join(BN,"COB_TIERRA","COB_USO_CIUDAD_A"),"NO_TEST")
    arcpy.RecalculateFeatureClassExtent_management(arcpy.os.path.join(BN,"COB_TIERRA","COB_USO_CIUDAD_A"))
    arcpy.Delete_management(arcpy.os.path.join(BN,"APT_TIERRAS"))
    arcpy.Delete_management(arcpy.os.path.join(BN,"GEOMORFOLOGIA"))
    arcpy.Delete_management(arcpy.os.path.join(BN,"CONDICIONES_VIDA"))
    arcpy.Delete_management(arcpy.os.path.join(BN,"DISP_TIERRAS"))
    arcpy.Delete_management(arcpy.os.path.join(BN,"EDAFOLOGIA"))
    arcpy.Delete_management(arcpy.os.path.join(BN,"EDUCACION"))
    arcpy.Delete_management(arcpy.os.path.join(BN,"DEMOGRAFIA"))
    nw = arcpy.os.path.join(BN,"COB_TIERRA","COB_USO_"+nom(i[0])+"_A")
    an = arcpy.os.path.join(BN,"COB_TIERRA","COB_USO_CIUDAD_A")
    arcpy.Rename_management(an,nw)
     