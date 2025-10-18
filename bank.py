import pandas as pd
data={'username':["user1"], 'email':["user1@gmail.com"],'password':["user1pass"] , 'savings':[8000]}

users=pd.DataFrame(data)
match = users[(users['username'] == 'user1') & (users['password'] == 'user1pass')]
print(match)
username='user1'
logged_user = users.index[users["username"] == username][0]

user_savings = users.at[logged_user, 'savings']
print(user_savings)
users.at[logged_user, 'savings'] += 500
logged_user = users.index[users["username"] == username][0]

user_savings = users.at[logged_user, 'savings']
print(user_savings)





# def bankcalculations(username,password):
#     global users
#     while True:
#         print("\n--- Bank Menu ---")
#         print("1. Check Balance")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Logout")
#         choice = input("Enter your choice: ")
#         logged_user = users.index[users["username"] == username][0]

#         print(logged_user)



    






# while True:
#     user_reg_or_log=input("press \n 1.Registration \n 2.Login \n 3.Quit \n Enter Your Choice:  ")
#     if user_reg_or_log=='1':
#         username=input("Enter user name:")
#         email=input("Enter email :")
#         password=input("Enter password:")
#         match = users[(users['username'] == username) & (users['password'] == password)]
#         if not match.empty:
                
#             print("Credentials already taken try another")

            
#         else:
#             initial_deposite=float(input("initial Deposite amount"))
            
#             new_user = {
#                 'username': username,
#                 'email': email,
#                 'password': password,
#                 'savings': initial_deposite
#             }

#             users=pd.concat([users,pd.DataFrame([new_user])],ignore_index=True)
#             print("Registration Successfull ")
        

#             bankcalculations(username,password)
    
#     elif user_reg_or_log=='2':
#         flag=1
#         while flag==1:
#             username=input("Enter user name:")
#             password=input("Enter password:")
#             match = users[(users['username'] == username) & (users['password'] == password)]
#             if not match.empty:
                
#                 print("Login successfull")
#                 bankcalculations(username,password)

#                 flag=0
#             else:
#                 print("Invalid credentials please try again ")
#                 user_input=input("press q quit C for continue ")
#                 if user_input=='q' or user_input=='Q':
#                     flag=0
#                 else:
#                     flag=1
#     elif user_reg_or_log=='3':
#         print(" Thank you for visiting ")
#         break

#     else:
#         print("invalide choice try again")







        