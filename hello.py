# using input 

first_name = input("what is your first name? ")
print("Your first name ", first_name )

# python Lambda
# lambda funcation is a small anonymous function can take any number arguments but can only have one expression


x = lambda a: a +12
print(x(5))

#function is a block of code which only runs when it is called 

def which_os(os):
    print(os)

which_os("Andorid")
which_os("Iphone")