import csv
import ifcopenshell
import sys
sys.path.append('/Users/sto/Code/IfcOpenShell/IfcOpenShell/src/ifctester/ifctester/')
from ifctester import ids, reporter

rhids=ids.Ids(title="IDS for RH1 and RH2 data")

with open('/Users/sto/Documents/Metropolia/Opetus/CiC/OPS/Syllabi/Computational-representations/RAVA2_tietosisältö_ RH1_RH2_ver_0_91.csv', encoding='utf-8', newline='') as file:
    reader=csv.DictReader(file, delimiter=';', quotechar='|')
    for row in reader:
        entity = row["RAVA IFC Entity"]
        propertyset = row["RAVA PropertySet"]
        property = row["RAVA Property"]
        datatype = row["RAVA IFC Data Type"]
        allowed = row["RAVA Sallitut arvot"]
        #allowedvalues = allowed.split(";")
        if (entity != None) and (propertyset != None) and (property != None):
            spec=ids.Specification(name=f'{entity} - {propertyset} - {property}')
            spec.applicability.append(ids.Entity(name=f'{entity}'))
            spec.requirements.append(ids.Property(name=property, propertySet = propertyset, datatype=datatype))
            rhids.specifications.append(spec)
    
result = rhids.to_xml("rhids-test.xml")
                                              
