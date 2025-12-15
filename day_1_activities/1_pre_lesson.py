# this is what we will use for the video intro to dictionaries
# dictoionary = collection of (key:value) pairs

capitals = {"Usa": "Washington D.C.",
            "India": "New delhi",
            "China": "Beijing",
            "Russia": "Mosscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("India"))

# if capitals.get("Japan"):
#     print("Exisit")
# else:
#     print("Doesnt exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"Usa": "Detriot"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()

# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# print(values)

# for value in capitals.values():
#     print(values)

# iteams = capitals.items()
# print(iteams)

for key, value in capitals.items():
    print(f"{key}: {value}")