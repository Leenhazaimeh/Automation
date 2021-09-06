import re
from faker import Faker


fake = Faker('en_US')
'''''
potential-contacts, find and collect all email addresses and phone numbers.
phone numbers with missing area code should presume 206
'''

potential_contacts = ""

for f in range(206):
    email_text = fake.email()
    phone_number = fake.phone_number()
    potential_contacts += phone_number
    potential_contacts += " " + email_text + " "
  
  
   
  
    potential_contacts += "\n"
with open("potential-contacts.txt", "w+") as f:
    f.write(potential_contacts)
# print(potential_contacts)



phone_regex = list(re.findall(r"\w{3}-\w{3}-\w{4}", potential_contacts))

email_regex = list(re.findall(r'[\w\.-]+@[\w\.-]+', potential_contacts))


'''
The ‘phone_numbers.txt’ and ‘emails.txt’ files will be verified by an automated system
'''
def phone(phone_regex):
     return (('\n').join(phone_regex))
phone_space=phone(phone_regex)

def email(email_regex):
     return (('\n').join(email_regex))
email_space=email(email_regex)


with open("phone_numbers.txt" , "w") as f:
    f.write(phone_space)

with open("email.txt" , "w") as f:
    f.write(email_space)




print(phone_regex) 
print(email_regex)

