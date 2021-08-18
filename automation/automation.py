import shutil
import re 
from faker import Faker

fake = Faker('en_US')

potential_contacts = ""

existing_contacts = ""
###########################
 #find and collect all email addresses and phone numbers.
 ###########################





def get_e_mails(file):
            
            emails = []
        
if i[0] not in emails:
            emails.append(i[0])
return emails

def get_phone_number(f:
            
            nums = []
for i in range(100):

    email = fake.email()
    phone_number = fake.phone_number()
if num not in nums:
            nums.append(num)





def auto(num, e_mails):

    with open('phone_numbers.txt', 'w+')as p:
        for x in num:
            p.write(x + '\n')

    with open('e_mails.txt', 'w+') as e: 
        for n in e_mails: 
            e.write(n + '\n')

if __name__ == '__main__':
    emails = get_emails(text)
    phone_nums = get_phone_number(text)
    save(phone_nums, emails)

    print(phone_nums)
    print(emails)
with open('./assets/potential-contacts.txt', 'r') as file:
    text = file.read().replace('\n', '')