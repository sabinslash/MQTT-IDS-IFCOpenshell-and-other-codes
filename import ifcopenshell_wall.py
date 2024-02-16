import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.selector 
import ifcopenshell.util.element
import ifcopenshell.util.placement
import ifcopenshell.util.classification
from ifcopenshell.api import run
import numpy


# Create a blank model
model = ifcopenshell.open("/Users/sabindahal/Desktop/Assignment/AC20-FZK-Haus-40.ifc")
# wall = run("root.create_entity", model, ifc_class="IfcWall")
# element = model.by_type('IfcWall')[0]
ifcopenshell.util.selector.filter_elements(model,'IfcWall, IfcSlab')

# walls = ifcopenshell.util.s(model,'!IfcWall')[0]
# selector = ifcopenshell.util.selector.filter_elements(model, "IfcWall")[0]
# element =(model,'IfcWall')

model.write("/Users/sabindahal/Desktop/Assignment/lipbalm.ifc")