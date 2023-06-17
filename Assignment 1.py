#!/usr/bin/env python
# coding: utf-8
Ans 1.

* - expression(multiplication operator)

'hello' - value(string)

-87.8 - value(floating point)

- -> expression(subtraction operator)

/ - expression(division operator)

+ - expression(addition operator)

6 - value(integer)
# Ans 2.
# 
# A string and a variable are two different concepts in programming.
# 
# A string is a data type that represents a sequence of characters. It is used to store and manipulate textual data. In Python, strings are enclosed in quotation marks (either single, double or triple). For example, "hello" and 'world' are both string literals.
# 
# A variable, on the other hand, is a symbolic name or identifier that represents a value in the memory of a computer program. Variables are used to store and manipulate data within a program. They can hold different types of values, including strings, numbers, and more.
# 
# In simpler terms, a string is a specific type of data, representing textual information, while a variable is a container that can hold different types of data, including strings. Variables allow you to assign and store values, while strings are one of the possible types of values that can be stored in variables.
# 
# For example, in Python, you can define a variable called name and assign it a string value:
# name = "John"
# 
# Here, name is the variable, and "John" is the string value assigned to it. The variable name can be used later in the program to access and manipulate the string data stored in it

# Ans 3.
# 
# three different data types in Python:
# 
# Integer (int): The integer data type represents whole numbers without any decimal points. It can be positive, negative, or zero. For example, 5, -10, and 0 are all integers. Integers are typically used for counting, indexing, and performing arithmetic operations.
# 
# String (str): The string data type represents a sequence of characters. It is used to store and manipulate textual data. Strings are usually enclosed in quotation marks (either single or double). For example, "hello" and 'world' are both strings. Strings can contain letters, numbers, symbols, and whitespace. They are commonly used for working with text, such as displaying messages, storing names, or processing textual data.
# 
# Boolean (bool): The boolean data type represents a logical value that can be either true or false. Booleans are used to express conditions and control the flow of a program. They are particularly useful in decision-making and control structures. For example, a boolean variable can be used to determine whether a condition is true or false and then execute different code paths accordingly.

# Ans 4.
# 
# An expression is a combination of values, variables, operators, and function calls that can be evaluated to produce a result. It represents a computation or a calculation. Expressions can be as simple as a single value or complex, involving multiple components and operations.
# 
# The primary purpose of an expression is to compute a value. When an expression is evaluated, the components and operations within it are executed, and a resulting value is obtained. The value can be used for further computations, assignments to variables, or as conditions for control structures (e.g., if statements, loops).
# 
# Expressions are fundamental in programming as they allow for manipulating and transforming data, performing calculations, making decisions, and controlling the flow of a program. They form the building blocks of algorithms and enable the creation of complex programs by combining simple operations and data.

# Ans 5.
# 
# In programming, expressions always have a value associated with them. They can be used within larger expressions or assigned to variables. For example, x = 2 + 3 is an assignment statement where the expression 2 + 3 is evaluated and the resulting value (5) is assigned to the variable x.
# 
# 
# A statement is a complete unit of code that performs an action. It represents an executable instruction or a sequence of instructions. Statements are used to control the flow of a program, define functions, declare variables, or perform other operations. Examples of statements include if statements, loops, function definitions, variable assignments, and print statements.
# 
# Unlike expressions, statements may not have a value associated with them, or the value may not be intended to be used further in the program. For example, an assignment statement like spam = 10 is a simple statement that assigns the value 10 to the variable spam, but it does not produce a value that can be used in an expression.
# 
# The main difference between an expression and a statement is that an expression evaluates to a value, whereas a statement performs an action or controls the flow of a program. Expressions can be used within statements, and statements can contain expressions, but they serve different purposes in programming.

# In[6]:



bacon = 22
bacon+1


# In[4]:


bacon


# Ans 6.
# 
# The variable bacon contains 22

# In[8]:


'spam' + 'spamspam'


# In[9]:


'spam'*3


# Ans 7.
# 
# In both cases, the result is the same string 'spamspamspam', but the operations used to obtain this value differ.

# Ans 8.
# 
# In Python, variable names need to adhere to certain rules and conventions. And one of the rule is,
# 
# Variable names should begin with a letter (a-z or A-Z) or an underscore (_). They cannot start with a number. 'eggs' starts with a letter, making it a valid variable name, and 100 is itself is digit making it inavalid.

# Ans 9.
# 
# int(): This function can be used to convert a value into an integer. It takes a value as its argument and returns the corresponding integer representation. If the value cannot be converted to an integer, it will raise a ValueError. For example:
# 

# In[10]:


num = int("10")  # Converts the string "10" to an integer 10


# float(): This function converts a value into a floating-point number. It takes a value as its argument and returns the corresponding floating-point representation. If the value cannot be converted to a float, it will raise a ValueError. For example:

# In[11]:


num = float("3.14")  # Converts the string "3.14" to a float 3.14


# str(): This function converts a value into a string. It takes a value as its argument and returns the corresponding string representation. It can convert various data types, including integers, floats, and other objects, into a string. For example:

# In[12]:


text = str(42)  # Converts the integer 42 to a string "42"


# Ans 10.
# 
# The expression 'I have eaten ' + 99 + ' burritos.' causes an error because it involves trying to concatenate a string ('I have eaten ') with an integer (99). In Python, the + operator is overloaded for both string concatenation and addition, but it does not automatically convert values of different types.
# 
# To fix this error, you need to ensure that all values involved in the concatenation are of the same type, in this case, strings. You can achieve this by converting the integer 99 into a string using the str() function. Here's the fixed expression:

# In[13]:


'I have eaten ' + str(99) + ' burritos.'


# By wrapping the 99 with str(), it converts the integer into a string before the concatenation takes place. This ensures that all the values are strings and can be concatenated without any errors.

# In[ ]:




