#create a program that will keep a track of items for a shopping list the program should keep asking for new items 
#untill nothingis entered (no input followed by enter or return key ) the program should then display the full shoppinglist
# Initialize an empty list for the shopping items
shopping_list = []

print("Shopping List Tracker")
print("Keep entering items for your shopping list. Press Enter without typing anything to finish.\n")

while True:
    # Prompt the user to input an item
    item = input("Enter an item (or press Enter to finish): ")
    
    # Check if the input is empty (user pressed Enter without typing)
    if item == "":
        break  # Exit the loop if input is empty
    
    # Add the item to the shopping list
    shopping_list.append(item)

# Display the full shopping list
print("\nYour Shopping List:")
for idx, item in enumerate(shopping_list, start=1):
    print(f"{idx}. {item}")
