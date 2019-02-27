print("This is python program for converting snake case string to camel case string :")
#input build in function to take input from user.
a=input("enter your snake case text here : ")
#I replace method to replace all '_' to " "(single space)
a=a.replace('_',' ')
# Title method to make the first letter capital of every word.  
y=a.title()
# again replace method used to remove unnecessary spaces
b=y.replace(' ','')
# here i used string formating usnig {}, with the help of string forn=mat we can concatenate string with integer without converting.
print("Output :{}".format(b))
