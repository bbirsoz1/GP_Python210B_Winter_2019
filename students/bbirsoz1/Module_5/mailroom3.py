#!/usr/bin/env python3

import sys  # imports go at the top of the file
import datetime

#Mailroom Part 2

donor_db = {"William Gates, III": [653772.32, 12.17],
            "Jeff Bezos": [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
            "Obama": [99999, 3333],
}

main_menu_prompt = "\n".join(("Welcome to the Mailroom Charity Menu!",
                    "Please choose from below options:",
                    "1 - Send a Thank You",
                    "2 - Create a Report",
                    "3 - Send letters to all donors",
                    "4 - Quit",
                    ">>> "))


thank_menu_prompt = "\n".join(("Please enter one of the following:",
                    "1 - Enter a new thank you note",
                    "2 - List of donors in the database",
                    "3 - Return to main menu",
                    '>>> '))

def list_of_donors():
    print("List of donors in the database:")
    donors_list = [donor.lower() for donor in donor_db] 
    print(donors_list)
    '''this seemed like the most appropriate place to try comprehensions (even though I liked the original simple line I had before).
    I don't like using lower/upper case restriction but code wouldn't work if I didn't add that. What do you reccomend I do to remove that?'''

def create_a_report():
    print("Report:")
    Header = ('Donor Name', 'Total Donation', "Number of Donations", 'Average Donation')
    print("-"*90)
    print("{:<20} | {:^24} | {:^19} | {:^15}".format(Header[0], Header[1], Header[2], Header[3]))
    print("-"*90)

    everything = [ ]
    #everything = [donor_db.items]
    for donor_name, donations in donor_db.items():
        total_donation = sum(donations)
        num_of_donation = len(donations)
        average_donation = int(total_donation / num_of_donation)
        print("{:<20} | {:>24} | {:^19} | {:>15}".format(donor_name, total_donation, num_of_donation, average_donation))
    print("-"*90)

def mail_donor():
    list_of_donors()
    current_d = "" #donors currently listed
    current_d = str(input("Who would you like to mail?:"))
    if current_d in donor_db:
        add_donation(current_d)
    else:
        donor_db[current_d] = []
        add_donation(current_d)

def add_donation(current_d):
    donation_times = float(input("How many donations have been made so far?: ")) #replaced int() with float()
    #if donation_times.isdigit(): #why does this not work instead of while true?
    while True:
        try:
            donation_times = int(donation_times)
            break
        except ValueError:
            print("Input must be an integer, try again.") #it doesnt show up, why???
            break
    total_donation = 0
    while donation_times > 0:
        new_donation = float(input("Donation amount?: "))
        donor_db[current_d].append(new_donation)
        donation_times -= 1
        total_donation += float(new_donation)
    mail_note(current_d, total_donation)
    
def mail_note(donor_name, total_donation):
    print(f"Thank you {donor_name} for your very kind donation of ${total_donation}")

def send_letters_to_all():
        for key in donor_db:
            with open(key+"_"+str(datetime.date.today())+".txt", 'w') as f:
                f.write("Dear {fullname},\n"
                        "Thank you for your very kind donation of ${amount:10.2f}."
                        " It will be put to very good use.\n"
                        "Sincerely,\n"
                        "~The Team".format(fullname=key, amount=donor_db[key][0]))
        print("Thank you letters to all donors have been saved to the local directory.\n")

def quit_program():
    print("Goodbye!")
    sys.exit()

def thank_menu():
    entry=("1","2","3")
    while True:
        mail = input(thank_menu_prompt)
        if mail not in entry:
            print("Not a valid option!")
        elif mail == "1":
            mail_donor()
        elif mail == "2":
            list_of_donors()
        elif mail == "3":
            break

def main():
    while True:
        response = int(input(main_menu_prompt))
        if response in dict_menu:
            dict_menu[response]()
        else:
            print("Not a valid option!")

dict_menu = {1: thank_menu,
             2: create_a_report,
             3: send_letters_to_all,
             4: quit_program,
}

if __name__ == "__main__":
    main()
