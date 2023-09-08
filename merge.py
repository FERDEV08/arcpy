import arcpy
#Cambiar a tu D
dp = r'D:\BORRAR\merge_socio_2023_prepublicacion\densidad_poblacional_a.shp'
#CAMBIAR A TU PRODUCTOS
raiz = r'Y:\2022_2025\PRODUCTOS_P\2023'
w = arcpy.env.workspace=raiz
#ARCHIDONA NO ESTÁ CONSIDERADA
carpetas =[ u'ATACAMES', u'ATUNTAQUI', u'BAEZA', u'BOLIVAR', u'CAYAMBE', u'CEVALLOS', u'CJ_AROSEMENA', u'COTACACHI', u'EL_ANGEL', u'EL_CHACO', u'EL_CORAZON', u'EL_DORADO', u'HUACA', u'JOYA_SACHAS', u'LA_BONITA', u'LA_CONCORDIA', u'LA_MANA', u'lim_conali_l.lyr', u'LORETO', u'LOS_BANCOS', u'LUMBAQUI', u'MACHACHI', u'MIRA', u'MOCHA', u'MUISNE', u'NUEVO_ROCAFUERTE', u'OTAVALO', u'PATATE', u'PELILEO', u'PILLARO', u'PIMAMPIRO', u'PUERTO_QUITO', u'PUJILI', u'PUTUMAYO', u'PV_MALDONADO', u'QUERO', u'RIOVERDE', u'ROSA_ZARATE', u'SANGOLQUI', u'SAN_GABRIEL', u'SAN_LORENZO', u'SAN_MIGUEL', u'SAQUISILI', u'SHUSHUFINDI', u'SIGCHOS', u'TABACUNDO', u'TARAPOA', u'TISALEO', u'URCUQUI', u'VALDEZ']
for i in carpetas: 
 dir = arcpy.os.path.join(raiz,i,r'C_TEMATICA\SOCIOECONOMICO\BDD\G_SOCIOEC_'+str(i)+'.gdb\DEMOGRAFIA\DENSIDAD_POB_'+str(i)+'_A')
 arcpy.Append_management(dir,dp,"NO_TEST")
 print(dir)



