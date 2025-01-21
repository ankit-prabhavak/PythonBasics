from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo=trainNo

    def book(self, boarding, destination):
        print(f"Ticket is booked for Train No. : {self.trainNo} From: {boarding} To: {destination}... ")

    def getStatus(self):
        print(f"Train No. : {self.trainNo} is running on time...")

    def getFare(self, boarding, destination):
        print(f"Ticket fare in Train No. : {self.trainNo} From: {boarding} To: {destination} is: {randint(500,2001)}.")

    
t=Train(11123)
t.book("Gomati Nagar","Thawe")
t.getStatus()
t.getFare("Gomati Nagar","Thawe")


