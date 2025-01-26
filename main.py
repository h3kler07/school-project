#grocery store management  MADE BY - SUSHANT KUMAR , CLASS 12TH A , ROLL NO. 38 , ACADEMIC YEAR 2024-25
import time
import pickle
import os
l = "-------------------------------------------------------------"
print("do you already have a store data file ? y/n")
choice= input()
if choice == "y" or choice == "Y":
   def menu():
      
      choices=R'''
      



               1. VIEW PRESENT ITEMS
               2. ADD NEW ITEMS IN STORE
               3. UPDATE ITEM QUANTITY
               4. VIEW ITEMS OUT OF STOCK
               5. REMOVE ITEMS FROM STOCK
               6. SELL ITEMS
               7. EXIT
      

      '''
      print(l)
      print(choices)
      print(l)
      m = int(input("ENTER RESPECTIVE NUMBER OF YOUR CHOICE:-   "))
      if m == 1:
         os.system('cls')
         view_present_items()
      elif m ==2:
         os.system('cls')
         add_new_items()
      elif m ==3:
         os.system('cls')
         add_quantity_in_stock()
      elif m ==4:
         os.system('cls')
         items_out_of_stock()
      elif m ==5:
         os.system('cls')
         remove_item_from_stock()
      elif m == 6:
         os.system('cls')
         sell()
      elif m == 7:
         exit()
   def redirect():

      try:
         a = input("--------ENTER ANYTHING TO GO TO MENU------      ")
         os.system('cls')
         menu()
      except Exception as e:
         
         os.system("cls")
         menu()
   def get_item_data():
      with open(r"D:\CODiNG\PYTHON\school_project\item_data.dat" , 'rb') as f:  
         x=pickle.load(f)

      return x
   def update(new_dict):
      with open(r"D:\CODiNG\PYTHON\school_project\item_data.dat" , 'wb') as f:
         pickle.dump(new_dict,f)

   def add_new_items():
         prev_data=get_item_data()
         
         while True:
            
            choice = str(input("Do you want to add more item in stock??  y/n :-    "))
            if  choice == "y" or choice=="Y":
               name = str(input(("enter item name:-     ")))
               name=name.lower()
               name.replace(" ","_")
               amount = int(input(f"enter amount of {name} you want to add :-     "))
               if name not in prev_data:
                  prev_data[name] = amount
                  print(l)
                  print(f"{name} with amount {amount}kgs has been added to stock")
                  print(l)
                  
               else:
                  print(f"{name} IS ALREADY PRESENT IN CURRENT STOCK")
                  redirect()
            elif choice == "n" or choice=="N":
               update(prev_data)
               os.system('cls')
               break
               
               
            else:
               os.system('cls')
               print("ERROR:  ---------PLEASE CHOOSE FROM y/n--------")

               add_new_items()
         menu()


   def add_quantity_in_stock():
         prev_data = get_item_data()      
         print_items(prev_data)
         item = input("choose an item from above (*case sensitive*) :-    ")
         if item in prev_data:
            amount = int(input("ENTER HOW MUCH AMOUNT IN KGS IS TO BE ADDED IN STOCK:-   "))
            print(f"amount for {item} has been changed succesfully... {str(prev_data[item])} ----------> {str(prev_data[item]+amount)}")
            prev_data[item] = prev_data[item]+amount
            update(prev_data)
            redirect()
         else:
            os.system('cls')

            print(f"ERROR: --------item {item} not in stock!!--------")
            
            add_quantity_in_stock()


   def print_items(data):
      num = 1
      print("---------|---------------|----------|")
      print("  S.NO.  "+"|"+"     ITEMS     "+"|"+"  AMOUNT  "+"|")
      print("---------|---------------|----------|")
      for i in data:
         
         print(str(num)+" "*(9-len(str(num)))+"|"+i+" "*(15-len(i))+"|" + str(data[i])+" "*(10-len(str(data[i])))+"|")
         print("---------|---------------|----------|")
         num = num+1


   def view_present_items():
      os.system('cls')
      data = get_item_data()
      print_items(data)
      
      redirect()
         
   def items_out_of_stock():
      data=get_item_data()
      out_of_stock = {}
      for i in data:
         if data[i] == 0:
            out_of_stock[i] = 0
         else:
            continue
         num = 1
      if len(out_of_stock) != 0:
         print_items(out_of_stock)
         redirect()
      else:
         os.system('cls')
         print("--------NO ITEMS ARE OUT OF STOCK--------")
         redirect()
         
   def remove_item_from_stock():
      data = get_item_data()
      print_items(data)
      if len(data) !=0:
         item = input("ENTER ITEM TO BE REMOVED FROM STOCK (*CASE SENSITIVE*) :-   ")
         if item in data:
            data.pop(item)
            os.system('cls')
            update(data)
            print(l)
            print(f"ITEM {item} SUCCESFULLY REMOVED FROM STOCK")
            print(l)
            redirect()      
         else:
            print(f"{item} NOT IN STOCK !!")
            redirect()
      else:
         print("NOTHING IN STOCK TO REMOVE")
         redirect()
   def sell():
      data = get_item_data()
      print_items(data)
      print(l)
      item = input("ENTER THE ITEM TO SELL (*CASE SENSITIVE*) :-   ")
      if data[item] !=0:
         amount = int(input(f"ENTER AMOUNT OF {item} TO SELL :-  "))
         if data[item]-amount <0:
            print(f"INSUFFICIENT AMOUNT OF {item} IN STOCK.   SHORT BY {(data[item]-amount)*(-1)} {item}")
            redirect()
         else:
            data[item] = data[item]-amount
            update(data)
            os.system('cls')   
            print(f"{amount} {item} SELL SUCCESFULLY")
            redirect()
      else:
         print(f"ITEM IS OUT OF STOCK!!! PLEASE ADD MORE {item} IN STOCK")
         redirect()
   menu()


else:
   print("initializing the store data file........")
   print("please restart the program and select 'y' next time when asked for store list")
   with open(r"D:\CODiNG\PYTHON\school_project\item_data.dat" , 'wb') as f:  
      y={}
      pickle.dump(y,f)
      print("dumped")



