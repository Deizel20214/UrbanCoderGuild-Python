#Program purpose: To store a list of countries entered by user 
print("This list stores any three countries ") 


#Empty list to store countries 
countries = [] 

#Ask the user for 3 country names
for i in range(3):
    country = input(f"Enter country #{i+1}: ")
    countries.append(country)    

# show the final list
print("your list countries:",countries)



# Program purpos favorite food of user and using list methodes to modify

# Start with a basic list
foods = ["Pizza", "Tacos," "Burgers, Sushi," "Fries"]
print(" starting Food list:",foods)

# Ask user to add a new food 
new_food = input("Enter a food you want to add to your list: ")
foods.append(new_food )
print(" Added! New list:",foods) 

# Ask user to remove 
remove_food = input("enter a food you want to remove from this list:")
if remove_food in foods:
    foods.remove(remove_food)
    print(f" Removed {remove_food}.") 
else:
    print(f" {remove_food} is not in the list.")
print("Curent list:",foods)

# show number of items 
print("Total items in the list:",) 

# Ask if user wants to sort the list 
should_sort = input("do you want to sort the list alphabeticly? (yes/no):").lower()
if should_sort == "yes": 
    foods.sort() 
    print("sorted list:", foods)
