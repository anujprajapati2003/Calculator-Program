#simple calculator

a=float(input("enter first number:"))
b=float(input("enter second number:"))


print("1.Addition")
print("2.subtraction")
print("3. multiplicatin")
print("4. division")

choice =int(input("enter choice(1-4):"))

if choice ==1:
    print("result=",a+b)
elif choice==2:
    print("result =",a-b)
elif choice==3:
    print("result=",a*b)
elif choice==4:
    if b !=0:
        print ("result =",a/b)
    else:
        print ("error:division by zero!")
else:
    print("invalid choice!")
    
