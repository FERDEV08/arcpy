import arcpy
#Cambiar a tu D
dp = r'D:\PREPUBLICACION_2023\densidad_poblacional_a.shp'
#CAMBIAR A TU PRODUCTOS
raiz = r'Y:\2022_2025\PRODUCTOS_P\2023'
w = arcpy.env.workspace=raiz
#NO ESTÁ CONSIDERADO BAÑOS
carpetas =[ u'ARCHIDONA', u'ATACAMES', u'ATUNTAQUI', u'BAEZA', u'BOLIVAR', u'CAYAMBE', u'CEVALLOS', u'CJ_AROSEMENA', u'COTACACHI', u'EL_ANGEL', u'EL_CHACO', u'EL_CORAZON', u'EL_DORADO', u'HUACA', u'JOYA_SACHAS', u'LA_BONITA', u'LA_CONCORDIA', u'LA_MANA', u'LORETO', u'LOS_BANCOS', u'LUMBAQUI', u'MACHACHI', u'MIRA', u'MOCHA', u'MUISNE', u'NUEVO_ROCAFUERTE', u'OTAVALO', u'PATATE', u'PELILEO', u'PILLARO', u'PIMAMPIRO', u'PUERTO_QUITO', u'PUJILI', u'PUTUMAYO', u'PV_MALDONADO', u'QUERO', u'RIOVERDE', u'ROSA_ZARATE', u'SANGOLQUI', u'SAN_GABRIEL', u'SAN_LORENZO', u'SAN_MIGUEL', u'SAQUISILI', u'SHUSHUFINDI', u'SIGCHOS', u'TABACUNDO', u'TARAPOA', u'TISALEO', u'URCUQUI', u'VALDEZ']
for i in carpetas: 
 dir = arcpy.os.path.join(raiz,i,r'C_TEMATICA\SOCIOECONOMICO\BDD\G_SOCIOEC_'+str(i)+'.gdb\CONDICIONES_VIDA\SERV_BASICOS_'+str(i)+'_A')
 arcpy.Append_management(dir,dp,"NO_TEST")
 print(dir)

-----------------------------------------------------
#geomorfologia
 dir = arcpy.os.path.join(raiz,i,r'C_TEMATICA\GEOMORFOLOGIA\BDD\FISIOGRAFIA_'+str(i)+'.gdb\GEOMORFOLOGIA\U_GEOM_'+str(i)+'_A')
 
 #geomorfologia linea
dir = arcpy.os.path.join(raiz,i,r'C_TEMATICA\GEOMORFOLOGIA\BDD\FISIOGRAFIA_'+str(i)+'.gdb\GEOMORFOLOGIA\GEOF_L')
 
 #geomorfologia punto
dir = arcpy.os.path.join(raiz,i,r'C_TEMATICA\GEOMORFOLOGIA\BDD\FISIOGRAFIA_'+str(i)+'.gdb\GEOMORFOLOGIA\GEOF_P')
 ----
  #COBERTURA
dir = arcpy.os.path.join(raiz,i,r'C_TEMATICA\COBERTURA_USO\BDD\COB_USO_'+str(i)+'.gdb\COB_TIERRA\COB_USO_'+str(i)+'_A')    
 
 #DENSIDAD
dir = arcpy.os.path.join(raiz,i,r'C_TEMATICA\SOCIOECONOMICO\BDD\G_SOCIOEC_'+str(i)+'.gdb\DEMOGRAFIA\DENSIDAD_POB_'+str(i)+'_A')
 #NIV SOCIOCIOEC 
dir = arcpy.os.path.join(raiz,i,r'C_TEMATICA\SOCIOECONOMICO\BDD\G_SOCIOEC_'+str(i)+'.gdb\CONDICIONES_VIDA\NIV_SOCIOEC_'+str(i)+'_A') 
 #NIV INSTRUCCION
dir = arcpy.os.path.join(raiz,i,r'C_TEMATICA\SOCIOECONOMICO\BDD\G_SOCIOEC_'+str(i)+'.gdb\EDUCACION\N_INSTRUCCION_'+str(i)+'_A')
 #SERVICIOS BASICOS
 dir = arcpy.os.path.join(raiz,i,r'C_TEMATICA\SOCIOECONOMICO\BDD\G_SOCIOEC_'+str(i)+'.gdb\CONDICIONES_VIDA\SERV_BASICOS_'+str(i)+'_A')
 
 ---
 #APFC
