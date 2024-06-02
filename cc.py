import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from random import *
import time
import tkinter
from tkinter import messagebox
l=[PRIMARY,SECONDARY,SUCCESS,INFO,WARNING,DANGER,LIGHT]
dark_theme=["cyborg","darkly","superhero","vapor",'solar']
def random_color():
    x=randint(0,len(l)-1)
    return l.pop(x)
def random_theme():
    x=randint(0,len(dark_theme)-1)
    return dark_theme.pop(x)
root = ttk.Window(themename=random_theme())
root.geometry("1920x1080")
pics=["pic1.png","pic2.png","pic3.png","pic4.png","pic5.png"]
def random_bg():
    x = randint(0, len(pics) - 1)
    return pics.pop(x)
bg = tkinter.PhotoImage(file =random_bg())
bg_wall=tkinter.Label(root,image=bg)
bg_wall.place(x=0,y=0)
mainheading=ttk.Label(text="caesar cipher",font=("Poor Richard",100),bootstyle=random_color())
mainheading.pack(pady=(200,0))
def ENCRYPTION():
    #a is encrypted string
    string_to_encrypt = e.get()
    e.destroy()
    def constant_encrypt(raw_string):
        a = randint(50, 88)  ##
        # print(a)
        c = 2 * a
        b = a % 26
        encrypted_string = ""
        for i in raw_string:
            j = chr(ord(i) + b)
            encrypted_string = encrypted_string + j
        return [encrypted_string, "kon" + str(c)]
    def ap_encrypt(raw_string):
        x = randint(1, 9)
        y = randint(10, 99)
        encrypted_string = ""
        d = 0
        m = []
        for i in range(0, len(raw_string)):
            m.append(x + i * y)
        # print(m)
        for i in raw_string:
            z = m[d] % 13
            # print(z)
            encrypted_string = encrypted_string + chr(ord(i) + z)
            d = d + 1
        return [encrypted_string, "urt" + str(x) + str(y)]
    def gp_encrypt(raw_string):
        x = randint(1, 9)
        y = randint(10, 99)
        encrypted_string = ""
        d = 0
        m = []
        for i in range(0, len(raw_string)):
            m.append(x * (y ** i))
        for i in raw_string:
            z = m[d] % 13
            encrypted_string = encrypted_string + chr(ord(i) + z)
            d = d + 1
        return [encrypted_string, "goo" + str(x) + str(y)]
    def fib_encrypt(raw_string):
        x = randint(1, 9)
        y = randint(10, 99)
        # print(x,y)
        s = x
        t = y
        encrypted_string = ""
        d = 0
        m = []
        for i in range(0, len(raw_string)):
            a = x
            m.append(x)
            x = x + y
            y = a
        # print(m)
        for i in raw_string:
            z = m[d] % 13
            encrypted_string = encrypted_string + chr(ord(i) + z)
            d = d + 1
        return (encrypted_string, "feb" + str(s) + str(t))
    def random_encrypt():
        ranencry= [constant_encrypt, ap_encrypt, gp_encrypt, fib_encrypt]
        return ranencry.pop(randint(0, len(ranencry) - 1))

    mainheading.config(text="encrypted string and key is:")
    text =ttk.Text(root, height=8)
    text.pack(pady=(50,0))
    g=random_encrypt()
    encrypted_string_with_key=g(string_to_encrypt)
    #print(encrypted_string_with_key)

    text.insert('1.0', "encrypted string :" ,"2.0",encrypted_string_with_key[0])
    text = ttk.Text(root, height=3)
    text.pack(pady=(50, 0))

    text.insert('1.0',"encrypted key :","2.0",encrypted_string_with_key[1])
    encrypt_button.config(text="exit",command=exit)
def string_encrypt():
    global e
    mainheading.config(text="Enter the string")
    e=ttk.Entry(bootstyle=random_color(),width=50,show="*")
    e.pack(pady=50)

    encrypt_button.config(text="enter",command=ENCRYPTION,bootstyle=random_color())
    decrypt_button.destroy()
