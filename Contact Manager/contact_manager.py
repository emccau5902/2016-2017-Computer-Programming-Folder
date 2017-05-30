# Computer Programming 1
# Mini-project: Contact Manager
#
# Name: Ethan McCauley
# Date: January
# TO DO: display records getting it to find said contact
# Directions:
#
# There are 10 coding tasks for you to complete. Each is worth 3 points.
# The testing portion will all be done in the shell when your program
# is working. Each testing step is worth 2 points. This will count as
# a 40-point major assessment.
#
# You can receive partial credit for non-working code. Comment out any
# code that crashes the program so it will still run when I grade. You
# are permitted to work with a partner on this project, however both
# should always make sure they have a working copy of the code at the
# end of class.

'''
pretty_json_string = json.dumps(languages, indent=4)
print(pretty_json_string)
'''
# 1. Include all necessary imports here.
import json



# Global variables. Do not change the names of the globals in template.

records = []   # list of all contacts
keys = ['name', 'address', 'city', 'state', 'zip', 'home', 'mobile', 'email']
data_file = 'contacts.json'



# 2. Read the json data file and import contents into the records
#    variable. Also, sort the records by the name field after loading.
#    Once the list is loaded, display a message stating the number of
#    contacts that were loaded.
def load():
    global records, keys
    with open('contacts.json') as data_file:
        contact_length = 0
        json_file = json.load(data_file)
        records = json.dumps(json_file, indent = 4)
        for keys in json_file:
            number_contacts = keys['name']
            contact_length = contact_length + len(number_contacts.splitlines())    
        print ('There were ' + str(contact_length) + ' contacts loaded.')


# 3. Write the records to a json file. Be sure to use 'pretty printing'
#    when you convert the data to a string. Once the list is saved, display
#    a message indicating that the save was successful.#
def save():
    global records
    with open('contacts.json', 'w') as c:
        c.write(records)
        print('Changes saved')



# 4. Print individual contact data formatted nicely. The following
#    fields (dict keys) must be supported: name, address, city, state,
#    zip, home (phone),  mobile (phone), email. Not all contacts will
#    contain all keys, so you you need to conditionally protect print
#    statements so that the program will not crash if a key is missing
#    for a particular contact. (The keys global variable can be used 
#    here so that each field for a record can be printed by looping
#    through keys rather than explicitly accessing each dictionary
#    element.
def display_record(contact):
    global keys
    for k in keys:
        if k in contact:
            print(contact[k])
    
    


    


# 5. Print all contact records. There should be no print statements in
#    this function. Loop through contacts and call your display_record
#    function for each contact. To make the ouput easier to read,
#    include a blank print statement after each record is displayed.
def all():
    pass
    #for r in records:
    
    



# 6. Search prints a list of all contacts that have values containing
#    the query. Again, use your display_record function to print rather
#    than including print statements in this function.
def find(query):
    print('Records matching "' + query + '"')



# 7. Add should prompt the user to enter new contact data for all keys.
#    Once the data is entered, a new dict should be created with those
#    key-value pairs and the dict should be added to records. Then the
#    records list needs to be resaved to the json file. If no value
#    is entered for a prompt, then that key:value pair should not be
#    added to the dictionary. Be sure that the add function calls
#    the save function you made earlier so that records are kept after
#    you quit the program.
def add():
    with open('contacts.json', 'w') as q:
        global records
        



# 8. Modify the all() function so that it displays the number
#    (index) of each contact in the list. This is necessary for the
#    next step.



# 9. The delete function should remove record at index n from the records
#    list. Then the records list needs to be rewritten to the json file.
#    Once the record has been deleted, a message such as '[name] has been
#    deleted.' should be displayed. If the user attempts to delete a record
#    that does not exist, then an error message should be displayed.
def delete(n):
    pass


# 10. Write a function called help() which displays instructions for how to
#     use each function. If a user types 'help()' at a shell prompt, then
#     your instructions should be displayed. This method should only contain
#     print statements. You will be graded on the clarity, quaility, and
#     neatness of your instructions.
def help():
    print('List of functions and their use:')
    print('1. "all()": Displays all contacts.')
    print('2. "display_record(contact)" : Search contacts by typing their name in the parathensis.')
    print('3. "find(query)": Typing this will let you search your contacts with the values of the query.')
    print('4. "add()": Allows you to create a new contact and their information.')
    print('6. "save()": Saves any changes you have made to the json file containing your contacts.')
    print('7. "delete(n)": With this command you can delete old unwanted contacts, simply type the command with the number corresponding to the contact in the parenthesis.')


# Start the program.
print('Contact Manager started.')
load()
print('Enter "help()" to see instructions.') 



"""
How to test...

In order to test your program, you'll need to create a json file called
contacts.json with data for at least 5 contacts. When the program runs,
you should see a message stating that the contacts have loaded.


a. Test your help function.

b. Enter the all() command in the shell to test that all contacts
   have been loaded and that your display_record function shows data
   nicely.

c. Test your search function. Be sure to try a few different queries.
   Make sure your search doesn't display duplicate contacts. Example
   commands could be find('ville'), find('864'), etc.

d. Test your add function to confirm that new contacts can be added. Be
   sure to call show_all and check the json file after adding a contact. 

e. Test your delete function. Call all() to see a list of numbered
   contacts. Then use a statement such as delete(3) to remove a contact.
   Call all() again and open the json file to confirm that the record 
   has been deleted.


When you have finished tesing, save your shell session from your final
test as demo.py in the same folder as your program and data file.

"""

