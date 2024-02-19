from Magazine import Magazine

class Gun:
    def __init__(self,):
        self.magazine = Magazine()



    def load(self, bullets):
        self.magazine.append(bullets)

    def number_of_bullets(self):
        return self.magazine

    def shoot(self):
        self.magazine.pop()






