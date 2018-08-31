print("Hello, Christian!")

# Whenever you are experimenting with a new feature, you should try to make mistakes. For example, in the “Hello, world!” program, what happens if you leave out one of the quotation marks? What if you leave out both? What if you spell print wrong?

print(Hello, world!")

# When I leave out one of the quotation marks, I get the following error, SyntaxError: invalid syntax/

print(Hello, world!)

# When I leave out both of the quotation marks, I get the following error,  SyntaxError: invalid syntax/

prin("Hello, world!")

# When I spell print wrong, I get the following error, NameError: name 'prin' is not defined

# Exercise 1
# 1.) In a print statement, what happens if you leave out one of the parentheses, or both? */

print("Hello, world!"

# When I leave out one of the parentheses, as shown above, I get the following error, SyntaxError: unexpected EOF while parsing

print"Hello, world!"

# When I leave out both of the parentheses, as shown above, I get the following error, SyntaxError: invalid syntax

# 2.) If you are trying to print a string, what happens if you leave out one of the quotation marks, or both?

print(Hello")

# When trying to print a string, if I left out one of the quotation marks, I get the following error, SyntaxError: EOL while scanning string literal

print(Hello)

# When trying to print a string, if I left out both of the quotation marks, I get the following error, NameError: name 'Hello' is not defined

# 3.) You can use a minus sign to make a negative number like -2. What happens if you put a plus sign before a number? What about 2++2?

print(+2)

# If you put a plus sign before a number like 2, as shown above, you get an output of 2.

print(2++2)

# If you try to perform 2++2, as shown above, you get the following error, SyntaxError: invalid syntax

# 4.) In math notation, leading zeros are ok, as in 02. What happens if you try this in Python?

print(02)

# When you try to include leading zeros, as shown above, you get the following error, SyntaxError: invalid token

# 5.) What happens if you have two values with no operator between them?

print(2 5)

# When you have two values with no operator between them, as shown above, you get the following error, SyntaxError: invalid syntax