def DECRYPTION():
    encrypted_string=b.get()
    key=c.get()
    def key_error():
        messagebox.showerror("Error", "Entered key value is invalid")
        time.sleep(0.1)
        exit()
    if len(key) != 6:
        key_error()
    elif key[0] + key[1] + key[2] != "kon" and key[0] + key[1] + key[2] != "urt" and key[0] + key[1] + key[2] != "feb" and key[0] + key[1] + key[2] != "goo":
        key_error()
    elif str(key[3] + key[4] + key[5]).isdigit()==False:
        key_error()
    mainheading.config(text="decrypted string is:")
    text = ttk.Text(root, height=8)
    text.pack(pady=(50,0))
    b.destroy()
    c.destroy()

    def constant_decrypt(encrypted_string, key):
        c = int(key[3] + key[4] + key[5])
        a = c // 2
        b = a % 26
        decrypted_string = ''
        for i in encrypted_string:
            j = chr(ord(i) - b)
            decrypted_string = decrypted_string + j
        return (decrypted_string)

    def ap_decrypt(encrypted_string, key):
        x = int(key[3])
        y = int(key[4] + key[5])
        decrypted_string = ''
        d = 0
        m = []
        for i in range(0, len(encrypted_string)):
            m.append(x + i * y)
        # print(m)
        for i in encrypted_string:
            z = m[d] % 13
            # print(z)
            decrypted_string = decrypted_string + chr(ord(i) - z)
            d = d + 1
        return (decrypted_string)

    def gp_decrypt(encrypted_string, key):
        x = int(key[3])
        y = int(key[4] + key[5])
        decrypted_string = ''
        d = 0
        m = []
        for i in range(0, len(encrypted_string)):
            m.append(x * (y ** i))
        for i in encrypted_string:
            z = m[d] % 13
            # print(z)
            decrypted_string = decrypted_string + chr(ord(i) - z)
            d += 1
        return (decrypted_string)

    def fib_decrypt(encrypted_string, key):
        x = int(key[3])
        y = int(key[4] + key[5])
        # print(x,y)
        decrypted_string = ''
        d = 0
        m = []
        for i in range(0, len(encrypted_string)):
            a = x
            m.append(x)
            x = x + y
            y = a
        # print(m)
        for i in encrypted_string:
            z = m[d] % 13
            decrypted_string = decrypted_string + chr(ord(i) - z)
            d = d + 1
        return (decrypted_string)

    if key[0] + key[1] + key[2] == "kon":
        f=constant_decrypt(encrypted_string, key)
    elif key[0] + key[1] + key[2] == "urt":
        f=ap_decrypt(encrypted_string, key)
    elif key[0] + key[1] + key[2] == "feb":
        f=fib_decrypt(encrypted_string, key)
    else:
        f=gp_decrypt(encrypted_string, key)
    text.insert('1.0',f )
    encrypt_button.config(text="exit", command=exit)
def string_decrypt():
    global b,c
    mainheading.config(text="Enter the details",bootstyle=random_color())
    b=ttk.Entry(width=50)
    b.pack(pady = (50,20))
    b.insert(0,"enter the encrypted string")
    c = ttk.Entry( width=50)
    c.pack()
    c.insert(0,"enter the key")
    encrypt_button.config(text = "Enter",command=DECRYPTION)
    decrypt_button.destroy()
decrypt_button = ttk.Button(text="Decrypt",width = 20,command=string_decrypt,bootstyle=random_color())
decrypt_button.pack(side=BOTTOM,pady=(0,200))
encrypt_button = ttk.Button(text="Encrypt",width = 20,command=string_encrypt,bootstyle=random_color())
encrypt_button.pack(side=BOTTOM,pady=50)
root.mainloop()
