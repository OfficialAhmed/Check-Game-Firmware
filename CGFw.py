import requests, re
from bs4 import BeautifulSoup as bs
from colorama import Fore, Back, Style, init
init(autoreset=True)

def result(playable, current_fw, Game_day, Game_month, Game_year):
    if playable == "Yes":
        print(Fore.GREEN +"\nInitial game release[dd/mm/yyyy]: " + str(Game_day) + " " + str(Game_month) + " " + str(Game_year))
        print(Fore.GREEN + "Playable on " + str(current_fw[0]) + " \n")
    elif playable == "No":
        print(Fore.RED + "\nInitial game release[dd/mm/yyyy]: " + str(Game_day) + " " + str(Game_month) + " " + str(Game_year))
        print(Fore.RED + "Unfortunately the game requires a later firmware than " + str(current_fw[0]) + " \n")
    else:
        print(Fore.YELLOW + "\nInitial game release[dd/mm/yyyy]: " + str(Game_day) + " " + str(Game_month) + " " + str(Game_year))
        print(Fore.YELLOW + "Unplayable on " + str(current_fw[0]) + " unless the game was built on an older SDK\n")

def main():
    month = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
    ver = 1.01
    with open("fw release date.ini", "r") as file:
        firmware = file.readlines()
        line_num = 0
        for line in range(len(firmware)):
            current_line = firmware[line_num]
            print(Fore.CYAN + str(line_num+1) + ". " + current_line[:current_line.find(" ")])
            line_num += 1
    
        latest_fw = False
        user_input = input("Choose a firmware[number exp: 1 or 2] or Q to quit:")
        if user_input == "Q" or user_input == "q":
            import sys, time
            print(Fore.CYAN + "Thanks for using CGFw (Check Game Firmware) v" + str(ver) + " by @OfficialAhmed0. Bye!")
            time.sleep(3)
            sys.exit()
        while(user_input.isdigit() == False):
            try:
                user_input = int(user_input)
            except:
                print(Back.RED + "Choose line number[1, 2, 3... etc]")
                user_input = input("Choose a firmware[number exp: 1 or 2] or Q to quit:")
        user_input = int(user_input) - 1

        while(user_input >= len(firmware) or user_input < 0):
            print("Invalid number...")
            user_input = int(input("Choose a firmware[number exp: 1 or 2]:"))-1
        
        if user_input == 0: #This is the latest fw
            latest_fw = True
        
        elif user_input < len(firmware) and user_input >= 0: #There is a later fw
            try:
                later_fw = firmware[user_input-1].split(" ")
                later_fw_ver = later_fw[0]
                later_fw_year = int(later_fw[3])
                later_fw_month = month[later_fw[1]]
                later_fw_day = int(later_fw[2])
            except Exception as e:
                print("Wrong form of the latest firmware info. Error[dev]:", e)
        
        #From selected firmware
        current_fw = firmware[user_input].split(" ")
        current_fw_year = int(current_fw[3])
        current_fw_month = month[current_fw[1]]
        current_fw_day = int(current_fw[2])
    
        GameTitle = input("Enter Game title: ")
        search = GameTitle.replace(" ", "+") + "+Playstation+4+store"
        google = "https://www.google.com/search?hl=en&sxsrf=ALeKk008zPfPySZ73hbkXUMf_Az50hGTMA%3A1600888031936&ei=35xrX7G9OKPuxgOlyKvYBw&q=" + search
        read = requests.get(google).text
        soup = bs(read, "html.parser")
        
        GameLink = []
        #Get game link for Playstation 4 store 
        for link in soup.find_all('a'):
            check = link.get('href')
            if "https://store.playstation.com/" in check:
                link = check[check.find("=")+1 : check.find("&")]
                GameLink.append(link)
    
        if len(GameLink) == 0:
            print("Cannot find", GameTitle, "in PlayStation store")
            main()
        else: #Try all links for a valid one
            foundReleaseDate = False
            counter = 0
            Game_year, Game_month, Game_day = 0, 0, 0
            while(foundReleaseDate == False and counter < len(GameLink)):
                read = requests.get(GameLink[counter]).text
                data = read.split(",")
                for info in data:
                    if "releaseDate" in info:
                        starting_point = len('"releaseDate":"')
                        date = re.findall("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]", info[starting_point:])
                        Game_release_date = date[0].split("-")
                        Game_year = int(Game_release_date[0])
                        Game_month = int(Game_release_date[1])
                        Game_day = int(Game_release_date[2])
                        foundReleaseDate = True
                        break
                counter += 1
            if foundReleaseDate == True:
                """
                Check if the game was released before a later fw release date 
                if selected firmware's not the latest
                otherwise all games would be playable
                """
                if latest_fw == False:# If this is not the latest official firmware available
                    if Game_year == later_fw_year:
                        if Game_month <= later_fw_month:
                            if Game_day <= later_fw_day:
                                result("Yes", current_fw, Game_day, Game_month, Game_year)
                            else:
                                result("Yes", current_fw, Game_day, Game_month, Game_year)
                        else:
                            result("Not sure", current_fw, Game_year, Game_month, Game_day)
                    elif Game_year < later_fw_year:
                        result("Yes", current_fw, Game_day, Game_month, Game_year)
                    else:
                        result("No", current_fw, Game_year, Game_month, Game_day)

                else: #If this is the latest official firmware available
                    result("Yes", current_fw, Game_day, Game_month, Game_year)
            else:
                print("Cannot find release date for", GameTitle)
        main()
main()
