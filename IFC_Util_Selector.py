import ifcopenshell
import ifcopenshell.util.selector



# Open the IFC file
model = ifcopenshell.open('/Users/sabindahal/Desktop/Assignment/AC20-FZK-Haus-40.ifc')
IfcWall = ifcopenshell.util.selector.filter_elements(model, "IfcWall, material!=concrete+IfcDoor")
filter_wall = model.by_type("IfcWall")

model.write('/Users/sabindahal/Desktop/Assignment/AC1DV.ifc')

                         