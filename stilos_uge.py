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
 else:
  return abrev

path1= arcpy.os.path.join(carpeta,"stl_"+nom_ugesp(ciudad).lower()+"_geomorfologia.sld")
file = open(path1, "w")

file.write("<?xml version='1.0' encoding='UTF-8'?>\n")
file.write("<StyledLayerDescriptor xmlns='http://www.opengis.net/se' xmlns:xlink='http://www.w3.org/1999/xlink' version='1.1.0' xsi:schemaLocation='http://www.opengis.net/se http://schemas.opengis.net/se/1.1.0/StyledLayerDescriptor.xsd' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:ogc='http://www.opengis.net/ogc' xmlns:se='http://www.opengis.net/se'>\n")
file.write("  <NamedLayer>\n")
file.write("    <se:Name>Unidad gen\xc3\xa9tica</se:Name>\n")
file.write("    <UserStyle>\n")
file.write("      <se:Name>UUnidad gen\xc3\xa9tica</se:Name>\n")
file.write("      <se:FeatureTypeStyle>\n")
file.write("        <se:Rule>\n")
file.write("          <se:Description>\n")
file.write("            <se:Title>Unidad gen\xc3\xa9tica</se:Title>\n")
file.write("          </se:Description>\n")
for i in capa:
      if i.getValue("uge") == "TECNOGENESIS":
        file.write("        </se:Rule>\n")
        file.write("        <se:Rule>\n")
        file.write("          <se:Name>TECNOGENESIS</se:Name>\n")
        file.write("          <se:Description>\n")
        file.write("            <se:Title>TECNOGENESIS</se:Title>\n")
        file.write("          </se:Description>\n")
        file.write("          <ogc:Filter xmlns:ogc='http://www.opengis.net/ogc'>\n")
        file.write("            <ogc:PropertyIsEqualTo>\n")
        file.write("              <ogc:PropertyName>uge</ogc:PropertyName>\n")
        file.write("              <ogc:Literal>TECNOGENESIS</ogc:Literal>\n")
        file.write("            </ogc:PropertyIsEqualTo>\n")
        file.write("          </ogc:Filter>\n")
        file.write("          <se:PolygonSymbolizer>\n")
        file.write("            <se:Fill>\n")
        file.write("                            <se:GraphicFill>\n")
        file.write("                                <se:Graphic>\n")
        file.write("                                    <se:Mark>\n")
        file.write("                                        <se:WellKnownName>shape://slash</se:WellKnownName>\n")
        file.write("                                        <se:Stroke>\n")
        file.write("                                            <se:SvgParameter name='stroke'>#6e6e6e</se:SvgParameter>\n")
        file.write("					      <se:SvgParameter name='stroke-width'>1</se:SvgParameter>\n")
        file.write("                                        </se:Stroke>\n")
        file.write("                                    </se:Mark>\n")
        file.write("				     <se:Size>7</se:Size>\n")
        file.write("                                </se:Graphic>\n")
        file.write("                            </se:GraphicFill>\n")
        file.write("                        </se:Fill>\n")
        file.write("            <se:Stroke>\n")
        file.write("              <se:SvgParameter name='stroke'>#232323</se:SvgParameter>\n")
        file.write("              <se:SvgParameter name='stroke-opacity'>0</se:SvgParameter>\n")
        file.write("              <se:SvgParameter name='stroke-width'>1</se:SvgParameter>\n")
        file.write("              <se:SvgParameter name='stroke-linejoin'>bevel</se:SvgParameter>\n")
        file.write("            </se:Stroke>\n")
        file.write("          </se:PolygonSymbolizer>\n")
      else:
       file.write("        </se:Rule>\n")
       file.write("        <se:Rule>\n")
       file.write("          <se:Name>"+i.getValue("UGE")+"</se:Name>\n")
       file.write("          <se:Description>\n")
       file.write("            <se:Title>"+i.getValue("UGE")+"</se:Title>\n")
       file.write("          </se:Description>\n")
       file.write("          <ogc:Filter xmlns:ogc='http://www.opengis.net/ogc'>\n")
       file.write("            <ogc:PropertyIsEqualTo>\n")
       file.write("              <ogc:PropertyName>uge</ogc:PropertyName>\n")
       file.write("              <ogc:Literal>"+i.getValue("UGE")+"</ogc:Literal>\n")
       file.write("            </ogc:PropertyIsEqualTo>\n")
       file.write("          </ogc:Filter>\n")
       file.write("          <se:PolygonSymbolizer>\n")
       file.write("            <se:Fill>\n")
       file.write(i.getValue("fill")+"\n")
       file.write(i.getValue("opacity")+"\n")
       file.write("            </se:Fill>\n")
       file.write("            <se:Stroke>\n")
       file.write("              <se:SvgParameter name='stroke'>#232323</se:SvgParameter>\n")
       file.write("              <se:SvgParameter name='stroke-opacity'>0</se:SvgParameter>\n")
       file.write("              <se:SvgParameter name='stroke-width'>1</se:SvgParameter>\n")
       file.write("              <se:SvgParameter name='stroke-linejoin'>bevel</se:SvgParameter>\n")
       file.write("            </se:Stroke>\n")
       file.write("          </se:PolygonSymbolizer>\n")

file.write("                </se:Rule>\n")
file.write("      </se:FeatureTypeStyle>\n")
file.write("    </UserStyle>\n")
file.write("  </NamedLayer>\n")
file.write("</StyledLayerDescriptor>")
file.close()
