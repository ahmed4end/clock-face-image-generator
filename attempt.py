from PIL import Image 
from random import randint

class Clock():
    def __init__(self, h, m, txt=True) -> None:
        self.clock_face = Image.open(f'./assets/clock/{"face" if txt else "face_nt"}.png')
        self.hour_hand = Image.open('./assets/clock/hr.png')
        self.hour_hand = self.hour_hand.rotate(-h*30-int(m/60*30), resample=Image.BICUBIC)
        self.minute_hand = Image.open('./assets/clock/min.png')
        self.minute_hand = self.minute_hand.rotate(-m*6, resample=Image.BICUBIC)
    def face(self):
        self.clock_face.paste(self.hour_hand, (0,0), mask=self.hour_hand)
        self.clock_face.paste(self.minute_hand, (0,0), mask=self.minute_hand)
        return self.clock_face

if __name__=='__main__':
    Clock(12, 15).face().show()
