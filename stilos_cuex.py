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
  
 elif abrev =="PUERTO EL CARMEN DEL PUTUMAYO":
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

path1= arcpy.os.path.join(carpeta,"stl_"+nom_ugesp(ciudad).lower()+"_cuex.sld")
file = open(path1, "w")


file.write("<?xml version='1.0' encoding='UTF-8'?>\n")
file.write("<sld:StyledLayerDescriptor xmlns='http://www.opengis.net/sld' xmlns:sld='http://www.opengis.net/sld' xmlns:ogc='http://www.opengis.net/ogc' xmlns:gml='http://www.opengis.net/gml' version='1.0.0'>\n")
file.write("    <sld:UserLayer>\n")
file.write("        <sld:LayerFeatureConstraints>\n")
file.write("            <sld:FeatureTypeConstraint/>\n")
file.write("        </sld:LayerFeatureConstraints>\n")
file.write("        <sld:UserStyle>\n")
file.write("            <sld:Name>Default Styler</sld:Name>\n")
file.write("            <sld:FeatureTypeStyle>\n")
file.write("                <sld:Name>group 0</sld:Name>\n")
file.write("                <sld:FeatureTypeName>Feature</sld:FeatureTypeName>\n")
file.write("                <sld:Rule>\n")
file.write("                    <sld:Name>Categor\xc3\xadas de conflictos de uso para zonas en expansi\xc3\xb3n</sld:Name>\n")
file.write("                    <sld:Title>Categor\xc3\xadas de conflictos de uso para zonas en expansi\xc3\xb3n</sld:Title>\n")
file.write("                    <sld:MinScaleDenominator>1000.0</sld:MinScaleDenominator>\n")
file.write("                    <sld:MaxScaleDenominator>450000.0</sld:MaxScaleDenominator>\n")
file.write("                    <sld:TextSymbolizer>\n")
file.write("                        <sld:Font>\n")
file.write("                            <sld:CssParameter name='font-family'>Dialog</sld:CssParameter>\n")
file.write("                            <sld:CssParameter name='font-size'>7.0</sld:CssParameter>\n")
file.write("                            <sld:CssParameter name='font-style'>italic</sld:CssParameter>\n")
file.write("                            <sld:CssParameter name='font-weight'>bold</sld:CssParameter>\n")
file.write("                        </sld:Font>\n")
file.write("                        <sld:LabelPlacement>\n")
file.write("                            <sld:PointPlacement>\n")
file.write("                                <sld:AnchorPoint>\n")
file.write("                                    <sld:AnchorPointX>0.5</sld:AnchorPointX>\n")
file.write("                                    <sld:AnchorPointY>0.0</sld:AnchorPointY>\n")
file.write("                                </sld:AnchorPoint>\n")
file.write("                                <sld:Displacement>\n")
file.write("                                    <sld:DisplacementX>0.5</sld:DisplacementX>\n")
file.write("                                    <sld:DisplacementY>0.0</sld:DisplacementY>\n")
file.write("                                </sld:Displacement>\n")
file.write("                                <sld:Rotation>345</sld:Rotation>\n")
file.write("                            </sld:PointPlacement>\n")
file.write("                        </sld:LabelPlacement>\n")
file.write("                        <sld:Fill>\n")
file.write("                            <sld:CssParameter name='fill'>#460000</sld:CssParameter>\n")
file.write("                           <sld:CssParameter name='fill-opacity'>0.8</sld:CssParameter>\n")
file.write("                       </sld:Fill>\n")
file.write("                       <sld:VendorOption name='autoWrap'>110</sld:VendorOption>\n")
file.write("                        <sld:VendorOption name='spaceAround'>30</sld:VendorOption>\n")
file.write("                    </sld:TextSymbolizer>\n")

capa=arcpy.da.SearchCursor(capa,['CUEX_1','fill'])
for i in capa:
   if i[0] =="NO APLICA":
       file.write("                </sld:Rule>\n                <sld:Rule>\n                    <sld:Name>NO APLICA</sld:Name>\n                    <sld:Title>NO APLICA</sld:Title>\n\n                    <ogc:Filter>\n                        <ogc:PropertyIsEqualTo>\n                            <ogc:PropertyName>cuc</ogc:PropertyName>\n                            <ogc:Literal>NO APLICA</ogc:Literal>\n                        </ogc:PropertyIsEqualTo>\n                    </ogc:Filter> \n                    <sld:PolygonSymbolizer>\n                        <sld:Fill>\n                            <sld:GraphicFill>\n                                <sld:Graphic>\n                                    <sld:Mark>\n                                        <sld:WellKnownName>shape://slash</sld:WellKnownName>\n                                        <sld:Stroke>\n                                            <sld:CssParameter name='stroke'>#6e6e6e</sld:CssParameter>\n                                            <sld:CssParameter name='stroke-width'>1</sld:CssParameter>\n     \n                                  </sld:Stroke>\n                                    </sld:Mark>\n                                    <sld:Size>7</sld:Size>\n                                </sld:Graphic>\n                            </sld:GraphicFill>  \n                        </sld:Fill>\n                    </sld:PolygonSymbolizer>\n")
   else:
       file.write("                </sld:Rule>\n")
       file.write("                <sld:Rule>\n")
       file.write("                    <sld:Name>"+i[0]+"</sld:Name>\n")
       file.write("                    <sld:Title>"+i[0]+"</sld:Title>\n")
       file.write("                    <ogc:Filter>\n")
       file.write("                        <ogc:PropertyIsEqualTo>\n")
       file.write("                            <ogc:PropertyName>cuex</ogc:PropertyName>\n")
       file.write("                            <ogc:Literal>"+i[0]+"</ogc:Literal>\n")
       file.write("                        </ogc:PropertyIsEqualTo>\n")
       file.write("                    </ogc:Filter>\n")
       file.write("                    <sld:PolygonSymbolizer>\n")
       file.write("                        <sld:Fill>\n")
       file.write("                            <sld:GraphicFill>\n")
       file.write("                                <sld:Graphic>\n")
       file.write("                                    <sld:ExternalGraphic>\n")
       file.write(i[1]+"\n")
       file.write("                                        <sld:Format>image/png</sld:Format>\n")
       file.write("                                    </sld:ExternalGraphic>\n")
       file.write("                                </sld:Graphic>\n")
       file.write("                            </sld:GraphicFill>\n")
       file.write("                        </sld:Fill>\n")
       file.write("                    </sld:PolygonSymbolizer>\n")
               
file.write("                </sld:Rule>\n")
file.write("			</sld:FeatureTypeStyle>\n")
file.write("        </sld:UserStyle>\n")
file.write("    </sld:UserLayer>\n")
file.write("</sld:StyledLayerDescriptor>")
file.close()
