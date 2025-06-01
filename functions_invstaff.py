import time
import datetime

def invstaff_register(new_username,new_password):
    with open("invstaff_register.txt", "a") as inv_register:
        inv_register.write(f"\n{new_username},{new_password}")
    time.sleep(1)

def addinvstaff_info(add_user,add_pass):
    with open("invstaff_info.txt", "a") as inv_info:
        inv_info.write(f"\n{add_user},{add_pass}")
    time.sleep(1)
    

def generate_order_id(length=3):

    timestamp = int(time.time() * 1000)
    or_id = str(timestamp)[-length:]
    return "O" + or_id


def add_order(order_id, username, order_time, order_items, total_text, order_status):
    with open("pur_order.txt", "a") as order_info:
        order_info.write(f"\n{order_id},{username},{order_time},{order_items},{total_text},{order_status}")
    time.sleep(1)

    