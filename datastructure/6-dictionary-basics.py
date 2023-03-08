# sob programming language e JSON data porar support thake
# dictionary hoise python er JSON
# JSON = JavaScript Object Notation
# Object = JavaScript e object hoise EKTA data pair
# data pair er example hoise : "name" : "Shayan"
# left side er ta re koy "Key"
# right side er ta re koy "Value"
# Key diya value call kore
# python a key sudhu single data type hoite pare : ekta string, ekta number (int)
# value ja ichha : string, int, float, list, dictionary, tuple, set, boolean

employee_db = {
    "name" : "Shayan Saha",
    "company" : "Wipro",
    "salary" : 45000,
    "experience" : 1.5,
    "address" : "Bengaluru, Karnataka"
}

# print(len(employee_db["name"]))

e_dbs = {
    "id" : [101,102,103,104],
    "firstname" : ["Shayan", "Arindam", "Prasanta", "Pranjit"],
    "lastname" : ["Saha", "Bhadra", "Debnath", "Choudhury"],
    "login_creds" : [('shayan1', 'pass1'), ('bhadra2', 'pass2'), ('prasanta3', 'pass3'), ('pranjit4', 'pass4')],
    "location_information" : {
        "state" : "Karnataka",
        "city" : "Bengaluru",
        "country" : "India",
        "zipcode" : 100100
    }
}

print(e_dbs["location_information"]["country"])
