'''
class Hotstar:
    def __int__(self,name):
        self.name = name
        print(f"Hi {self.name}, Welcome to the hotstar")
        
    def login(self):
        print("You can login")
    def dashboard(self):
        print("You can see the dashboard items")
    def search(self):
        print("You can search")
    def languages(self):
        print("you select the languages")
    def playcontrollers(self):
        print("You can pause and play the video")
    def ads(self):
        print("Ads will run")
    def movies(self):
        print("you can  limited access for movies")
    def sports(self):
        print("Limited time you can watch sports")
    def quality(self):
        print("limited quality")

srikanth = Hotstar('srikanth')
srikanth.login()
srikanth.dashboard()
srikanth.search()
srikanth.languages()
srikanth.playcontrollers()
srikanth.ads()
srikanth.movies()
srikanth.sports()
srikanth.quality()
'''

'''
class PremiumHotstar:
    def __int__(self,name):
        self.name = name
        print(f"Hi {self.name}, Welcome to the Premium Hotstar")
        
    def ads(self):
        print("Ads won't run")
    def movies(self):
        print("you can  unlimited access for movies")
    def sports(self):
        print("you can watch sports")
    def quality(self):
        print("High quality")

srikanth = Hotstar('srikanth')
srikanth.login()
srikanth.dashboard()
srikanth.search()
srikanth.languages()
srikanth.playcontrollers()
srikanth.ads()
srikanth.movies()
srikanth.sports()


srikanth = Hotstar('srikanth')
srikanth.login()
srikanth.dashboard()
srikanth.search()
srikanth.languages()
srikanth.playcontrollers()
srikanth.ads()
srikanth.movies()
srikanth.sports()
srikanth.quality()

'''

class Number:
    def __init__(self,n):
        self.n =n
    def __add__(self,other):
        return self.n + other.n
    def __sub__(self,other):
        return self.n - other.n
    def __mul__(self,other):
        return self.n * other.n
    def __truediv__(self,other):
        return self.n / other.n
    def __eq__(self,other):
        return self.n == other.n
    def __lt__(self,other):
        return self.n < other.n
    def __gt__(self,other):
        return self.n > other.n
    def __str__(self,other):
        return str(self.n)

n1 =Number(10)
n2 =Number(20)

print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)

print(n1==n2)
print(n1<n2)
print(n1>n2)
print(n1,n2)






























srikanth.quality()
