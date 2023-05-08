import json

#create a blank dictonary to hold username, password, and location
user_info = {}

#create a json file with user_info 
with open('user_info.json', 'w') as f:
    json.dump(user_info, f)

#closes the file
f.close()

#input username and password
username = input("Enter your username: ")
password = input("Enter your password: ")
location = "The Middle of Nowhere"

#add username, password, and location to user_info
user_info["username"] = username
user_info["password"] = password
user_info["location"] = location

#open json file and write user_info to it
with open('user_info.json', 'w') as f:
    json.dump(user_info, f)
#closes the file
f.close()

#open json file and read user_info from it
with open('user_info.json', 'r') as f:
    #print the user_info
    print(json.load(f))
    #add user_info to user_info
#closes the file
f.close()