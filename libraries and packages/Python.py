Python:
-interpreted
-interactive
-Object oriented
-easy to learn
-easy to maintain
-broad mandatory
-portable
-extendable
-databases
-scalabale
-garbage collection
____________________________________________________
print (a)
print ("pankaj")
print ('%d equals %d * %d' % (num,i,j))
print (num, 'is a prime number')
print ('Current fruit :', fruits[index])
print ("Python is really a great language,", "isn't it?")
print "Hello {0} {1}! You just delved into python.".format(raw_input(), raw_input())
____________________________________________________
import class def print
and or not is in
if else elif for while break continue return
try except finally
from with
exec pass global raise del lambda yield
____________________________________________________
#comments
____________________________________________________
counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string
a = b = c = 1
a,b,c = 1,2,"john"
____________________________________________________
str = 'Hello World!'
print str          # Prints complete string
print str[0]       # Prints first character of the string
print str[2:5]     # Prints characters starting from 3rd to 5th
print str[2:]      # Prints string starting from 3rd character
print str * 2      # Prints string two times
print str + "TEST" # Prints concatenated string

Hello World!
H
llo
llo World!
Hello World!Hello World!
Hello World!TEST
____________________________________________________
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print list          # Prints complete list
print list[0]       # Prints first element of the list
print list[1:3]     # Prints elements starting from 2nd till 3rd 
print list[2:]      # Prints elements starting from 3rd element
print tinylist * 2  # Prints list two times
print list + tinylist # Prints concatenated lists

['abcd', 786, 2.23, 'john', 70.2]
abcd
[786, 2.23]
[2.23, 'john', 70.2]
[123, 'john', 123, 'john']
['abcd', 786, 2.23, 'john', 70.2, 123, 'john']
____________________________________________________
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print tuple           # Prints complete list
print tuple[0]        # Prints first element of the list
print tuple[1:3]      # Prints elements starting from 2nd till 3rd 
print tuple[2:]       # Prints elements starting from 3rd element
print tinytuple * 2   # Prints list two times
print tuple + tinytuple # Prints concatenated lists

('abcd', 786, 2.23, 'john', 70.2)
abcd
(786, 2.23)
(2.23, 'john', 70.2)
(123, 'john', 123, 'john')
('abcd', 786, 2.23, 'john', 70.2, 123, 'john')

Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. 
tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list
____________________________________________________
Python's dictionaries are kind of hash table type.'
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print dict['one']       # Prints value for 'one' key
print dict[2]           # Prints value for 2 key
print tinydict          # Prints complete dictionary
print tinydict.keys()   # Prints all the keys
print tinydict.values() # Prints all the values

This is one
This is two
{'dept': 'sales', 'code': 6734, 'name': 'john'}
['dept', 'code', 'name']
['sales', 6734, 'john']
____________________________________________________
int(x [,base]) 			Converts x to an integer. base specifies the base if x is a string.
long(x [,base] )        Converts x to a long integer. base specifies the base if x is a string.
float(x)				Converts x to a floating-point number.
complex(real [,imag])	Creates a complex number.
str(x)					Converts object x to a string representation.
repr(x) 				Converts object x to an expression string.
eval(str) 				Evaluates a string and returns an object.
tuple(s)				Converts s to a tuple.
list(s)					Converts s to a list.
set(s)					Converts s to a set.
dict(d) 				Creates a dictionary. d must be a sequence of (key,value) tuples.
frozenset(s) 			Converts s to a frozen set
chr(x) 					Converts an integer to a character.
unichr(x)				Converts an integer to a Unicode character.
ord(x)					Converts a single character to its integer value.	
hex(x) 					Converts an integer to a hexadecimal string.
oct(x)					Converts an integer to an octal string.
____________________________________________________
+	- 	*	/	%
a**b   # a^b
a//b   #Floor Division

