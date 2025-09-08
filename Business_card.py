#prompts will ask for user information
#output a simplified business card

"""
Business_card.py
The idea with this line of code is to take the data that has been inputed
and then to generate a neet business card 
Maintained by: Sir Max
"""

__version__ = 0.1

#input data
Name = ""
Surname = ""
email = ""
Title = ""

#prompts that will ask for user data 
Name = input('What is your name? ')
Surname = input('What is your surname? ')
email = input('What is your email address? ')
Title = input('What is your current occupation? - are you a (Coder / Scientist / Manager) ')

#this will be the output 
fancy_line_1 = "OoOoOoOoOoOoOoOoOoOoOOoOoOoOoOoOoOoOoOoOoO"
fancy_line_2 = "................ ( ͡° ͜ʖ ͡°).............."

print("\n", fancy_line_1)
print("\t", Surname)
print("\t", Name)
print("\t", email)
print("\t", 'I am a', Title)
print(fancy_line_2, "\n")
