import ifcopenshell
import ifcopenshell.api


# Open the IFC file
model = ifcopenshell.open("/Users/sabindahal/Desktop/Assignment/AC20-FZK-Haus-40.ifc")

# Create an empty list to store filtered walls
filtered_walls = []

# Iterate through all IfcWall elements
for wall in model.by_type("IfcWall"):
    # Check if the wall is made of concrete material (you can adjust the material check as needed)
    if hasattr(wall, "IsDefinedBy"):
        for rel in wall.IsDefinedBy:
            if hasattr(rel, "RelatingMaterial"):
                material = rel.RelatingMaterial
                if hasattr(material, "Name") and "concrete" in material.Name:
                    filtered_walls.append(wall)

# Create a new IFC file with the filtered walls
output_file = "/Users/sabindahal/Desktop/Assignment/abcd.ifc"
# filtered_model = api.run(output_file, [wall.id() for wall in filtered_walls])

# Close the original model
model.close()

# Print the filtered walls
for wall in filtered_walls:
    print(wall)

print(f"Filtered IFC file saved to {output_file}")


