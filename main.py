from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
import random


class Karra(App):
    savol = StringProperty("")
    natija = StringProperty("")
    ball = StringProperty("Ball: 0")

    def build(self):
        self.togri = 0
        self.yangi_savol()
        return Builder.load_file("karra.kv")

    def yangi_savol(self):
        self.a = random.randint(2, 9)
        self.b = random.randint(2, 9)
        self.savol = f"{self.a} × {self.b} = ?"
        self.natija = ""

    def tekshir(self, javob):
        try:
            if int(javob) == self.a * self.b:
                self.togri += 1
                self.natija = "✅ To'g'ri!"
            else:
                self.natija = f"❌ Xato! Javob: {self.a * self.b}"

            self.ball = f"Ball: {self.togri}"
            self.yangi_savol()

        except:
            self.natija = "Son kiriting!"


Karra().run()