import mysql.connector as sql
def crt_db():
    con=sql.connect(host='localhost',user='root',passwd='student')
    cur=con.cursor()
    qry='create database initial_d'
    try:
        cur.execute(qry)
    except:
        pass
    con.close()
crt_db()

con=con=sql.connect(host='localhost',user='root',passwd='student',database='initial_d')
cur=con.cursor()
def crt_cars():
    qry='''create table cars(
car_id varchar(05) PRIMARY KEY,
car_name varchar(40),
type varchar(15),
base_price int);'''
    try:
        cur.execute(qry)
    except:
        pass
    qry2='''insert into cars
values
('S1','Mahindra XUV700','SUV',5000),
('S2','Toyota Urban Cruiser','SUV',4000),
('S3','Tata Harrier','SUV',5500),
('S4','Toyota Fortuner','SUV',5000),
('S5','Volkswagen Tiguan','SUV',7000),
('S6','Mercedes G63 AMG','SUV',25000),
('H1','Hyundai i20','Hatchback',3000),
('H2','Honda Jazz','Hatchback',3500),
('H3','MINI Cooper JCW','Hatchback',8000),
('H4','Mercedes Benz AMG A45 S','Hatchback',10000),
('H5','Tata Altroz','Hatchback',4000),
('SE1','Volkswagen Virtus','Sedan',4000),
('SE2','Honda City','Sedan',3500),
('SE3','Maruti Suzuki Ciaz','Sedan',3500),
('SE4','Lexus ES','Sedan',8000),
('SE5','Mercedes Benz C-Class','Sedan',7500),
('SS1','MCLaren 765 LT','Supercar',35000),
('SS2','Ferrari SF90 Stradale','Supercar',40000),
('SS3','Aston Martin Vanquish S','Supercar',30000),
('SS4','Lamborghini Huracan STO','Supercar',30000),
('SS5','Jaguar F-Type','Supercar',30000),
('OF1','BOWLER Bulldog','Offroad',25000),
('OF2','BOWLER CSP575','Offroad',24000),
('OF3','Mammoth TRX 1000','Offroad',30000),
('OF4','Ford Supersnake','Offroad',24000);'''
    try:
        cur.execute(qry2)
    except:
        pass
    con.commit()
crt_cars()

def crt_user():
    qry='''create table users
(username varchar(20) primary key,
email varchar(40),
password varchar(20),
car_id varchar(5),
days int(2),
profile varchar(10));'''
    try:
        cur.execute(qry)
    except:
        pass
    qry2='''insert into users
values('admin','admin1@gmail.com','admin@123',NULL,NULL,'admin')'''
    try:
        cur.execute(qry2)
    except:
        pass
    con.commit()
crt_user()

def add_car():
    print('-'*54)
    cid=input('ENTER CAR ID : ')
    cname=input('ENTER CAR NAME : ')
    ctype=input('ENTER CAR TYPE : ')
    cprice=int(input('ENTER BASE PRICE : '))
    print('-'*54)
    qry='''insert into cars
values('{}','{}','{}',{})'''
    try:
        cur.execute(qry.format(cid,cname,ctype,cprice))
    except:
        pass
    con.commit()
    print('CAR ADDED'.center(30))
    print('-'*54)

def mod_car():
    print('-'*54)
    cid=input('ENTER CAR ID TO BE MODIFIED : ')
    nprice=int(input('ENTER NEW PRICE : '))
    print('-'*54)
    qry='''update cars
set base_price= {} where car_id='{}' '''
    try:
        cur.execute(qry.format(nprice,cid))
    except:
        pass
    con.commit()
    print('CAR DETAILS MODIFIED'.center(30))

def del_car():
    print('-'*54)
    cid=input('ENTER CAR ID TO BE DELETED : ')
    print('-'*54)
    qry='''delete from cars
where car_id='{}' '''
    try:
        cur.execute(qry.format(cid))
    except:
        pass
    con.commit()
    print('CAR DETAILS DELETED'.center(30))

def sign_up():
    print('-'*54)
    us=input('ENTER USERNAME : ')
    eml=input('ENTER EMAIL : ')
    passwd=input('ENTER PASSWORD : ')
    print('-'*54)
    qry='''insert into users
values('{}','{}','{}',NULL,NULL,'user')'''
    try:
        cur.execute(qry.format(us,eml,passwd))
        print('SIGN UP SUCCESSFUL'.center(30))
    except:
        pass
    con.commit()
    print('-'*54) 

us=''
check=0
flag=0
def login():
    global flag
    global us
    global check
    print('-'*54)
    us=input('ENTER USERNAME : ')
    passwd=input('ENTER PASSWORD : ')
    print('-'*54)
    qry='''select * from users'''
    cur.execute(qry)
    rec=cur.fetchall()
    for i in rec:
        if i[0]==us and i[2]==passwd and i[5]!='admin':
            print('LOGIN SUCCESSFUL'.center(30))
            check=0
            flag=1
            break
        elif i[0]==us and i[2]==passwd and i[5]=='admin':
            check=1
            flag=1
            print('LOGIN SUCCESSFUL'.center(30))
            break
    else :
        print('PLEASE SIGN-UP'.center(30))
        return

def rent_car():
    print('-'*54)
    ch=int(input('''WHAT TYPE OF CAR WOULD U LIKE 
1.SUV \U0001F699
2.Sedan \U0001F697
3.Hatchback \U0001F697 
4.Supercar \U0001F3CE  
5.Offroad \U0001F699 \n'''))
    if ch==1:
        car='SUV'
    elif ch==2:
        car='Sedan'
    elif ch==3:
        car='Hatchback'
    elif ch==4:
        car='Supercar'
    elif ch==5:
        car='Offroad'
    else:
        print('INVALID CHOICE'.center(30))
        return
    qry='''select * from cars
where type='{}' '''
    cur.execute(qry.format(car))
    print('-'*54)
    print('AVAILABLE CARS'.center(30))
    print('-'*54)
    print('{:<8}{:<30}{:<10}{:<7}'.format('CAR ID','NAME','TYPE','PRICE'))
    print('-'*54)
    rec=cur.fetchall()
    cid=[]
    for i in rec:
        print('{:<8}{:<30}{:<10}{:<7}'.format(i[0],i[1],i[2],i[3]))
        cid.append(i[0])
    print('-'*54)
    crch=input('ENTER CAR ID TO RENT : ')
    crch=crch.upper()
    print('-'*54)
    if crch not in cid:
        print('INVALID CHOICE ')
        return
    cur.execute('select * from users where username="{}" '.format(us))
    rec2=cur.fetchone()
    if rec2[3]!=None:
        print('SORRY WE PROVIDE ONLY ONE VEHICLE PER USER'.center(30))
    else:
        day=int(input('HOW MANY DAYS WILL YOU BE RENTING IT FOR : '))
        qry2='''update users
set car_id ='{}',days='{}' where username='{}' '''
        cur.execute(qry2.format(crch,day,us))
        print('-'*54)
        print('CAR RENTED SUCCESSFULLY'.center(30))
    con.commit()

def inv():
    cur.execute('select * from cars')
    print('OUR CARS'.center(50))
    print('-'*54)
    print('{:<8}{:<30}{:<10}{:<7}'.format('CAR ID','NAME','TYPE','PRICE'))
    print('-'*54)
    rec=cur.fetchall()
    for i in rec:
        print('{:<8}{:<30}{:<10}{:<7}'.format(i[0],i[1],i[2],i[3]))

def us_details():
    qry='''select username,email,c.car_id,car_name,days,base_price from users u,cars c
where c.car_id=u.car_id'''
    try:
        cur.execute(qry)
        rec=cur.fetchone()
        f=rec[4]
        print('{:<20}|{:<25}|{:<7}|{:<24}|{:<12}|{:<7}'.format('USERNAME','EMAIL','CAR ID','CAR NAME','DAYS RENTED','TOTAL PRICE'))
        print('{:<20}|{:<25}|{:<7}|{:<24}|{:<12}|{:<7}'.format(rec[0],rec[1],rec[2],rec[3],rec[4],rec[4]*rec[5]))
    except:
        print('YOU HAVE NO ORDERS AT THE MOMENT'.center(50))
        
def cnc_order():
    ch=input('PLEASE CONFIRM ORDER CANCELLATION [Y/y] : ')
    if ch in 'Yy':
        qry='''update users
set car_id=NULL,days=NULL where username='{}' '''
        cur.execute(qry.format(us))
        print('YOUR ORDER HAS BEEN CANCELLED'.center(30))
        con.commit()
    
def admenu():
    while True:
        print('-'*54)     
        print('''1. ADD CAR               \u2B55
2. MODIFY CAR DETAILS    \u2B55
3. REMOVE CAR            \u2B55
4. RETURN TO HOMEPAGE    \u2716''')
        print('-'*54)
        ch=int(input('ENTER CHOICE : '))
        print('-'*54)
        if ch==1:
            add_car()
        elif ch==2:
            mod_car()
        elif ch==3:
            del_car()
        elif ch==4:
            break

def umenu():
    while True:
        print('-'*54)            
        print('''1. RENT A CAR            \u2B55
2. CURRENT ORDER         \u2B55
3. CANCEL ORDER          \u2B55
4. CAR INVENTORY         \u2B55
5. RETURN TO HOMEPAGE    \u2716''')
        print('-'*54)
        ch=int(input('ENTER CHOICE : '))
        print('-'*54)
        if ch==1:
            rent_car()
        elif ch==2:
            us_details()
        elif ch==3:
            cnc_order()
        elif ch==4:
            inv()
        elif ch==5:
            break

print('WELCOME TO INITIAL D'.center(50))      
while True:
    print('-'*54)
    print('''1. SIGN UP       \u2B55
2. LOGIN         \u2B55
3. LEAVE GARAGE  \u2716''')
    print('-'*54)
    ch=int(input('ENTER CHOICE : '))
    if ch==1:
        sign_up()
    elif ch==2:
        login()
        if flag==1:
            if check==1:
                admenu()
            elif check==0:
                umenu()
    elif ch==3:
        print('THANK YOU FOR VISITING INITIAL D'.center(50))
        break
