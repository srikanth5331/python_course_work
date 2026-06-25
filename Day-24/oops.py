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

'''
'''

class Instagram:
    def __init__(self):
        self._post = []
    @property
    def accesspost(self):
        return self._post

    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)

dinesh = Instagram()
print(dinesh.accesspost)
dinesh.accesspost = 'class and object'
print(dinesh.accesspost)

'''

'''
class whatsappv1:
    def message(self):
        print("You can send messages to people")

class whatsappv2(whatsappv1):
    def calls(self):
        print("you can do video/audio calls")

srikanth = whatsappv1()
print("v1- srikanth")
srikanth.message()

naresh = whatsappv2()
print("v2 - naresh")
naresh.message()
naresh.calls()

'''

'''
class whatsappv1:
    def message(self):
        print("You can send messages to people")

class whatsappv2:
    def calls(self):
        print("you can do video/audio calls")

class whatsappv3:
    def media(self):
        print("you can share your photos/videos")

class whatsappv4(whatsappv1,whatsappv2,whatsappv3):
    def status(self):
        print("you can share status-[24 hours]")

srikanth = whatsappv4()
print("v1- srikanth")
srikanth.message()
srikanth.calls()
srikanth.media()
srikanth.status()

'''

'''
class whatsappv1:
    def message(self):
        print("You can send messages to people")

class whatsappv2(whatsappv1):
    def emojis(self):
        print("you can send messages with emojis to people")

class whatsappv3(whatsappv1):
    def stickers(self):
      print("you can send messages with emojis to people")

srikanth = whatsappv3()
print("v3")
srikanth.stickers()
srikanth.messages()


srikanth = whatsappv2()
print("v2")
srikanth.emojis()
srikanth.messages()
'''

'''
class wpv1:
    def status(self):
        print("You can upload images/videos")
class wpv2(wpv1):
    def status(self):
        super().status()
        print("You can react and reply")

class wpv3(wpv2):
    def status(self):
        super().status()
        print("You can like and reshare")

sahith = wpv3()
sahith.status()
'''

class wpv1:
    def status(self):
        print("You can upload images/videos")
class wpv2(wpv1):
    def status(self):
        super().status()
        print("You can react and reply")

class wpv3(wpv2,wpv1):
    def status(self):
        wpv1.status(self)
        wpv2.status(self)
        print("You can like and reshare")

sahith = wpv3()
sahith.status()





























