shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None

for index in range(0, 6):
    if shopping_list[index] == "spam":
        found_at = index
        break

print(found_at)