dir = arcpy.os.path.join(raiz,i,r'C_TEMATICA\SINTESIS\BDD\EVAL_TIERRA_'+str(i)+'.gdb\APT_TIERRAS\APFC_'+str(i)+'_A')    

 #CA
dir = arcpy.os.path.join(raiz,i,r'C_TEMATICA\SINTESIS\BDD\EVAL_TIERRA_'+str(i)+'.gdb\APT_TIERRAS\CA_'+str(i)+'_A')    

 #CUC
dir = arcpy.os.path.join(raiz,i,r'C_TEMATICA\SINTESIS\BDD\EVAL_TIERRA_'+str(i)+'.gdb\DISP_TIERRAS\CUC_'+str(i)+'_A')    

 #CUEX
dir = arcpy.os.path.join(raiz,i,r'C_TEMATICA\SINTESIS\BDD\EVAL_TIERRA_'+str(i)+'.gdb\DISP_TIERRAS\CUEX_'+str(i)+'_A')    

 #SUELO
dir = arcpy.os.path.join(raiz,i,r'C_TEMATICA\SUELO\BDD\FISIOGRAFIA_'+str(i)+'.gdb\EDAFOLOGIA\SUELO_'+str(i)+'_A')

 #U_CUT
dir = arcpy.os.path.join(raiz,i,r'C_TEMATICA\SUELO\BDD\FISIOGRAFIA_'+str(i)+'.gdb\EDAFOLOGIA\U_CUT_'+str(i)+'_A')
 

-----------------------------------------------------
#PUBLICACION 
#BLOQUE 1 FALTA BAÑOS
carpetas =[ u'CEVALLOS', u'MOCHA', u'PATATE', u'PELILEO', u'PILLARO', u'QUERO',  u'TISALEO']

carpetas =[ u'CEVALLOS',u'LA_MANA', u'MOCHA', u'PATATE', u'PELILEO', u'PILLARO', u'PUJILI', u'QUERO', u'SAN_MIGUEL', u'SAQUISILI', u'SIGCHOS', u'TISALEO']

#BLOQUE 2 
#PUBLICACION 
#BLOQUE 1 FALTA BAÑOS u'EL_CORAZON', u'LA_CONCORDIA', u'LOS_BANCOS', u'MUISNE', u'PIMAMPIRO', u'PUERTO_QUITO', u'PV_MALDONADO', u'ROSA_ZARATE', u'RIOVERDE', u'VALDEZ' u'URCUQUI', u'SAN_LORENZO',]

#BLOQUE 2
carpetas =[ u'ATUNTAQUI', u'BOLIVAR', u'BAEZA', u'CAYAMBE', u'COTACACHI',  u'EL_ANGEL', u'EL_CHACO', u'HUACA', u'MIRA', u'OTAVALO',u'TABACUNDO', u'SAN_GABRIEL',]

#BLOQUE 3
carpetas =[u'MACHACHI', u'SANGOLQUI']

#BLOQUE 5
carpetas =[u'ARCHIDONA', u'CJ_AROSEMENA', u'EL_DORADO', u'JOYA_SACHAS', u'LA_BONITA', u'LORETO',  u'LUMBAQUI', u'NUEVO_ROCAFUERTE', u'PUTUMAYO', u'SHUSHUFINDI', u'TARAPOA']

#PUBLICACION 
#socio
carpetas =[ u'ROSA_ZARATE', u'ATACAMES', u'MUISNE', u'RIOVERDE', u'SAN_LORENZO', u'VALDEZ', u'PUTUMAYO']

carpetas =[ u'SAN_LORENZO', u'MUISNE', u'VALDEZ', u'PUTUMAYO']

carpetas =[ u'ROSA_ZARATE', u'MUISNE', u'VALDEZ',u'SAN_LORENZO', u'RIOVERDE', u'PUTUMAYO']

carpetas =[ u'ATACAMES', u'MUISNE',u'SAN_LORENZO', u'RIOVERDE', u'PUTUMAYO']