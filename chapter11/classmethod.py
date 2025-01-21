class Num:
    a=5
    @classmethod
    def show(cls):
        print(f"The class value of a is: {cls.a}")


e=Num()

e.a=45

e.show()