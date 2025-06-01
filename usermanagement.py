
import datetime
import time

def superusermenu():
    print("""--------------------------------------superuser Menu-------------------------------------------
Please select from the option below to proceed.
1. Add Users
2. Verify New Customer
3. Modify User Personal Details
4. Disable User Access
5. Inquiry of User’s system usage
6. Check Customer Order Status
7. Reports
8. Log Out""")

def customer_name(tempname):
    while True:  
        name = str(input(tempname))
        if name.isalpha() or name.split():
            return name
        elif name.isdigit():
            print('please try again')
        elif name == "":
            print("name cannot be empty")


def customer_ic(temp):
    while True:
        ic = str(input(temp))
        if ic.isdigit() and len(ic) == 12:
            return ic
        elif ic == "":
            print("ic cannot be empty")
        else:
            print('ic must be 12 digit numbers')


def customer_phone(temp):
    while True:
        phone = str(input(temp))
        if phone.isdigit() and len(phone) == 10 or len(phone) == 11:
            return phone
        elif phone == "":
            print("phone cannot be empty")
        else:
            print('phone number must consist 10 or 11 digits')



def customer_city(temp):
    while True:
        city = str(input(temp))
        if city.isalpha():
            return city
        elif city == "":
            print("city cannot be empty")
        else:
            print('please try again')


def customer_date():
        return datetime.date.today()

def customer_username(temp):
    while True:
        username = str(input(temp))
        if username == "":
            print("username cannot be empty")
        else:
            return username


def customer_password(temp):
    while True:
        password = str(input(temp))
        if password == "":
            print("name cannot be empty")
        else:
            return password


def admin_name(tempname):
    while True:
        name = input(tempname)
        if name.isalpha() or name.split():
            return name
        elif name.isdigit():
            print('please try again')
        elif name == "":
            print("name cannot be empty")


def admin_ic(temp):
    while True:
        ic = str(input(temp))
        if ic.isdigit() and len(ic) == 12:
            return ic
        elif ic == "":
            print("ic cannot be empty")
        else:
            print('ic must be 12 digit numbers')


def admin_phone(temp):
    while True:
        phone = str(input(temp))
        if phone.isdigit() and len(phone) == 10 or len(phone) == 11:
            return phone
        elif phone == "":
            print("phone cannot be empty")
        else:
            print('phone number must consist 10 or 11 digits')


def admin_city(temp):
    while True:
        city = str(input(temp))
        if city.isalpha():
            return city
        elif city == "":
            print("city cannot be empty")
        else:
            print('please try again')


def admin_date():
    return datetime.date.today()



def admin_username(temp):
    while True:
        username = str(input(temp))
        if username == "":
            print("username cannot be empty")
        else:
            return username

def admin_password(temp):
    while True:
        password = str(input(temp))
        if password == "":
            print("name cannot be empty")
        else:
            return password
        

