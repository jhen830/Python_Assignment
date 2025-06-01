

import time
import functions_invstaff as fi

invstaff_info = []

while True:
    print("""----------------------------------------Login Menu----------------------------------------
Welcome Inventory Staff!
1. Sign up
2. Login
3. Exit""")
    
    login_choice = input("Please select an option above (1,2,3) : ")
    
    if not login_choice.isdigit() or int(login_choice) not in [1, 2, 3]:
        print("Invalid input! Please enter a valid option (1, 2, or 3).")
        continue
    
    login_choice = int(login_choice)

    if login_choice == 3:
        continue

    elif login_choice == 1:
        new_username = input("Please create your username: ")
        new_password = input("Please create your password: ")
        print("Your registration is now waiting for verification.")
        fi.invstaff_register(new_username, new_password)
        time.sleep(1)
        # Assume verification logic here (Need to wait for super user to verify registration.)
        verification = False

        if verification:
            add_user = new_username
            add_pass = new_password
            print("Your registration is successful. Please log in.")
            fi.addinvstaff_info(add_user, add_pass)

            continue

    elif login_choice == 2:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        login_successful = False

        with open("invstaff_info.txt", "r") as g:
            for line in g:
                stored_credentials = line.strip().split(",")
                if len(stored_credentials) == 2:
                    stored_username, stored_password = stored_credentials
                    if username == stored_username and password == stored_password:
                        login_successful = True
                        break

        if login_successful:
            print("You have logged in successfully!")
            with open("reports.txt", "a") as pur_order_report:
                pur_order_report.write(f"\nUser with username : {username} has logged in on {time.strftime('%Y-%m-%d %H:%M:%S')}")
            time.sleep(1)
            break

        else:
            print("Invalid login")
            time.sleep(1)
            continue

    else:
        print("Invalid option, please try again.")
        continue
            
