from tkinter.ttk import*
from tkinter import*
window=Tk()
window.title("cryptography")
window.geometry("1024x768")
window.configure(background="#011627")
lbl=Label(window,text="Caesar Cipher",font=("Times New Roman",40),fg='#F71735')
key=Entry(window,width=40,font=("Times New Roman",20))
plain=Entry(window,width=40,font=("Times New Roman",20))
ciper=Entry(window,width=40,font=("Times New Roman",20))
def encrypt(string, shift):
 
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  
  return cipher
def decrypt(string, shift):
 
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)
  
  return cipher
def clicked():
    s=plain.get()
    k=int(key.get())
    lbl5.configure(text=encrypt(s,k))
def decry():
    s=ciper.get()
    k=int(key.get())
    lbl7.configure(text=decrypt(s,k))

lbl2=Label(window,text="Plain Text :",font=("Times New Roman",40),fg="#41EAD4")
lbl3=Label(window,text="Key :",font=("Times New Roman",40),fg="#41EAD4")
lbl4=Label(window,text="Cipher Text",font=("Times New Roman",40),fg="#41EAD4")
lbl5=Label(window,text="",font=("Times New Roman",40),fg='#FF9F1C')
lbl6=Label(window,text="DECIPHER TEXT",font=("Times New Roman",40),fg='#41EAD4')
lbl7=Label(window,text="",font=("Times New Roman",40),fg='#FF9F1C')
lbld=Label(window,text="Cipher",font=("Times New Roman",40),fg='#41EAD4')
ptn=Button(window,text="CYPHER",font=("Times New Roman",40),bg="#F71735",fg="white",command=clicked)
ptnd=Button(window,text="DECYPHER",font=("Times New Roman",40),bg="#F71735",fg="white",command=decry)
lbl.configure(background="#011627")
lbl2.configure(background="#011627")
lbl3.configure(background="#011627")
lbl4.configure(background="#011627")
lbl5.configure(background="#011627")
lbl6.configure(background="#011627")
lbl7.configure(background="#011627")
lbld.configure(background="#011627")
lbl.grid(column=1,row=0)
lbl2.grid(column=1,row=1)
plain.grid(column=2,row=1)
lbl3.grid(column=1,row=2)
key.grid(column=2,row=2)
lbl4.grid(column=1,row=3)
lbl5.grid(column=2,row=3)
ptn.grid(column=1,row=6)#cipher
ptnd.grid(column=2,row=6)#decipher
lbld.grid(column=1,row=4)#decipher
ciper.grid(column=2,row=4)#enter cipher
lbl6.grid(column=1,row=5)#decrypt
lbl7.grid(column=2,row=5)#result decrypt
window.mainloop()
