#TIY 5.3

#5.8 Hello Admin - 5 users with greetings, special greeting for admin
users = ["Alice","Bob","Charlie","Doug","Evelyn","Admin","admin"]
users = ["Alice","Bob","Charlie","Doug","Evelyn","Admin","admin"]

for user in users:
    if user == "admin":
        print("WARNING: LOGGING IN WITH ELEVATED PERMISSIONS. ALL CHANGES ARE PERMANENT")
        print("\nwelcome admin")
    else:
        print(f"Hello {user}")


#5.9 no users - add if test
users = []

if users == "":
    print("We need to find some users!")
else:
    print(f"Hello {user}!")


#5-10 (p144) Checking Usernames - Live demo
