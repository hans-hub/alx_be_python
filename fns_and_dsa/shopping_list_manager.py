#FUNCTION TO DISPLAY MENU

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            # Prompt for and add an item
            item = input("Add an item: ")
            shopping_list.append(item)
            print(f"'{item}' has been added")

        elif choice == '2':
            # Prompt for and remove an item
            item_remove = input("Remove item: ").strip()
            for item in shopping_list:
                if item_remove == item:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed")
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()