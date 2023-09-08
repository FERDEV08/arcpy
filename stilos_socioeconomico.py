# -*- coding: latin-1 -*-
import os, arcpy
arcpy.env.overwriteOutput = True

capa=arcpy.GetParameterAsText(0)
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

path1= arcpy.os.path.join(carpeta,"_densidad_pob_a_"+nom_ugesp(ciudad).lower()+".sld")
file = open(path1, "w")


file.write("<?xml version='1.0' encoding='UTF-8'?>\n")
file.write("<StyledLayerDescriptor xmlns='http://www.opengis.net/sld' xmlns:ogc='http://www.opengis.net/ogc' xmlns:se='http://www.opengis.net/se' version='1.1.0' xsi:schemaLocation='http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd' xmlns:xlink='http://www.w3.org/1999/xlink' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'>")
file.write("  <NamedLayer>")
file.write("    <se:Name>v_densidad_pob_a_"+nom_ugesp(ciudad).lower()+"</se:Name>")
file.write("    <UserStyle>")
file.write("      <se:Name>v_densidad_pob_a_"+nom_ugesp(ciudad).lower()+"</se:Name>")
file.write("      <se:FeatureTypeStyle>")
file.write("        <se:Rule>")
file.write("          <se:Description>")
file.write("            <se:Title>Densidad poblacional</se:Title>")
file.write("          </se:Description>")
file.write("        </se:Rule>")


capa=arcpy.da.SearchCursor(capa,['depo'])
for i in capa:
      file.write("                </sld:Rule>\n")
      file.write("                <sld:Rule>\n")
      file.write("                    <sld:Name>"+i[0]+"</sld:Name>\n")
      file.write("                    <sld:Title>"+i[0]+"</sld:Title>\n")
      file.write("                    <ogc:Filter>\n")
      file.write("                        <ogc:PropertyIsEqualTo>\n")
      file.write("                            <ogc:PropertyName>nis</ogc:PropertyName>\n")
      file.write("                            <ogc:Literal>"+i[0]+"</ogc:Literal>\n")
      file.write("                        </ogc:PropertyIsEqualTo>\n")
      file.write("                    </ogc:Filter>\n")
      file.write("                    <sld:PolygonSymbolizer>\n")
      file.write("                        <sld:Fill>\n")
      file.write(i[1]+"\n")
      file.write("                             <sld:CssParameter name='fill-opacity'>0.5</sld:CssParameter>\n")
      file.write("                        </sld:Fill>\n")
      file.write("                    </sld:PolygonSymbolizer>\n")
file.write("                </sld:Rule>\n")
file.write("			</sld:FeatureTypeStyle>\n")
file.write("        </sld:UserStyle>\n")
file.write("    </sld:UserLayer>\n")
file.write("</sld:StyledLayerDescriptor>")
file.close()
