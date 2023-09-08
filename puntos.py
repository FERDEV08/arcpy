import arcpy
arcpy.env.overwriteOutput = True

capa = GDB = arcpy.GetParameterAsText(0)
capa=arcpy.SearchCursor(capa)
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





path1= arcpy.os.path.join(carpeta,"stl_"+nom_ugesp(ciudad).lower()+"_puntos_geom.sld")
file = open(path1, "w")

file.write(" <?xml version='1.0' encoding='utf-8'?>\n")
file.write("<StyledLayerDescriptor xmlns='http://www.opengis.net/sld' xmlns:ogc='http://www.opengis.net/ogc' xmlns:xlink='http://www.w3.org/1999/xlink' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' version='1.0.0' xsi:schemaLocation='http://www.opengis.net/sld StyledLayerDescriptor.xsd'>\n")
file.write("  <NamedLayer>\n")
file.write("    <Name>puntos_geom</Name>\n")
file.write("    <UserStyle>\n")
file.write("      <Title>puntos_geom</Title>\n")
file.write("      <FeatureTypeStyle>\n")
file.write("\n")
file.write("\n")
file.write("\n")

file.write("")
for i in capa:
 
 if i.getValue("geof_p") == "TERRAZA":
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>30000</MaxScaleDenominator>\n")
  file.write("          <Name>TERRAZA</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>TERRAZA</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/terraza.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>32</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>\n")


 elif i.getValue("geof_P") == "CHEVRON":
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>CHEVRON</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>CHEVRON</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/chevron.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>32</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>\n")

 elif i.getValue("geof_P") == "CUESTA":
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>CUESTA</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>CUESTA</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/cuesta.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>32</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>\n")
 
 elif i.getValue("geof_P") == "EROSION ANTROPICA_135":
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>EROSION ANTROPICA</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>EROSION ANTROPICA_135</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/erosion_antropica_135.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>32</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>\n")
 
 elif i.getValue("geof_P") == "EROSION ANTROPICA_225":
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>EROSION ANTROPICA</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>EROSION ANTROPICA_225</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/erosion_antropica_225.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>32</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>\n")

 elif i.getValue("geof_P") == "EROSION ANTROPICA_270":
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>EROSION ANTROPICA</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>EROSION ANTROPICA_270</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/erosion_antropica_270.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>32</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>\n")

 elif i.getValue("geof_P") == "EROSION ANTROPICA_315":
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>EROSION ANTROPICA</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>EROSION ANTROPICA_315</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/erosion_antropica_315.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>32</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>\n")

 elif i.getValue("geof_P") == "EROSION ANTROPICA_45":
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>EROSION ANTROPICA</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>EROSION ANTROPICA_45</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/erosion_antropica_45.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>32</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>   \n")

 elif i.getValue("geof_P") == "EROSION ANTROPICA_90":
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>EROSION ANTROPICA</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>EROSION ANTROPICA_90</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/erosion_antropica_90.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>          \n")

 elif i.getValue("geof_P") == "EROSION DEL CAUCE_90":
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>EROSION DEL CAUCE</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>EROSION DEL CAUCE_90</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/erosion_cauce_90.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>           \n")
 
 elif i.getValue("geof_P") == "EROSION LAMINAR_180": 
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>EROSION LAMINAR</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>EROSION LAMINAR_180</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/erosion_laminar_180.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>         \n")

 elif i.getValue("geof_P") == "EROSION LAMINAR_270": 
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>EROSION LAMINAR</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>EROSION LAMINAR_270</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/erosion_laminar_270.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>        \n")

 elif i.getValue("geof_P") == "EROSION LAMINAR_360": 
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>EROSION LAMINAR</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>EROSION LAMINAR_360</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/erosion_laminar_360.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>           \n")

 elif i.getValue("geof_P") == "EROSION LAMINAR_45": 
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>EROSION LAMINAR</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>EROSION LAMINAR_45</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/erosion_laminar_45.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>           \n")

 elif i.getValue("geof_P") == "GLACIS DE ESPARCIMIENTO_135": 
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>GLACIS DE ESPARCIMIENTO</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>GLACIS DE ESPARCIMIENTO_135</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/glacis_esparcimiento_135.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>  \n")

 elif i.getValue("geof_P") == "GLACIS DE ESPARCIMIENTO_180": 
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>GLACIS DE ESPARCIMIENTO</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>GLACIS DE ESPARCIMIENTO_180</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/glacis_esparcimiento_180.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>         \n")

 elif i.getValue("geof_P") == "GLACIS DE ESPARCIMIENTO_225": 
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>GLACIS DE ESPARCIMIENTO</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>GLACIS DE ESPARCIMIENTO_225</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/glacis_esparcimiento_225.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule> \n")

 elif i.getValue("geof_P") == "GLACIS DE ESPARCIMIENTO_270": 
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>GLACIS DE ESPARCIMIENTO</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>GLACIS DE ESPARCIMIENTO_270</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/glacis_esparcimiento_270.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>\n")

 elif i.getValue("geof_P") == "GLACIS DE ESPARCIMIENTO_315": 
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>GLACIS DE ESPARCIMIENTO</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>GLACIS DE ESPARCIMIENTO_315</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/glacis_esparcimiento_315.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>  \n")

 elif i.getValue("geof_P") == "GLACIS DE ESPARCIMIENTO_360": 
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>GLACIS DE ESPARCIMIENTO</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>GLACIS DE ESPARCIMIENTO_360</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/glacis_esparcimiento_360.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>  \n")
 
 elif i.getValue("geof_P") == "GLACIS DE ESPARCIMIENTO_45": 
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>GLACIS DE ESPARCIMIENTO</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>GLACIS DE ESPARCIMIENTO_45</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/glacis_esparcimiento_45.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>  \n")
 
 elif i.getValue("geof_P") == "GLACIS DE ESPARCIMIENTO_90": 
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>GLACIS DE ESPARCIMIENTO</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>GLACIS DE ESPARCIMIENTO_90</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/glacis_esparcimiento_90.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>          \n")

 elif i.getValue("geof_P") == "MESA": 
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>MESA</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>MESA</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <Mark>\n")
  file.write("                <WellKnownName>ttf://DejaVu Sans Condensed#0x002B</WellKnownName>\n")
  file.write("                <Fill>\n")
  file.write("                  <CssParameter name='fill'>#9900FF</CssParameter>\n")
  file.write("                  <CssParameter name='fill-opacity'>1</CssParameter>\n")
  file.write("                </Fill>\n")
  file.write("                <Stroke>\n")
  file.write("                  <CssParameter name='stroke'>#9900FF</CssParameter>\n")
  file.write("                  <CssParameter name='stroke-width'>2</CssParameter>\n")
  file.write("                </Stroke>\n")
  file.write("              </Mark>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>\n")

 elif i.getValue("geof_P") == "MESA MARINA": 
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>MESA MARINA</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>MESA MARINA</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <Mark>\n")
  file.write("                <WellKnownName>ttf://DejaVu Sans Condensed#0x002B</WellKnownName>\n")
  file.write("                <Fill>\n")
  file.write("                  <CssParameter name='fill'>#00FFFF</CssParameter>\n")
  file.write("                  <CssParameter name='fill-opacity'>1</CssParameter>\n")
  file.write("                </Fill>\n")
  file.write("                <Stroke>\n")
  file.write("                  <CssParameter name='stroke'>#00FFFF</CssParameter>\n")
  file.write("                  <CssParameter name='stroke-width'>2</CssParameter>\n")
  file.write("                </Stroke>\n")
  file.write("              </Mark>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>         \n")

 elif i.getValue("geof_P") == "VERTIENTE ABRUPTA_225":
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>VERTIENTE ABRUPTA</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>VERTIENTE ABRUPTA_225</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/vertiente_abrupta_225.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>         \n")

 elif i.getValue("geof_P") == "VERTIENTE ABRUPTA_270":
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>VERTIENTE ABRUPTA</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>VERTIENTE ABRUPTA_270</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/vertiente_abrupta_270.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>          \n")

 elif i.getValue("geof_P") == "VERTIENTE ABRUPTA_45":
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>VERTIENTE ABRUPTA</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>VERTIENTE ABRUPTA_45</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/vertiente_abrupta_45.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>          \n")

 elif i.getValue("geof_P") == "CALDERA":
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>CALDERA</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>CALDERA</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/caldera.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>          \n")  
  
 elif i.getValue("geof_P") == "CRATER":
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>CRATER</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>CRATER</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/crater.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>          \n")  
  
 elif i.getValue("geof_P") == "EROSION ANTROPICA_360":
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>EROSION ANTROPICA_360</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>EROSION ANTROPICA_360</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/erosion_antropica_360.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>          \n")  
  
 elif i.getValue("geof_P") == "EROSION DEL CAUCE_180":
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>EROSION DEL CAUCE_180</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>EROSION DEL CAUCE_180</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/erosion_cauce_180.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>          \n")  

 elif i.getValue("geof_P") == "EROSION LAMINAR_135":
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>EROSION LAMINAR_135</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>EROSION LAMINAR_135</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/erosion_laminar_135.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>          \n")  

 elif i.getValue("geof_P") == "EROSION LAMINAR_90":
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>EROSION LAMINAR_135</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>EROSION LAMINAR_90</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/erosion_laminar_90.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>          \n")  

 elif i.getValue("geof_P") == "VERTIENTE ABRUPTA_135":
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>VERTIENTE ABRUPTA_135</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>VERTIENTE ABRUPTA_135</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/erosion_abrupta_135.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>          \n")  

 elif i.getValue("geof_P") == "VERTIENTE ABRUPTA_180":
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>VERTIENTE ABRUPTA_180</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>VERTIENTE ABRUPTA_180</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/erosion_abrupta_180.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>          \n")  

 elif i.getValue("geof_P") == "VERTIENTE ABRUPTA_360":
  file.write("        <Rule>\n")
  file.write("          <MaxScaleDenominator>20000.0</MaxScaleDenominator>\n")
  file.write("          <Name>VERTIENTE ABRUPTA_360</Name>\n")
  file.write("          <ogc:Filter>\n")
  file.write("            <ogc:PropertyIsEqualTo>\n")
  file.write("              <ogc:PropertyName>geof_p</ogc:PropertyName>\n")
  file.write("              <ogc:Literal>VERTIENTE 360</ogc:Literal>\n")
  file.write("            </ogc:PropertyIsEqualTo>\n")
  file.write("          </ogc:Filter>\n")
  file.write("          <PointSymbolizer>\n")
  file.write("            <Graphic>\n")
  file.write("              <ExternalGraphic>\n")
  file.write("                <OnlineResource\n")
  file.write("                                xlink:type='simple'\n")
  file.write("                                xlink:href='https://www.geoportaligm.gob.ec/visualizador_ca/estilos_geomorfologia/itc/erosion_abrupta_360.png' />\n")
  file.write("                <Format>image/png</Format>\n")
  file.write("              </ExternalGraphic>\n")
  file.write("              <Size>50</Size>\n")
  file.write("            </Graphic>\n")
  file.write("          </PointSymbolizer>\n")
  file.write("        </Rule>          \n")  



else:
  file.write("\n")

file.write("      </FeatureTypeStyle>\n")
file.write("    </UserStyle>\n")
file.write("  </NamedLayer>\n")
file.write("</StyledLayerDescriptor>\n")  
 
file.close()
