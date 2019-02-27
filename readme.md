In this repository, I will explain how to convert snake case string into camel case using a simple python script.

<strong>Requirements:</strong>

python 3.5+

<strong>what you will learn form this post:</strong>
<ul>
	<li>input function</li>
	<li>replace function</li>
	<li>print function</li>
	<li>string formationg</li>
</ul>
<h1><strong>This is source code:</strong></h1>
<pre>print("This is python program for converting snake case string to camel case string :")
#input build in function to take input from user.
a=input("enter your snake case text here : ")
#I replace method to replace all '_' to " "(single space)
a=a.replace('_',' ')
# Title method to make the first letter capital of every word.  
y=a.title()
# again replace method used to remove unnecessary spaces
b=y.replace(' ','')
# here i used string formating usnig {}, with the help of string forn=mat we can concatenate string with integer without converting.
print("Output :{}".format(b))</pre>
<h1>How to run this code:</h1>
<ul>
	<li>copy this code and pase in blank text file or download it from this repository</li>
	<li>rename it 01-task.py</li>
	<li>open terminal or command propmpt</li>
	<li>enter the following command</li>
	<li>python3 01-task.py</li>
</ul>
<h1></h1>
<h1><strong>Output:</strong></h1>
