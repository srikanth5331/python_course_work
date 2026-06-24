'''
class Flipkart:
    pass
pranathi = Flipkart()
vamsi = Flipkart()
dinesh = Flipkart()
'''

'''
class Flipkart:
    discount = 10
    products = ['laptop','phone','mouse','charger']

    @classmethod
    def showproducts (cls):
        print(cls.products)

    #instance method
    def login(self,username,password):
        self.username = username
        self.password = password
        print(f'welcome to the flipkart {self.username}')
    
    @staticmethod
    def banner():
        print("10% dicount is going on flipkart,shop now!")
    
pranathi = Flipkart()
pranathi.login('pranathi','pranati@123')
pranathi.banner()
pranathi.showproducts()

Flipkart.showproducts()
Flipkart.banner()
'''

'''
class Instagram:
    def __int__(self,username,password):
        self.username = username
        self.password = password
        self.followers = []
        print(f'Welcome to the Instagram, {self.username}')

vamsi = Instagram('vamsi','vamsi@123')

'''

class Instagram:
    def __int__(self,username,password):
        self.username = username
        self.__password = password
        self.followers = []
    def getpassword(self):
        return self.__password
    def setpassword(self,newpassword):
        self.__password = newpassword

vamsi = Instagram('vamsi','vamsi@123')

print("Before username",vamsi.username)
vamsi.praneeth = 'praneeth'
print("After username:",vamsi.username)

print("Before password:",vamsi.getpassword())
vamsi.setpassword('praneeth@123')
print("After password:",vamsi.getpassword())






























