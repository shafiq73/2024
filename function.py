# def great_user(): 
#     print("hello, user!")
# great_user()

# def aoa():
#     print('assalam o alekum, i am from pakistan')
# # aoa()

# def aoa(name):
#     print(f"assalam o alekum, {name}!,aap kaisy ho?")
# # aoa('shafiq')

# def aoa(name='khuda ke bandy'):
#     print(f"assalam o elekum ,{name}!,kaisy ho aap?")
# # aoa("adeel")

# Retrun values

# def square (number):
#     return number * number
# print(square(5))



# Recursion

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(6))

# lambda function
# lambda function is a small anonymous function that can take any number of arguments, but can only have

def x (a):
    return a/2

x  = lambda a: a/2
print(x(4))

x = lambda a: a + 10
print(x(5))  

x = lambda a,b: a * b
print(x(5,6))
    
