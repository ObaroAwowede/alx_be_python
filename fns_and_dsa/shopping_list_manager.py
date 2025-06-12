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
        choice = input("Enter your choice: ")

        if choice == '1':
            item_added = str(input("Enter the value to be added: "))
            shopping_list.append(item_added)
            pass
        elif choice == '2':
            item_remove = int(input("Which item number on the list do you want removed?: "))
            shopping_list.pop((item_remove - 1))
            pass
        elif choice == '3':
            for i in range(len(shopping_list)):
                    print(shopping_list[i])
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
            
main()