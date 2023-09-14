###----------------------------------------------
###            !VERY IMPORTANT NOTE!
###    THIS MUST BE RUN FROM A SEPARATE IDE
###    RUNNING IT IN REPLIT WILL LIKELY LEAD
###                TO CRASHING!
###-----------------------------------------------

import os
import time
from random import randint,choice
from tkinter import *
import tkinter.messagebox
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import datetime
import string

needAuth = True
gameStart = True
loop = True
location = "0"
clear = lambda: os.system('cls')

pEncry = open("! dependencies\\encrypted.dll","r")
pEncry = pEncry.read()
pDecry = ""
key = open("! dependencies\\key.dll","r")
key = key.read()
key = list(key)
chars = open("! dependencies\\chars.dll","r")
chars = chars.read()
chars = list(chars)

for letter in pEncry:
	index = key.index(letter)
	pDecry += chars[index]


def confirm():
	global money,location
	if tkinter.messagebox.askokcancel("Quit", "If you close window, money is lost! If you want to go home, press the home button. You sure you want to reset work progress?"):
		location = "0"
		workWn.destroy()

def layBrick():
	global moneyMade
	moneyMade += 1*multiplier
	moneyMadeText.config(text="You have made "+str(moneyMade)+" dabloons so far.")

def goHome():
	global money,location
	location = "0"
	workWn.destroy()
	money = money + moneyMade
	moneyFile = open(username+"\\money.txt","w")
	moneyFile.write(str(money))
	moneyFile.close()

letters = string.ascii_lowercase

