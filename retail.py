import mysql.connector

def admin_auth():
    hu="admin"
    hp="pass"
    while True:
        auser=input("Enter Username : ")
        

        if auser==hu:
            apass=input("Enter Password : ")
            if apass==hp:
                print("Login Ho Gya")
                admin()
                return

            else:
                print("Fir se Try kar chomu")
        else:
            print("Try again")


def admin():
    while True:
        alert()
        work=int(input(f"\n1. Manage Stock \n"
                   f"2. Track Stock \n"
                   f"3. Back to main menu\n  "))
    
        if work==1:
            manage()
            
        elif work==2:
            track()
        else:
            print("Thik se dekh ke input daal")



def manage():
    
    
    while True:
        alert()
        work=int(input(f"\n1. Add items\n"
                   f"2. Update items\n"
                   f"3. Delete items\n"
                   f"4. Search items\n"
                   f"5. Back\n  "))
        if work==1:
            add()
        elif work==2:
            update()
        elif work==3:
            delete()
        elif work==4:
            search()
        elif work==5:
            return
        else:
            print("Thik se dekh ke input daal")


def add():
    name=input("Enter product name\n")
    price=input("Product price\n")
    quantity=input("Quantity\n")
    
    query=f"insert into item VALUES ('{name}',{price},{quantity})"
    cursor.execute(query)
    con.commit()
    print("product added succesfully")
    return

def update():
    name=input("product name \n")
    what=input("what you want to change\n")
    new=input(f"Enter new {what}\n")
    query=f"update item set {what}={new} where name = '{name}'"
    cursor.execute(query)
    con.commit()
    print("product updated ")
    return
def delete():
    name=input("product name\n")
    sure=input(f"are you sure want to delete {name}\n (Y/N)")
    if sure =="y"or sure=="Y":
        query=f"delete from item where name ='{name}'"
        cursor.execute(query)
        con.commit()
        print(f"{name} deleted")
        return
    else:
        return
def search():
    name=input("Product name\n")
    query=f"select * from item where name = '{name}'"
    cursor.execute(query)
    result=cursor.fetchall()
    if result:
        for data in result:
            print(f"\n\n\n{data[0]:<10} {data[1]} rupees  {data[2]:>10} left")
    else:
        print(f"{name} not found")

    p=input()
    return

def track():
    query="select name,quantity from item"
    cursor.execute(query)
    result=cursor.fetchall()
    if result:
        for data in result:
            print(f"{data[0]:<10} {data[1]} Left")
    else:
        print("NO STOCK")

    p=input()
    return

def alert():
    query="select * from item"
    cursor.execute(query)
    result=cursor.fetchall()
    for data in result:
        if data[2]<6:
            print(f"{data[0]:<5} LOW STOCK")

def staff():
    pass

if __name__=="__main__":
    
    con=mysql.connector.connect(
        user="root",
        password="root",
        host="localhost",
        database="invent"
    )
    cursor=con.cursor()
    
    print("RETAILS")
    
    
    while True:
        user=int(input(f"1. Admin \n"
                   f"2. Staff \n  "))
        if user==1:
            admin_auth()
        elif user==2:
            staff()
        else:
            print("invalid entry")

    