while True:
        print("""----------------------------------------Inventory Menu----------------------------------------
            Welcome to the Inventory Menu!
            1. Purchase Order
            2. Stock Check / Adjustments
            3. Check Purchase Order Status
            4. Modify Purchase Order
            5. Cancel Purchase Order
            6. Reports
            7. Exit
----------------------------------------------------------------------------------------------""")
        
        inven_choice = input("Please select your action (1, 2, 3 ...) : ")
        time.sleep(1)

        if not inven_choice.isdigit() or int(inven_choice) not in [1, 2, 3, 4, 5, 6, 7]:
            print("Invalid input! Please enter a valid option.")
            continue
        
        inven_choice = int(inven_choice)

        if inven_choice == 1:



            products = {
                "PPC1": ("Pre-built PC 1", 5000.00),
                "PPC2": ("Pre-built PC 2", 4500.00),
                "PPC3": ("Pre-built PC 3", 3500.00),
                "CPU1": ("AMD Ryzen 9 7950X", 2699.00),
                "CPU2": ("AMD Ryzen 7 7700X", 1659.00),
                "GPU1": ("GIGABYTE GeForce RTX 4090", 10399.00),
                "GPU2": ("GIGABYTE GeForce RTX 4070", 2899.00),
                "MTB1": ("GIGABYTE B450M Motherboard", 429.00),
                "RAM1": ("Kingston HyperX FURY Ram DDR4 8GB", 55.00),
                "SSD2": ("Samsung 970 EVO PLUS M.2 2280 PCIe NVMe 1TB SSD", 387.00),
                "MON1": ("Samsung 22\" Essential Monitor S3 S31C", 329.00),
                "KMC1": ("Logitech MK215 Wireless Keyboard and Mouse Combo", 81.00)
            }

            def generate_order_id(length=3):
                timestamp = int(time.time() * 1000)
                or_id = str(timestamp)[-length:]
                return "O" + or_id

            order_list = []
            order_total_price = 0.00
            order_id = generate_order_id()

            print("""----------------------------------------Order Menu----------------------------------------
            Welcome to the Purchase Order Menu, this is the product list.

            PPC1 : Pre-built PC 1 - Price : RM 5000.00
            PPC2 : Pre-built PC 2 - Price : RM 4500.00
            PPC3 : Pre-built PC 3 - Price : RM 3500.00
            CPU1 : AMD Ryzen 9 7950X - Price : RM 2699.00
            CPU2 : AMD Ryzen 7 7700X - Price : RM 1659.00
            GPU1 : GIGABYTE GeForce RTX 4090 - Price : RM 10399.00
            GPU2 : GIGABYTE GeForce RTX 4070 - Price : RM 2899.00
            MTB1 : GIGABYTE B450M Motherboard - Price : RM 429.00
            RAM1 : Kingston HyperX FURY Ram DDR4 8GB - Price : RM 55.00
            SSD2 : Samsung 970 EVO PLUS M.2 2280 PCIe NVMe 1TB SSD - Price : RM 387.00
            MON1 : Samsung 22" Essential Monitor S3 S31C - Price : RM 329.00
            KMC1 : Logitech MK215 Wireless Keyboard and Mouse Combo - Price : RM 81.00
-------------------------------------------------------------------------------------------""")
            print("Your Order ID is:", order_id)

            purchase_choice = ""
            order_status = "unpaid"

            while purchase_choice != "0":
                purchase_choice = input("Please select which products would you like to order (PPC1, PPC2, etc.), enter 0 to end your order: ").upper()

                if purchase_choice in products:
                    product_name, product_price = products[purchase_choice]
                    quantity = int(input(f"Enter quantity of {product_name} you would like to order: "))
                    order_list.append([purchase_choice, product_name, f"{product_price:.2f}", quantity])
                    order_total_price += product_price * quantity
                    print(f"{product_name} x {quantity} have been ordered, your total is {order_total_price:.2f}")

                if purchase_choice == "0":
                    pur_confirm = input("Are you sure you want to end your purchase order? YES/NO: ").upper()

                    if pur_confirm == "YES":
                        while True:
                            pay_confirm = int(input("Pay for order now or leave unpaid? 1 = Pay Now ; 2 = Leave unpaid "))
                            
                            if pay_confirm == 1:
                                order_status = "pending"
                                break
                            elif pay_confirm == 2:
                                order_status = "unpaid"
                                break
                            else:
                                print("Invalid input, please try again.")

                        total_text = f"{order_total_price:.2f}"
                        order_time = time.strftime('%Y-%m-%d %H:%M:%S')
                        # Assuming fi.add_order is a function to save the order details
                        fi.add_order(order_id, username, order_time, order_list, total_text, order_status)
                        with open("reports.txt", "a") as inv_report:
                            inv_report.write(f"\nUser with username : {username} has made purchase order with Order ID {order_id} on {time.strftime('%Y-%m-%d %H:%M:%S')}")
                        time.sleep(1)
                        print(f"Your order with Order ID {order_id} and total price {order_total_price:.2f} has been placed.")

                    if pur_confirm == "NO":
                        purchase_choice = ""

        if inven_choice == 2:
            
            check_choice = 1
            while check_choice != 0 :

                print("""----------------------------------------Stock Check / Adjustments Menu----------------------------------------  
            1. Check All Stock
            2. Check Stock of Specific Items
            3. Add / Subtract Stock                
--------------------------------------------------------------------------------------------------------------""")
                time.sleep(1)
              
                check_choice = int(input("Please select your action (1, 2, 3), enter 0 to end your checks/adjustments."))
            
                if check_choice == 1:                    

                    with open("stock.txt", "r") as st:
                        for line in st:
                            stored_stock = line.strip().split(",")
                            if len(stored_stock) == 4:
                                item_id, stock_name, price, stock_quan = stored_stock
                                print("Item Name:", stock_name, "Quantity:", stock_quan)

                    with open("reports.txt", "a") as check1_report:
                        check1_report.write(f"\nUser with username : {username} has checked all stock on {time.strftime('%Y-%m-%d %H:%M:%S')}")
                    time.sleep(1)
            
                    continue

                if check_choice == 2:

                    def filter_item_stock(file_path, user_input):
                        try:
                            with open(file_path, 'r') as file:
                                for line in file:
                                    items = line.strip().split(',')
                                    if len(items) == 4:
                                        item_id, item_name, price, stock_quan = items
                                        if any(word.lower() in item_name.lower() for word in user_input.split()):
                                            print(f"Item Name: {item_name}, Quantity: {stock_quan}")
                                            with open("reports.txt", "a") as check2_report:
                                                check2_report.write(f"\nUser with username : {username} has checked specific stock on {time.strftime('%Y-%m-%d %H:%M:%S')}")
                                            time.sleep(1)
                        except FileNotFoundError:
                            print(f"File '{file_path}' not found.")

                    user_input = input("Enter Product Name (separated by spaces): ")

                    file_path = 'stock.txt'
                    filter_item_stock(file_path, user_input)

                if check_choice == 3 :
                    
                    
                    file_path = "stock.txt"

                    def load_stock_data(file_path):
                        stock_data = {}
                        try:
                            with open(file_path, "r") as file:
                                for line in file:
                                    item_id, item_name, price, quantity = line.strip().split(",")
                                    stock_data[item_id] = {
                                        "name": item_name,
                                        "price": float(price),
                                        "quantity": int(quantity)
                                    }
                        except FileNotFoundError:
                            print(f"Error: {file_path} not found.")
                            exit()
                        return stock_data

                    def save_stock_data(file_path, stock_data):
                        try:
                            with open(file_path, "w") as file:
                                for item_id, item_info in stock_data.items():
                                    file.write(f"{item_id},{item_info['name']},{item_info['price']},{item_info['quantity']}\n")
                        except IOError:
                            print(f"Error: Unable to write to {file_path}.")
                            exit()

                    def display_stock_items(stock_data):
                        print("Available stock items:")
                        for i, (item_id, item_info) in enumerate(stock_data.items(), start=1):
                            print(f"{i}. {item_info['name']} (ID: {item_id})")

                    def get_user_input(stock_data):
                        while True:
                            try:
                                item_number = int(input(f"Enter the number of the stock item you want to update (1-{len(stock_data)}): "))
                                if 1 <= item_number <= len(stock_data):
                                    return item_number
                                else:
                                    print(f"Invalid input. Please enter a valid number between 1 and {len(stock_data)}.")
                            except ValueError:
                                print("Invalid input. Please enter a valid integer.")

                    def update_stock(stock_data, item_number, action, quantity_change):
                        stock_ids = list(stock_data.keys())
                        selected_item_id = stock_ids[item_number - 1]

                        while True:
                            if action == "add":
                                stock_data[selected_item_id]["quantity"] += quantity_change
                                break
                            elif action == "subtract":
                                stock_data[selected_item_id]["quantity"] -= quantity_change
                                break
                            else:
                                print("Invalid action. Please enter 'add' or 'subtract'.")
                                action = input("Enter action ('add' or 'subtract'): ")

                        print(f"{stock_data[selected_item_id]['name']} stock updated. New quantity: {stock_data[selected_item_id]['quantity']}")
                        with open("reports.txt", "a") as check3_report:
                            check3_report.write(f"\nUser with username : {username} has updated stock of {stock_data[selected_item_id]['name']} on {time.strftime('%Y-%m-%d %H:%M:%S')}")
                        time.sleep(1)

                    # Load stock data
                    stock_data = load_stock_data(file_path)

                    # Display stock items
                    display_stock_items(stock_data)

                    # Get user input
                    item_number = get_user_input(stock_data)
                    action = input("Do you want to add or subtract stock? (add/subtract): ")

                    try:
                        quantity_change = int(input(f"Enter the quantity to {action}: "))
                    except ValueError:
                        print("Invalid input. Please enter a valid integer for quantity.")
                        exit()

                    # Update stock
                    update_stock(stock_data, item_number, action, quantity_change)

                    # Save updated stock data
                    save_stock_data(file_path, stock_data)

            continue

        if inven_choice == 3:

            def get_order_details(order_id):
                # Read the file content
                with open("pur_order.txt", "r") as file:
                    orders = file.readlines()

                # Iterate through each line to find the order with the given order_id
                for order in orders:
                    details = order.split(',')
                    if details[0] == order_id:
                        # Print the required details
                        print(f"OrderID: {details[0]}")
                        print(f"Order Time: {details[2]}")
                        print(f"Total Price: RM {details[-2]}")
                        print(f"Order Status: {details[-1].strip()}")
                        with open("reports.txt", "a") as checkstatus_report:
                            checkstatus_report.write(f"\nUser with username : {username} has checked status of OrderID {details[0]} on {time.strftime('%Y-%m-%d %H:%M:%S')}")
                        time.sleep(1)                        
                        return

                # If order_id is not found
                print("Order ID not found.")

            # Receive input from user
            order_id = input("Enter the Order ID you want to check: ")

            # Get and print the order details
            get_order_details(order_id)

        if inven_choice == 4:

            def modify_order(username):
                while True:
                    print("-----------------------------------------Modify Order Page------------------------------------------")

                    order_type = input("""Enter 1 to modify purchase order
Enter 3 to quit from purchase order page: """)

                    if order_type == "3":
                        break

                    elif order_type != "1" and order_type != "3":
                        print("Invalid option. Please enter 1 or 3.\n")

                    elif order_type == '1':
                        cart = []
                        order = []
                        order_list = []
                        unpaid_order = []
                        updated_lines = []
                        old_lines = []
                        with open("pur_order.txt", "r") as p:
                            lines = p.readlines()
                            for line in lines:
                                line = line.strip()
                                p_order_id = line.split(",")[0]
                                p_username = line.split(",")[1]
                                p_status = line.split(",")[-1]
                                if username == p_username and p_status == "unpaid":
                                    unpaid_order.append(p_order_id)


                        print(
                            "---------------------------------------------Order List---------------------------------------------")

                        for i in unpaid_order:
                            print(i)

                        # try:
                        while True:
                            modify_order = input("Please select order to modify by enter the orderID: ")

                            if modify_order not in unpaid_order:
                                print("This order does not exist.\n")

                            else:
                                break

                        with open("pur_order.txt", "r") as p:
                            order_list = []
                            lines = p.readlines()
                            for line in lines:
                                line = line.strip()
                                p_order_id = line.split(",")[0]
                                order_list.append(p_order_id)
                                p_username = line.split(",")[1]
                                p_order_status = line.split(",")[-1]

                                if p_order_id == modify_order:
                                    p_datetime = line.split(",")[2]
                                    p_total_price = str(line.split(",")[-2])
                                    order = line.split(",")
                                    items = ",".join(order[3:-2])
                                    print(f"""
-------------------------------------------Order Details--------------------------------------------
            Inventory Staff Username: {p_username}
            OrderID: {p_order_id}
            Order Time: {p_datetime}
            Items:""")

                                    for item in eval(items):
                                        itemID, item_name, item_price, quantity = item
                                        cart.append(item)
                                        print(f"{item_name} (ItemID: {itemID}), Price: RM{item_price}, Quantity: {quantity}")

                        print("""----------------------------------------------------------------------------------------------------
            Enter 1 to Add Item
            Enter 2 to Remove Item
            Enter 3 to Quit
            """)

                        while True:
                            modify_type = input("Please enter your option: ")

                            if modify_type != "1" and modify_type != "2" and modify_type != "3":
                                print("Invalid input. Please try again.\n")
                                time.sleep(0.7)

                            elif modify_type == "3":
                                break

                            elif modify_type == "1" or modify_type == "2":
                                break

                        if modify_type == '1':
                            with open("item_list.txt", "r") as menu:
                                print(f"""
---------------------------------------------Item List---------------------------------------------
ID    Item                                                       Price        Quantity""")
                                for line in menu:
                                    item = line.strip()
                                    id = item.split(",")[0]
                                    name = item.split(",")[1]
                                    price = item.split(",")[2]
                                    quantity = item.split(",")[3]
                                    order_list.append(id)
                                    print(f"{id:>4}. {name:50}     {price:>9}     {quantity:>8}")

                            while True:
                                add_item = input("Please select item to add by enter the itemID (Enter Q to quit): ")

                                if add_item.upper() == "Q":
                                    break

                                elif add_item not in order_list:
                                    print("Invalid input. Please enter a itemID.\n")

                                else:

                                    with open("item_list.txt", "r") as menu:
                                        for line in menu:
                                            item = line.strip()
                                            id = item.split(",")[0]
                                            id_list = []
                                            id_list.append(id)

                                            if add_item in id_list:
                                                name = item.split(",")[1]
                                                price = item.split(",")[2]
                                                quantity = item.split(",")[3]

                                                try:
                                                    add_quantity = int(input("Please enter the quantity: "))
                                                except ValueError:
                                                    print("\nPlease enter an integer.")
                                                    time.sleep(0.7)
                                                cart.append([add_item, name, price, add_quantity])

                                    with open("pur_order.txt", "r") as p:
                                        lines = p.readlines()
                                        for line in lines:
                                            old_line = line.strip()
                                            p_order_id = old_line.split(",")[0]
                                            old_p_total_price = float(old_line.split(",")[-2])
                                            order = line.split(",")
                                            old_cart = ",".join(order[3:-2])

                                            if modify_order != p_order_id:
                                                old_lines.append(line)

                                            elif modify_order == p_order_id:
                                                price = float(price)
                                                new_p_total_price = old_p_total_price + (price * add_quantity)
                                                updated_line = line.replace(str(old_cart), str(cart))
                                                updated_line = updated_line.replace(str(old_p_total_price), str(new_p_total_price))
                                                updated_lines.append(updated_line)
                                                updated_lines[-1] = updated_lines[-1].strip()

                                    with open("pur_order.txt", "w") as p:
                                        p.writelines(old_lines)

                                    with open("pur_order.txt", "a") as p:
                                        p.writelines(updated_lines)
                                        print("\nThis item has been added successfully.")
                                        time.sleep(1)

                                    with open("reports.txt", "a") as additem_report:
                                        additem_report.write(f"\nUser with username : {username} has added item to {p_order_id} on {time.strftime('%Y-%m-%d %H:%M:%S')}")
                                        time.sleep(1)
                                
                                    break

                        elif modify_type == '2':
                            item_list = []

                            with open("pur_order.txt", "r") as p:
                                lines = p.readlines()
                                for line in lines:
                                    line = line.strip()
                                    p_order_id = line.split(",")[0]
                                    p_total_price = str(line.split(",")[-2])
                                    order = line.split(",")
                                    items = ",".join(order[3:-2])

                                    if modify_order == p_order_id:
                                        for item in eval(items):
                                            item_list.append(item)
                                        break

                            while True:
                                remove_item = input("Please select item to remove by enter the itemID: ")
                                item_exist = False

                                for item in item_list:
                                    itemID, item_name, item_price, quantity = item

                                    if remove_item == itemID:
                                        item_exist = True
                                        break

                                if item_exist == False:
                                    print("\nThis item is not in the order.")
                                    time.sleep(0.7)

                                elif item_exist == True:
                                    item_list.remove(item)

                                    if item_list == []:
                                        print("\nThis is the only item in the order. This item cannot be removed.")
                                        time.sleep(0.7)
                                        break

                                    else:
                                        print(item_list)
                                        print(p_total_price)

                                        with open("pur_order.txt", "r") as p:
                                            lines = p.readlines()
                                            for line in lines:
                                                old_line = line.strip()
                                                p_order_id = old_line.split(",")[0]
                                                old_p_total_price = float(old_line.split(",")[-2])
                                                order = line.split(",")
                                                old_cart = ",".join(order[3:-2])

                                                if modify_order != p_order_id:
                                                    old_lines.append(line)

                                                elif modify_order == p_order_id:
                                                    item_price = float(item_price)
                                                    new_p_total_price = old_p_total_price - (item_price * quantity)
                                                    updated_line = line.replace(str(old_cart), str(item_list))
                                                    updated_line = updated_line.replace(str(old_p_total_price),
                                                                                        str(new_p_total_price))
                                                    updated_lines.append(updated_line)

                                        with open("pur_order.txt", "w") as p:
                                            old_lines[-1] = old_lines[-1].strip()
                                            p.writelines(old_lines)

                                        with open("pur_order.txt", "a") as p:
                                            updated_lines[-1] = updated_lines[-1].strip()
                                            p.write("\n")
                                            p.writelines(updated_lines)
                                            print("\nThis item has been removed successfully.")
                                            time.sleep(1)

                                        with open("reports.txt", "a") as additem_report:
                                            additem_report.write(f"\nUser with username : {username} has removed item from {p_order_id} on {time.strftime('%Y-%m-%d %H:%M:%S')}")
                                            time.sleep(1)

                                            break

                        else:
                            print("\nInvalid input. Please try again.")

            modify_order(username)





            

        if inven_choice == 5:

            def cancel_order():
                while True:
                    cancel_id = input("Enter the order ID you want to cancel: ")

                    with open("pur_order.txt", "r") as file:
                        lines = file.readlines()

                    order_found = False
                    updated_lines = []

                    for line in lines:
                        details = line.split(',')
                        if details[0] == cancel_id:
                            order_found = True
                            if details[-1].strip() == "pending":
                                print("This order has already been paid, unable to cancel.")
                                return
                            else:
                                continue  # Skip adding this line to updated_lines to cancel the order
                        updated_lines.append(line)

                    if not order_found:
                        print("Invalid Order ID. Please try again.")
                    else:
                        with open("pur_order.txt", "w") as file:
                            file.writelines(updated_lines)
                        print(f"Order with ID {cancel_id} has been canceled.")
                        with open("reports.txt", "a") as cancel_report:
                            cancel_report.write(f"\nUser with username : {username} has cancelled OrderID {cancel_id} on {time.strftime('%Y-%m-%d %H:%M:%S')}")
                        time.sleep(1) 

                        return

            # Call the function to cancel an order
            cancel_order()


        if inven_choice == 6:
            while True:
                print("-----------------------------------------Reports Page------------------------------------------")

                order_type = input("""Enter 1 to check all reports
Enter 2 to filter out login reports
Enter 3 to quit from reports page: """)

                if order_type == "3":
                    break

                elif order_type != "1" and order_type != "2" and order_type != "3":
                    print("Invalid option. Please enter 1 ,2 or 3.\n")

                elif order_type == '1':
                    try:
                        with open('reports.txt', 'r') as file:
                            # Read and print each line
                            for line in file:
                                print(line.strip())
                                time.sleep(0.1)
                    except FileNotFoundError:
                        print("File not found. Please check the file path.")

                elif order_type == '2':
                    try:
                        with open('reports.txt', 'r') as file:
                            # Filter out lines containing the word "logged"
                            for line in file:
                                if "logged" not in line:
                                    print(line.strip())
                                    time.sleep(0.1)
                    except FileNotFoundError:
                        print("File not found. Please check the file path.")


        if inven_choice == 7:
            break