while True: #user_type
    print("""----------------------------------------Main Menu----------------------------------------------
Welcome to KL Central Computer Company (KLCCC)!
1. Admin
2. Superuser
""")
    user_type = str(input("What user are you? : "))
    if user_type == '':
        print('cannot be empty')
        continue
    elif user_type.isalpha():
        print('numbers only')
        continue
            
    elif user_type == '1':
        print("""-----------------------------------Admin Menu---------------------------------------------
Welcome to KL Central Computer Company (KLCCC)!
1. Sign up
2. Login
3. Back""")

    elif user_type == '2':
        print("""---------------------------------superuser Menu------------------------------------------- 
Welcome to KL Central Computer Company (KLCCC)!
1. Login
2. Back""")
    else:
        print('please try again')
        continue
    ope = input("Please select from option above: ")
    if ope == '':
        print('cannot be empty')
        continue

    elif ope.isalpha():
        print('numbers only')
        continue

    elif user_type == '1' and ope == '1':
        while True:
            while True:
                username = str(input("Please create your username: "))
                if username == '':
                    print('username cannot be empty')
                    continue
                else:
                    break

            while True:
                password = str(input("Please create your password: "))
                if password == '':
                    print('password cannot be empty')
                    continue
                else:
                    break

            while True:
                name = input("Please enter your name: ")
                if name == "":
                    print("name cannot be empty")
                    continue
                elif name.isdigit():
                    print('name cannot have numbers')
                    continue
                else:
                    break

            while True:
                ic = input("Please enter your IC or passport number: ")
                if ic.isdigit() and len(ic) == 12:
                    break
                else:
                    print('ic must be 12 digit numbers')
                    continue

            while True:
                phone = input("Please enter your phone number: ")
                if phone.isdigit() and len(phone) == 10 or len(phone) == 11:
                    break
                else:
                    print('phone number must consist of 10 or 11 digit numbers')
                    continue

            while True:
                city = input("Please enter your city of domicile: ")
                if city.isdigit():
                    print('city cannot have numbers')
                    continue
                elif city == '':
                    print('city cannot be empty')
                    continue
                else:
                    break

            date = datetime.date.today()

            with open("admin_information.txt", "a") as ad_info:
                ad_info.write(f"\n{name},{ic},{phone},{city},{date},{username},{password}")
                print("Your registration is now waiting for verification.")
                time.sleep(1)
                break

    elif user_type == '1' and ope == '2':
        while True:
            username = input('Please enter username: ')
            if username == '':
                print('cannot be empty')
                continue
            else:
                break

        while True:
            password = input('Please enter password: ')
            if password == '':
                print('cannot be empty')
                continue
            else:
                break

        is_admin = False

        with open('admin_login_file.txt', 'r') as cus_log:
            for line in cus_log:
                # Removing brackets and spaces, then splitting by comma
                cleaned_line = line.strip().replace(' ', '')

                # Check if the line contains a comma
                if ',' not in cleaned_line:
                    continue

                stored_username, stored_password = cleaned_line.split(',')
                if stored_username == username and stored_password == password:
                    is_admin = True
                    break

        if is_admin:
            with open('admin_action.txt','a') as ad_act:
                ad_act.write(f"\n{username} logged in , login time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("Login successful")
        #admin login fail
        else:
            print("Login failed")
            continue
        while True:
            print('''
----------------------------------------------welcome admin-------------------------------------------''')
            print('''
1) Verify new customer
2) Check customer order status
3) customer report
4) back''')        
        
            admin_choice = input('which option do you want to access?')
            if admin_choice == '':
                print('cannot be empty')
                continue
            
            elif admin_choice.isalpha():
                print('numbers only')
                continue

            elif admin_choice == '1':
                with open('admin_action.txt','a') as ad_act1:
                    ad_act1.write(f"\nadmin {username} verifying customer, time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                print('customer list:')
                print('data format: name,ic,phone,city,date,username,password')
                with open('customer_register_info.txt','r') as cus_log:
                    print(cus_log.read())
                while True:
                    while True:
                        username = str(input("please enter the username of the customer: "))
                        if username == '':
                            print('username cannot be empty')
                            continue
                        else:
                            break

                    while True:
                        password = str(input("please enter the password of the customer: "))
                        if password == '':
                            print('password cannot be empty')
                            continue
                        else:
                            break

                    while True:
                        name = input("please enter the name of the customer: ")
                        if name == "":
                            print("name cannot be empty")
                            continue
                        elif name.isdigit():
                            print('name cannot have numbers')
                            continue
                        else:
                            break

                    while True:
                        ic = input("please enter the ic of the customer: ")
                        if ic.isdigit() and len(ic) == 12:
                            break
                        else:
                            print('ic must be 12 digit numbers')
                            continue

                    while True:
                        phone = input("please enter the phone of the customer: ")
                        if phone.isdigit() and len(phone) == 10 or len(phone) == 11:
                            break
                        else:
                            print('phone number must consist of 10 or 11 digit numbers')
                            continue

                    while True:
                        city = input("please enter the city of the customer: ")
                        if city.isdigit():
                            print('city cannot have numbers')
                            continue
                        elif city == '':
                            print('city cannot be empty')
                            continue
                        else:
                            break

                    date = datetime.date.today()

                    with open('customer_information.txt','a') as cus_log:
                        cus_log.write(f"\n{name},{ic},{phone},{city},{date},{username},{password}")

                    with open("customer_login_file.txt", "a") as file2:
                        file2.write(f"\n{username},{password}")

                    # Read data from user == '2':
                    with open('customer_information.txt', 'r') as cus_log:
                        customer_info_data = set(cus_log.readlines())

                    # Read data from customer_login.txt
                    with open('customer_login_file.txt', 'r') as file2:
                        customer_login_data = set(file2.readlines())

                    # Filter out entries from customer_register_info.txt
                    with open('customer_register_info.txt', 'r') as file3:
                        register_info_data = file3.readlines()

                    filtered_entries = []
                    for entry in register_info_data:
                        if not any(value in entry for value in customer_login_data):
                            filtered_entries.append(entry)
                        elif not any(value in entry for value in customer_info_data):
                            filtered_entries.append(entry)

                    # Write the filtered entries back to customer_register_info.txt
                    with open('customer_register_info.txt', 'w') as file3:
                        file3.writelines(filtered_entries)

                    with open('admin_action.txt','a') as ad_act2:
                        ad_act2.write(f"\nadmin {username} verified customer, time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    print('you have successfully verified customer')
                    print('verified customers:')
                    break

            elif admin_choice == '2':
                while True:
                    print('Check customer order status')
                    with open('admin_action.txt','a') as ad_act3:
                        ad_act3.write(f"\nadmin {username} opened customer order status, time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    with open('purchase_order_list.txt','r') as read_purchase:
                        print(read_purchase.read())
                    with open('repair_order_list.txt','r') as read_repair:
                        print(read_repair.read())        
                    off = input('press q to quit: ')
                    if off == 'q':
                        break
                    else:
                        continue    

            elif admin_choice == '3':
                while True:
                    print('customer report')
                    with open('customer_system_usage.txt','r') as read_cus_act:
                        print(read_cus_act.read())
                    with open('admin_action.txt','a') as ad_act4:
                        ad_act4.write(f"\nadmin {username} ,checked customer report, time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    off = input('press q to quit: ')
                    if off == 'q':
                        break
                    else:
                        continue               


            elif admin_choice == '4':
                print('logging off....')
                time.sleep(1)
                with open('admin_action.txt','a') as ad_act5:
                    ad_act5.write(f"\nadmin {username} logged off, time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    break
            
            else:
                print('Please try again')
                continue

    elif user_type == '1' and ope == '3':
        print('exiting...')
        continue
    elif user_type == '2' and ope =='1':
        while True:
            username = input('Please enter username: ')
            if username == '':
                print('cannot be empty')
                continue
            else:
                break

        while True:
            password = input('Please enter password: ')
            if password == '':
                print('cannot be empty')
                continue
            else:
                break

        is_superuser = False

        with open('superuser.txt', 'r') as cus_log:
            for line in cus_log:
                # Removing brackets and spaces, then splitting by comma
                cleaned_line = line.strip().replace(' ', '')
                stored_username, stored_password = cleaned_line.split(',')
                if stored_username == username and stored_password == password:
                    is_superuser = True
                    break

        if is_superuser:
            while True:
                print("Welcome, Super User!")
                superusermenu()
                choice = str(input('Please select an option: '))

                # add_user
                if choice == '1':
                    while True:
                        user_choice = str(input('''
users:
1) customer
2) admin
3) back
which user you registering? :'''))
                        if user_choice == '':
                            print('cannot be empty')
                            continue

                        elif user_choice.isalpha():
                            print('numbers only')
                            continue

                        elif user_choice == '1':
                            print("""
--------------------------------------------add customer------------------------------------------------""")

                            def_name = customer_name('please enter customer name: ')
                            def_ic = customer_ic('please enter customer ic: ')
                            def_phone = customer_phone('please enter customer phone number: ')
                            def_city = customer_city("please enter customer's city: ")
                            def_date = customer_date()
                            def_username = customer_username("please enter customer's username: ")
                            def_password = customer_password("please enter customer's password: ")

                            with open("customer_login_file.txt", "a") as cus_log:
                                cus_log.write(f"\n{def_username},{def_password}")

                            with open('customer_information.txt','a') as cus_full:
                                cus_full.write(f"\n{def_name},{def_ic},{def_phone},{def_city},{def_date},{def_username},{def_password}")

                            print()
                            time.sleep(1)
                            print("customer added successfully!")
                            time.sleep(0.5)
                            break
                            

                        if user_choice == '2':
                            print("""
---------------------------------------------add admin--------------------------------------------------------""")

                            print('registered admin info:')
                            print('data format: name,ic,phone,city,date,username,password')
                            with open('admin_information.txt','r') as ad_read:
                                print(ad_read.read())
                            ad_name = admin_name("please enter admin's name :")
                            ad_ic = admin_ic("please enter admin's ic :")
                            ad_phone = admin_phone("please enter admin's phone number: ")
                            ad_city = admin_city("please enter admin's city: ")
                            ad_date = admin_date()
                            ad_username = admin_username("please enter admin's username: ")
                            ad_password = admin_password("please enter admin's password: ")

                            with open('admin_login_file.txt', "a") as ad_log:
                                ad_log.write(f"\n{ad_username},{ad_password}")

                            with open('admin_information.txt','a') as ad_full:
                                ad_full.write(f"\n{ad_name}, {ad_ic},{ad_phone},{ad_city},{ad_date},{ad_username},{ad_password}")


                            print()
                            print(f"admin added successfully!")
                            break

                        
                        elif user_choice == '3':
                            print('exiting....')
                            time.sleep(1)
                            break

                #verify_new_customers
                elif choice == '2':
                    while True:
                        print('registered customer list:')
                        print('data format: name,ic,phone,city,date,username,password')
                        with open('customer_register_info.txt','r') as cus_log:
                            print(cus_log.read())
                        while True:
                            username = str(input("please enter the username of the customer: "))
                            if username == '':
                                print('username cannot be empty')
                                continue
                            else:
                                break

                        while True:
                            password = str(input("please enter the password of the customer: "))
                            if password == '':
                                print('password cannot be empty')
                                continue
                            else:
                                break

                        while True:
                            name = input("please enter the name of the customer: ")
                            if name == "":
                                print("name cannot be empty")
                                continue
                            elif name.isdigit():
                                print('name cannot have numbers')
                                continue
                            else:
                                break

                        while True:
                            ic = input("please enter the ic of the customer: ")
                            if ic.isdigit() and len(ic) == 12:
                                break
                            else:
                                print('ic must be 12 digit numbers')
                                continue

                        while True:
                            phone = input("please enter the phone of the customer: ")
                            if phone.isdigit() and len(phone) == 10 or len(phone) == 11:
                                break
                            else:
                                print('phone number must consist of 10 or 11 digit numbers')
                                continue

                        while True:
                            city = input("please enter the city of the customer: ")
                            if city.isdigit():
                                print('city cannot have numbers')
                                continue
                            elif city == '':
                                print('city cannot be empty')
                                continue
                            else:
                                break
                        
                        date = datetime.date.today()

                        with open('customer_information.txt','a') as cus_log:
                            cus_log.write(f"\n{name},{ic},{phone},{city},{date},{username},{password}")

                        with open("customer_login_file.txt", "a") as file2:
                            file2.write(f"\n{username},{password}")

                        # Read data from customer_information.txt
                        with open('customer_information.txt', 'r') as cus_log:
                            customer_info_data = set(cus_log.readlines())

                        # Read data from customer_login.txt
                        with open('customer_login_file.txt', 'r') as file2:
                            customer_login_data = set(file2.readlines())

                        # Filter out entries from customer_register_info.txt
                        with open('customer_register_info.txt', 'r') as file3:
                            register_info_data = file3.readlines()

                        filtered_entries = []
                        for entry in register_info_data:
                            if not any(value in entry for value in customer_login_data):
                                filtered_entries.append(entry)
                            elif not any(value in entry for value in customer_info_data):
                                filtered_entries.append(entry)

                        # Write the filtered entries back to customer_register_info.txt
                        with open('customer_register_info.txt', 'w') as file3:
                            file3.writelines(filtered_entries)

                        print('you have successfully verified customer')
                        break

                # modify_user_personal_details       
                elif choice == '3':   
                    while True:
                        print('''
which user do you want to modify?
1) customer
2) admin
3) back
''')        
                        cus_log = input('please choose an option: ')
                        if cus_log == '':
                            print('cannot be empty')
                            continue

                        elif cus_log.isalpha():
                            print('numbers only')
                            continue

                        elif cus_log == '1':  
                                print('''
Which customer data do you want to modify?
1) Name
2) Phone number
3) City
4) Date
5) Username
6) Password         
7) Back         
''')                               

                                choice = input("Please choose which data value to modify: ")
                                if choice == '':
                                    print('cannot be empty')
                                    continue

                                elif choice.isalpha():
                                    print('numbers only')
                                    continue

                                elif choice == '1':
                                    while True:
                                        print("customer information:")
                                        print('data format: name,ic,phone,city,date,username,password')
                                        with open("customer_information.txt", "r") as cus_info:
                                            print(cus_info.read())
                                        
                                        while True:
                                            old_name = input("Please input the customer's previous name: ")
                                            if old_name == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break
                                        
                                        while True:
                                            new_name = input("Please input the customer's new name: ")
                                            if new_name == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break                

                                        with open("customer_information.txt", "r") as file:
                                            lines = file.readlines()

                                        for line in lines:
                                            if old_name in line:
                                                lines = [line.replace(old_name, new_name) for line in lines]
                                                with open("customer_information.txt", "w") as file2:
                                                    file2.writelines(lines)
                                        
                                        with open("customer_information.txt", "r") as file3:
                                            lines2 = file3.readlines()

                                        for line in lines2:
                                            if old_name in line:
                                                lines2 = [line.replace(old_name, new_name) for line in lines2]
                                                with open("customer_information.txt", "w") as file3:
                                                    file3.writelines(lines2)

                                        print()
                                        print('customer information list:')
                                        with open("customer_information.txt", "r") as read2:
                                            print(read2.read())
                                        break



                                elif choice == '2':
                                    while True:
                                        print("customer information:")
                                        print('data format: name,ic,phone,city,date,username,password')
                                        with open("customer_information.txt", "r") as cus_info:
                                            print(cus_info.read())

                                        while True:
                                            old_phone = input("Please input the customer's previous phone number: ")
                                            if old_phone == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break
                                        
                                        while True:
                                            new_phone = input("Please input the customer's new phone number: ")
                                            if new_phone == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break       
                                        with open("customer_information.txt", "r") as file:
                                            lines = file.readlines()

                                        for line in lines:
                                            if old_phone in line:
                                                lines = [line.replace(old_phone, new_phone) for line in lines]
                                                with open("customer_information.txt", "w") as file2:
                                                    file2.writelines(lines)
                                        
                                        with open("customer_information.txt", "r") as file3:
                                            lines2 = file3.readlines()

                                        for line in lines2:
                                            if old_phone in line:
                                                lines2 = [line.replace(old_phone, new_phone) for line in lines2]
                                                with open("customer_information.txt", "w") as file3:
                                                    file3.writelines(lines2)

                                        print()
                                        print('customer information list:')
                                        print('data format: name,ic,phone,city,date,username,password')
                                        with open("customer_information.txt", "r") as read2:
                                            print(read2.read())
                                        break


                                elif choice == '3':
                                    while True:
                                        print("customer information:")
                                        print('data format: name,ic,phone,city,date,username,password')
                                        with open("customer_information.txt", "r") as cus_info:
                                            print(cus_info.read())

                                        while True:
                                            old_city = input("Please input the customer's previous city: ")
                                            if old_city == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break
                                        
                                        while True:
                                            new_city = input("Please input the customer's new city: ")
                                            if new_city == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break      

                                        with open("customer_information.txt", "r") as file:
                                            lines = file.readlines()

                                        for line in lines:
                                            if old_city in line:
                                                lines = [line.replace(old_city, new_city) for line in lines]
                                                with open("customer_information.txt", "w") as file2:
                                                    file2.writelines(lines)
                                        
                                        with open("customer_information.txt", "r") as file3:
                                            lines2 = file3.readlines()

                                        for line in lines2:
                                            if old_city in line:
                                                lines2 = [line.replace(old_city, new_city) for line in lines2]
                                                with open("customer_information.txt", "w") as file3:
                                                    file3.writelines(lines2)

                                        print()
                                        print('customer information list:')
                                        print('data format: name,ic,phone,city,date,username,password')
                                        with open("customer_information.txt", "r") as read2:
                                            print(read2.read())
                                        break


                                elif choice == '4':
                                    while True:
                                        print("customer information:")
                                        print('data format: name,ic,phone,city,date,username,password')
                                        with open("customer_information.txt", "r") as cus_info:
                                            print(cus_info.read())

                                        while True:
                                            old_date = input("Please input the customer's previous date: ")
                                            if old_date == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break
                                        
                                        while True:
                                            new_date = input("Please input the customer's new date: ")
                                            if new_date == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break      

                                        with open("customer_information.txt", "r") as file:
                                            lines = file.readlines()

                                        for line in lines:
                                            if old_date in line:
                                                lines = [line.replace(old_date, new_date) for line in lines]
                                                with open("customer_information.txt", "w") as file2:
                                                    file2.writelines(lines)
                                        
                                        with open("customer_information.txt", "r") as file3:
                                            lines2 = file3.readlines()

                                        for line in lines2:
                                            if old_date in line:
                                                lines2 = [line.replace(old_date, new_date) for line in lines2]
                                                with open("customer_information.txt", "w") as file3:
                                                    file3.writelines(lines2)

                                        print()
                                        print('customer information list:')
                                        print('data format: name,ic,phone,city,date,username,password')
                                        with open("customer_information.txt", "r") as read3:
                                            print(read3.read())
                                        break


                                elif choice == '5':
                                    while True:
                                        print("customer login information:")
                                        with open("customer_login_file.txt", "r") as cus_log:
                                            print(cus_log.read())

                                        while True:
                                            old_username = input("Please input the customer's previous username: ")
                                            if old_username == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break
                                        
                                        while True:
                                            new_username = input("Please input the customer's new username: ")
                                            if new_username == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break      

                                        with open("customer_login_file.txt", "r") as file:
                                            lines = file.readlines()

                                        for line in lines:
                                            if old_username in line:
                                                lines = [line.replace(old_username, new_username) for line in lines]
                                                with open("customer_login_file.txt", "w") as file2:
                                                    file2.writelines(lines)
                                        
                                        with open("customer_information.txt", "r") as file3:
                                            lines2 = file3.readlines()

                                        for line in lines2:
                                            if old_username in line:
                                                lines2 = [line.replace(old_username, new_username) for line in lines2]
                                                with open("customer_information.txt", "w") as file3:
                                                    file3.writelines(lines2)

                                        print()
                                        print('customer login list:')
                                        print('data format: username,password')
                                        with open("customer_login_file.txt", "r") as read2:
                                            print(read2.read())
                                        print('customer information list:')
                                        print('data format: name,ic,phone,city,date,username,password')
                                        with open("customer_information.txt", "r") as read3:
                                            print(read3.read())
                                        break

                                elif choice == '6':
                                    while True:
                                        print("customer login information:")
                                        print('data format: username,password')
                                        with open("customer_login_file.txt", "r") as cus_log:
                                            print(cus_log.read())

                                        while True:
                                            old_pass = input("Please input the customer's previous password: ")
                                            if old_pass == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break
                                        
                                        while True:
                                            new_pass = input("Please input the customer's new password: ")
                                            if new_pass == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break      

                                        with open("customer_login_file.txt", "r") as file:
                                            lines = file.readlines()

                                        for line in lines:
                                            if old_pass in line:
                                                lines = [line.replace(old_pass, new_pass) for line in lines]
                                                with open("customer_login_file.txt", "w") as file2:
                                                    file2.writelines(lines)
                                        
                                        with open("customer_information.txt", "r") as file3:
                                            lines2 = file3.readlines()

                                        for line in lines2:
                                            if old_pass in line:
                                                lines2 = [line.replace(old_pass, new_pass) for line in lines2]
                                                with open("customer_information.txt", "w") as file3:
                                                    file3.writelines(lines2)

                                        print()
                                        print('customer login list:')
                                        print('data format: username,password')
                                        with open("customer_login_file.txt", "r") as read2:
                                            print(read2.read())
                                        print('customer information list:')
                                        print('data format: name,ic,phone,city,date,username,password')
                                        with open("customer_information.txt", "r") as read3:
                                            print(read3.read())
                                        break

                                elif choice == '7':
                                    print('going back....')
                                    time.sleep(1)
                                    break

                                else:
                                    print('please try again')
                                    continue

                        elif cus_log == '2':
                            while True:
                                print('''
Which admin data do you want to modify?
1) Name
2) Phone number
3) City
4) Date
5) Username
6) Password 
7) Back                 
''')        

                                choice = input("Please choose which data value to modify: ")
                                if choice == '':
                                    print('cannot be empty')
                                    continue

                                elif choice.isalpha():
                                    print('numbers only')
                                    continue

                                elif choice == '1':
                                    while True:
                                        print("admin information:")
                                        print('data format: name,ic,phone,city,date,username,password')
                                        with open("admin_information.txt", "r") as ad_info:
                                            print(ad_info.read())

                                        while True:
                                            old_name = input("Please input the customer's previous name: ")
                                            if old_name == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break
                                        
                                        while True:
                                            new_name = input("Please input the customer's new name: ")
                                            if new_name == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break   

                                        with open("admin_information.txt", "r") as file:
                                            lines = file.readlines()

                                        for line in lines:
                                            if old_name in line:
                                                lines = [line.replace(old_name, new_name) for line in lines]
                                                with open("admin_information.txt", "w") as file2:
                                                    file2.writelines(lines)
                                        
                                        with open("admin_information.txt", "r") as file3:
                                            lines2 = file3.readlines()

                                        for line in lines2:
                                            if old_name in line:
                                                lines2 = [line.replace(old_name, new_name) for line in lines2]
                                                with open("admin_information.txt", "w") as file3:
                                                    file3.writelines(lines2)

                                        print()
                                        print('admin information list:')
                                        print('data format: name,ic,phone,city,date,username,password')
                                        with open("admin_information.txt", "r") as read3:
                                            print(read3.read())
                                        break



                                elif choice == '2':
                                    while True:
                                        print("admin information:")
                                        print('data format: name,ic,phone,city,date,username,password')
                                        with open("admin_information.txt", "r") as ad_info:
                                            print(ad_info.read())

                                        while True:
                                            old_phone = input("Please input the customer's previous phone number: ")
                                            if old_phone == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break

                                        while True:
                                            new_phone = input("Please input the customer's new phone number: ")
                                            if new_phone == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break

                                        with open("admin_information.txt", "r") as file:
                                            lines = file.readlines()

                                        for line in lines:
                                            if old_phone in line:
                                                lines = [line.replace(old_phone, new_phone) for line in lines]
                                                with open("admin_information.txt", "w") as file2:
                                                    file2.writelines(lines)

                                        with open("admin_information.txt", "r") as file3:
                                            lines2 = file3.readlines()

                                        for line in lines2:
                                            if old_phone in line:
                                                lines2 = [line.replace(old_phone, new_phone) for line in lines2]
                                                with open("admin_information.txt", "w") as file3:
                                                    file3.writelines(lines2)

                                        print()
                                        print('admin information list:')
                                        print('data format: name,ic,phone,city,date,username,password')
                                        with open("admin_information.txt", "r") as read3:
                                            print(read3.read())
                                        break


                                elif choice == '3':
                                    while True:
                                        print("admin information:")
                                        print('data format: name,ic,phone,city,date,username,password')
                                        with open("admin_information.txt", "r") as ad_info:
                                            print(ad_info.read())

                                        while True:
                                            old_city = input("Please input the customer's previous city: ")
                                            if old_city == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break
                                        
                                        while True:
                                            new_city = input("Please input the customer's new city: ")
                                            if new_city == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break   

                                        with open("admin_information.txt", "r") as file:
                                            lines = file.readlines()

                                        for line in lines:
                                            if old_city in line:
                                                lines = [line.replace(old_city, new_city) for line in lines]
                                                with open("admin_information.txt", "w") as file2:
                                                    file2.writelines(lines)
                                        
                                        with open("admin_information.txt", "r") as file3:
                                            lines2 = file3.readlines()

                                        for line in lines2:
                                            if old_city in line:
                                                lines2 = [line.replace(old_city, new_city) for line in lines2]
                                                with open("admin_information.txt", "w") as file3:
                                                    file3.writelines(lines2)

                                        print()
                                        print('admin information list:')
                                        print('data format: name,ic,phone,city,date,username,password')
                                        with open("admin_information.txt", "r") as read3:
                                            print(read3.read())
                                        break


                                elif choice == '4':
                                    while True:
                                        print("admin information:")
                                        print('data format: name,ic,phone,city,date,username,password')
                                        with open("admin_information.txt", "r") as ad_info:
                                            print(ad_info.read())

                                        while True:
                                            old_date = input("Please input the customer's previous name: ")
                                            if old_date == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break
                                        
                                        while True:
                                            new_date = input("Please input the customer's new name: ")
                                            if new_date == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break   
                                        with open("admin_information.txt", "r") as file:
                                            lines = file.readlines()

                                        for line in lines:
                                            if old_date in line:
                                                lines = [line.replace(old_date, new_date) for line in lines]
                                                with open("admin_information.txt", "w") as file2:
                                                    file2.writelines(lines)
                                        
                                        with open("admin_information.txt", "r") as file3:
                                            lines2 = file3.readlines()

                                        for line in lines2:
                                            if old_date in line:
                                                lines2 = [line.replace(old_date, new_date) for line in lines2]
                                                with open("admin_information.txt", "w") as file3:
                                                    file3.writelines(lines2)

                                        print()
                                        print('admin information list:')
                                        print('data format: name,ic,phone,city,date,username,password')
                                        with open("admin_information.txt", "r") as read3:
                                            print(read3.read())
                                        break



                                elif choice == '5':
                                    while True:
                                        print("admin login information:")
                                        print('data format: username,password')
                                        with open("admin_login_file.txt", "r") as ad_log:
                                            print(ad_log.read())

                                        while True:
                                            old_username = input("Please input the customer's previous name: ")
                                            if old_username == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break
                                        
                                        while True:
                                            new_username = input("Please input the customer's new name: ")
                                            if new_username == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break   
                                        with open("admin_login_file.txt", "r") as file:
                                            lines = file.readlines()

                                        for line in lines:
                                            if old_username in line:
                                                lines = [line.replace(old_username, new_username) for line in lines]
                                                with open("admin_login_file.txt", "w") as file2:
                                                    file2.writelines(lines)
                                        
                                        with open("admin_information.txt", "r") as file3:
                                            lines2 = file3.readlines()

                                        for line in lines2:
                                            if old_username in line:
                                                lines2 = [line.replace(old_username, new_username) for line in lines2]
                                                with open("admin_information.txt", "w") as file3:
                                                    file3.writelines(lines2)

                                        print()
                                        print('admin login list:')
                                        print('data format: username,password')
                                        with open("admin_login_file.txt", "r") as read2:
                                            print(read2.read())
                                        print('admin information list:')
                                        print('data format: name,ic,phone,city,date,username,password')
                                        with open("admin_information.txt", "r") as read3:
                                            print(read3.read())
                                        break

                                elif choice == '6':
                                    while True:
                                        print("admin login information:")
                                        print('data format: username,password')
                                        with open("admin_login_file.txt", "r") as ad_log:
                                            print(ad_log.read())

                                        while True:
                                            old_pass = input("Please input the customer's previous name: ")
                                            if old_pass == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break
                                        
                                        while True:
                                            new_pass = input("Please input the customer's new name: ")
                                            if new_pass == '':
                                                print('cannot be empty')
                                                continue
                                            else:
                                                break   

                                        with open("admin_login_file.txt", "r") as file:
                                            lines = file.readlines()

                                        for line in lines:
                                            if old_pass in line:
                                                lines = [line.replace(old_pass, new_pass) for line in lines]
                                                with open("admin_login_file.txt", "w") as file2:
                                                    file2.writelines(lines)
                                        
                                        with open("admin_information.txt", "r") as file3:
                                            lines2 = file3.readlines()

                                        for line in lines2:
                                            if old_pass in line:
                                                lines2 = [line.replace(old_pass, new_pass) for line in lines2]
                                                with open("admin_information.txt", "w") as file3:
                                                    file3.writelines(lines2)

                                        print()
                                        print('admin login list:')
                                        print('data format: username,password')
                                        with open("admin_login_file.txt", "r") as read2:
                                            print(read2.read())
                                        print('full admin information list:')
                                        print('data format: name,ic,phone,city,date,username,password')
                                        with open("admin_information.txt", "r") as read3:
                                            print(read3.read())
                                        break

                                elif choice == '7':
                                    print('going back....') 
                                    time.sleep(1)
                                    break 

                                else:
                                    print('please try again')
                                    continue

                        elif cus_log == '3':             
                            print('going back...')
                            time.sleep(1)         
                            break
                        
                        else:
                            print('please try again')
                            continue

                # disable user access
                elif choice == '4':
                    while True:
                        print('''
which user do you want to disable?
1) Customer 
2) Admin
3) Back''')

                        user = input('Please select an option: ')
                        if user == '':
                            print('cannot be empty')
                            continue

                        elif user == '1':
                            print("These are the names and details of customers")
                            print('data format: name,ic,phone,city,date,username,password')
                            with open("customer_information.txt", 'r') as cus_detail:
                                print(cus_detail.read())   
                            print("These are the list of users that are currently accessible:")
                            print('data format: username,password')
                            with open("customer_login_file.txt", 'r') as cus_detail:
                                print(cus_detail.read())   
                            

                            while True:
                                username = str(input('please input the username of the customer: ')) 
                                if username == '':
                                    print('cannot be empty')
                                    continue
                                else:
                                    break   
                            
                            while True:
                                password = str(input('please input the password of the customer: ')) 
                                if password == '':
                                    print('cannot be empty')
                                    continue
                                else:
                                    break   
                            with open("customer_login_file.txt", 'r') as cus_log:
                                info_rows = cus_log.readlines()
                            delete_username = [row for row in info_rows if username not in row] 
                            delete_password = [row for row in info_rows if password not in row] 
                            
                            with open("customer_login_file.txt", 'w') as cus_log:
                                cus_log.writelines(delete_username)


                            time.sleep(1)
                            print('you have disabled the customer')
                            break


                        elif user == '2':
                            print("These are the names and details of admins")
                            print('data format: name,ic,phone,city,date,username,password')
                            with open("admin_information.txt", 'r') as ad_detail:
                                print(ad_detail.read())   
                            print("These are the list of users that are currently accessible:")
                            print('data format: username,password')
                            with open("admin_login_file.txt", 'r') as ad_detail:
                                print(ad_detail.read())   
                                                
                            while True:
                                username = str(input('please input the username of the admin: ')) 
                                if username == '':
                                    print('cannot be empty')
                                    continue
                                else:
                                    break   
                            
                            while True:
                                password = str(input('please input the password of the admin: ')) 
                                if password == '':
                                    print('cannot be empty')
                                    continue
                                else:
                                    break   
                            with open("admin_login_file.txt", 'r') as ad_log:
                                info_rows = ad_log.readlines()
                            delete_username = [row for row in info_rows if username not in row] 
                            delete_password = [row for row in info_rows if password not in row] 

                            with open("admin_login_file.txt", 'w') as ad_log:
                                ad_log.writelines(delete_username)

                            time.sleep(1)
                            print('you have disabled the admin')
                            break
                        
                        elif user == '3':
                            print('going back....')
                            time.sleep(1)
                            break
                        
                        else:
                            print("please try again")
                            
                elif choice == '5':
                    username = input("Enter customer username: ")
                    with open("customer_system_usage.txt", "r") as c:
                        lines = c.readlines()
                        for line in lines:
                            line = line.strip()
                            username = line.split(",")[0]
                            if username == username:
                                print(line)
                        while True:
                            quit = input("Enter Q to quit: ")
                            if quit.upper() == "Q":
                                break
                            else:
                                continue



                elif choice == '6':
                    with open('purchase_order_list.txt','r') as read_purchase:
                        print(read_purchase.read())
                    with open('repair_order_list.txt','r') as read_repair:
                        print(read_repair.read())        
                        while True:
                            off = input('press q to quit: ')
                            if off == 'q':
                                time.sleep(0.5)
                                break
                            else:
                                continue   
                    continue

                elif choice == '7':
                    while True:
                        print('''
which user report do you want to access?
1) customer
2) admin
''')
                        superuser_choice = input('please select an option: ')
                        if superuser_choice == '':
                            print('cannot be empty')
                            continue
                        elif superuser_choice == '1':
                            with open('customer_system_usage.txt','r') as read_cus_act:
                                print(read_cus_act.read())
                            off = input('press q to quit: ')
                            if off == 'q':
                                break
                            else:
                                continue
                        elif superuser_choice == '2':
                            with open('admin_action.txt','r') as read_ad_act:
                                print(read_ad_act.read())
                            off = input('press q to quit: ')
                            if off == 'q':
                                break
                            else:
                                continue
                    

                elif choice == '8':
                    print('going back....')
                    time.sleep(1)
                    break

                    
                else:
                    print('please try again!')
                    continue
        
        #super user log in error
        else:
            print("Invalid username or password.")
            continue

    elif user_type == '2' and ope =='2':
        print('exiting menu...')
        time.sleep(0.5)
        continue
    
    else:
        print('please try again')
        continue
