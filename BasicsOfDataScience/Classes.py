class Laptop:
    # ram='8gb'
    # hardisk='500 gb'
    # screen='ips display'
    # resolution='4k'
    
    def __init__(self, brd, ram, hdd, resolution, space):#constructur
        self.brand = brd
        self.ram = ram
        self.hdd = hdd
        self.res = resolution
        self.space = space

    def playGame(self):
        if self.ram > 8:
            print('Laptop plays games')
        else:
            print('Not Sufficient RAM')

    def playvideo(self):
        print('laptop play videos')

# lappy = laptop()

# lappy.playgame()

# print(lappy.ram)

mylappy = Laptop('ASUS', 8, '1 TB', '1080p', 124)

print(mylappy.brand)
mylappy.playGame()

mylappy2 = Laptop('HP', 16, '2TB', '720p', 450)

print(mylappy2.hdd)
mylappy2.playGame()
print(mylappy2.space)
