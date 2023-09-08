# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# TOPO_COMPLETA.py
# Created on: 2022-04-27 15:25:08.00000
# Usage: FERNANDA SALGADO <GDB> 
# Description: 
# ---------------------------------------------------------------------------

# Set the necessary product code
import arceditor


# Import arcpy module

import arcpy, os


arcpy.env.overwriteOutput = True

# Script arguments
GDB = arcpy.GetParameterAsText(0)

#Valor de la capa
arcpy.env.workspace = GDB

datasets = arcpy.ListDatasets()
arcpy.AddMessage("____________________________________________________________")
for j in datasets:

 DATASET = arcpy.os.path.join(GDB,j)
 arcpy.env.workspace = DATASET
 arcpy.AddMessage("DATASET: "+ j)
 fc = arcpy.ListFeatureClasses()
 for i in fc:
  f_classes = arcpy.os.path.join(DATASET,i)
  nam = arcpy.Describe(f_classes)
  if nam.shapeType == "Polygon":
   CAPA = f_classes
   topology_point = arcpy.os.path.join(GDB, DATASET, str(i)+ "_topology_point")
   topology_line = arcpy.os.path.join(GDB, DATASET, str(i)+"_topology_line")
   topology_poly = arcpy.os.path.join(GDB, DATASET, str(i)+ "_topology_poly")
   TOPO = arcpy.CreateTopology_management(DATASET, str(i)+"_topology")
   TOPO = arcpy.os.path.join(DATASET,str(i)+"_topology")
   arcpy.AddFeatureClassToTopology_management(TOPO, CAPA, "1", "1")
   arcpy.AddRuleToTopology_management(TOPO, "Must Not Have Gaps (Area)", CAPA, "", "", "")
   arcpy.AddRuleToTopology_management(TOPO, "Must Not Overlap (Area)", CAPA, "", "", "")
   arcpy.ValidateTopology_management(TOPO, "Full_Extent")
   arcpy.ExportTopologyErrors_management(TOPO, DATASET, str(i)+"_topology")
   arcpy.AddMessage("Feature Class: "+ i)
   t_point = arcpy.GetCount_management(topology_point)
   t_line = arcpy.GetCount_management(topology_line)
   t_poly = arcpy.GetCount_management(topology_poly)
   topology_line= arcpy.Rename_management(topology_line, arcpy.os.path.join(GDB, DATASET, str(i)+"_topology_gaps"))
   topology_poly=arcpy.Rename_management(topology_poly, arcpy.os.path.join(GDB, DATASET, str(i)+ "_topology_overlaps"))   
   if str(t_point) == '0':
    arcpy.AddMessage("PUNTOS: "+ str(t_point))
    arcpy.Delete_management(topology_point)
    arcpy.Delete_management(TOPO) 
   else: 
    arcpy.AddWarning("PUNTOS: " + str(t_point))
    
   if str(t_poly) == '0':
    arcpy.AddMessage("OVERLAP'S: " + str(t_poly))
    arcpy.Delete_management(topology_poly)
    arcpy.Delete_management(TOPO) 
   else: 
    arcpy.AddWarning("OVERLAP'S: " + str(t_poly))
    arcpy.Delete_management(TOPO)
   if str(t_line) == '1':
    arcpy.AddMessage("GAP'S: " + str(t_line))
    arcpy.Delete_management(TOPO)
    arcpy.Delete_management(topology_line) 
   else: 
    arcpy.AddWarning("GAP'S: " + str(t_line))
    arcpy.Delete_management(TOPO)
    arcpy.Delete_management(topology_line)
 del i
 arcpy.AddMessage("____________________________________________________________")
