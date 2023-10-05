from tkinter import *
from PIL import ImageTk, Image

win = Tk()
win.geometry("500x700")
FONT = ("Ariel", 12, "normal")

frame = Frame(width=600, height=400)

img = ImageTk.PhotoImage(Image.open("secret.png"))
label = Label(frame, image=img)
label.pack()

frame.place(anchor="center", relx=0.5, rely=0.5)
frame.pack(pady=50)

enter_your_title_label = Label(text="Enter your title", font=FONT)
enter_your_title_label.pack()
title_input = Entry(width=26)
title_input.pack(pady=5)
enter_your_secret_label = Label(text="Enter your secret", font=FONT)
enter_your_secret_label.pack(pady=5)

enter_your_secret = Text(height=15, width=40)
enter_your_secret.pack(pady=5)

masterkey_label = Label(text="Enter your masterkey", font=FONT)
masterkey_label.pack(pady=5)
masterkey_entry = Entry(width=26)
masterkey_entry.pack(pady=5)

save_encrypt_button = Button(text="Save & Encrypt",)
save_encrypt_button.pack(pady=5)
decrypt_button = Button(text="Decrypt")
decrypt_button.pack(pady=5)


win.mainloop()
