from tkinter import *
from PIL import ImageTk, Image
import cryptocode
import tkinter.messagebox


win = Tk()
win.geometry("700x600")
FONT = ("ariel", 12, "normal")

my_password = "123"

frame = Label(width=100, height=25)

img = ImageTk.PhotoImage(Image.open("secret.png"))
label = Label(frame, image=img)
label.pack()

frame.place(anchor="center", relx=0.5, rely=0.5)
frame.pack(pady=25)

title_name = Label(text="Enter your title", font=FONT)
title_name.pack(pady=5)
title_name_input = Entry()
title_name_input.pack(pady=5)

secret_label = Label(text="Enter your secret", font=FONT)
secret_label.pack(pady=5)
secret_text = Text(height=15, width=30)
secret_text.pack(pady=5)

masterkey_label = Label(text="Enter your masterkey", font=FONT)
masterkey_input = Entry()
masterkey_label.pack(pady=5)
masterkey_input.pack(pady=5)
my_encrypted_message = cryptocode.encrypt(secret_text.get("1.0", "end"), password=masterkey_input.get())
my_decrypted_message = cryptocode.decrypt(secret_text.get("1.0", "end"), password=masterkey_input.get())
cryptocode_encrypted_message = cryptocode.encrypt(secret_text.get("1.0", "end"), "123")
cryptocode_decrypted_message = cryptocode.decrypt(secret_text.get("1.0", "end"), "123")

def file_creator():
    global my_password
    if masterkey_input.get() == my_password:
        file = open("Secret.txt", "a+")
        file.write(f"{title_name_input.get()}: \n")
        file.write(cryptocode_encrypted_message)
        file.close()
    else:
        tkinter.messagebox.showinfo("Error!", "Wrong masterkey")


def decrypt_it():
    global my_password
    if masterkey_input.get() == my_password:
        secret_text.delete("1.0", "end")
        message = secret_text.get("1.0", "end")
        decrypt = secret_text.get("1.0")
        decoded = cryptocode.decrypt(message, decrypt)
        secret_text.insert("1.0", decoded)
    else:
        tkinter.messagebox.showinfo("Error!", "Wrong masterkey")


save_and_encrypt_button = Button(text="Save & Encrypt", command=file_creator)
decrypt_button = Button(text="Decrypt", command=decrypt_it)
save_and_encrypt_button.pack(pady=5)
decrypt_button.pack(pady=0.5)


win.mainloop()


"""

cryptocode_decrypt_message = 
"""