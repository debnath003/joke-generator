print("JOKE GENERATOR")

import pyjokes

x=input("Type of input, \nString or Integer?: ")

if(x=="String" or x=="string" or x=="STRING"):
	a=input("Type start: ")
	if(a=="start" or a=="Start" or a=="START"):
		jokes=pyjokes.get_joke(language="en",category="all")
		print(jokes)
	else:
		print("Go to hell!!!")

elif(x=="Integer" or x=="integer" or x=="INTEGER"):
	b=int(input("Enter any number from 1 to 10: "))
	if(b<=0):
		print("Not Possible")
	elif(b>0 and b<10):
		c=input("Want 1 or more than 1 joke: ")
		if(c=="1"):
			j=pyjokes.get_joke(language="en",category="all")
			print(j)
		elif(c=="more than 1" or c=="More than 1"):
			d=int(input("How many?: "))
			list_jokes=pyjokes.get_jokes(language="en",category="neutral")
			for i in range(0, d):
				print(list_jokes[i], sep="\t   ")
		else:
			print("Don't Waste YOUR TIME")
	elif(b>10):
		print("Sleep WELL, Work HARD")
else:
	print("Do your own work")
			
		
