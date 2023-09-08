import arcpy

#VARIABLES
BV = arcpy.GetParameterAsText (0)
LAYER_nis = arcpy.GetParameterAsText (1)
LAYER_dis = arcpy.GetParameterAsText (2)
LAYER_depo = arcpy.GetParameterAsText (3)
LAYER_niv = arcpy.GetParameterAsText (4)
base = arcpy.GetParameterAsText (5)
CARPETA = arcpy.GetParameterAsText (6)

LAYER_nis = arcpy.MakeFeatureLayer_management(LAYER_nis)
LAYER_dis = arcpy.MakeFeatureLayer_management(LAYER_dis)
LAYER_depo = arcpy.MakeFeatureLayer_management(LAYER_depo)
LAYER_niv = arcpy.MakeFeatureLayer_management(LAYER_niv)


def nom(c):
 if c == "SAN MIGUEL":
  return "SAN_MIGUEL"
 elif c =="SAN MIGUEL DE LOS BANCOS":
  return "LOS_BANCOS"
 elif c =="PEDRO VICENTE MALDONADO":
  return "PV_MALDONADO"
 elif c =="PUERTO QUITO":
  return "PUERTO_QUITO"
 elif c =="LA CONCORDIA":
  return "LA_CONCORDIA"
 elif c =="ROSA ZARATE":
  return "ROSA_ZARATE"
 elif c =="SAN LORENZO":
  return "SAN_LORENZO"
 elif c =="EL ANGEL":
  return "EL_ANGEL"
 elif c =="SAN GABRIEL":
  return "SAN_GABRIEL"
 elif c =="LA BONITA":
  return "LA_BONITA"
 elif c =="EL DORADO DE CASCALES":
  return "EL_DORADO"
 elif c =="PUERTO EL CARMEN DE PUTUMAYO":
  return "PUTUMAYO"
 elif c =="LA JOYA DE LOS SACHAS":
  return "JOYA_SACHAS"
 elif c =="NUEVO ROCAFUERTE":
  return "NUEVO_ROCAFUERTE"
 elif c =="CARLOS JULIO AROSEMENA TOLA":
  return "CJ_AROSEMENA"
 elif c =="EL CHACO":
  return "EL_CHACO"
 elif c =="EL CORAZON":
  return "EL_CORAZON"
 elif c =="LA MANA":
  return "LA_MANA"
 else:
  return c


j = arcpy.da.SearchCursor(base,"UGESP_DES")
for i in j:
    BN = arcpy.os.path.join(CARPETA,"G_SOCIOEC_"+nom(i[0]).encode('latin1')+".gdb")
    arcpy.Copy_management(BV,BN)
    
    arcpy.SelectLayerByAttribute_management(LAYER_nis,"NEW_SELECTION","UGESP_DES ="+"'"+i[0].encode('latin1')+"'")
    arcpy.Append_management(LAYER_nis,arcpy.os.path.join(BN,"CONDICIONES_VIDA","NIV_SOCIOEC_CIUDAD_A"),"NO_TEST")
    arcpy.RecalculateFeatureClassExtent_management(arcpy.os.path.join(BN,"CONDICIONES_VIDA","NIV_SOCIOEC_CIUDAD_A"))
    
    arcpy.SelectLayerByAttribute_management(LAYER_dis,"NEW_SELECTION","UGESP_DES ="+"'"+i[0].encode('latin1')+"'")
    arcpy.Append_management(LAYER_dis,arcpy.os.path.join(BN,"CONDICIONES_VIDA","SERV_BASICOS_CIUDAD_A"),"NO_TEST")
    arcpy.RecalculateFeatureClassExtent_management(arcpy.os.path.join(BN,"CONDICIONES_VIDA","SERV_BASICOS_CIUDAD_A"))
    
    arcpy.SelectLayerByAttribute_management(LAYER_depo,"NEW_SELECTION","UGESP_DES ="+"'"+i[0].encode('latin1')+"'")
    arcpy.Append_management(LAYER_depo,arcpy.os.path.join(BN,"DEMOGRAFIA","DENSIDAD_POB_CIUDAD_A"),"NO_TEST")
    arcpy.RecalculateFeatureClassExtent_management(arcpy.os.path.join(BN,"DEMOGRAFIA","DENSIDAD_POB_CIUDAD_A"))
    
    arcpy.SelectLayerByAttribute_management(LAYER_niv,"NEW_SELECTION","UGESP_DES ="+"'"+i[0].encode('latin1')+"'")
    arcpy.Append_management(LAYER_niv,arcpy.os.path.join(BN,"EDUCACION","N_INSTRUCCION_CIUDAD_A"),"NO_TEST")
    arcpy.RecalculateFeatureClassExtent_management(arcpy.os.path.join(BN,"EDUCACION","N_INSTRUCCION_CIUDAD_A"))
    
    arcpy.Delete_management(arcpy.os.path.join(BN,"COB_TIERRA"))
    arcpy.Delete_management(arcpy.os.path.join(BN,"APT_TIERRAS"))
    arcpy.Delete_management(arcpy.os.path.join(BN,"GEOMORFOLOGIA"))
    arcpy.Delete_management(arcpy.os.path.join(BN,"DISP_TIERRAS"))
    arcpy.Delete_management(arcpy.os.path.join(BN,"EDAFOLOGIA"))
    
    nw1 = arcpy.os.path.join(BN,"CONDICIONES_VIDA","NIV_SOCIOEC_"+nom(i[0]).encode('latin1')+"_A")
    an1 = arcpy.os.path.join(BN,"CONDICIONES_VIDA","NIV_SOCIOEC_CIUDAD_A")
    arcpy.Rename_management(an1,nw1)
    
    nw2 = arcpy.os.path.join(BN,"CONDICIONES_VIDA","SERV_BASICOS_"+nom(i[0]).encode('latin1')+"_A")
    an2 = arcpy.os.path.join(BN,"CONDICIONES_VIDA","SERV_BASICOS_CIUDAD_A")
    arcpy.Rename_management(an2,nw2)

    nw3 = arcpy.os.path.join(BN,"DEMOGRAFIA","DENSIDAD_POB_"+nom(i[0]).encode('latin1')+"_A")
    an3 = arcpy.os.path.join(BN,"DEMOGRAFIA","DENSIDAD_POB_CIUDAD_A")
    arcpy.Rename_management(an3,nw3)
    
    nw4 = arcpy.os.path.join(BN,"EDUCACION","N_INSTRUCCION_"+nom(i[0]).encode('latin1')+"_A")
    an4 = arcpy.os.path.join(BN,"EDUCACION","N_INSTRUCCION_CIUDAD_A")
    arcpy.Rename_management(an4,nw4)        