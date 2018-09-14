import threading
import grpc
import time
import uuid
# import the generated classes
import message_pb2 as chat
import message_pb2_grpc as rpc

from tkinter import *
from tkinter import simpledialog

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

LIMIT = 0 # limit


class Client:

    def __init__(self, u: str, window):
        # the frame to put ui components on
        self.window = window
        self.username = u
        self.last = 0
        # create a gRPC channel + stub
        channel = grpc.insecure_channel('localhost:50051')
        self.conn = rpc.ChatServerStub(channel)
        # create new listening thread for when new message streams come in
        threading.Thread(target=self.__listen_for_messages, daemon=True).start()
        self.__setup_ui()
        self.window.mainloop()

    def __listen_for_messages(self):
        """
        This method will be ran in a separate thread as the main/ui thread, because the for-in call is blocking
        when waiting for new messages
        """
        for note in self.conn.ChatStream(chat.Empty()):
            print("R[{}] {}".format(note.name, note.message))
            self.chat_list.insert(END, "[{}] {}\n".format(note.name, note.message))

    def send_message(self, event):
        if time.time() - self.last < LIMIT:
            return

        self.last = time.time()

        """
        This method is called when user enters something into the textbox
        """
        message = self.entry_message.get()

        if message is not '':
            self.entry_message.delete(0, 'end')

            n = chat.Note()
            n.name = self.username
            n.message = message
            n.uuid = str(uuid.uuid4())
            print('uuid: ', n.uuid)
            print("S[{}] {}".format(n.name, n.message))
            self.conn.SendNote(n)

    def __setup_ui(self):
        self.chat_list = Text()
        self.chat_list.pack(side=TOP)
        self.lbl_username = Label(self.window, text=self.username)
        self.lbl_username.pack(side=LEFT)
        self.entry_message = Entry(self.window, bd=5)
        self.entry_message.bind('<Return>', self.send_message)
        self.entry_message.focus()
        self.entry_message.pack(side=BOTTOM)

if __name__ == '__main__':
    root = Tk()
    frame = Frame(root, width=300, height=300)
    frame.pack()
    root.withdraw()
    username = str(uuid.uuid1())
    if len(username) >= 10:
        username = username[:10]

    root.deiconify()
    c = Client(username, frame)