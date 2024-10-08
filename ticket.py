from random import randint
class Train:
    def __init__(self,Name,From,To):
        self.trainno=randint(2222,5555)
        self.seatno=randint(1,100)
        self.Fare=randint(5000,5555)
        self.Name=Name 
        self.From=From
        self.To=To

    def ticket(self):
        print(f'''Name : {self.Name}
        From {self.From} to {self.To}
        Train number : {self.trainno}
        Seat number : {self.seatno}
        Fare : {self.Fare}''')

b=input('Enter name: ')
frm=input('Enter Destination from: ')
to=input('Enter destination to: ')
a=Train(b,frm,to)
a.ticket()