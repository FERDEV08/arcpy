# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# uge.py
# Created on: 2022-07-26 09:10:56.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
u_geom_1_salida = "u_geom_1_salida"
u_geom_1_salida__2_ = u_geom_1_salida

# Process: Calculate Field
arcpy.CalculateField_management(u_geom_1_salida, "uge1", "clasificar( !uge! )", "PYTHON_9.3", "def clasificar(uge):\\n if uge ==\"TECTONICO\":\\n  return 1\\n elif uge ==\"TECTONICO EROSIVO\":\\n  return 2\\n elif uge ==\"VOLCANICO\":\\n  return 3\\n elif uge ==\"GLACIAR\":\\n  return 4\\n elif uge ==\"FLUVIO - GLACIAR\":\\n  return 5\\n elif uge ==\"PERIGLACIAR\":\\n  return 6\\n elif uge ==\"ESTRUCTURAL\":\\n  return 7\\n elif uge ==\"GRAVEDAD Y MOVIMIENTOS EN MASA\":\\n  return 8\\n elif uge ==\"DENUDATIVO\":\\n  return 9\\n elif uge ==\"EROSIVO\":\\n  return 10\\n elif uge ==\"DEPOSICIONAL EROSIVO\":\\n  return 11\\n elif uge ==\"FLUVIO - LACUSTRE\":\\n  return 12\\n elif uge ==\"DEPOSICIONAL\":\\n  return 13\\n elif uge ==\"EROSION FLUVIAL\":\\n  return 14\\n elif uge ==\"TECTONICO MARINO\":\\n  return 15\\n elif uge ==\"MARINO Y FLUVIO-MARINO\":\\n  return 16\\n elif uge ==\"POLIGENICAS\":\\n  return 17\\n elif uge ==\"KARSTICO\":\\n  return 18\\n elif uge ==\"TECNOGENESIS\":\\n  return 19\\n elif uge ==\"NO APLICA\":\\n  return 998\\n")