while loop:

	while needAuth:
		clear()
		print("----------------------")
		print("Welcome to DabloonLife")
		print("----------------------")
		print()
		print("1. Login")
		print("2. Sign-up")
		print("3. Forgot password?")
		print("4. Quit")
		print()
		authOption = input("1/2/3/4: ")
		
		if authOption == "1":
			clear()
			username = str(input("Enter your username: "))
			if os.path.exists(username):
				file = open(username+"\\password.txt","r")
				actualPassword = file.read()
			else:
				pass
			password = str(input("Enter your password: "))
			while not os.path.exists(username) or password != actualPassword:
				clear()
				print()
				print("Username or Password are wrong!")
				print()
				username = str(input("Enter your username: "))
				if  os.path.exists(username):
					file = open(username+"\\password.txt","r")
					actualPassword = file.read()
				else:
					pass
				password = str(input("Enter your password: "))
			needAuth = False

		elif authOption == "2":
			try:
				clear()
				username = str(input("Enter your desired username: "))
				
				while os.path.exists(username):
					print()
					username = str(input("USERNAME TAKEN! Try another: "))
				print()
				print("NOTE: Password must be at least 8 characters long!")
				print()
				password = str(input("Enter your password: "))
				
				while len(password) < 8:
					print()
					print("Password must be at least 8 characters long!")
					password = str(input("Enter another password: "))

				clear()
				print("NOTE: This will be used later to recover your account if needed.")
				emailSignUp = str(input("Please enter your email: "))

				activationKey = randint(100000,999999)
				activationKey = str(activationKey)

				sent = (f"Hello {username}!\n\n"
					f"You have requested to create an account on Dabloon Life using this email."
					f"\n\nHere is your verification code: {activationKey}"
					f"\n\nYou need this code in order to create your account."
					f"\n\n\nKind regards,\nDabloon Life")
				txt = sent
				msg = MIMEMultipart()
				msg['Subject'] = "Account Creation"
				msg.attach(MIMEText(txt))

				smtp = smtplib.SMTP('smtp-mail.outlook.com', '587')
				smtp.ehlo()
				smtp.starttls()

				smtp.login('DabloonLifeOfficial@outlook.com', pDecry)

				smtp.sendmail('DabloonLifeOfficial@outlook.com', emailSignUp, msg.as_string())

				smtp.quit()

				clear()
				print("A verification key was sent to your email.")
				print()
				print("WARNING! If you quit the app now, account will not be created!")
				print()
				userKeyInput = str(input("What is your verification key: "))

				while userKeyInput != activationKey:
					clear()
					print("WRONG VERIFICATION KEY!")
					print("A verification key was sent to your email.")
					print()
					print("WARNING! If you quit the app now, account will not be created!")
					print()
					userKeyInput = str(input("What is your verification key: "))

				os.makedirs(username)
				file = open(username+"\\password.txt","w")
				file.write(password)
				file.close()

				file = open(username+"\\email.txt","w")
				file.write(emailSignUp)
				file.close()

				file = open(username+"\\money.txt","w")
				file.write("20000")
				file.close()

				file = open(username+"\\firstTime.txt","w")
				file.write("1")
				file.close()

				file = open(username+"\\robbed.txt","w")
				file.write("0")
				file.close

				file = open(username+"\\lastRobber.txt","w")
				file.write("")
				file.close()

				file = open(username+"\\rank.txt","w")
				file.write("[Pleb]")
				file.close()

				file = open(username+"\\multiplier.txt","w")
				file.write("1")
				file.close()

				clear()
				print("Account created successfully!")
				print()
				time.sleep(2)
			except:
				print("Error occured...")
				time.sleep(2)

		elif authOption == "3":
			clear()
			username = str(input("What is the username of the account you are trying to recover: "))
			if os.path.exists(username):
				
				email = open(username+"\\email.txt","r")
				email = email.read()
				password = open(username+"\\password.txt","r")
				password = password.read()

				timeRequested = datetime.datetime.now()

				sent = (f"Hello {username}!\n\n"
					f"You have requested to recover your account on {timeRequested}"
					f"\n\nHere is your current password: {password}"
					f"\n\nIf you didn't request this, please change your password IMMEDIATELY!"
					f"\n\nIn order to change your password, log in to your account on the game. After doing this,\n"
					f"you should see the option 'Settings' in the main menu. In settings, you can choose to change your password."
					f"\n\n\nKind regards,\nDabloon Life")
				txt = sent
				msg = MIMEMultipart()
				msg['Subject'] = "Account Recovery"
				msg.attach(MIMEText(txt))

				smtp = smtplib.SMTP('smtp-mail.outlook.com', '587')
				smtp.ehlo()
				smtp.starttls()

				smtp.login('DabloonLifeOfficial@outlook.com', pDecry)

				smtp.sendmail('DabloonLifeOfficial@outlook.com', email, msg.as_string())

				smtp.quit()

				print("An email was successfully sent to your email address!")
				print("NOTE: This only works if you used a valid email address..")
				time.sleep(1)
			else:
				print("Invalid username.. Redirecting..")
				time.sleep(1)


		elif authOption == "4":
			os.quit()

		else:
			print("INVALID OPTION! Redirecting to main menu...")
			time.sleep(1)
			print()

	while not needAuth:
		clear()
		file = open(username+"\\firstTime.txt","r")
		firstTime = file.read()
		if firstTime == "1":
			print("Welcome",username+"! Since this is the first time you play, let me give you some information:")
			time.sleep(2)
			print("1. The ways to gain money at the moment are:")
			print("  a) Gambling - Flipping Coins, Choosing a lucky number etc.")
			print("  b) Lottery - 0.000001% chance to win 100 million")
			print("  c) Job - At the moment, only job is a Clicker which gives you 1 coin/click")
			print("  d) AFK - 100 coins/minute in the AFK screen")
			print("  e) [NEW!] Robbery - You can rob other existing users (1 in 400 chance of success)")
			print()
			time.sleep(10)
			print("2. The money you gain can be used to buy ranks at the moment. These ranks give you a set multiplier to the money you earn (robbing people doesn't get multipled)")
			time.sleep(3)
			print()
			print("3. Since the app is in development, feel free to let me know about any bugs/errors + suggestions for what I should add")
			time.sleep(3)
			print()
			print("That's all! Enjoy!")
			time.sleep(2)
			file = open(username+"\\firstTime.txt","w")
			file.write("0")
			file.close()
		else:
			robbedFile = open(username+"\\robbed.txt","r")
			robbedCheck = robbedFile.read()
			if robbedCheck == "1":
				clear()
				robbedFile = open(username+"\\robbed.txt","w")
				robbedFile.write("0")
				robbedFile.close()
				robberFile = open(username+"\\lastRobber.txt","r")
				robber = robberFile.read()
				print("Unfortunately you have been robbed by '"+robber+"'. They stole all of your money. Try and rob them back! You have nothing to lose..")
				time.sleep(8)
			while gameStart:
				rankFile = open(username+"\\rank.txt","r")
				rank = rankFile.read()
				
				multiplierFile = open(username+"\\multiplier.txt","r")
				multiplier = multiplierFile.read()
				multiplier = int(multiplier)

				while location == "0":
					clear()
					moneyFile = open(username+"\\money.txt","r")
					money = moneyFile.read()
					money = int(money)
					print("Hello",rank,username+"! You are now in your house.")
					print("You have",str(money),"dabloons.")
					print()
					print("1. Go to the casino")
					print("2. Go to the corner shop")
					print("3. Go to work")
					print("4. Go to sleep (app needs restart to wake up)")
					print("5. Go rob another player")
					print("6. Settings")
					print("7. Quit")
					print()
					try:
						location = str(input("1/2/3/4/5/6/7: "))
						locationInt = int(location)
					except:
						clear()
						print("Invalid option! Redirecting to menu...")
						location = "0"
						time.sleep(1)

				while location == "1":
					clear()
					print("You walk into the casino with",money,"dabloons.")
					print("Go to:")
					print("1. Coin Flip")
					print("2. Random Number Generator")
					print("3. Horse racing")
					print("4. Go back home")
					casinoChoice = input("1/2/3/4: ")

					if casinoChoice == "1":
						clear()
						bettingMoney = str(input("How much are you going to bet: "))
						while not bettingMoney.isdigit() or int(bettingMoney) <= 0 or int(bettingMoney) > money:
							bettingMoney = str(input("Must be a number greater than 0 (and you must also have that much!): "))
						clear()
						print("BET AMOUNT: "+str(bettingMoney))
						print("---------------This is how this section works:----------------")
						print(" You choose either Heads or Tails and a coin will be flipped.")
						print("  If the coin lands on what you chose, you double your bet.  ")
						print("--------------------------------------------------------------")
						print("1. Heads")
						print("2. Tails")
						print("3. Go back")
						coinflipChoice = str(input("1/2/3: "))
						if coinflipChoice == "1" or coinflipChoice == "2":
							coinRandom = randint(1,2)
							if int(coinflipChoice) == coinRandom:
								win = int(bettingMoney)*2*multiplier
								clear()
								money = money + ((int(bettingMoney)*2)*multiplier)
								moneyFile = open(username+"\\money.txt","w")
								moneyFile.write(str(money))
								moneyFile.close()
								print("You got lucky! You are going back home with",str(win),"dabloons!")
								time.sleep(2.5)
							elif int(coinflipChoice) != coinRandom:
								clear()
								money = money - int(bettingMoney)
								moneyFile = open(username+"\\money.txt","w")
								moneyFile.write(str(money))
								moneyFile.close()
								print("You got unlucky! You lost the money and are now going home with a heart full of sadness.")
								time.sleep(2.5)
						elif coinflipChoice == 3:
							pass
						else:
							print("Invalid option! Redirecting...")
							time.sleep(1)

					elif casinoChoice == "2":
						clear()
						bettingMoney = str(input("How much are you going to bet: "))
						while not bettingMoney.isdigit() or int(bettingMoney) <= 0 or int(bettingMoney) > money:
							bettingMoney = str(input("Must be a number greater than 0 (and you must also have that much!): "))
						clear()
						print("BET AMOUNT: "+str(bettingMoney))
						print("---------------This is how this section works:----------------")
						print(" You have to enter a number between 1 and 100. If the random ")
						print("   number is the same as yours, you win x50 betting money!  ")
						print("--------------------------------------------------------------")
						
						randomNumberChoice = str(input("Please enter your number: "))
						while not randomNumberChoice.isdigit() or int(randomNumberChoice) < 1 or int(randomNumberChoice) > 100:
							randomNumberChoice = str(input("Must be a number between 1 and 100: "))
						randomNumberChoice = int(randomNumberChoice)
						
						randomGeneratedNumber = randint(1,100)
						if int(randomNumberChoice) == randomGeneratedNumber:
							win = int(bettingMoney)*50*multiplier
							clear()
							print("---------------------------------------------------------------------------------------------")
							print("YOUR HEART DROPS AS YOU REALISE YOU WON! YOU ARE TAKING A SWEET",str(win),"DABLOONS!")
							print("---------------------------------------------------------------------------------------------")
							money = money + ((int(bettingMoney)*2)*multiplier)
							moneyFile = open(username+"\\money.txt","w")
							moneyFile.write(str(money))
							moneyFile.close()
							time.sleep(6)
						elif randomNumberChoice != randomGeneratedNumber:
							clear()
							print("Unfortunately you lost, yet what can you expect.. Such low odds. Maybe try again!")
							money = money - int(bettingMoney)
							moneyFile = open(username+"\\money.txt","w")
							moneyFile.write(str(money))
							moneyFile.close()
							time.sleep(2.5)
					
					elif casinoChoice == "3":
						clear()
						bettingMoney = str(input("How much are you going to bet: "))
						while not bettingMoney.isdigit() or int(bettingMoney) <= 0 or int(bettingMoney) > money:
							bettingMoney = str(input("Must be a number greater than 0 (and you must also have that much!): "))
						clear()
						print("BET AMOUNT: "+str(bettingMoney))
						print("-----------------This is how this section works:-------------------")
						print("  You have a selection of 4 different race horses to choose from.")
						print(" If the horse is fast enough and wins, you'll get x4 betting money")
						print("-------------------------------------------------------------------")
						horseRandom = randint(1,4)
						print("You have the following choice of horses:")
						print("1. Old Joey")
						print("2. Dasher")
						print("3. Lightning")
						print("4. Frosty")
						
						horseChoice = str(input("Which horse will you put your money on: "))
						while not horseChoice.isdigit() or int(horseChoice) < 1 or int(horseChoice) > 4:
							horseChoice = str(input("Must be a number between 1 and 4: "))
						
						if horseChoice == str(horseRandom):
							win = (int(bettingMoney)*4)*multiplier
							if horseChoice == "1":
								clear()
								print("Old Joey was your lucky choice! You are going home with",str(win),"extra dabloons!")
								time.sleep(2.5)
							elif horseChoice == "2":
								clear()
								print("Dasher was your lucky choice! You are going home with",str(win),"extra dabloons!")
								time.sleep(2.5)
							elif horseChoice == "3":
								clear()
								print("Lightning was your lucky choice! You are going home with",str(win),"extra dabloons!")
								time.sleep(2.5)
							elif horseChoice == "4":
								clear()
								print("Frosty was your lucky choice! You are going home with",str(win),"extra dabloons!")
								time.sleep(2.5)
							money = money + ((int(bettingMoney)*4)*multiplier)
							moneyFile = open(username+"\\money.txt","w")
							moneyFile.write(str(money))
							moneyFile.close()
							time.sleep(1)

						elif horseChoice != str(horseRandom):
							if horseChoice == "1":
								clear()
								print("Old Joey was too slow! Better luck next time!")
								time.sleep(2.5)
							elif horseChoice == "2":
								clear()
								print("Dasher was too slow! Better luck next time!")
								time.sleep(2.5)
							elif horseChoice == "3":
								clear()
								print("Lightning was too slow! Better luck next time!")
								time.sleep(2.5)
							elif horseChoice == "4":
								clear()
								print("Frosty was too slow! Better luck next time!")
								time.sleep(2.5)

							money = money - int(bettingMoney)
							moneyFile = open(username+"\\money.txt","w")
							moneyFile.write(str(money))
							moneyFile.close()
							time.sleep(1)

					elif casinoChoice == "4":
						location = "0"

					else:
						print("Invalid option! Redirecting..")
						location = "1"
						time.sleep(1)

				while location == "2":
					clear()
					moneyFile = open(username+"\\money.txt","r")
					money = moneyFile.read()
					money = int(money)
					print("You walk in bossman's shop.")
					print("You have",str(money),"dabloons left in your bank account.")
					print("1. Buy a ticket (10 dabloons)")
					print("2. Buy a rank")
					print("3. Say goodbye to bossman and leave")
					shopChoice = input("1/2/3: ")
					if shopChoice == "1":
						lotteryRandom1 = randint(1,1000)
						lotteryRandom2 = randint(1,1000)
						if lotteryRandom1 == lotteryRandom2:
							clear()
							print("-------------------------------------------------------------------------------------------------")
							print("YOU GO TO YOUR TV LATER THAT DAY AND FIND OUT THAT YOU ARE THE WINNER OF 100 MILLION DABLOONS!!!!")
							print("-------------------------------------------------------------------------------------------------")
							money = money + (100000000*multiplier)
							moneyFile = open(username+"\\money.txt","w")
							moneyFile.write(str(money))
							moneyFile.close()
							time.sleep(5)
						else:
							clear()
							print("You didn't win anything, yet you only lost 10 dabloons so the loss wasn't so huge.")
							money = money - 10
							moneyFile = open(username+"\\money.txt","w")
							moneyFile.write(str(money))
							moneyFile.close()
							time.sleep(2.5)

					elif shopChoice == "2":
						clear()
						moneyFile = open(username+"\\money.txt","r")
						money = moneyFile.read()
						money = int(money)
						clear()
						print("You have",str(money),"dabloons.")
						print()
						print("Here are all the ranks available:")
						print("1. Pro (x2 money) - 100,000 dabloons")
						print("2. High IQ (x3 money) - 250,000 dabloons")
						print("3. Hacker (x4 money) - 500,000 dabloons")
						print("4. GOD (x5 money) - 1,000,000 dabloons")
						print("5. NO LIFE (x10 money) - 100,000,000,000 dabloons")
						print()
						print("6. Go back")
						rankShopChoice = str(input("1/2/3/4/5/6: "))
						if rankShopChoice == "1":
							if money < 100000:
								clear()
								print("You are too poor BROKIE!")
								time.sleep(2)
							else:
								clear()
								print("You are now a Pro!")
								rankFile = open(username+"\\rank.txt","w")
								rankFile.write("[Pro]")
								rankFile.close()
								multiplierFile = open(username+"\\multiplier.txt","w")
								multiplierFile.write("2")
								multiplierFile.close()
								moneyFile = open(username+"\\money.txt","w")
								moneyFile.write(str(money-100000))
								moneyFile.close()
								time.sleep(3)
						elif rankShopChoice == "2":
							if money < 250000:
								clear()
								print("You are too poor BROKIE!")
								time.sleep(2)
							else:
								clear()
								print("You are now a High IQ member!")
								rankFile = open(username+"\\rank.txt","w")
								rankFile.write("[High IQ]")
								rankFile.close()
								multiplierFile = open(username+"\\multiplier.txt","w")
								multiplierFile.write("3")
								multiplierFile.close()
								moneyFile = open(username+"\\money.txt","w")
								moneyFile.write(str(money-250000))
								moneyFile.close()
								time.sleep(3)
						elif rankShopChoice == "3":
							if money < 500000:
								clear()
								print("You are too poor BROKIE!")
								time.sleep(2)
							else:
								clear()
								print("You are now a Hacker member!")
								rankFile = open(username+"\\rank.txt","w")
								rankFile.write("[Hacker]")
								rankFile.close()
								multiplierFile = open(username+"\\multiplier.txt","w")
								multiplierFile.write("4")
								multiplierFile.close()
								moneyFile = open(username+"\\money.txt","w")
								moneyFile.write(str(money-500000))
								moneyFile.close()
								time.sleep(3)
						elif rankShopChoice == "4":
							if money < 1000000:
								clear()
								print("You are too poor BROKIE!")
								time.sleep(2)
							else:
								clear()
								print("You are now a GOD member!")
								rankFile = open(username+"\\rank.txt","w")
								rankFile.write("[GOD]")
								rankFile.close()
								multiplierFile = open(username+"\\multiplier.txt","w")
								multiplierFile.write("5")
								multiplierFile.close()
								moneyFile = open(username+"\\money.txt","w")
								moneyFile.write(str(money-1000000))
								moneyFile.close()
								time.sleep(3)
						elif rankShopChoice == "5":
							if money < 100000000000:
								clear()
								print("You are too poor BROKIE!")
								time.sleep(2)
							else:
								clear()
								print("You are now a NO LIFER!")
								rankFile = open(username+"\\rank.txt","w")
								rankFile.write("[NO LIFE]")
								rankFile.close()
								multiplierFile = open(username+"\\multiplier.txt","w")
								multiplierFile.write("10")
								multiplierFile.close()
								moneyFile = open(username+"\\money.txt","w")
								moneyFile.write(str(money-100000000000))
								moneyFile.close()
								time.sleep(3)

						elif rankShopChoice == "6":
							pass
						
						else:
							clear()
							print("Invalid choice! Redirecting...")
							time.sleep(1)

					elif shopChoice == "3":
						location = "0"

					else:
						clear()
						print("Invalid option! Redirecting...")
						time.sleep(1)

				while location == "3":
					clear()
					moneyMade = 0

					workWn = Tk()
					workWn.configure(background="cyan")
					workWn.title("Construction Site")
					workWn.geometry("400x280+350+350")
					workWn.protocol("WM_DELETE_WINDOW",confirm)

					instructFrame = LabelFrame(text="Instructions:",bg="cyan")
					instructFrame.pack()

					instructions = Label(instructFrame,text="You work as a brick layer. In order to make money, you have to 'lay bricks',\n which can be done by clicking the button below.\nOnce you are done, go back home by pressing the HOME button.",bg="#9cf3ff")
					instructions.pack()

					moneyMadeText = Label(text="You have made "+str(moneyMade)+" dabloons so far.",bg="#9cf3ff")
					moneyMadeText.pack()

					layBrickButton = Button(text="Lay brick",width="20",height="7",command=layBrick,bg="#9cf3ff")
					layBrickButton.pack(pady=15)

					homeButton = Button(text="HOME",width="20",command=goHome,bg="#9cf3ff")
					homeButton.pack(pady=5,padx=20)

					workWn.mainloop()

				while location == "4":
					clear()
					print("Every 60 seconds you get 100 dabloons")
					print("You have",str(money),"right now.")
					print("IF YOU WANT TO WAKE UP, RESTART APP")
					time.sleep(60)
					money = money + (100*multiplier)
					moneyFile = open(username+"\\money.txt","w")
					moneyFile.write(str(money))
					moneyFile.close()

				while location == "5":
					clear()
					print("You put on your balaclava and take out your dangerous-looking banana and go out on the streets.")
					print("1. Proceed with the robbery (10,000 dabloons payment)")
					print("2. Go back home")
					choiceRob = str(input("1/2: "))
					if choiceRob == "2":
						clear()
						print("You spot a police van and decide today isn't your day.")
						location = "0"
						time.sleep(1)
					elif choiceRob == "1":
						if money < 10000:
							clear()
							print("You are too poor BROKIE! Go get a job and come back later...")
							location = "0"
							time.sleep(2)
						else:
							personRobbed = str(input("Who are you going to rob: "))
							while not os.path.exists(personRobbed) or personRobbed == username:
								personRobbed = input("Try someone else (user must exist and it can't be you!): ")
							robSuccess = randint(1,400)
							if robSuccess == 1:
								clear()
								moneyVictim = open(personRobbed+"\\money.txt","r")
								moneyStolen = moneyVictim.read()
								print("You caught the poor soul by surprise and emptied his entire bank account.")
								print("You walk back home with a mischievous smile on your face.")
								moneyFile = open(username+"\\money.txt","w")
								moneyFile.write(str(money+int(moneyStolen)))
								moneyFile.close()
								moneyVictim = open(personRobbed+"\\money.txt","w")
								moneyVictim.write("0")
								moneyVictim.close()
								victomRobbedCheck = open(personRobbed+"\\robbed.txt","w")
								victomRobbedCheck.write("1")
								victomRobbedCheck.close()
								robberRecordName = open(personRobbed+"\\lastRobber.txt","w")
								robberRecordName.write(username)
								robberRecordName.close()
								location = "0"
								time.sleep(5)
							else:
								clear()
								print(personRobbed,"realised your banana isn't very lethal.")
								print("They laughed at you, made fun of you on social media and walked away.")
								print("You run away home crying..")
								location = "0"
								time.sleep(5)

					else:
						clear()
						print("Invalid option! Redirecting...")
						time.sleep(1)

				while location == "6":
					clear()
					print("1. Change password")
					print("2. Go back")
					choiceSettings = str(input("1/2: "))
					if choiceSettings == "1":
						clear()
						oldPassword = str(input("What is your old password: "))
						if oldPassword == password:
							clear()
							print("NOTE: Password must be over 8 characters!")
							newPassword = str(input("Enter new password: "))
							while len(newPassword) < 8:
								newPassword = str(input("Must be over 8 characters: "))
							passwordFile = open(username+"\\password.txt","w")
							passwordFile.write(newPassword)
							passwordFile.close()
							clear()
							print("Password changed successfully!")
							location = "0"
							needAuth = True
						else:
							clear()
							print("That is not your current password..")
							time.sleep(2)



				while location == "7":
					os.quit()

				while int(location) > 7:
					clear()
					print("Invalid option! Redirecting to menu...")
					location = "0"
					time.sleep(2)
