import socket
import threading
import time
from tkinter import *

root = Tk()

#Basic Specification
width = 455
height = 635
root.geometry(f"{width}x{height}")
root.minsize(width, height)
root.maxsize(width, height)
root.title("ChatApp by Ambar - [Server Side Application]")

#functions
def t_recv():
    r = threading.Thread(target=recv)
    r.start()

def recv():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listensocket:
        port = 5354
        maxconnections = 9
        ip = socket.gethostbyname(socket.gethostname())
        print(ip)
        server = (ip, port)
        FORMAT = 'utf-8'

        listensocket.bind((server))
        listensocket.listen(maxconnections)
        (clientsocket, address) = listensocket.accept()
        msg = f'[ALERT] {address} has joined the chat.'
        lstbox.insert(0, msg)

        while True:
            (clientsocket, address) = listensocket.accept()
            sendermessage = clientsocket.recv(1024).decode(FORMAT)
            if not sendermessage == "":
                time.sleep(2)
                lstbox.insert(0, 'Client: ' +sendermessage)
        

def t_sendmsg():
    s = threading.Thread(target=sendmsg)
    s.start()

at = 0

def sendmsg():
    global at
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as g:
        hostname = 'Lenovo-PC'
        port = 5986

        if at==0:
            g.connect((hostname, port))
            msg = messagebox.get()
            lstbox.insert(0, 'You: ' +msg)
            g.send(msg.encode())
            at += 1

        else:
            g.connect((hostname, port))
            msg = messagebox.get()
            lstbox.insert(0, 'You: ' +msg)
            g.send(msg.encode())      


#Full Specification
connectwithserver = Button(root, text="Connect to Client", command=t_recv)
connectwithserver.place(x=15, y=30)

lstbox = Listbox(root, bg="white", width=70, height=25, font="Helvetica 10 normal")
lstbox.place(x = 15, y = 70)

message = StringVar
messagebox = Entry(root, width=30, font="Helvetica 15 normal", textvariable=message)
messagebox.place(x=15, y=530)
lab = Label(text="Enter your message below:").place(x=15, y=500)

send = Button(root, text="Send", command=t_sendmsg, width=10)
send.place(x=350, y=530)

root.mainloop()