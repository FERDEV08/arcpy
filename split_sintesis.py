import arcpy

#VARIABLES
BB = arcpy.GetParameterAsText (0)
BV = arcpy.GetParameterAsText (1)
LAYER_apfc = arcpy.GetParameterAsText (2)
LAYER_ca = arcpy.GetParameterAsText (3)
LAYER_cuc = arcpy.GetParameterAsText (4)
LAYER_cuex = arcpy.GetParameterAsText (5)
base = arcpy.GetParameterAsText (6)
CARPETA = arcpy.GetParameterAsText (7)

LAYER_apfc = arcpy.MakeFeatureLayer_management(LAYER_apfc)
LAYER_ca = arcpy.MakeFeatureLayer_management(LAYER_ca)
LAYER_cuc = arcpy.MakeFeatureLayer_management(LAYER_cuc)
LAYER_cuex = arcpy.MakeFeatureLayer_management(LAYER_cuex)


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
 elif c =="EL SALITRE (LAS RAMAS)":
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
    BN = arcpy.os.path.join(CARPETA,"EVAL_TIERRA_"+nom(i[0])+".gdb")
    arcpy.Copy_management(BV,BN)
    
    arcpy.SelectLayerByAttribute_management(LAYER_apfc,"NEW_SELECTION","UGESP_DES ="+"'"+i[0]+"'")
    arcpy.Append_management(LAYER_apfc,arcpy.os.path.join(BN,"APT_TIERRAS","APFC_CIUDAD_A"),"NO_TEST")
    arcpy.RecalculateFeatureClassExtent_management(arcpy.os.path.join(BN,"APT_TIERRAS","APFC_CIUDAD_A"))
    
    arcpy.SelectLayerByAttribute_management(LAYER_ca,"NEW_SELECTION","UGESP_DES ="+"'"+i[0]+"'")
    arcpy.Append_management(LAYER_ca,arcpy.os.path.join(BN,"APT_TIERRAS","CA_CIUDAD_A"),"NO_TEST")
    arcpy.RecalculateFeatureClassExtent_management(arcpy.os.path.join(BN,"APT_TIERRAS","CA_CIUDAD_A"))
    
    arcpy.SelectLayerByAttribute_management(LAYER_cuc,"NEW_SELECTION","UGESP_DES ="+"'"+i[0]+"'")
    arcpy.Append_management(LAYER_cuc,arcpy.os.path.join(BN,"DISP_TIERRAS","CUC_CIUDAD_A"),"NO_TEST")
    arcpy.RecalculateFeatureClassExtent_management(arcpy.os.path.join(BN,"DISP_TIERRAS","CUC_CIUDAD_A"))
    
    arcpy.SelectLayerByAttribute_management(LAYER_cuex,"NEW_SELECTION","UGESP_DES ="+"'"+i[0]+"'")
    arcpy.Append_management(LAYER_cuex,arcpy.os.path.join(BN,"DISP_TIERRAS","CUEX_CIUDAD_A"),"NO_TEST")
    arcpy.RecalculateFeatureClassExtent_management(arcpy.os.path.join(BN,"DISP_TIERRAS","CUEX_CIUDAD_A"))
    
    arcpy.Delete_management(arcpy.os.path.join(BN,"COB_TIERRA"))
    arcpy.Delete_management(arcpy.os.path.join(BN,"CONDICIONES_VIDA"))
    arcpy.Delete_management(arcpy.os.path.join(BN,"EDAFOLOGIA"))
    arcpy.Delete_management(arcpy.os.path.join(BN,"EDUCACION"))
    arcpy.Delete_management(arcpy.os.path.join(BN,"DEMOGRAFIA"))
    arcpy.Delete_management(arcpy.os.path.join(BN,"GEOMORFOLOGIA"))
    
    nw1 = arcpy.os.path.join(BN,"APT_TIERRAS","APFC_"+nom(i[0])+"_A")
    an1 = arcpy.os.path.join(BN,"APT_TIERRAS","APFC_CIUDAD_A")
    arcpy.Rename_management(an1,nw1)
    
    nw2 = arcpy.os.path.join(BN,"APT_TIERRAS","CA_"+nom(i[0])+"_A")
    an2 = arcpy.os.path.join(BN,"APT_TIERRAS","CA_CIUDAD_A")
    arcpy.Rename_management(an2,nw2)

    nw3 = arcpy.os.path.join(BN,"DISP_TIERRAS","CUC_"+nom(i[0])+"_A")
    an3 = arcpy.os.path.join(BN,"DISP_TIERRAS","CUC_CIUDAD_A")
    arcpy.Rename_management(an3,nw3)
    
    nw4 = arcpy.os.path.join(BN,"DISP_TIERRAS","CUEX_"+nom(i[0])+"_A")
    an4 = arcpy.os.path.join(BN,"DISP_TIERRAS","CUEX_CIUDAD_A")
    arcpy.Rename_management(an4,nw4)        