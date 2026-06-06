pasta = ("Pasta Arrabiata", "Italian", 20, "Medium")
biryani=("Chicken Biryani", "Indian", 45, "Hard")

print("Recipe 1:", pasta)
print("Recipe name: ", pasta[0])
print("Cuisine: ", pasta[1])
print("Difficulty: ", pasta[-1])

all_recipes = (pasta, biryani)
print("First Recipe Name: ", all_recipes[0][0])
print("Second Recipe Time: ", all_recipes[1][2], " minutes")
print("Pasta detail (sliced)", pasta[1:3])

for detail in pasta:
    print("-", detail)

pasta_ingredients = {"Tomato", "Garlic", "Olive oil", "Chili", "Pasta", "Garlic"}
print(pasta_ingredients)
biryiani_ingredients = {"Rice", "Chicken", "Garlic", "Onion", "Tomato", "Spices"}
print(biryiani_ingredients)

print(len(pasta_ingredients))

pasta_ingredients.add("Parmesan")
pasta_ingredients.discard("Chili")
print("Updated pasta ingredients", pasta_ingredients)

all_ingredients = pasta_ingredients.union(biryiani_ingredients)
common = pasta_ingredients.intersection(biryiani_ingredients)
only_pasta = pasta_ingredients.difference(biryiani_ingredients)
unique_to_each = pasta_ingredients.symmetric_difference(biryiani_ingredients)

print("All ingredients", all_ingredients)
print("Common ingredients", common)
print("Ingredients only in pasta", only_pasta)
print("Ingredients unique to each other", unique_to_each)