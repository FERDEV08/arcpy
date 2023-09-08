#libreries
import arcpy
GDB_DOMAINS = arcpy.GetParameterAsText(0)
fc = arcpy.GetParameterAsText (1)
dominio = arcpy.GetParameterAsText (2)
dominio = dominio.split(';')

gdb_domains = arcpy.da.ListDomains(GDB_DOMAINS)

arcpy.AddMessage(type(dominio))

for h in dominio:
 arcpy.AddMessage ("ESTE DOMINIO ESTA VERIFICANDO:    "+ str(h))
 for i in gdb_domains:
  if i.name == h:
   domain = i
   arcpy.AddMessage (str(domain.name))
 
 arcpy.AddField_management(fc,str(h)+"1","LONG")

 if domain.name == h:        
  if domain.domainType == 'CodedValue':
   coded_values = domain.codedValues
   cursor = arcpy.da.UpdateCursor(fc,[str(h),str(h) +"1"])
   for row in cursor:
    for val, desc in coded_values.iteritems():
     if (str(val)+'.- '+row[0].encode('latin1')== desc.encode('latin1')) or (row[0].encode('latin1')==desc.encode('latin1')):
      row[1]=(val)
      arcpy.AddMessage (str(desc.encode('latin1')))
      cursor.updateRow(row)

 arcpy.DeleteField_management(fc,str(h))
 arcpy.AddField_management(fc,str(h),"LONG")
 cursor1 = arcpy.da.UpdateCursor(fc,[str(h),str(h) +"1"])
 for row1 in cursor1:
     row1[0]=row1[1]
     cursor1.updateRow(row1)
 arcpy.DeleteField_management(fc,str(h)+"1") 
