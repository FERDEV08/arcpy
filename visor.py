import arcpy,os
arcpy.env.overwriteOutput = True
shp=arcpy.GetParameterAsText(0)
ciudad=arcpy.GetParameterAsText(1)
carpeta=arcpy.GetParameterAsText(2)


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

 elif abrev == "EL SALITRE (LAS RAMAS)":
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
  return abrev

shp=arcpy.da.SearchCursor(shp,['UGESP_DES','xmin','xmax','ymin','ymax'])




for i in shp:
 path1= arcpy.os.path.join(carpeta,"CA_"+nom_ugesp(i[0])+".json")
 file = open(path1, "w")
 file.write("{\n")
 file.write("    \"initialCamera\": {\n")
 file.write("        \"west\":" +i[1]+",\n")
 file.write("        \"south\":" +i[3]+",\n")
 file.write("        \"east\":" +i[2]+",\n")
 file.write("        \"north\": " +i[4]+"\n")
 file.write("    },\n")
 file.write("    \"homeCamera\": {\n")
 file.write("        \"west\":" +i[1]+",\n")
 file.write("        \"south\":" +i[3]+",\n")
 file.write("        \"east\":" +i[2]+",\n")
 file.write("        \"north\": " +i[4]+"\n")
 file.write("    },\n")
 file.write("    \"catalog\": [\n")
 file.write("        {\n")
 file.write("            \"name\": \"Capacidad de Acogida del Cant\xc3\xb3n "+ str(i[0]) +"  2022\",\n")
 file.write("            \"type\": \"group\",\n")
 file.write("            \"preserveOrder\": true,\n")
 file.write("            \"isOpen\": true,\n")
 file.write("            \"items\": [\n")
 file.write("                {\n")
 file.write("                    \"name\": \"GEOGRAF\xc3\x8dA SOCIOECON\xc3\x93MICA\",\n")
 file.write("                    \"type\": \"group\",\n")
 file.write("                    \"preserveOrder\": true,\n")
 file.write("                    \"items\": [\n")
 file.write("                        {\n")
 file.write("                            \"name\": \"Condiciones de Vida\",\n")
 file.write("                            \"type\": \"group\",\n")
 file.write("                            \"preserveOrder\": true,\n")
 file.write("                            \"items\": [\n")
 file.write("                                {\n")
 file.write("                                    \"layers\": \"igm_ca2022:v_nivel_socioeconomico_a\",\n")
 file.write("                                    \"isEnabled\": false,\n")
 file.write("                                    \"isShown\": false,\n")
 file.write("                                    \"parameters\": {\n")
 file.write("                                        \"tiled\": true,\n")
 file.write("                                        \"style\": \"igm_ca22:stl_"+nom_ugesp(i[0]).lower()+"_nse\",\n")
 file.write("                                        \"CQL_FILTER\": \"ugesp_des='"+i[0]+"'\"\n")
 file.write("                                    },\n")
 file.write("                                    \"opacity\": 1,\n")
 file.write("                                    \"name\": \"Nivel Socioecon\xc3\xb3mico\",\n")
 file.write("                                    \"getFeatureInfoFormats\": [\n")
 file.write("                                        {\n")
 file.write("                                            \"type\": \"json\"\n")
 file.write("                                        }\n")
 file.write("                                    ],\n")
 file.write("                                    \"url\": \"https://www.geoportaligm.gob.ec/igm_afc/igm_ca2022/wms?\",\n")
 file.write("                                    \"type\": \"wms\",\n")
 file.write("                                    \"featureInfoTemplate\": {\n")
 file.write("                                        \"name\": \"{{objeto}} - {{dpa_descan}}: {{ugesp_des}}\",\n")
 file.write("                                        \"template\": \"</html>\\n<table border='1' cellpadding='10' cellspacing='0' >\\n    <tbody>\\n      <tr>\\n        <td colspan='4' align='middle' ><b>Nivel Socioecon\xc3\xb3mico</td>\\n      </tr>\\n      <tr>\\n        <td  align='middle'>Categor\xc3\xada</td>\\n        <td>Superficie(ha)</td>\\n      </tr>\\n      <tr>\\n        <td>{{nse}}</td>\\n        <td >{{ard}}</td>\\n      </tr>\\n    </tbody>\\n</body>\\n</html>\\n\"\n")
 file.write("                                    }\n")
 file.write("                                },\n")
 file.write("                                {\n")
 file.write("                                    \"layers\": \"igm_ca2022:v_servicios_basicos_a\",\n")
 file.write("                                    \"isEnabled\": true,\n")
 file.write("                                    \"isShown\": false,\n")
 file.write("                                    \"parameters\": {\n")
 file.write("                                        \"tiled\": true,\n")
 file.write("                                        \"style\": \"igm_ca22:stl_"+nom_ugesp(i[0]).lower()+"_dis\",\n")
 file.write("                                        \"CQL_FILTER\": \"ugesp_des='"+i[0]+"'\"\n")
 file.write("                                    },\n")
 file.write("                                    \"opacity\": 1,\n")
 file.write("                                    \"name\": \"Servicios B\xc3\xa1sicos\",\n")
 file.write("                                    \"getFeatureInfoFormats\": [\n")
 file.write("                                        {\n")
 file.write("                                            \"type\": \"json\"\n")
 file.write("                                        }\n")
 file.write("                                    ],\n")
 file.write("                                    \"url\": \"https://www.geoportaligm.gob.ec/igm_afc/igm_ca2022/wms?\",\n")
 file.write("                                    \"type\": \"wms\",\n")
 file.write("                                    \"featureInfoTemplate\": {\n")
 file.write("                                        \"name\": \"{{objeto}} - {{dpa_descan}}: {{ugesp_des}}\",\n")
 file.write("                                        \"template\": \"</html>\\n<table border='1' cellpadding='10' cellspacing='0' >\\n    <tbody>\\n      <tr>\\n        <td colspan='4' align='middle' ><b>Disponibilidad de servicios b\xc3\xa1sicos</td>\\n      </tr>\\n      <tr>\\n        <td  align='middle'>Categor\xc3\xada</td>\\n        <td>Superficie(ha)</td>\\n      </tr>\\n      <tr>\\n        <td>{{dis}}</td>\\n        <td >{{ard}}</td>\\n      </tr>\\n    </tbody>\\n</body>\\n</html>\\n\"\n")
 file.write("                                    }\n")
 file.write("                                }\n")
 file.write("                            ]\n")
 file.write("                        },\n")
 file.write("                        {\n")
 file.write("                            \"name\": \"Demograf\xc3\xada\",\n")
 file.write("                            \"type\": \"group\",\n")
 file.write("                            \"preserveOrder\": true,\n")
 file.write("                            \"items\": [\n")
 file.write("                                {\n")
 file.write("                                    \"layers\": \"igm_ca2022:v_densidad_pob_a_"+nom_ugesp(i[0]).lower()+"\",\n")
 file.write("                                    \"isEnabled\": true,\n")
 file.write("                                    \"isShown\": false,\n")
 file.write("                                    \"parameters\": {\n")
 file.write("                                        \"tiled\": true,\n")
 file.write("                                        \"CQL_FILTER\": \"ugesp_des='"+i[0]+"'\"\n")
 file.write("                                    },\n")
 file.write("                                    \"opacity\": 1,\n")
 file.write("                                    \"name\": \"Densidad Poblacional\",\n")
 file.write("                                    \"getFeatureInfoFormats\": [\n")
 file.write("                                        {\n")
 file.write("                                            \"type\": \"json\"\n")
 file.write("                                        }\n")
 file.write("                                    ],\n")
 file.write("                                    \"url\": \"https://www.geoportaligm.gob.ec/igm_afc/igm_ca2022/wms?\",\n")
 file.write("                                    \"type\": \"wms\",\n")
 file.write("                                    \"featureInfoTemplate\": {\n")
 file.write("                                        \"name\": \"{{objeto}} - {{dpa_descan}}: {{ugesp_des}}\",\n")
 file.write("                                        \"template\": \"</style>\\n<table border='1' cellpadding='10' cellspacing='0' >\\n    <tbody>\\n      <tr>\\n        <td colspan='4' align='middle' ><b>Densidad Poblacional</td>\\n      </tr>\\n      <tr>\\n        <td>Categor\xc3\xada</td>\\n        <td>Superficie(ha)</td>\\n      </tr>\\n      <tr>\\n        <td>{{depo_desc}}</td>\\n        <td align='middle'>{{ard}}</td>\\n      </tr>\\n    </tbody>\\n</body>\\n</html>\\n\"\n")
 file.write("                                    }  \n")
 file.write("                                }\n")
 file.write("                            ]\n")
 file.write("                        },\n")
 file.write("                        {\n")
 file.write("                            \"name\": \"Educaci\xc3\xb3n\",\n")
 file.write("                            \"type\": \"group\",\n")
 file.write("                            \"preserveOrder\": true,\n")
 file.write("                            \"items\": [\n")
 file.write("                                {\n")
 file.write("                                    \"layers\": \"igm_ca2022:v_nivel_instruccion_a\",\n")
 file.write("                                    \"isEnabled\": true,\n")
 file.write("                                    \"isShown\": false,\n")
 file.write("                                    \"parameters\": {\n")
 file.write("                                        \"tiled\": true,\n")
 file.write("                                        \"style\": \"igm_ca22:stl_"+nom_ugesp(i[0]).lower()+"_nis\",\n")
 file.write("                                        \"CQL_FILTER\": \"ugesp_des='"+i[0]+"'\"\n")
 file.write("                                    },\n")
 file.write("                                    \"opacity\": 1,\n")
 file.write("                                    \"name\": \"Nivel de Instrucci\xc3\xb3n\",\n")
 file.write("                                    \"getFeatureInfoFormats\": [\n")
 file.write("                                        {\n")
 file.write("                                            \"type\": \"json\"\n")
 file.write("                                        }\n")
 file.write("                                    ],\n")
 file.write("                                    \"url\": \"https://www.geoportaligm.gob.ec/igm_afc/igm_ca2022/wms?\",\n")
 file.write("                                    \"type\": \"wms\",\n")
 file.write("                                    \"featureInfoTemplate\": {\n")
 file.write("                                        \"name\": \"{{objeto}} - {{dpa_descan}}: {{ugesp_des}}\",\n")
 file.write("                                        \"template\": \"</style>\\n<table border='1' cellpadding='10' cellspacing='0' >\\n    <tbody>\\n      <tr>\\n        <td colspan='4' align='middle' ><b>Nivel Instrucci\xc3\xb3n</td>\\n      </tr>\\n      <tr>\\n        <td colspan='2' align='middle'>Categor\xc3\xada</td>\\n        <td>Superficie(ha)</td>\\n      </tr>\\n      <tr>\\n        <td>{{nis_clas}}</td>\\n        <td >{{nis}}</td>\\n        <td align='middle'>{{ard}}</td>\\n      </tr>\\n    </tbody>\\n</body>\\n</html>\"\n")
 file.write("                                    }  \n")
 file.write("                                }\n")
 file.write("                            ]\n")
 file.write("                        }\n")
 file.write("                    ]\n")
 file.write("                },\n")
 file.write("                {\n")
 file.write("                    \"name\": \"COBERTURA Y USO\",\n")
 file.write("                    \"type\": \"group\",\n")
 file.write("                    \"preserveOrder\": true,\n")
 file.write("                    \"items\": [\n")
 file.write("                        {\n")
 file.write("                            \"name\": \"Cobertura y uso de la tierra\",\n")
 file.write("                            \"type\": \"group\",\n")
 file.write("                            \"preserveOrder\": true,\n")
 file.write("                            \"layers\": \"igm_ca2022:v_cobertura_tierra_a\",\n")
 file.write("                            \"isEnabled\": true,\n")
 file.write("                            \"isShown\": false,\n")
 file.write("                            \"parameters\": {\n")
 file.write("                                \"tiled\": true,\n")
 file.write("								\"style\": \"igm_ca22:stl_"+nom_ugesp(i[0]).lower()+"_cob_uso\",\n")
 file.write("                                \"CQL_FILTER\": \"ugesp_des='"+i[0]+"'\"\n")
 file.write("                            },\n")
 file.write("                            \"opacity\": 1,\n")
 file.write("                            \"name\": \"Cobertura y uso de la tierra, Cobertura Natural (Niveles de Alteraci\xc3\xb3n)\",\n")
 file.write("                            \"getFeatureInfoFormats\": [\n")
 file.write("                                {\n")
 file.write("                                    \"type\": \"json\"\n")
 file.write("                                }\n")
 file.write("                            ],\n")
 file.write("                            \"url\": \"https://www.geoportaligm.gob.ec/igm_afc/igm_ca2022/wms?\",\n")
 file.write("                            \"type\": \"wms\",\n")
 file.write("                            \"featureInfoTemplate\": {\n")
 file.write("                                \"name\": \"{{objeto}} - {{dpa_descan}}: {{ugesp_des}}\",\n")
 file.write("                                \"template\": \"</style>\\n<table border='1' cellpadding='10' cellspacing='0' >\\n    <tbody>\\n      <tr>\\n        <td colspan='4' align='middle'>Cobertura y Uso de la Tierra</td>\\n      </tr>\\n      <tr>\\n        <td>Uso</td>\\n        <td>Cobertura de la tierra y temporalidad</td>\\n        <td>Cobertura de la tierra</td>\\n        <td>Superficie (ha)</td>\\n      </tr>\\n      <tr>\\n        <td>{{uso}}</td>\\n        <td align='middle'>{{otmp}}</td>\\n        <td align='middle'>{{cbt}}</td>\\n        <td align='middle'>{{ard}}</td>\\n      </tr>\\n    </tbody>\\n</table>\\n</body>\\n</html>\\n\"\n")
 file.write("                            }  \n")
 file.write("                        }\n")
 file.write("                    ]\n")
 file.write("                },\n")
 file.write("                {\n")
 file.write("                    \"name\": \"GEOMORFOLOG\xc3\x8dA\",\n")
 file.write("                    \"type\": \"group\",\n")
 file.write("                    \"preserveOrder\": true,\n")
 file.write("                    \"items\": [\n")
 file.write("                        {\n")
 file.write("                            \"name\": \"Unidad geomorfol\xc3\xb3gica\",\n")
 file.write("                            \"type\": \"group\",\n")
 file.write("                            \"preserveOrder\": true,\n")
 file.write("                            \"layers\": \"igm_ca2022:g_geomorfologia_"+nom_ugesp(i[0]).lower()+"\",\n")
 file.write("                            \"isEnabled\": true,\n")
 file.write("                            \"isShown\": false,\n")

 file.write("                            \"opacity\": 1,\n")
 file.write("                            \"name\": \"Unidad geomorfol\xc3\xb3gica\",\n")
 file.write("                            \"getFeatureInfoFormats\": [\n")
 file.write("                                {\n")
 file.write("                                    \"type\": \"json\"\n")
 file.write("                                }\n")
 file.write("                            ],\n")
 file.write("                            \"url\": \"https://www.geoportaligm.gob.ec/igm_afc/igm_ca2022/wms?\",\n")
 file.write("                            \"type\": \"wms\",\n")
 file.write("                            \"featureInfoTemplate\": {\n")
 file.write("                                \"name\": \"{{objeto}} - {{dpa_descan}}: {{ugesp_des}}\",\n")
 file.write("                                \"template\": \"</style>\\n<table border='1' cellpadding='10' cellspacing='0' >\\n    <tbody>\\n      <tr>\\n        <td colspan='4' align='middle'>Geomorfolog\xc3\xada</td>\\n      </tr>\\n      <tr>\\n        <td>Unidada Gen\xc3\xa9tica</td>\\n        <td>Geoforma</td>\\n        <td>Morfometr\xc3\xada</td>\\n        <td>Superficie (ha)</td>\\n      </tr>\\n      <tr>\\n        <td rowspan='2'>{{uge}}</td>\\n        <td rowspan='2'>{{geof}}</td>\\n        <td>Pendiente: {{rpdt}}</td>\\n        <td rowspan='2'>{{ard}}</td>\\n      </tr>\\n      <tr >\\n        <td>Desnivel relativo: {{dre}}</td>\\n      </tr>\\n    </tbody>\\n</table>\\n</body>\\n</html>\\n\"\n")
 file.write("                            } \n")
 file.write("                        }\n")
 file.write("                    ]\n")
 file.write("                },\n")
 file.write("                {\n")
 file.write("                    \"name\": \"S\xc3\x8dNTESIS\",\n")
 file.write("                    \"type\": \"group\",\n")
 file.write("                    \"preserveOrder\": true,\n")
 file.write("                    \"items\": [\n")
 file.write("                        {\n")
 file.write("                            \"name\": \"Aptitud Tierras\",\n")
 file.write("                            \"type\": \"group\",\n")
 file.write("                            \"preserveOrder\": true,\n")
 file.write("                            \"items\": [\n")
 file.write("                                {\n")
 file.write("                                    \"layers\": \"igm_ca2022:v_aptitud_fisica_constructiva_a\",\n")
 file.write("                                    \"isEnabled\": true,\n")
 file.write("                                    \"isShown\": false,\n")
 file.write("                                    \"parameters\": {\n")
 file.write("                                        \"tiled\": true,\n")
 file.write("                                        \"style\": \"igm_ca22:stl_"+nom_ugesp(i[0]).lower()+"_apfc\",\n")
 file.write("                                        \"CQL_FILTER\": \"ugesp_des='"+i[0]+"'\"\n")
 file.write("                                    },\n")
 file.write("                                    \"opacity\": 1,\n")
 file.write("                                    \"name\": \"Aptitud F\xc3\xadsica Constructiva\",\n")
 file.write("                                    \"getFeatureInfoFormats\": [\n")
 file.write("                                        {\n")
 file.write("                                            \"type\": \"json\"\n")
 file.write("                                        }\n")
 file.write("                                    ],\n")
 file.write("                                    \"url\": \"https://www.geoportaligm.gob.ec/igm_afc/igm_ca2022/wms?\",\n")
 file.write("                                    \"type\": \"wms\",\n")
 file.write("                                    \"featureInfoTemplate\": {\n")
 file.write("                                        \"name\": \"{{objeto}} - {{dpa_descan}}: {{ugesp_des}}\",\n")
 file.write("                                        \"template\": \"</style>\\n<table border='1' cellpadding='10' cellspacing='0' >\\n    <tbody>\\n      <tr>\\n        <td colspan='4' align='middle' ><b>Aptitud F\xc3\xadsica Constructiva</td>\\n      </tr>\\n      <tr>\\n        <td>Categor\xc3\xada</td>\\n        <td align='middle' >Superficie(ha)</td>\\n      </tr>\\n      <tr>\\n        <td>{{apfc}}</td>\\n        <td align='middle' >{{ard}}</td>\\n      </tr>\\n    </tbody>\\n</body>\\n</html>\\n\"\n")
 file.write("                                    }                                    \n")
 file.write("\n")
 file.write("                                },\n")
 file.write("                                {\n")
 file.write("                                    \"layers\": \"igm_ca2022:v_capacidad_acogida_a\",\n")
 file.write("                                    \"isEnabled\": true,\n")
 file.write("                                    \"isShown\": true,\n")
 file.write("                                    \"parameters\": {\n")
 file.write("                                        \"tiled\": true,\n")
 file.write("                                        \"style\": \"igm_ca22:stl_"+nom_ugesp(i[0]).lower()+"_ca\",\n")
 file.write("                                        \"CQL_FILTER\": \"ugesp_des='"+i[0]+"'\"\n")
 file.write("                                    },\n")
 file.write("                                    \"opacity\": 1,\n")
 file.write("                                    \"name\": \"Capacidad de Acogida\",\n")
 file.write("                                    \"getFeatureInfoFormats\": [\n")
 file.write("                                        {\n")
 file.write("                                            \"type\": \"json\"\n")
 file.write("                                        }\n")
 file.write("                                    ],\n")
 file.write("                                    \"url\": \"https://www.geoportaligm.gob.ec/igm_afc/igm_ca2022/wms?\",\n")
 file.write("                                    \"type\": \"wms\",\n")
 file.write("                                    \"featureInfoTemplate\": {\n")
 file.write("                                        \"name\": \"{{objeto}} - {{dpa_descan}}: {{ugesp_des}}\",\n")
 file.write("                                        \"template\": \"</style>\\n<table border='1' cellpadding='10' cellspacing='0' >\\n    <tbody>\\n      <tr>\\n        <td colspan='4' align='middle' ><b>Capacidad de Acogida</td>\\n      </tr>\\n      <tr>\\n        <td>Categor\xc3\xada</td>\\n        <td align='middle' >Superficie(ha)</td>\\n      </tr>\\n      <tr>\\n        <td>{{ca}}</td>\\n        <td align='middle' >{{ard}}</td>\\n      </tr>\\n    </tbody>\\n</body>\\n</html>\\n\"\n")
 file.write("                                    }        \n")
 file.write("                                }\n")
 file.write("                            ]\n")
 file.write("                        },\n")
 file.write("                        {\n")
 file.write("                            \"name\": \"Disponibilidad de Tierra\",\n")
 file.write("                            \"type\": \"group\",\n")
 file.write("                            \"preserveOrder\": true,\n")
 file.write("                            \"items\": [\n")
 file.write("                                {\n")
 file.write("                                    \"layers\": \"igm_ca2022:v_conflicto_uso_consolidado_a\",\n")
 file.write("                                    \"isEnabled\": true,\n")
 file.write("                                    \"isShown\": false,\n")
 file.write("                                    \"parameters\": {\n")
 file.write("                                        \"tiled\": true,\n")
 file.write("                                        \"style\": \"igm_ca22:stl_"+nom_ugesp(i[0]).lower()+"_cuc\",\n")
 file.write("                                        \"CQL_FILTER\": \"ugesp_des='"+i[0]+"'\"\n")
 file.write("                                    },\n")
 file.write("                                    \"opacity\": 1,\n")
 file.write("                                    \"name\": \"Conflictos de uso consolidado\",\n")
 file.write("                                    \"getFeatureInfoFormats\": [\n")
 file.write("                                        {\n")
 file.write("                                            \"type\": \"json\"\n")
 file.write("                                        }\n")
 file.write("                                    ],\n")
 file.write("                                    \"url\": \"https://www.geoportaligm.gob.ec/igm_afc/igm_ca2022/wms?\",\n")
 file.write("                                    \"type\": \"wms\",\n")
 file.write("                                    \"featureInfoTemplate\": {\n")
 file.write("                                        \"name\": \"{{objeto}} - {{dpa_descan}}: {{ugesp_des}}\",\n")
 file.write("                                        \"template\": \"</style>\\n<table border='1' cellpadding='10' cellspacing='0' >\\n    <tbody>\\n      <tr>\\n        <td colspan='4' align='middle' ><b>Conflictos de uso para Zonas Consolidadas</td>\\n      </tr>\\n      <tr>\\n        <td>Categor\xc3\xada</td>\\n        <td align='middle' >S\xc3\xadmbolo</td>\\n        <td>Superficie(ha)</td>\\n      </tr>\\n      <tr>\\n        <td>{{cuc}}</td>\\n        <td>{{cuc_simb}}</td>\\n        <td>{{ard}}</td>\\n      </tr>\\n    </tbody>\\n</body>\\n</html>\\n\"\n")
 file.write("                                    }\n")
 file.write("                                },\n")
 file.write("                                {\n")
 file.write("                                    \"layers\": \"igm_ca2022:v_conflicto_uso_expansion_a\",\n")
 file.write("                                    \"isEnabled\": true,\n")
 file.write("                                    \"isShown\": false,\n")
 file.write("                                    \"parameters\": {\n")
 file.write("                                        \"tiled\": true,\n")
 file.write("                                        \"style\": \"igm_ca22:stl_"+nom_ugesp(i[0]).lower()+"_cuex\",\n")
 file.write("                                        \"CQL_FILTER\": \"ugesp_des='"+i[0]+"'\"\n")
 file.write("                                    },\n")
 file.write("                                    \"opacity\": 1,\n")
 file.write("                                    \"name\": \"Conflictos de uso en expansi\xc3\xb3n\",\n")
 file.write("                                    \"getFeatureInfoFormats\": [\n")
 file.write("                                        {\n")
 file.write("                                            \"type\": \"json\"\n")
 file.write("                                        }\n")
 file.write("                                    ],\n")
 file.write("                                    \"url\": \"https://www.geoportaligm.gob.ec/igm_afc/igm_ca2022/wms?\",\n")
 file.write("                                    \"type\": \"wms\",\n")
 file.write("                                    \"featureInfoTemplate\": {\n")
 file.write("                                        \"name\": \"{{objeto}} - {{dpa_descan}}: {{ugesp_des}}\",\n")
 file.write("                                        \"template\": \"</style>\\n<table border='1' cellpadding='10' cellspacing='0' >\\n    <tbody>\\n      <tr>\\n        <td colspan='4' align='middle' ><b>Conflictos de uso para Zonas en Expansi\xc3\xb3n</td>\\n      </tr>\\n      <tr>\\n        <td>Categor\xc3\xada</td>\\n        <td align='middle' >S\xc3\xadmbolo</td>\\n        <td>Superficie(ha)</td>\\n      </tr>\\n      <tr>\\n        <td>{{cuex}}</td>\\n        <td>{{cuex_simb}}</td>\\n        <td>{{ard}}</td>\\n      </tr>\\n    </tbody>\\n</body>\\n</html>\\n\"\n")
 file.write("                                    }\n")
 file.write("                                }\n")
 file.write("                            ]\n")
 file.write("                        }\n")
 file.write("                    ]\n")
 file.write("                },\n")
 file.write("                {\n")
 file.write("                    \"name\": \"SUELO\",\n")
 file.write("                    \"type\": \"group\",\n")
 file.write("                    \"preserveOrder\": true,\n")
 file.write("                    \"items\": [\n")
 file.write("                        {\n")
 file.write("                            \"name\": \"Edafolog\xc3\xada\",\n")
 file.write("                            \"type\": \"group\",\n")
 file.write("                            \"preserveOrder\": true,\n")
 file.write("                            \"items\": [\n")
 file.write("                                {\n")
 file.write("                                    \"layers\": \"igm_ca2022:v_suelo_a\",\n")
 file.write("                                    \"isEnabled\": true,\n")
 file.write("                                    \"isShown\": false,\n")
 file.write("                                    \"parameters\": {\n")
 file.write("                                        \"tiled\": true,\n")
 file.write("                                        \"style\": \"igm_ca22:stl_"+nom_ugesp(i[0]).lower()+"_ttdp\",\n")
 file.write("                                        \"CQL_FILTER\": \"ugesp_des='"+i[0]+"'\"\n")
 file.write("                                    },\n")
 file.write("                                    \"opacity\": 1,\n")
 file.write("                                    \"name\": \"Suelo\",\n")
 file.write("                                    \"getFeatureInfoFormats\": [\n")
 file.write("                                        {\n")
 file.write("                                            \"type\": \"json\"\n")
 file.write("                                        }\n")
 file.write("                                    ],\n")
 file.write("                                    \"url\": \"https://www.geoportaligm.gob.ec/igm_afc/igm_ca2022/wms?\",\n")
 file.write("                                    \"type\": \"wms\",\n")
 file.write("                                    \"featureInfoTemplate\": {\n")
 file.write("                                        \"name\": \"{{objeto}} - {{dpa_descan}}: {{ugesp_des}}\",\n")
 file.write("                                        \"template\": \"</style>\\n<table border='1' cellpadding='10' cellspacing='0' >\\n    <tbody>\\n      <tr>\\n        <td colspan='4' align='middle' ><b>Textura a partir de los 50 cm de PROFUNDIDAD</td>\\n      </tr>\\n      <tr>\\n        <td>Categor\xc3\xada</td>\\n        <td align='middle' colspan='4'>Superficie(ha)</td>\\n      </tr>\\n      <tr>\\n        <td>{{ttdp}}</td>\\n        <td align='middle' colspan='4'>{{ard}}</td>\\n      </tr>\\n      <tr>\\n        <td colspan='4' align='middle'><b>Pedregosidad</td>\\n      </tr>\\n      <tr>\\n        <td>Categor\xc3\xada</td>\\n        <td align='middle' colspan='4'>Superficie(ha)</td>\\n      </tr>\\n      <tr>\\n        <td>{{pdrc}}</td>\\n        <td align='middle' colspan='4'>{{ard}}</td>\\n                  <tr>\\n        <td colspan='4' align='middle'><b>Nivel Fre\xc3\xa1tico</td>\\n      </tr>\\n      <tr>\\n        <td>Categor\xc3\xada</td>\\n        <td align='middle' colspan='4'>Superficie(ha)</td>\\n      </tr>\\n      <tr>\\n        <td>{{nfc}}</td>\\n        <td align='middle' colspan='4'>{{ard}}</td>\\n                  <tr>\\n        <td colspan='4' align='middle'><b>Drenaje</td>\\n      </tr>\\n      <tr>\\n        <td>Categor\xc3\xada</td>\\n        <td align='middle' >S\xc3\xadmbolo</td>\\n        <td align='middle' >Superficie(ha)</td>\\n      </tr>\\n      <tr>\\n        <td>{{ndr}}</td>\\n        <td align='middle'>{{ndr_simb}}</td>\\n          <td align='middle'>{{ard}}</td>\\n    </tbody>\\n</body>\\n</html>\\n\"\n")
 file.write("                                    }  \n")
 file.write("                                },\n")
 file.write("                                {\n")
 file.write("                                    \"layers\": \"igm_ca2022:v_unidad_capacidad_uso_tierra_a\",\n")
 file.write("                                    \"isEnabled\": true,\n")
 file.write("                                    \"isShown\": false,\n")
 file.write("                                    \"parameters\": {\n")
 file.write("                                        \"tiled\": true,\n")
 file.write("                                        \"style\": \"igm_ca22:stl_"+nom_ugesp(i[0]).lower()+"_cut\",\n")
 file.write("                                        \"CQL_FILTER\": \"ugesp_des='"+(i[0])+"'\"\n")
 file.write("                                    },\n")
 file.write("                                    \"opacity\": 1,\n")
 file.write("                                    \"name\": \"Capacidad de Uso de las Tierras\",\n")
 file.write("                                    \"getFeatureInfoFormats\": [\n")
 file.write("                                        {\n")
 file.write("                                            \"type\": \"json\"\n")
 file.write("                                        }\n")
 file.write("                                    ],\n")
 file.write("                                    \"url\": \"https://www.geoportaligm.gob.ec/igm_afc/igm_ca2022/wms?\",\n")
 file.write("                                    \"type\": \"wms\",\n")
 file.write("                                    \"featureInfoTemplate\": {\n")
 file.write("                                        \"name\": \"{{objeto}} - {{dpa_descan}}: {{ugesp_des}}\",\n")
 file.write("                                        \"template\": \"</style>\\n<table border='1' cellpadding='10' cellspacing='0' >\\n     <tbody>\\n       <tr>\\n         <td colspan='4' align='middle' ><b>Capacidad de Uso de las Tierras</td>\\n       </tr>\\n       <tr>\\n         <td  align='middle'>Clase</td>\\n         <td>Unidad de manejo</td>\\n         <td>Superficie(ha)</td>\\n       </tr>\\n       <tr>\\n         <td>{{cag}}</td>\\n         <td align='middle'>{{udm}}</td>\\n         <td >{{ard}}</td>\\n       </tr>\\n     </tbody>\\n </body>\\n </html>\\n \"\n")
 file.write("                                    }  \n")
 file.write("                                }\n")
 file.write("                            ]\n")
 file.write("                        }\n")
 file.write("                    ]\n")
 file.write("                },\n")
 file.write("                {\n")
 file.write("                    \"name\": \"Unidad de Paisaje\",\n")
 file.write("                    \"type\": \"group\",\n")
 file.write("                    \"preserveOrder\": true,\n")
 file.write("                    \"layers\": \"igm_ca2022:v_perfil_suelo_2022\",\n")
 file.write("                    \"isEnabled\": true,\n")
 file.write("                    \"isShown\": false,\n")
 file.write("                    \"parameters\": {\n")
 file.write("                        \"tiled\": true,\n")
 file.write("                        \"CQL_FILTER\": \"ugesp_des='"+(i[0])+"'\"\n")
 file.write("                    },\n")
 file.write("                    \"opacity\": 1,\n")
 file.write("                    \"name\": \"Unidad de Paisaje\",\n")
 file.write("                    \"getFeatureInfoFormats\": [\n")
 file.write("                        {\n")
 file.write("                            \"type\": \"json\"\n")
 file.write("                        }\n")
 file.write("                    ],\n")
 file.write("                    \"url\": \"https://www.geoportaligm.gob.ec/igm_afc/igm_ca2022/wms?\",\n")
 file.write("                    \"type\": \"wms\",\n")
 file.write("                    \"featureInfoTemplate\": {\n")
 file.write("                        \"name\": \"Unidad de Paisaje\",\n")
 file.write("                        \"template\": \"</style>\\n<table border='1' cellpadding='10' cellspacing='0' >\\n<tbody>\\n<tr>\\n<td colspan='4' align='middle'>Unidad de Paisaje</td>\\n</tr>\\n<tr>\\n<td>provincia</td>\\n<td>canton</td>\\n <td>c\xc3\xb3digo perfil</td>\\n<td>Descarga</td>\\n</tr>\\n<tr>\\n        <td>\\n{{provincia}}</td>\\n                                <td >{{canton}}</td>\\n                                <td>{{codigo_perfil}}</td>\\n                               <td><a href='{{link}}' target='_blank'>{{link}}</a>\\n                              </tr>\\n                              <tr >\\n                                  </tr>\\n                                </tbody>\\n                            </table>\\n                            </body>\\n                   </html>\\n\"\n")
 file.write("                    }  \n")
 file.write("                },\n")
 file.write("                {\n")
 file.write("                    \"name\": \"\xc3\x81rea de Estudio\",\n")
 file.write("                    \"type\": \"group\",\n")
 file.write("                    \"preserveOrder\": true,\n")
 file.write("                    \"layers\": \"igm_ca2022:v_areas_estudio\",\n")
 file.write("                    \"isEnabled\": true,\n")
 file.write("                    \"isShown\": true,\n")
 file.write("                    \"parameters\": {\n")
 file.write("                        \"tiled\": true,\n")
 file.write("                        \"CQL_FILTER\": \"ugesp_des='"+i[0]+"'\"\n")
 file.write("                    },\n")
 file.write("                    \"opacity\": 1,\n")
 file.write("                    \"name\": \"\xc3\x81rea de Estudio\",\n")
 file.write("                    \"getFeatureInfoFormats\": [\n")
 file.write("                        {\n")
 file.write("                            \"type\": \"html\"\n")
 file.write("                        }\n")
 file.write("                    ],\n")
 file.write("                    \"url\": \"https://www.geoportaligm.gob.ec/igm_afc/igm_ca2022/wms?\",\n")
 file.write("                    \"type\": \"wms\"\n")
 file.write("                },\n")
 file.write("                {\n")
 file.write("                    \"name\": \"Descargar Informaci\xc3\xb3n\",\n")
 file.write("                    \"type\": \"group\",\n")
 file.write("                    \"preserveOrder\": true,\n")
 file.write("                    \"isEnabled\": false,\n")
 file.write("                    \"name\": \"Descarga de Informaci\xc3\xb3n\",\n")
 file.write("                    \"type\": \"url-template\",\n")
 file.write("                    \"dataUrl\": \"https://www.geoportaligm.gob.ec/nextcloud/index.php/s/"+nom_ugesp(i[0])+"\"\n")
 file.write("                }\n")
 file.write("            ]\n")
 file.write("        }\n")
 file.write("    ]\n")
 file.write("}\n")
 file.close()
 