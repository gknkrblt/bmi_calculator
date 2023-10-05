import base64

asd = input("")
asdpassword = input("")
password = "123"
checker = False

encoded_string = base64.b64encode(asd)
print(encoded_string)


def master_key():
    global checker
    if asdpassword == password:
        decoded_string = base64.b64decode(encoded_string)
        checker = True
    else:
        print("invalid password")
