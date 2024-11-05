import hashlib


def crack_sha1_hash(hash, use_salts=False):
    count = 0
    result = 'PASSWORD NOT IN DATABASE'
    if use_salts:
        passwords = []
        salts_list = []

        with open("./top-10000-passwords.txt") as lst:
            passwords = lst.read().split("\n")

        with open("known-salts.txt", "r") as lst1:
            salts_list = lst1.read().split("\n")

        pws_plus_salts = {}  # Append or prepend salts to each password
        for password in passwords:
            for salt in salts_list:
                pws_plus_salts[f'{password}-{salt}'] = {
                    'append': f'{salt}{password}',
                    'prepend': f'{password}{salt}'
                }
        print(len(pws_plus_salts.keys()))

        for key, password in pws_plus_salts.items():
            # print(key, "->", password)
            currentPass = key.split("-")[0]
            count += 1
            test = hashlib.sha1()
            test.update(password['append'].encode('utf-8'))
            if (hash == test.hexdigest()):
                print("Match: password is: " + currentPass + "->" + password['append'] +
                      " and was found in " + str(count) + " attempts through known salts append")
                return currentPass
            test = hashlib.sha1()
            test.update(password['prepend'].encode('utf-8'))
            if (hash == test.hexdigest()):
                print("Match: password is: " + currentPass + "->" + password['prepend'] +
                      " and was found in " + str(count) + " attempts through known salts prepend")
                return currentPass

        return result

    else:
        passwords = []
        with open("./top-10000-passwords.txt") as lst:
            passwords = lst.read().split("\n")

        for password in passwords:
            count += 1
            test = hashlib.sha1()
            test.update(password.encode('utf-8'))
            if (hash == test.hexdigest()):
                # print("Match: password is: " + password + " and was found in " +
                #       str(count) + " attempts through brute force")
                result = password
    return result
