import arcpy, os
map_document = r"D:\PLANILLA_LAYOUT\01_FEBRERO\m_cob_uso_bahia.mxd"
database = r"D:\CORTES_CARTOGRAFIA_BASE\01_CORTES_FEBRERO\CB_BAHIA.gdb"
map_object = arcpy.mapping.MapDocument(map_document)
data_frame = arcpy.mapping.ListDataFrames(map_object,"Layers")
resource_layers = arcpy.mapping.ListLayers(map_object)
