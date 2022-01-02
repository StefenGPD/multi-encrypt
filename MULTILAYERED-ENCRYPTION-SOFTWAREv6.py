import tkinter as tk
from tkinter import Frame, Image, Label, filedialog, Text
import os
from ALGORITHMS import make_key_list, auf_encrypt, auf_decrypt
import ast

root = tk.Tk()
root.title("MULTILAYERED TEXT EDITOR")
root.resizable(False, False)
apps = []

window_height = 250
window_width = 450
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


MTE = tk.Label(root, text="MULTILAYERED TEXT ENCRYPTOR",
                font="Arial 14 bold", padx=10, pady=5)
MTE.place(x=45, y=50)
MTE = tk.Label(root, text="By Capuno, Decena, Ferrer, Ignacio and Sicangco",
                padx=10, pady=5)
MTE.place(x=85, y=80)

def addApp():
    filename= filedialog.askopenfilename(initialdir="/", title="Select File",
              filetypes=(("executables", "*.exe"), ("all files", "." )))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(text=app, bg="black")
        label.pack()

def retrieve_input(input, finalKey, encryptedMessage):

    fileDirectory = filedialog.askdirectory(initialdir="/", title="Select File")

    fileName = fileDirectory + "/" + input + ".aufenc"
    print(fileName)
    f = open(fileName,"w+")
    f.write(encryptedMessage)
    f.close()

    fileName = fileDirectory + "/" + input + ".aufkey"
    g = open(fileName,"w+")
    g.write(str(finalKey))
    g.close()

def retrieve_output(input, decryptedMessage):

    fileDirectory = filedialog.askdirectory(initialdir="/", title="Select File")

    fileName = fileDirectory + "/" + input + ".txt"
    print(fileName)
    f = open(fileName,"w+")
    f.write(decryptedMessage)
    f.close()

def encryptWindow():

    filename= filedialog.askopenfilename(initialdir="/", title="Select File",
              filetypes=(('text files', '.txt'), ("all files", "." )))

    message = None
    with open(filename, 'r') as file:
        message = file.read()

    print(message)

    finalKey = make_key_list()

    encryptedMessage = auf_encrypt(finalKey, message)

    encryptWindow = tk.Toplevel()
    encryptWindow.title("MULTILAYERED TEXT ENCRYPTOR")

    apps = []
    #encryptWindow.geometry("505x260")
    #root.geometry("450x250")
    encryptWindow.resizable(False, False)

    window_height = 260
    window_width = 505
    screen_width = encryptWindow.winfo_screenwidth()
    screen_height = encryptWindow.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    encryptWindow.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    MTE = tk.Label(encryptWindow, text="MULTILAYERED TEXT ENCRYPTOR",
                    font="Arial 14 bold", padx=10, pady=5)
    MTE.place(x=70, y=10)

    tk.Label(encryptWindow, text="Before", padx=10, pady=5,
                        fg="black", bg="gray").place(x=50, y=50)
    tk.Label(encryptWindow, text="After", padx=10, pady=5,
                        fg="black", bg="gray").place(x=400, y=50)
    tk.Label(encryptWindow, text=message, padx=10, pady=5, wraplength=180, justify="left",
                        fg="black", bg="gray", width=25, height=6).place(x=20, y=90)
    tk.Label(encryptWindow, text=encryptedMessage, padx=10, pady=5, wraplength=180, justify="left",
                        fg="black", bg="gray", width=25, height=6).place(x=280, y=90)

    tk.Label(encryptWindow, text="File Name", padx=10, pady=8,
                        fg="black", bg="gray", width=7, height=1).place(x=90, y=205)
    FileNameEncrypted = tk.Text(encryptWindow,padx=10, pady=8,
                        fg="black", bg="white", height=1, width=27)
    FileNameEncrypted.place(x=175,y=205)

    Back = tk.Button(encryptWindow, text="BACK", padx=10, pady=5,
                        fg="white", bg="red", command=encryptWindow.destroy)
    Back.place(x=20, y=205)

    Save = tk.Button(encryptWindow, text="SAVE", padx=10, pady=5,
                        fg="white", bg="green", command=lambda: retrieve_input(FileNameEncrypted.get("1.0",'end-1c'), finalKey, encryptedMessage))
    Save.place(x=423, y=205)

    encryptWindow.mainloop()

