from random import randint

class Train:
    def __init__(slf, trainNo):
        slf.trainNo=trainNo

    def book(senorita, boarding, destination):
        print(f"Ticket is booked for Train No. : {senorita.trainNo} From: {boarding} To: {destination}... ")

    def getStatus(kabutar):
        print(f"Train No. : {kabutar.trainNo} is running on time...")

    def getFare(krrish, boarding, destination):
        print(f"Ticket fare in Train No. : {krrish.trainNo} From: {boarding} To: {destination} is: {randint(500,2001)}.")

    
t=Train(11123)
t.book("Gomati Nagar","Thawe")
t.getStatus()
t.getFare("Gomati Nagar","Thawe")


#changing self parameter.