Name = input("Enter the name:")
Password = input("Enter Password:")
YOB = input("Enter Year of Birth (YOB)")

print(Name)
print(Password)
print(YOB)

if len(Password) < 8:
    print("Password has to be at least 8 short.")
elif Name in Password:
    print("Name can not be used in your password")
elif YOB in Password:
    print("YOB can not be used in Password")
elif not Password.isalpha() and not Password.isnumeric() and not Password.isalnum():
    print("Password is wrong.")
print('Password is set')