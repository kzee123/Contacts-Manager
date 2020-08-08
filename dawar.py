import os
import subprocess as sp
import msvcrt
sp.call('cls',shell=True)



contacts = []





dict = eval(open("user.txt").read())

x = 0
flag = 0
while True:
	if flag == 0:
		user = raw_input("Enter Username: ")
		password = raw_input("Enter Password: ")
		while x < len(dict):
			if dict[x] == user and dict[x+1] == password:
				sp.call('cls',shell=True)
				print ("login successfully")
				flag = 1
				break
			x = x+2
		
		if x ==len(dict):
				print("Wrong username or password")
				print("Continue?: (y/n)")
				con = msvcrt.getch()
				if con == "y":
					sp.call('cls',shell=True)
					x = 0
					continue
				else:
					sp.call('cls',shell=True)
					break
				


	print("Welcome to Phone Book, what would you like to do?")
	print(" 1 - Add \n 2 - Delete \n 3 - Search \n 4 - Add user \n 5 - Logout \n 6 - Print Phone Book \n 7 - Quit")
		
	char = msvcrt.getch()
			
	if char == "1":
		sp.call('cls',shell=True)
		cont = raw_input("Enter name: ")
		if cont in contacts:
			print("contact exists already")
			print("Press any key to continue..")
			msvcrt.getch()
			sp.call('cls',shell=True)
			continue
		else:
			contacts.append(cont)
			numb = raw_input("Enter Number: ")
			contacts.append(numb)
			with open('contacts.txt', 'w') as f:
				for item in contacts:
					f.write("%s\n" % item)
			print("Contact added.\nPress any key to continue..")
			msvcrt.getch ()
			sp.call('cls',shell=True)
			continue
			sp.call('cls',shell=True)
			continue
	elif char == "2":
		sp.call('cls',shell=True)
		cont = raw_input("Enter contact name to delete: ")
		x = 0
		for i in contacts:
			if i == cont:
				del contacts[x+1]
				contacts.remove(i)
				break
			x = x+1
		with open('contacts.txt', 'w') as f:
				for item in contacts:
					f.write("%s\n" % item)
		print("Contact deleted.\nPress any key to continue...")
		msvcrt.getch()
		sp.call('cls',shell=True)
		continue
	elif char == "3":
		sp.call('cls',shell=True)
		cont = raw_input("Enter contact name to search: ")
		x = 0
				
		for i in contacts:
			if i == cont:
				print("Number: \b")
				print contacts[x+1]
				print("Press any key to continue...")
				msvcrt.getch()
				sp.call('cls',shell=True)
				break
			x = x+1
		if x == len(contacts):
			print("Contact not found.\nPress any key to continue...")
			msvcrt.getch()
			sp.call('cls',shell=True)
			continue
	elif char == "4":
		sp.call('cls',shell=True)
		cont = raw_input("Enter new username: ")
		pass2 = raw_input("Enter password: ")
		
		dict.append(cont)
		dict.append(pass2)
		print("New user added. \nPress any key to continue...")
		msvcrt.getch()
		sp.call('cls',shell=True)
		continue
			
	elif char == "5":
		sp.call('cls',shell=True)
		flag = 0
		continue
		
					
	elif char == "6":
		x = 0
		sp.call('cls',shell=True)
		print "Name       Number"
		while x < len(contacts):
			print contacts[x],"    ",contacts[x+1]
			x = x+2
		print("\nPress any key to continue...")
		msvcrt.getch()
		sp.call('cls',shell=True)
		continue
			
	
	
	
	elif char == "7":
		print("Do come back again")
		print("Press any key to exit...")
		msvcrt.getch()
		sp.call('cls',shell=True)
		open('contacts.txt', 'w').close()
		break
		
	else:
		print("\nWrong choice, please select from the given choices")
		msvcrt.getch()
		sp.call('cls',shell=True)
		continue

		
		


	

	