==	!=	<> 	>	<	>=	<=
=	+=	-=	*=	/=	%=	**=	//=
&	|	^	~	<<	>>
and or not
in, not in  #in Evaluates to true if it finds a variable in the specified sequence and false otherwise.
is, is not  #is Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
# Ternary Operator:
[on_true] if [expression] else [on_false] 
min = a if a < b else b 
____________________________________________________
Precedence:
**
~	+	- #unary
*	/	%	//
+	-
<<	>>
&
^	|
<=	<	>	>=
<>	==	!=
=	+=	-=	*=	/*	%=	//=	**=
is, is not
in, not in
and or not
____________________________________________________
#Conditional
var = 100
if var < 200:
   print "Expression value is less than 200"
   if var == 150:
      print "Which is 150"
   elif var == 100:
      print "Which is 100"
else:
   print "Could not find true expression"

____________________________________________________
#Loops
while (count < 9):
   print ('The count is:', count)
   count = count + 1

#else with while
count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")

#for
for letter in 'Python':     # First Example
   print ('Current Letter :', letter)

#for with index
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print 'Current fruit :', fruits[index]

#else with loops
for num in range(10,20):     #to iterate between 10 to 20
   for i in range(2,num):    #to iterate on the factors of the number
      if num%i == 0:         #to determine the first factor
         j=num/i             #to calculate the second factor
         print '%d equals %d * %d' % (num,i,j)
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print num, 'is a prime number'
____________________________________________________
#break continue pass
The pass statement is a null operation; nothing happens when it executes. 
The pass is also useful in places where your code will eventually go, but has not been written yet
____________________________________________________
#Numbers
You can delete a single object or multiple objects by using the del statement. For example −
	del var
	del var_a, var_b
Types:
	int
	long
	float
	complex
Conversion:
	int(x)
	long(x)
	float(x)
	complex(x)   	#x + i0
	complex(x,y)	#x + iy
Functions:
	pow(x,y,m)  # x^y % m
	import math
	math.abs(x)
		ceil(x)
		floor(x)
		cmp(x,y)	#-1 if x < y, 0 if x == y, or 1 if x > y
		exp(x)		#	e^x
		pow(x,y)
		sqrt(x)
		fabs(x) 	# |x| for floor types
		log(x)		# natural log of x
		log10(x)
		max(x1, x2,...)
		min(x1, x2,...)
		round(x [,n]) 	#x rounded to n digits from the decimal point.
						#Python rounds away from zero as a tie-breaker: round(0.5) is 1.0 and round(-0.5) is -1.0.
		acos(x)			#Return the arc cosine of x, in radians.
		asin(x)
		atan(x)
		sin(x)
		cos(x)
		tan(x)
		atan2(y, x)		#Return atan(y / x), in radians.
		degrees(x)		#Converts angle x from radians to degrees.
		radians(x)		#Converts angle x from degrees to radians.
		pi 
		e
	import random
		random.choice(seq)		#returns a random item from a list, tuple, or string.
			   randrange ([start,] stop [,step])
		       random()			#[0,1)
		       seed([x])
		       shuffle(lst)		#Randomizes the items of a list in place. Returns None.
		       uniform(x, y)	#A random float r, such that x is less than or equal to r and r is less than y
____________________________________________________
#Strings
var1 = 'Hello World!'
var2 = "Python Programming"
print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]

var1[0]:  H
var2[1:5]:  ytho

a + b 			#concatenate
a*2 			#Repetition : multiple copies of the same string
[]				#Slice - Gives the character from the given index
[ : ]			#Range Slice - Gives the characters from the given range	
in
not in
r/R 			# raw string
u 				# unicode
% 				#Format - Performs String formatting

#String Formatting Operator
print "My name is %s and weight is %d kg!" % ('Zara', 21)
%c	character
%s	string conversion via str() prior to formatting
%i	signed decimal integer
%d	signed decimal integer
%u	unsigned decimal integer
%o	octal integer
%x	hexadecimal integer (lowercase letters)
%X	hexadecimal integer (UPPERcase letters)
%e	exponential notation (with lowercase 'e')
%E	exponential notation (with UPPERcase 'E')
%f	floating point real number
%g	the shorter of %f and %e
%G	the shorter of %f and %E
*	argument specifies width or precision
-	left justification
+	display the sign
<sp>	leave a blank space before a positive number
#	add the octal leading zero ( '0' ) or hexadecimal leading '0x' or '0X', depending on whether 'x' or 'X' were used.
0	pad from left with zeros (instead of spaces)
%	'%%' leaves you with a single literal '%'
(var)	mapping variable (dictionary arguments)
m.n.	m is the minimum total width and n is the number of digits to display after the decimal point (if appl.)

#Triple Quotes
print """abc
		def"""
output:
	abc
	def

#raw Strings
Raw strings do not treat the backslash as a special character at all. Every character you put into a raw string stays the way you wrote it −
print r'C:\\nowhere'
output:
	C:\\nowhere

#Unicode String
Normal strings in Python are stored internally as 8-bit ASCII, while Unicode strings are stored as 16-bit Unicode.
print u'Hello, world!'

#Methods
	len(string)
	str.endswith(suffix, beg=0, end=len(string))
	str.startswith(str, beg=0,end=len(string))
	find(str, beg=0 end=len(string)) 			#eturns index if found and -1 otherwise.
	index(str, beg=0, end=len(string))			#Same as find(), but raises an exception if str not found.
	rfind(str, beg=0,end=len(string))	#Same as find(), but search backwards in string.
	rindex( str, beg=0, end=len(string))#Same as index(), but search backwards in string.
	join(seq)			#Merges (concatenates) the string representations of elements in sequence seq into a string, with separator string.
	lstrip() 			#Removes all leading whitespace in string.
	rstrip()
	split(str="", num=string.count(str))
			#Splits string according to delimiter str (space if not provided) and returns list of substrings; split into at most num substrings if given.
	str.capitalize()		#Capitalizes first letter of string
	max(str)			#Returns the max alphabetical character from the string str.
	min(str)
	replace(old, new [, max])		#Replaces all occurrences of old in string with new or at most max occurrences if max given.
	isdecimal()
	isnumeric()
	isupper()
	islower()
	isspace()
	isdigit()
	istitle()			#Returns true if string is properly "titlecased" and false otherwise.
	isalpha()			#Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.
	isalnum()			#Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.
	str.upper()
	str.lower()
	str.title()
	count(str, beg= 0,end=len(string))	#Counts how many times str occurs in string or in a substring of string if starting index beg and ending index end are given.
	decode(encoding='UTF-8',errors='strict')
	encode(encoding='UTF-8',errors='strict')

st = st + str(i) 					#concatenate
ss = '-'.join(X) 					# X = iterable   #this-is-a-string
print "Hello {0} {1}! You just delved into python.".format(raw_input(), raw_input())
s[a:b]     							#gives s substring from index a to b-1
s[::-1] 							#reverse a string
len([i for i in range(len(s)) if s[i:i+len(b)] == b])   #count all (overlapping) occurence of b in s

#check if string s contains an alphanumeric, alphabetical, digits, lower, upper
print (any(c.isalnum()  for c in s))
print (any(c.isalpha() for c in s))
print (any(c.isdigit() for c in s))
print (any(c.islower() for c in s))
print (any(c.isupper() for c in s))

#wrap the string into a paragraph of width
import textwrap
def wrap(s, width):
    l = textwrap.wrap(s,width)
    res = ""
    for x in l:
        res+=(x+'\n')
    return res

# width of n in binary format
width = len("{0:b}".format(n))
____________________________________________________
#Lists
**items in a list need not be of the same type.

#creating list
list1 = ['physics', 'chemistry', 1997, 2000];

#prrinting list
print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]

#update
list[2] = 2001;
print list[2]

append(value) 	#add at last

#delete
del list1[2];    #by index
remove(value)	 #by value

Python Expression				Results									Description
len([1, 2, 3])						3										Length
[1, 2, 3] + [4, 5, 6]			[1, 2, 3, 4, 5, 6]							Concatenation
['Hi!'] * 4						['Hi!', 'Hi!', 'Hi!', 'Hi!']				Repetition
3 in [1, 2, 3]					True										Membership
for x in [1, 2, 3]: print x,	1 2 3										Iteration

#for L = ['spam', 'Spam', 'SPAM!']
L[2]							SPAM!										Offsets start at zero
L[-2]							Spam										Negative: count from the right(starets With -1)
L[1:]							['Spam', 'SPAM!']							Slicing fetches sections

#operations:
cmp(list1,list2) 				#Compares elements of both lists.
len(list)
max(list)
min(list)
list(seq) 						#Converts a tuple into list.

list.append(obj)
list.count(obj)
list.extend(seq)				#Appends the contents of seq to list
list.index(obj)					#Returns the lowest index in list that obj appears
list.insert(index, obj)			#Inserts object obj into list at offset index
list.pop(obj=list[-1])			#Removes and returns last object or obj from list
list.remove(obj)          		#sRemoves object obj from list
list.reverse()					#Reverses objects of list in place
list.sort([func])				#Sorts objects of list, use compare func if given
____________________________________________________
#tuple
A tuple is a sequence of immutable Python objects.
the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

tup1 = ('physics', 'chemistry', 1997, 2000);
tup1 = ();
tup1 = (50,); #To write a tuple containing a single value you have to include a comma, even though there is only one value
#access
tup1[0];
tup2[1:5];
#update
Tuples are immutable which means you cannot update or change the values of tuple elements. You are able to take portions of existing tuples to create new tuples
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');
tup3 = tup1 + tup2;
#delete
Not possible

#operations
Python Expression				Results									Description
len((1, 2, 3)						3										Length
(1, 2, 3) + (4, 5, 6)			(1, 2, 3, 4, 5, 6)							Concatenation
('Hi!') * 4						('Hi!', 'Hi!', 'Hi!', 'Hi!')				Repetition
3 in (1, 2, 3)					True										Membership
for x in (1, 2, 3): print x,	1 2 3										Iteration

#for L = ['spam', 'Spam', 'SPAM!']
L[2]							SPAM!										Offsets start at zero
L[-2]							Spam										Negative: count 'from' the right
L[1:]							['Spam', 'SPAM!']							Slicing fetches sections

#Function
cmp(tuple1,tuple2)
len(tuple)
max(tuple)
min(tuple)
tuple(seq)
____________________________________________________
#Dictionary

#Keys are unique within a dictionary 'while' values may not be. 
#The values of a dictionary can be of any type, but the keys must be of an immutable data type such 'as' strings, numbers, or tuples.
#An empty dictionary without any items is written 'with' just two curly braces, like this: {}
#If we attempt to access a data item with a key, which is not part of the dictionary, we get an error

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']

#update
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8;
#delete
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict['Name']; # remove entry with key 'Name'
del dict ;        #delete entire dictionary
dict.clear();     # remove all entries in dict

#functions
cmp(dic1,dic2)
len(dict)
str(dict)		#Produces a printable string representation of a dictionary
type(variable)	#Returns the type of the passed variable.

dict.clear()
dict.copy() 	#Returns a shallow copy of dictionary dict
dict.fromkeys()	#Create a new dictionary with keys from seq and values set to value.
dict.get(key, default=None)	#For key key, returns value or default if key not in dictionary
dict.has_key(key)			#Returns true if key in dictionary dict, false otherwise
dict.items()				#Returns a list of dict's (key, value) tuple pairs
dict.keys()					#Returns list of dictionary dict's keys
dict.values()				#Returns list of dictionary dict's values
dict.setdefault(key, default=None)	#Similar to get(), but will set dict[key]=default if key is not already in dict
dict.update(dict2)			#Adds dictionary dict2's key-values pairs to dict
____________________________________________________
#Functions
def functionname( parameters ):
   "function_docstring"
   function_suite
   return [expression]

#calling
	functionname(parameters)

#pass by reference vs value
All parameters (arguments) in the Python language are passed by reference. 
It means if you change what a parameter refers to within a function, the change also reflects back in the calling function.

#Function Arguments
	Required arguments
		def fname(arg1,arg2,arg3):
			"docstring"
			function_suite
			return [expression]

		fname(arg1,arg2,arg3)
	Keyword arguments
		# Function definition is here
		def printinfo( name, age ):
		   "This prints a passed info into this function"
		   print "Name: ", name
		   print "Age ", age
		   return;

		# Now you can call printinfo function
		printinfo( age=50, name="miki" )
	Default arguments
		A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument.
		# Function definition is here
		def printinfo( name, age = 35 ):
		   "This prints a passed info into this function"
		   print "Name: ", name
		   print "Age ", age
		   return;

		# Now you can call printinfo function
		printinfo( age=50, name="miki" )
		printinfo( name="miki" )
	Variable-length arguments
		# Function definition is here
		def printinfo( arg1, *vartuple ):
		   "This prints a variable passed arguments"
		   print "Output is: "
		   print arg1
		   for var in vartuple:
		      print var
		   return;

		# Now you can call printinfo function
		printinfo( 10 )
		printinfo( 70, 60, 50 )


#lambda functions
	#can take any number of arguments but return just one value in the form of an expression. 

sum = lambda arg1, arg2: arg1 + arg2;
____________________________________________________
import module1[, module2[,... moduleN]
from modname import name1[, name2[, ... nameN]]
from modname import *

the Python interpreter searches for the module in the following sequences −
	The current directory.
	If the module isn't found, Python then searches each directory in the shell variable PYTHONPATH.
	If all else fails, Python checks the default path. On UNIX, this default path is normally /usr/local/lib/python/.
____________________________________________________
I/O
raw_input([prompt])
input([prompt])

Before you can read or write a file, you have to open it using Python's built-in open() function.
file object = open(file_name [, access_mode][, buffering])

#access mode
r readonly
rb readonly in binary format
r+ r/w
rb+
w     : Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
wb
w+
wb+
a  		appending at end
ab
a+      append+reading
ab+

#buffering
if buffering value = 0, no buffering
elif buffering value = 1, line buffering is performed while accessing a file.
elif buffering value > 1, then buffering action is performed with the indicated buffer size. 
elif buffering value < 1 the buffer size is the system default(default behavior).

#file object attributes
print (fo.name)
fo.closed
fo.mode
fo.softspace : Returns false if space explicitly required with print, true otherwise

#methods
fileobject.close()
fo.write(string) # write() method does not add a newline character ('\n') to the end of the string
fo.read([count]) # passed parameter is the number of bytes to be read from the opened file

*tell() : tells you the current position within the file; in other words, the next read or write will occur at that many bytes from the beginning of the file.
*seek(offset[, from]) method changes the current file position. 
	The offset argument indicates the number of bytes to be moved. 
	The from argument specifies the reference position from where the bytes are to be moved.
	if from = 0, it means use the beginning of the file as the reference position and 1 means use the current position as the reference position and if it is set to 2 then the end of the file would be taken as the reference position.

#Renaming and Deleting Files
Python os module provides methods that help you perform file-processing operations, such as renaming and deleting files,mkdir,chdir etc.

os.rename(current_file_name, new_file_name)
os.remove(file_name)
os.mkdir("newdir")
os.chdir("newdir") #argument, which is the name of the directory that you want to make the current directory.
os.chdir("/home/newdir")
os.getcwd() # current working directory.
os.rmdir('dirname')	#deletes the directory
os.rmdir( "/tmp/test"  )
https://www.tutorialspoint.com/python/os_file_methods.htm
https://www.tutorialspoint.com/python/file_methods.htm
____________________________________________________
#Exception
Exception # Base class for all exceptions
StandardError # Base class for all built-in exceptions except StopIteration and SystemExit.
ArithmeticError # Base class for all errors that occur for numeric calculation.
LookupError # Base class for all lookup errors.
EnvironmentError # Base class for all exceptions that occur outside the Python environment.

StopIteration # Raised when the next() method of an iterator does not point to any object.
SystemExit # Raised by the sys.exit() function.
OverflowError # Raised when a calculation exceeds maximum limit for a numeric type.
FloatingPointError # Raised when a floating point calculation fails.
ZeroDivisionError # Raised when division or modulo by zero takes place for all numeric types.
AssertionError # Raised in case of failure of the Assert statement.
AttributeError # Raised in case of failure of attribute reference or assignment.
EOFError # Raised when there is no input from either the raw_input() or input() function and the end of file is reached.
ImportError # Raised when an import statement fails.	
KeyboardInterrupt # Raised when the user interrupts program execution, usually by pressing Ctrl+c.
IndexError # Raised when an index is not found in a sequence.
KeyError # Raised when the specified key is not found in the dictionary.
NameError # Raised when an identifier is not found in the local or global namespace.
UnboundLocalError # Raised when trying to access a local variable in a function or method but no value has been assigned to it.
IOError # Raised when an input/ output operation fails, such as the print statement or the open() function when trying to open a file that does not exist.
IOError # Raised for operating system-related errors.
SyntaxError # Raised when there is an error in Python syntax.
IndentationError # Raised when indentation is not specified properly.
SystemError # Raised when the interpreter finds an internal problem, but when this error is encountered the Python interpreter does not exit.
SystemExit # Raised when Python interpreter is quit by using the sys.exit() function. If not handled in the code, causes the interpreter to exit.
TypeError # Raised when an operation or function is attempted that is invalid for the specified data type.
ValueError # Raised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified.
RuntimeError # Raised when a generated error does not fall into any category.
NotImplementedError # Raised when an abstract method that needs to be implemented in an inherited class is not actually implemented.

#Assertions (a raise-if-not statement)
assert Expression[, Arguments]

try:
	..
except ExceptionI:
	..
except ExceptionII:
   ..
else:
   If there is no exception then execute this block. 

#The except Clause with No Exceptions
#try-except statement catches all the exceptions that occur. Using this kind of try-except statement is not considered a good programming practice though
try:
   You do your operations here;
   ..
except:
   ..
else:
   ..

# The except Clause with Multiple Exceptions
try:
   You do your operations here;
   ......................
except(Exception1[, Exception2[,...ExceptionN]]]):
   If there is any exception from the given exception list, then execute this block.
   ......................
else:
   If there is no exception then execute this block. 

#The try-finally Clause
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
finally:
   print ("Error: can\'t find file or read data")

#Argument of an Exception
#An exception can have an argument, which is a value that gives additional information about the problem.
#The argument is optional; if not supplied, the exception argument is None.
try:
   raise Networkerror("Bad hostname")
except Networkerror,e:
   print e.args
   
#Raising an Exceptions
raise [Exception [, args [, traceback]]]

def functionName( level ):
   if level < 1:
      raise "Invalid level!", level
      # The code below to this would not be executed
      # if we raise the exception
try:
   Business Logic here...
except "Invalid level!":
   Exception handling here...
else:
   Rest of the code here...

#User-Defined Exceptions
class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg

try:
   raise Networkerror("Bad hostname")
except Networkerror,e:
   print e.args
____________________________________________________
#OOPS

#creating class
#The class has a documentation string, which can be accessed via ClassName.__doc__

class Employee:
   'Optional class documentation string'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)
	  
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")

# __init__() is a special method, which is called class constructor or initialization method that Python calls when you create a new instance of this class.
# You declare other class methods like normal functions with the exception that the first argument to each method is self. 
# Python adds the self argument to the list for you; you do not need to include it when you call the methods.

#creating instance
you call the class using class name and pass in whatever arguments its __init__ method accepts.
emp1 = Employee("Zara", 2000)
emp1.displayEmployee()

#Instead of using the normal statements to access attributes, you can use the following functions −
hasattr(emp1, 'salary')    # Returns true if 'salary' attribute exists
getattr(emp1, 'salary')    # Returns value of 'salary' attribute
setattr(emp1, 'salary', 7000) # Set attribute 'salary' at 7000
delattr(emp1, 'salary')    # Delete attribute 'salary'

#Built-In Class Attributes
__dict__  # Dictionary containing the class's namespace.
__doc__   # Class documentation string or none, if undefined.
__name__  # Class name.
__module__# Module name in which the class is defined. This attribute is "__main__" in interactive mode.
__bases__ # A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.

#Destroying Objects (Garbage Collection)
automatically called when reference count reaches 0
However, a class can implement the special method __del__(), called a destructor, that is invoked when the instance is about to be destroyed. This method might be used to clean up any non-memory resources used by an instance.

#inheritance
class SubClassName (ParentClass1[, ParentClass2, ...]):
   'Optional class documentation string'
   class_suite

issubclass(sub, sup) : returns True, if the given subclass sub is indeed a subclass of the superclass sup.
isinstance(obj, Class): returns True, if obj is an instance of class Class or is an instance of a subclass of Class

#Overriding
class Parent:        # define parent class
   def myMethod(self):
      print ('Calling parent method')

class Child(Parent): # define child class
   def myMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.myMethod()         # child calls overridden method

#Base Overloading Methods
__init__ ( self [,args...] )
	Constructor (with any optional arguments)
	Sample Call : obj = className(args)
__del__( self )
	Destructor, deletes an object
	Sample Call : del obj	
__repr__( self )
	Evaluatable string representation
	Sample Call : repr(obj)	
__str__( self )
	Printable string representation
	Sample Call : str(obj)	
__cmp__ ( self, x )
	Object comparison
	Sample Call : cmp(obj, x)

#Data Hiding
You need to name attributes with a double underscore prefix, and those attributes then will not be directly visible to outsiders.
class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print (self.__secretCount)
____________________________________________________
enumerate(iterable, start=0)
if A=[43,45,47]
for k, z in enumerate(A):
	print k,z
0	43
1	45
2	47
____________________________________________________
create 2-D array
dp=[[0]*col for i in range(row)]

parent= list(range(r*c))
#parent= [i for i in range(r*c)]
____________________________________________________
String:
length = len(str)
rev = str[::-1]
ch=str[i]
____________________________________________________
Data Structure:
Lists:
	l=[1,2,3]
	l=[i for i in range(3)]
	l=list(range(2,10,2))
	c=l[i]
	l.append(23)  #appends at last
	l.extend([12,23,45])
	l.index(23)
	l.index(23,2) #looks for 23 after index 2
	l.insert(2,'a') # insert 'a' at index 2
	l.remove('a')   # Delete the first occurrence 
	l.pop()			# from last
	l.count()
	l.sort()
	l.sort(reverse=True)
	sorted(list)
	l.reverse()
	max(list)
	#list as stack -> l.append('a') and l.pop()
	#list as queue -> l.append('a') and l.pop(0) or l.remove(0)
	list2=list(list1) 	# copy list
	list2 = list1[:]
	#Inserting items into a sorted list¶
		>>> x = [4, 1]
		>>> x.sort()
		>>> import bisect
		>>> bisect.insort(x, 2)
		>>> x
		[1, 2, 4]
Set:
		>>> a.add(val)
		>>> a = set([1, 2, 3, 4])
		>>> b = set([3, 4, 5, 6])
		>>> a | b # Union
		{1, 2, 3, 4, 5, 6}
		>>> a & b # Intersection 			c = a.intersection(b)
		{3, 4}
		>>> a < b # Subset					c.issubset(a)			c.issuperset(a)
		False
		>>> a - b # Difference				a.difference(b)
		{1, 2}
		>>> a ^ b # Symmetric Difference    a.symmetric_difference(b)
		{1, 2, 5, 6}

collections module:
	Deque
		>>> from collections import deque
		>>> q = deque(range(5))
		>>> q.append(5)
		>>> q.appendleft(6)
		>>> q 
		deque([6, 0, 1, 2, 3, 4, 5])
		>>> q.pop()
		5
		>>> q.popleft()
		6
		>>> q.rotate(3)
		>>> q 
		deque([2, 3, 4, 0, 1])
		
____________________________________________________
#factorial
import math
test=input()
while test>0:
    test-=1
    n=input()
    print math.factorial(n)
____________________________________________________
class Solution:
    def findLongestChain(self, pairs):
        dp=[0]
        pairs.sort(key = self.sortFirst, reverse = False)
        print(pairs)
        #pairs.sort(key = lambda x: x[1], reverse = False)
        for x in range(1,len(pairs)):
            if(pairs[x][0]>pairs[x-1][1]):
                dp.append(dp[x-1]+1)
            else:
                dp.append(dp[x-1])
            
        return dp[len(pairs)-1]
    def sortFirst(self,pair):
        return pair[1]
____________________________________________________
	class Solution(object):
    def canVisitAllRooms(self, rooms):
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        #At the beginning, we have a todo list "stack" of keys to use
        #'seen' represents at some point we have entered this room
        while stack:  				  # While we have keys
            node = stack.pop() 		  # get the next key 'node'
            for nei in rooms[node]:   # For every key in room # 'node'
                if not seen[nei]: 	  # ... that hasn't been used yet
                    seen[nei] = True  # mark that we've entered the room
                    stack.append(nei) # add the key to the todo list
        return all(seen) 			  # Return true iff we've visited every room
____________________________________________________
#eval function:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1

if __name__ == '__main__':
    n = int(input())

l = []
for _ in range(n):
    s = list(map(str,input().split()))
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print(l)
____________________________________________________
#take input:
N = map(int,input().split())

X = list(map(int, input().strip().split(' ')))

x,y,z,n = [input() for i in range(4)]
x,y = [x for x in map(int,input().split(' '))]

x,y,z,n = [input() for i in range(4)]
print([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n])

l = ([i*i for i in range(n)])

set([marks for name, marks in marksheet]) 		# set of marks from a list([name,marks])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
____________________________________________________
Formatting:
print ('%d equals %d * %d' % (num,i,j))
print("%0.2f" %(sum(score)/3))
print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))
____________________________________________________
zipping
	The purpose of zip() is to map the similar index of multiple containers so that they can be used just using as single entity.
	name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ] 
	roll_no = [ 4, 1, 3, 2 ] 
	marks = [ 40, 50, 60, 70 ] 
	  
	# using zip() to map values 
	mapped = zip(name, roll_no, marks)
UnZipping:
	namz, roll_noz, marksz = zip(*mapped)
	
for pl, sc in zip(players, scores): 
    print ("Player :  %s     Score : %d" %(pl, sc)) 
