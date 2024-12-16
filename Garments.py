import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as pt
from datetime import date

pd.set_option("display.max_rows", None, "display.max_columns", None)

print("\t\t\tWelcome to ABC Garments")
print("-"*40)
while(1):
    print("\t\t\t 1.Admin")
    print("\t\t\t 2.Customer")
    print("\t\t\t 3. Quit")
    print()
    ch=int(input("Choose your option "))
    if (ch==1):
        while(1):
            print("\t\t\t 1. Product Details")
            print ("\t\t\t 2. Customer Details")
            print("\t\t\t 3. Sales Report")
            print("\t\t\t 4. Exit")
            choice=int(input("Enter your choice "))
            if (choice==1):
                while(1):
                    print("\t\t 1. View Stock")
                    print("\t\t 2. Add Item ")
                    print("\t\t 3. Search Item")
                    print("\t\t 4. Update Stock")
                    print("\t\t 5. Remove Item")
                    print("\t\t 6. Exit")
                    ch1=int(input("Enter your Choice: "))
                    if (ch1==1):
                        df=pd.read_csv("Product.csv",index_col='id')
                        print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
                      
                    elif(ch1==2):
                        pid=int(input("Enter  Id : "))
                        name=input("Enter Product Name Pant/Shirt/T-Shirt: ")
                        brand=input("Enter Brand: ")
                        size=input("Enter Size S/M/L/XL/XXL: ")
                        color=input("Enter Colour: ")
                        price=float(input("Enter Price: "))
                        stock=int(input("Enter Stock : "))
                        df=pd.DataFrame({'id':[pid],'Name':[name],'Brand':[brand],'Size':[size],'Color':[color],'Price':[price],'Quantity':[stock]})
                        df.to_csv("Product.csv",mode='a',header=None,index=False)
                        print("New Item added")
                    elif(ch1==3):
                        df=pd.read_csv("Product.csv",index_col='id')
                        
                        ser=input("Search based on Brand/Size: ")
                        if ser=='Brand':
                            
                            print(df['Brand'].unique())
                            brand=input("Enter the brand: ")
                            print(df[df['Brand']==brand])
                        elif ser=='Size':
                            
                            print(df['Size'].unique())
                            size=input("Enter the Size: ")
                            print(df[df['Size']==size])
                        else:
                            print("Sorry, Incorrect Choice")
                    elif(ch1==4):
                        op='y'
                        df=pd.read_csv("Product.csv",index_col='id')
                        print(df['Brand'].unique())
                        brand=input("Enter the Brand: ")
                        print(df[df['Brand']==brand])
                        while(op=='y'):
                            pid=int(input("Enter Product ID: "))
                            stock=int(input("Enter Stock : "))
                            df.loc[pid,'Quantity']=stock
                            df.to_csv("Product.csv")
                            print("Changes applied")
                            op=input("Do you want to update further on this brand y/n ")
                            if op=='n':
                                break
                        
                    elif(ch1==5):
                        op='y'
                        df=pd.read_csv("Product.csv",index_col='id')
                        print(df['Brand'].unique())
                        brand=input("Enter the Brand: ")
                        print(df[df['Brand']==brand])
                        while(op=='y'):
                            pid=int(input("Enter Product Id to be deleted : "))
                            df=df.drop(pid)
                            print("Item deleted")
                            print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
                            df.to_csv("Product.csv")
                            op=input("Do you want to update further on this brand y/n ")
                            if op=='n':
                                break
                    
                    elif(ch1==6):
                        break
                    else:
                        print("Invalid Choice")
            elif(choice==2):
                while(1):
                    print("\t\t1.View Customer")
                    print("\t\t2. Search Customer")
                    print("\t\t3. Update Customer")
                    print("\t\t4. Delete Customer")
                    print("\t\t5. Exit")
                    ch2=int(input("Enter your Choice "))
                    if (ch2==1):
                        df=pd.read_csv("Customer1.csv",index_col='Cid')
                        print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
                    elif(ch2==2):
                        flag=False
                        df = pd.read_csv("Customer1.csv",index_col='Cid')
                        print(df.index)
                        cid=int(input("Enter Customer Id: "))
                        for i in df.index:
                            if (i==cid):
                                flag=True
                                break
                        if (flag==True):
                            print(df.loc[cid])
                        else:
                            print("Sorry, Record not found")
                    elif(ch2==3):
                        flag=False
                        df = pd.read_csv("Customer1.csv",index_col='Cid')
                        print(df.index)
                        cid=int(input("Enter Customer Id: "))
                        for i in df.index:
                            if (i==cid):
                                flag=True
                                break
                        if (flag==True):
                            name=input("Enter Name: ")
                            contact=int(input("Contact: "))
                            bill_amt = float(input("Bill Amount: "))
                            date=input("Enter date  ")
                            df.loc[cid]=[name,contact,bill_amt,date]
                            df.to_csv("Customer1.csv")
                            print("Values are updated")
                        else:
                            print("Sorry, Record not found")
                    elif(ch2==4):
                        flag=False
                        df = pd.read_csv("Customer1.csv",index_col='Cid')
                        print(df.index)
                        cid=int(input("Enter Customer Id: "))
                        for i in df.index:
                            if (i==cid):
                                flag=True
                                break
                        if (flag==True):
                            df=df.drop(cid)
                            df.to_csv("Customer1.csv")
                            print("Customer is Removed")
                        else:
                            print("Sorry, Record not found")
                    elif(ch2==5):
                        break
                    else:
                        print("Invalid Choice")
                        
            elif(choice==3):
                df=pd.read_csv("Sales1.csv")
                df=df.groupby('Brand').Quantity.sum()
                df.plot(kind='bar')
                pt.xlabel("Brand Name")
                pt.ylabel("Quantity Sold")
                pt.title("Sales Analysis")
                pt.show()
            elif(choice==4):
                break
            else:
                print("Invalid Choice")
    elif(ch==2):
        while(1):
            print("\t\t1. Place order")
            print("\t\t2. View Order")
            print("\t\t3. Bill")
            print("\t\t4. Exit")
            op=int(input("Choose your option : "))
            
            if (op==1):
                op1='y'
                brand=[]
                qty=[]
                price=[]
                bill_amt=[]
                id1=[]
                prod=[]
                item=pd.DataFrame()
                while(op1=='y'):
                    print("1. Pants")
                    print("2. Shirts")
                    print("3. T-Shirts")
                    op2=int(input("Enter your choice : "))
                    df=pd.read_csv("Product.csv",index_col='id')
                    if op2==1:
                        df1=df[df['Name']=='Pant']
                        product="Pant"
                    elif op2==2:
                        df1=df[df['Name']=='Shirt']
                        product="Shirt"
                    elif op2==3:
                        df1=df[df['Name']=='T-Shirt']
                        product="T-Shirt"
                    else:
                        break
                    
                    size=input("Enter Size : ")
                    
                    
                    if (df1[df1['Size']==size].empty):
                        print("Sorry , no Stock")
                        continue
                    else:
                        
                        print(tabulate( df1[df1['Size']==size],headers = 'keys', tablefmt = 'psql'))
                        order=int(input("Enter Product Id: "))
                        
                        no=int(input("Enter Quantity: "))
                        if (no>df.loc[order,'Quantity']):
                            print("Out of Stock")
                            continue
                        else:
                            
                            prod.append(product)
                            id1.append(order)
                            qty.append(no)
                            brand.append(df.loc[order,'Brand'])
                            price.append(df.loc[order,'Price'])
                            bill=no*df.loc[order,'Price']
                            bill_amt.append(bill)
                            op1=input("Do you wish to continue? (y/n) ")
                            if (op1=='n'):
                                item=pd.DataFrame({'id':id1,'Product':prod,'Brand':brand,'Quantity':qty,'Price':price,'Bill_amt':bill_amt})
                                item.set_index("id",inplace=True)
                                break
                modify=input("Do you want to change quantity? y/n")
                if (modify=='y'):
                    print("\t\tYour Order")
                    print(item)
                    
                    id1=int(input("Enter Product id "))
                    qty=int(input("Enter new quantity "))
                    
                    df=pd.read_csv("Product.csv",index_col='id')
                    if qty>df.loc[id1,'Quantity']:
                        print("Out of Stock ")
                        continue
                    else:
                        item.loc[id1,'Quantity']=qty
                        item.loc[id1,'Bill_amt']=item.loc[id1,'Price']*qty
                        print("Quantity Altered... Now Products on your list")
                        print(item)
                delete=  input("Do you want to cancel order? y/n")
                if delete=='y':
                      
                    print("Your Order")
                    
                    print(item)
                    
                    id1=int(input("Enter Product id to be cancelled "))
                    item=item.drop(id1)
                    print("Item cancelled... Now Items on your list")
                    print(item)
                    
                    
            elif(op==2):
                print(item)
                
            elif(op==3):
                print()
                today=date.today()
                print("Your Order")
                print("------------------")
                print()
                print('-'*40)
                print("\t\t ABC Garments, Chennai")
                print("\t\t\t Invoice")
                print("Date: ",today.strftime("%B %d, %Y"))
                print("-"*40)
                
                print(item)
                total=item['Bill_amt'].sum()
                gst=total*5/100
                net=total+gst
                print("-"*40)
                print("\t\t\t Total : ",total)
                print("*-"*40)
                print("\t\t\t GST : ",gst)
                print("-"*40)
                print("\t\t Net Amount Payable ",net)
                print("-"*40)
                name=input("Enter your name: ")
                contact=int(input("Your contact no: "))
                
                df2=pd.read_csv("Customer1.csv",index_col='Cid')
                if (df2.empty):
                    cid=1
                else:
                    
                    cid=df2.index[len(df2)-1]+1
                
                cust=pd.DataFrame({'Cid':[cid],'Name':[name],'Contact':[contact],'Bill_Amt':[net],'Date':[today]})
                cust.to_csv("Customer1.csv",index=False,mode='a',header=None)
                item.to_csv("Sales1.csv",mode='a',header=None)
                item.to_csv("dummy.csv")
                check=pd.read_csv("dummy.csv",index_col='id')
                
                df=pd.read_csv("Product.csv",index_col='id')
                    
                for i in check.index:
                    df.loc[i,'Quantity']=df.loc[i,'Quantity']-item.loc[i,'Quantity']
                df.to_csv("Product.csv")
                print ("Your order is Successful ")
                print("-"*40)
                print("Thank you...Come Again!!")
                print("-"*40)
                
            elif(op==4):
                break
            else:
                    print("Invalid Choice")
                
                    
            
    elif(ch==3):
        break
    else:
            print("Invalid Choice")




            
