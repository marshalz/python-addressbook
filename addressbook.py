def main():
	infile = open("contacts.txt", 'r') # Opens a file for reading
	outfile = open("contacts.txt", 'w') # opens a file for writing
	bigList = infile.readlines() # turns any existing addresses into the huge list
	existing = [] # initializes the existing list
	contents = [] # initializes the contents list
	if contents != []: # if there are contents in the text file
		for contact in contents:
			existing = contact.split(" ") # splits any contacts in the file
			bigList.append(existing) # adds the split contents to the big list

	x = 0
	while x >= 0:
		# prints the address book menu
		print("""
			Main Menu
			1. Add New Contact
			2. Print the Address Book
			3. Search for a contact
			4. Modify a contact
			5. Delete a contact
			6. Exit
			""")

		# takes user input for a command
		userChoice = input("Enter a number to perform a command!")

		# if option 1
		if userChoice == "1":
			smallList = [] 
			name = input("Name: ") # takes in name
			name = name.title() # makes sure its Capitalized
			smallList.append(name)

			address = input("Address: ") # takes in address
			address = address.title() # makes sure its capitalized
			smallList.append(address)
			
			number = input("Phone Number: ") # takes in the number
			smallList.append(number)

			email = input("Email Address: ") # takes in the email
			smallList.append(email)

			bigList.append(smallList) # adds new contact to address book
			print("Contact added!")

		# if option 2
		elif userChoice == "2":
			if bigList == []:
				print("There are no existing contacts in the address book. Add some!")
			else:
				for contact in bigList:
					print(contact) # prints each index of the address book list

		# if option 3
		elif userChoice == "3":
			name = input("Enter a name to search for.") # asks user for a name to search
			name = name.title() # makes sure its capitalized
			for indexNum in range(len(bigList)): # for loop checking each list in the big list
				if name in bigList[indexNum][0]: # prints name and info if name is found
					print(bigList[indexNum])
					break
			if name not in bigList[indexNum][0]:
				print("There is no contact with that name in the address book.")

		# if option 4
		elif userChoice == "4":
			name = input("Enter a contact name to modify.") # asks user for a name to search
			name = name.title() # makes sure its capitalized
			if name not in bigList[indexNum][0]:
				print("That name is not in the address book.")
			for indexNum in range(len(bigList)): # for loop checking each list in the big list
				if name in bigList[indexNum][0]: # prints name and info if name is found
					print("Contact found!")
					y = 0
					while y >= 0: # prints out the menu for modification
						print("""
							Modification Menu
							1. Name
							2. Address
							3. Phone Number
							4. Email Address
							5. Exit
							""")
						userChoice = input("Which would you like to modify?") # asks user to choose modification
						if userChoice == "1": # if user chose to modify name
							rewrite = input("Write the name you would like to replace it with.") # asks for replacement name
							rewrite = rewrite.title() # makes sure its capitalized
							bigList[indexNum].remove(bigList[indexNum][0])
							bigList[indexNum].insert(0, rewrite)
							print("Name replaced!")

						elif userChoice == "2": # if user chose to modify address
							rewrite = input("Write the address you would like to replace it with.") # asks for replacement address
							rewrite = rewrite.title() # makes sure its capitalized
							bigList[indexNum].remove(bigList[indexNum][1])
							bigList[indexNum].insert(1, rewrite)
							print("Address replaced!")

						elif userChoice == "3": # if user chose to modify phone number
							rewrite = input("Write the phone number you would like to replace it with.") # asks for replacement phone number
							bigList[indexNum].remove(bigList[indexNum][2])
							bigList[indexNum].insert(2, rewrite)
							print("Phone Number replaced!")

						elif userChoice == "4": # if user chose to modify email
							rewrite = input("Write the email you would like to replace it with.") # asks for replacement email
							bigList[indexNum].remove(bigList[indexNum][3])
							bigList[indexNum].insert(3, rewrite)
							print("Email replaced!")

						elif userChoice == "5": # if user chose to exit
							break
						else: 
							print("That is not an option on the menu. Please try again.")

		# if option 5
		elif userChoice == "5":
			name = input("Enter a contact name to delete.") # asks user for a contact name to delete
			name = name.title() # makes sure name is capitalized properly
			for indexNum in range(len(bigList)): # for loop checking each list in the big list
				if name not in bigList[indexNum][0] and indexNum == len(bigList): # breaks loop at the end
					break
				if name in bigList[indexNum][0]: # removes contact and breaks
					bigList.remove(bigList[indexNum])
					print("Contact removed!")
					break

		# if option 6
		elif userChoice == "6":
			for contact in bigList: # for each contact in the huge list
				contactString = str(contact) # converts the contacts in the list into strings
				outfile.write(contactString) # saves the file
			break
			

	infile.close()

main()