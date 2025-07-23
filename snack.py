print("Welcome to the Top 3 snacks collecter!") 
snacks = [] # start with an empty list 
count = 0

# Use while loop to collect 3 favorite snacks 
while count < 3:
 snack = input (f"Enter snack #{count + 1}:")   
 snacks.append(snack)
 count += 1


print("\n Your favorite snacks are: ", snacks)

snacks.sort()
print("sorted snacks: ",snacks)



remove_item = input("what item would you like to remove: ")

if remove_item in snacks:
 snacks.remove(remove_item)
 print("remove snack: ", remove_item)
else:
 print(" Snack not found!")


print("\n Final snack list: ", snacks)
print("Total snacks now: ", len(snacks))





















