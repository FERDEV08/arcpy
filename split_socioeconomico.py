import arcpy

#VARIABLES
BB = arcpy.GetParameterAsText (0)
BV = arcpy.GetParameterAsText (1)
LAYER_nis = arcpy.GetParameterAsText (2)
LAYER_dis = arcpy.GetParameterAsText (3)
LAYER_depo = arcpy.GetParameterAsText (4)
LAYER_niv = arcpy.GetParameterAsText (5)
base = arcpy.GetParameterAsText (6)
CARPETA = arcpy.GetParameterAsText (7)

LAYER_nis = arcpy.MakeFeatureLayer_management(LAYER_nis)
LAYER_dis = arcpy.MakeFeatureLayer_management(LAYER_dis)
LAYER_depo = arcpy.MakeFeatureLayer_management(LAYER_depo)
LAYER_niv = arcpy.MakeFeatureLayer_management(LAYER_niv)


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
 elif c =="CORONEL MARCELINO MARIDUE\xc3\x91A":
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
 elif abrev == "SAN MIGUEL":
  return "SAN_MIGUEL"
  
 elif abrev =="SAN MIGUEL DE LOS BANCOS":
  return "LOS_BANCOS"
  
 elif abrev =="PEDRO VICENTE MALDONADO":
  return "PV_MALDONADO"
  
 elif abrev =="PUERTO QUITO":
  return "PUERTO_QUITO"
  
 elif abrev =="LA CONCORDIA":
  return "LA_CONCORDIA"
  
 elif abrev =="ROSA ZARATE":
  return "ROSA_ZARATE"
  
 elif abrev =="SAN LORENZO":
  return "SAN_LORENZO"
  
 elif abrev =="EL ANGEL":
  return "EL_ANGEL"
 elif abrev =="EL CORAZON":
  return "EL_CORAZON"
 elif abrev =="LA MANA":
  return "LA_MANA"  
 elif abrev =="SAN GABRIEL":
  return "SAN_GABRIEL"
  
 elif abrev =="LA BONITA":
  return "LA_BONITA"
  
 elif abrev =="EL DORADO DE CASCALES":
  return "EL_DORADO"
  
 elif abrev =="PUERTO EL CARMEN DE PUTUMAYO":
  return "PUTUMAYO"
  
 elif abrev =="LA JOYA DE LOS SACHAS":
  return "JOYA_SACHAS"
  
 elif abrev =="NUEVO ROCAFUERTE":
  return "NUEVO_ROCAFUERTE"
  
 elif abrev =="CARLOS JULIO AROSEMENA TOLA":
  return "CJ_AROSEMENA"
  
 elif abrev =="EL CHACO":
  return "EL_CHACO"  
 else:
  return c



j = arcpy.da.SearchCursor(base,"UGESP_DES")
for i in j:
    BN = arcpy.os.path.join(CARPETA,"G_SOCIOEC_"+nom(i[0])+".gdb")
    arcpy.Copy_management(BV,BN)
    
    arcpy.SelectLayerByAttribute_management(LAYER_nis,"NEW_SELECTION","UGESP_DES ="+"'"+i[0]+"'")
    arcpy.Append_management(LAYER_nis,arcpy.os.path.join(BN,"CONDICIONES_VIDA","NIV_SOCIOEC_CIUDAD_A"),"NO_TEST")
    arcpy.RecalculateFeatureClassExtent_management(arcpy.os.path.join(BN,"CONDICIONES_VIDA","NIV_SOCIOEC_CIUDAD_A"))
    
    arcpy.SelectLayerByAttribute_management(LAYER_dis,"NEW_SELECTION","UGESP_DES ="+"'"+i[0]+"'")
    arcpy.Append_management(LAYER_dis,arcpy.os.path.join(BN,"CONDICIONES_VIDA","SERV_BASICOS_CIUDAD_A"),"NO_TEST")
    arcpy.RecalculateFeatureClassExtent_management(arcpy.os.path.join(BN,"CONDICIONES_VIDA","SERV_BASICOS_CIUDAD_A"))
    
    arcpy.SelectLayerByAttribute_management(LAYER_depo,"NEW_SELECTION","UGESP_DES ="+"'"+i[0]+"'")
    arcpy.Append_management(LAYER_depo,arcpy.os.path.join(BN,"DEMOGRAFIA","DENSIDAD_POB_CIUDAD_A"),"NO_TEST")
    arcpy.RecalculateFeatureClassExtent_management(arcpy.os.path.join(BN,"DEMOGRAFIA","DENSIDAD_POB_CIUDAD_A"))
    
    arcpy.SelectLayerByAttribute_management(LAYER_niv,"NEW_SELECTION","UGESP_DES ="+"'"+i[0]+"'")
    arcpy.Append_management(LAYER_niv,arcpy.os.path.join(BN,"EDUCACION","N_INSTRUCCION_CIUDAD_A"),"NO_TEST")
    arcpy.RecalculateFeatureClassExtent_management(arcpy.os.path.join(BN,"EDUCACION","N_INSTRUCCION_CIUDAD_A"))
    
    arcpy.Delete_management(arcpy.os.path.join(BN,"COB_TIERRA"))
    arcpy.Delete_management(arcpy.os.path.join(BN,"APT_TIERRAS"))
    arcpy.Delete_management(arcpy.os.path.join(BN,"GEOMORFOLOGIA"))
    arcpy.Delete_management(arcpy.os.path.join(BN,"DISP_TIERRAS"))
    
    nw1 = arcpy.os.path.join(BN,"CONDICIONES_VIDA","NIV_SOCIOEC_"+nom(i[0])+"_A")
    an1 = arcpy.os.path.join(BN,"CONDICIONES_VIDA","NIV_SOCIOEC_CIUDAD_A")
    arcpy.Rename_management(an1,nw1)
    
    nw2 = arcpy.os.path.join(BN,"CONDICIONES_VIDA","SERV_BASICOS_"+nom(i[0])+"_A")
    an2 = arcpy.os.path.join(BN,"CONDICIONES_VIDA","SERV_BASICOS_CIUDAD_A")
    arcpy.Rename_management(an2,nw2)

    nw3 = arcpy.os.path.join(BN,"DEMOGRAFIA","DENSIDAD_POB_"+nom(i[0])+"_A")
    an3 = arcpy.os.path.join(BN,"DEMOGRAFIA","DENSIDAD_POB_CIUDAD_A")
    arcpy.Rename_management(an3,nw3)
    
    nw4 = arcpy.os.path.join(BN,"EDUCACION","N_INSTRUCCION_"+nom(i[0])+"_A")
    an4 = arcpy.os.path.join(BN,"EDUCACION","N_INSTRUCCION_CIUDAD_A")
    arcpy.Rename_management(an4,nw4)        