# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# topología3.py
# Created on: 2022-04-27 15:25:08.00000
# Usage: topología3 <GDB> 
# Description: 
# ---------------------------------------------------------------------------

# Set the necessary product code
import arceditor


# Import arcpy module
import arcpy, os

arcpy.env.overwriteOutput = True

# Script arguments
GDB = arcpy.GetParameterAsText(0)

DATASET = arcpy.os.path.join (GDB, "GEOMORFOLOGIA")

#Valor de la capa
arcpy.env.workspace = DATASET
fc = arcpy.ListFeatureClasses()

for i in fc:
 f_classes = arcpy.os.path.join(DATASET,i)
 nam = arcpy.Describe(f_classes)
 if nam.shapeType == "Polygon":
  CAPA = arcpy.os.path.join(DATASET,i)
del i

# Local variables:
TOPO = arcpy.os.path.join(GDB, "topology")


topology_point = arcpy.os.path.join(GDB, DATASET, "topology_point")
topology_line = arcpy.os.path.join(GDB, DATASET, "topology_line")
topology_poly = arcpy.os.path.join(GDB, DATASET, "topology_poly")


TOPO = arcpy.CreateTopology_management(DATASET, "topology", "")
arcpy.AddFeatureClassToTopology_management(TOPO, CAPA, "1", "1")
arcpy.AddRuleToTopology_management(TOPO, "Must Not Have Gaps (Area)", CAPA, "", "", "")
arcpy.AddRuleToTopology_management(TOPO, "Must Not Overlap (Area)", CAPA, "", "", "")
arcpy.ValidateTopology_management(TOPO, "Full_Extent")
arcpy.ExportTopologyErrors_management(TOPO, DATASET, "topology")


#Informe
arcpy.AddMessage(GDB)
arcpy.AddMessage("PUNTOS: ")
arcpy.AddMessage(str(arcpy.GetCount_management(topology_point)))
arcpy.AddMessage("GAP'S: ") 
arcpy.AddMessage(str(arcpy.GetCount_management(topology_line)))
arcpy.AddMessage("OVERLAP'S: ")
arcpy.AddMessage(str(arcpy.GetCount_management(topology_poly)))
arcpy.AddMessage("========================================== ")

