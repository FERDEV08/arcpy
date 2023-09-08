# Set the necessary product code
import arcpy
from zipfile import ZipFile
import os
from os.path import basename
import re

arcpy.env.overwriteOutput = True

# Script arguments
Folder = arcpy.GetParameterAsText(0)

arcpy.env.workspace = Folder
files = arcpy.ListFeatureClasses()
F = []
for i in files:
 F.append(i[:-4])

arcpy.AddMessage('archivos: ' + str(F))

def zipFilesInDir(dirName, zipFileName, filter):
 for folderName, subfolders, filenames in os.walk(dirName):
  with ZipFile(zipFileName, 'w') as zipObj:
   for filename in filenames:
    if filter(filename):
     filePath = os.path.join(folderName, filename)
     zipObj.write(filePath, basename(filePath))
del i
for i in F:
     niv_socioec = '^niv_socioec_'
     n_instruccion = '^n_instruccion'
     cob_uso = '^cob_uso'
     u_geom = '^u_geom'
     apfc = '^apfc'
     ca = '^ca'
     cuc = '^cuc'
     cuex = '^cuex'
     densidad_pob = '^densidad_pob'
     serv_basicos = '^serv_basicos'
     u_cut = '^u_cut'
     if re.match(niv_socioec,i):
         h = i.split('niv_socioec_')
         nam = ('niv_socioec_'+h[1])
	 zipFilesInDir(Folder, arcpy.os.path.join(Folder,nam+'.zip'), lambda name: i in name)
     elif re.match(cob_uso,i):
         h = i.split('cob_uso')
         nam = ('cob_uso'+h[1])
	 zipFilesInDir(Folder, arcpy.os.path.join(Folder,nam+'.zip'), lambda name: i in name)
     elif re.match(u_geom,i):
         h = i.split('u_geom_')
         nam = ('u_geom_'+h[1])
	 zipFilesInDir(Folder, arcpy.os.path.join(Folder,nam+'.zip'), lambda name: i in name)
     elif re.match(apfc,i):
         h = i.split('apfc')
         nam = ('apfc'+h[1])
	 zipFilesInDir(Folder, arcpy.os.path.join(Folder,nam+'.zip'), lambda name: i in name)
     elif re.match(ca,i):
         h = i.split('ca')
         nam = ('ca_'+h[1])
	 zipFilesInDir(Folder, arcpy.os.path.join(Folder,nam+'.zip'), lambda name: i in name)
     elif re.match(cuc,i):
         h = i.split('cuc')
         nam =('cuc'+h[1])
	 zipFilesInDir(Folder, arcpy.os.path.join(Folder,nam+'.zip'), lambda name: i in name)
     elif re.match(cuex,i):
         h = i.split('cuex')
         nam = ('cuex'+h[1])
	 zipFilesInDir(Folder, arcpy.os.path.join(Folder,nam+'.zip'), lambda name: i in name)
     elif re.match(n_instruccion,i):
         h = i.split('n_instruccion_')
         nam = ('n_instruccion_'+h[1])
	 zipFilesInDir(Folder, arcpy.os.path.join(Folder,nam+'.zip'), lambda name: i in name)
     elif re.match(u_cut,i):
         h = i.split('u_cut')
         nam = ('u_cut'+h[1])
	 zipFilesInDir(Folder, arcpy.os.path.join(Folder,nam+'.zip'), lambda name: i in name)
     elif re.match(densidad_pob,i):
         h = i.split('densidad_pob')
         nam = ('densidad_pob'+h[1])
	 zipFilesInDir(Folder, arcpy.os.path.join(Folder,nam+'.zip'), lambda name: i in name)
     elif re.match(serv_basicos,i):
         h = i.split('serv_basicos')
         nam = ('serv_basicos'+h[1])
	 zipFilesInDir(Folder, arcpy.os.path.join(Folder,nam+'.zip'), lambda name: i in name)
     else:
         zipFilesInDir(Folder, arcpy.os.path.join(Folder, i +'.zip'), lambda name: i in name)

del i


arcpy.AddMessage("====================================================")
arcpy.AddMessage("=============Proceso finalizado=====================")
arcpy.AddMessage("====================================================")

arcpy.AddMessage("********* Elaborado: FERNANDA SALGADO  *************")

 
