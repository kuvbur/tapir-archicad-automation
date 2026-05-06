import aclib

# Get all details of all properties and groups
propertyIds = aclib.RunCommand ('API.GetAllPropertyIds', {'propertyType': 'UserDefined'})
propertyDefinitions = aclib.RunCommand ('API.GetDetailsOfProperties', {'properties': propertyIds})
propertyDefinitionAvailabilityList = aclib.RunCommand ('API.GetPropertyDefinitionAvailability', {'propertyIds': propertyIds})
propertyGroupIds = aclib.RunCommand ('API.GetAllPropertyGroupIds', {'propertyType': 'UserDefined'})
propertyGroups = aclib.RunCommand ('API.GetPropertyGroups', {'propertyGroupIds': propertyGroupIds})
print(1)
