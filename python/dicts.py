# A dictionary is a set of key-value pairs. Each key has a value as in a dictionary
# It is not ordered and canbe mutable
# A problem I noticed with dicts is that the keys are case sensitive: Broom is different from broom
items = {"Plate": "A tool used for eating", "River": "A channeled pool of water", "Patrick": "Name of a person"}
print("Plate definition:")
print(items["Plate"])
items["Broom"] = "Item used for sweeping"
print("Broom definition:")
print(items["Broom"])