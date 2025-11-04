def calculate_cost(price, qty):
    total = price * qty
    gst = total * 0.05
    return total, gst



orders = []

def cafe_menu():
    while True:
        print('''
//********Wlcome to Mine Cafe********//
------ Main Menus ------
1. Food Items
2. Drinks
3. Show Bill
4. Exit''')

        choice = int(input("Enter your choice: "))

        if choice == 1:
            while True:
                print('''
-- Food Items --
1. Pizza - Rs.120
2. Burger - Rs.50
3. Sandwich - Rs.69
4. Return to Main Menu''')
                sub_choice = int(input("Enter your sub choice: "))
                
                if sub_choice == 1:
                    item, price = "Pizza", 120
                elif sub_choice == 2:
                    item, price = "Burger", 50
                elif sub_choice == 3:
                    item, price = "Sandwich", 69
                elif sub_choice == 4:
                    break
                else:
                    print("Invalid sub-choice!..")
                    continue

                qty = int(input(f"Enter quantity of {item}: "))
                total, gst = calculate_cost(price, qty)
                orders.append((item, price, qty, total, gst))
                print(f"Added {qty} x {item} = Rs.{total} + GST Rs.{gst:.2f}")

        elif choice == 2:
            while True:
                print('''
-- Drinks --
1. Mango Juice - Rs.80
2. Pineapple Juice - Rs.90
3. Mix Fruit - Rs.100
4. Return to Main Menu''')  
                sub_choice = int(input("Enter your sub choice: "))
                
                if sub_choice == 1:
                    item, price = "Mango Juice", 80
                elif sub_choice == 2:
                    item, price = "Pineapple Juice", 90
                elif sub_choice == 3:
                    item, price = "Mix Fruit", 100
                elif sub_choice == 4:
                    break
                else:
                    print("Invalid sub-choice!........")
                    continue

                qty = int(input(f"Enter quantity of {item}: "))
                total, gst = calculate_cost(price, qty)
                orders.append((item, price, qty, total, gst))
                print(f"Added {qty} x {item} = Rs.{total} + GST Rs.{gst:.2f}")

        elif choice == 3:
            print("\n------ BILL of all ------")
            total_amount = 0
            total_gst = 0
            for item, price, qty, total, gst in orders:
                print(f"{item} (Rs.{price} x {qty}) = Rs.{total:.2f} + GST Rs.{gst:.2f}")
                total_amount += total
                total_gst += gst
            print(f"\nTotal (without GST): Rs.{total_amount}")
            print(f"Total GST (5%): Rs.{total_gst:.2f}")
            print(f"Grand Total: Rs.{total_amount + total_gst:.2f}")

        elif choice == 4:
            print("Thank you for visiting! Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

cafe_menu()