def decryptWindow():

    encryptedfilename = filedialog.askopenfilename(initialdir="/", title="Select Encrypted File",
              filetypes=(('text files', '.aufenc'), ("all files", "." )))
    keyfilename = filedialog.askopenfilename(initialdir="/", title="Select Key File",
              filetypes=(('text files', '.aufkey'), ("all files", "." )))

    message = None
    with open(encryptedfilename, 'r') as file:
        message = file.read()
    print(message)

    finalKey = None
    with open(keyfilename, 'r') as file:
        finalKey = file.read()
    finalKey = ast.literal_eval(finalKey)
    print(type(finalKey))
    print(finalKey)

    decryptedMessage = auf_decrypt(finalKey, message)

    decryptWindow = tk.Toplevel()
    decryptWindow.title("MULTILAYERED TEXT ENCRYPTOR")

    apps = []
    #encryptWindow.geometry("505x260")
    #root.geometry("450x250")
    decryptWindow.resizable(False, False)

    window_height = 260
    window_width = 505
    screen_width = decryptWindow.winfo_screenwidth()
    screen_height = decryptWindow.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    decryptWindow.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    MTE = tk.Label(decryptWindow, text="MULTILAYERED TEXT DECRYPTOR",
                    font="Arial 14 bold", padx=10, pady=5)
    MTE.place(x=70, y=10)

    tk.Label(decryptWindow, text="Before", padx=10, pady=5,
                        fg="black", bg="gray").place(x=50, y=50)
    tk.Label(decryptWindow, text="After", padx=10, pady=5,
                        fg="black", bg="gray").place(x=400, y=50)
    tk.Label(decryptWindow, text=message, padx=10, pady=5, wraplength=180, justify="left",
                        fg="black", bg="gray", width=25, height=6).place(x=20, y=90)
    tk.Label(decryptWindow, text=decryptedMessage, padx=10, pady=5, wraplength=180, justify="left",
                        fg="black", bg="gray", width=25, height=6).place(x=280, y=90)

    tk.Label(decryptWindow, text="File Name", padx=10, pady=8,
                        fg="black", bg="gray", width=7, height=1).place(x=90, y=205)
    FileNameEncrypted = tk.Text(decryptWindow,padx=10, pady=8,
                        fg="black", bg="white", height=1, width=27)
    FileNameEncrypted.place(x=175,y=205)

    Back = tk.Button(decryptWindow, text="BACK", padx=10, pady=5,
                        fg="white", bg="red", command=decryptWindow.destroy)
    Back.place(x=20, y=205)

    Save = tk.Button(decryptWindow, text="SAVE", padx=10, pady=5,
                        fg="white", bg="green", command=lambda: retrieve_output(FileNameEncrypted.get("1.0",'end-1c'), decryptedMessage))
    Save.place(x=423, y=205)

    decryptWindow.mainloop()

#ABOUT THE SOFTWARE
def about():

    about = tk.Toplevel()
    about.title("MULTILAYERED TEXT ENCRYPTOR")

    apps = []
    about.resizable(False, False)

    window_height = 330
    window_width = 500
    screen_width = about.winfo_screenwidth()
    screen_height = about.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    about.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    MTE = tk.Label(about, text="MULTILAYERED TEXT ENCRYPTOR",
                    font="Arial 14 bold", padx=10, pady=5)
    MTE.place(x=71, y=10)
    tk.Label(about, text="This program encrypts and decrypts files with the following file extensions: \n  .txt - to get the file to be encrypted \n  .aufkey - to provide the cipher key to be used if any \n  .aufdec - to be used when decrypting the encrypted file.", padx=10, pady=5, wraplength=350, justify="left", fg="black", bg="gray", width=48, height=5).place(x=70, y=40)

    E = tk.Label(about, text="ENCRYPTION",
                    font="Arial 14 bold", padx=10, pady=5)
    E.place(x=25, y=150)
    tk.Label(about, text="Press Encrypt. Select a text file to be encrypted. \nEnter a file name and click save. \nSelect a location to save the encrypted file (.aufenc). Open after.", padx=10, pady=5, wraplength=190, justify="left", fg="black", bg="gray", width=25, height=6).place(x=25, y=180)

    D = tk.Label(about, text="DECRYPTION",
                    font="Arial 14 bold", padx=10, pady=5)
    D.place(x=320, y=150)
    tk.Label(about, text="Press Decrypt. Select the .aufkey and .aufenc file to be decrypted. \nEnter a file name and click save. \nSelect a location to save the decrypted file (.aufdec). Open after.", padx=10, pady=5, wraplength=190, justify="left", fg="black", bg="gray", width=25, height=6).place(x=270, y=180)

    Back = tk.Button(about, text="BACK", padx=10, pady=5,
                        fg="white", bg="red", command=about.destroy)
    Back.place(x=215, y=290)


    about.mainloop()


#BUTTONS
encrypt = tk.Button(root, text="ENCRYPT", padx=10, pady=5,
                    fg="white", bg="black", command=encryptWindow)
encrypt.place(x=125, y=110)

decrypt = tk.Button(root, text="DECRPYT", padx=10, pady=5,
                    fg="white", bg="black", command=decryptWindow)
decrypt.place(x=255, y=110)

software = tk.Button(root, text="ABOUT OUR SOFTWARE", padx=10, pady=5,
                    fg="white", bg="gray", command=about)
software.place(x=150, y=150)

root.mainloop()