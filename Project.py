
#AIRPORT PASSENGERS DATA MANAGEMENT SYSTEM

import mysql.connector

mydb = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='hotel')
mycursor=mydb.cursor()

def registercust():
    global name
    global addr
    global jr_date
    global source
    global destination
    name=input("Enter Name:")
   
    addr=input("Enter Address:")
    
    jr_date=input("Enter date of Journey:")
    
    source=input("Enter Source:")
    
    destination=input("Enter Destination:")
              
def ticketprice():
        global price
        print("Do yoy want to see Flight classs type available : Enter 1 for yes :")
        ch=int(input("Enter your choice:"))
        if ch==1:
            sql="select * from classtype"
            mycursor.execute(sql)
            rows=mycursor.fetchall()
            for x in rows:
                  print(x)
        print ("We have the following Flight Tickets for you:-")
        print ("1.  Type First class---->Rs 6000 Per person\-")
        print ("2.  Type Business class---->Rs 4000 Per person\-")
        print ("3.  Type Economy class---->Rs 2000 Per person\-")
        x=int(input("Enter Your Choice Please->"))
        n=int(input("No of passenger:"))
        if (x==1):
            print ("You have opted First class")
            price=6000*n
        elif (x==2):
            print ("You have opted Business class")
            price=4000*n
        elif (x==3):
            print ("You have opted Economy class")
            price=2000*n
        else:
            print ("Please choose a class type")
        print ("Your Flight Ticket Price is =",price,"\n")
        return price

def orderitem():
    global s
    print("Do yoy want to see menu available : Enter 1 for yes :")
    ch=int(input("Enter the food of your choice:"))
    if ch==1:
        sql="select * from food"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
              print(x)
              
    print("do you want to purchase from above list:enter your choice:")
    d=int(input("Enter the food of your choice:"))
    if(d==1):
        print("you have ordered tea")
        a=int(input("enter quantity:"))
        s=10*a
        print("your amount for tea is :",s,"\n")
    elif (d==2):
        print("you have ordered coffee")
        a=int(input("enter quantity:"))
        s=10*a
        print("your amount for coffee is :",s,"\n")
    elif(d==3):
        print("you have ordered colddrink")
        a=int(input("enter quantity:"))
        s=20*a
        print("your amount for colddrink is :",s,"\n")
    elif(d==4):
        print("you have ordered samosa")
        a=int(input("enter quantity:"))
        s=10*a
        print("your amount fopr samosa is :",s,"\n")
    elif(d==5):
        print("you have ordered sandwich")
        a=int(input("enter quantity:"))
        s=50*a
        print("your amount fopr sandwich is :",s,"\n")
    elif(d==6):
        print("you have ordered dhokla")
        a=int(input("enter quantity:"))
        s=30*a
        print("your amount for dhokla is :",s,"\n")
    elif(d==7):
        print("you have ordered kachori")
        a=int(input("enter quantity:"))
        s=10*a
        print("your amount for kachori is :",s,"\n")
    elif(d==8):
        print("you have ordered milk")
        a=int(input("enter quantity:"))
        s=20*a
        print("your amount for kachori is :",s,"\n")
    elif(d==9):
        print("you have ordered noodles")
        a=int(input("enter quantity:"))
        s=50*a
        print("your amount for noodles is :",s,"\n")
    elif(d==10):
        print("you have ordered pasta")
        a=int(input("enter quantity:"))
        s=50*a
        print("your amount for pasta is :",s,"\n")
    else:
        print("please enter your choice from the menu")
    return s

def lugagebill():
    global Lgbl
    print("Do yoy want to see rate for luggage  : Enter 1 for yes :")
    ch=int(input("enter your choice:"))
    if ch==1:
        sql="select * from luggage"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
    y=int(input("Enter Your weight of extra luggage->"))
    Lgbl=y*1000
    print("your luggage bill:",Lgbl,"\n")
    return Lgbl
    
    
def appen():
    L=[]
    L.append(name)
    L.append(addr)
    L.append(jr_date)
    L.append(source)
    L.append(destination)
    L.append(Lgbl)
    L.append(s)
    L.append(price)
    cust=(L)
    sql="insert into pdata(custname,addr,jrdate,source,destination,lugagebill,foodbill,Ticket_Price)values(%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,cust)
    mydb.commit()
    
def ticketamount():
    global namecus
    namecus=input("Enter Customer Name:")
    print("Customer Name :",namecus,"\n")
    print("Lugage Bill:")
    lb()
    print("Food Bill:")
    res()
    print("Ticket Price")
    billl()
    return namecus
    

def lb():
    sql1 = "SELECT lugagebill FROM pdata WHERE custname = %s"
    adr1 = (namecus, )

    mycursor.execute(sql1,adr1)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def res():
    sql2 = "SELECT foodbill FROM pdata WHERE custname = %s"
    adr2 = (namecus, )

    mycursor.execute(sql2, adr2)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
        
def billl():
    sql3 = "SELECT Ticket_Price FROM pdata WHERE custname = %s"
    adr3 = (namecus,)

    mycursor.execute(sql3, adr3)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    

def runagain():
    runagn=input("\n Want to run again y/n:")
    while (runagn.lower()=='y'):
        if (runagn.lower()=='y'):
            Menuset()
            runagn=input("\n Want to run again y/n:")
    else:
        print("Thank You")
        
def quit():
    print("Thank You")
    runagn = "n"
                          
def Menuset():
    print("Enter 1: To enter customer data")
    print("Enter 2 : For  view ticket price and select flight class")
    print("Enter 3 : For Food Menu and Bill")
    print("enter 4 : For luggage bill")
    print("enter 5 : For complete amount")
    print("enter 6 : For exit:")
        
    userinput=int(input("Enter Your Choice :"))
    if(userinput==1):
        registercust()
    elif(userinput==2):
         ticketprice()
    elif(userinput==3):
        orderitem()
    elif(userinput==4):
        lugagebill()
        appen()
    elif(userinput==5):
        ticketamount()
    elif(userinput==6):
        quit()
    else:
        print("Enter correct Choice :")
Menuset()
runagain()

