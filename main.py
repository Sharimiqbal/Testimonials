from customtkinter import *
from PIL import Image

SLIDINGTIME = 2   # seconds
set_appearance_mode("light")
set_default_color_theme("green")

class Animation:

    def __init__(self, win, autoAnimFunc):
        self.win = win
        self.frame1 = None
        self.frame2 = None
        self.loop = None
        self.autoAnimFunc = autoAnimFunc
        self.autoAnimation = self.win.after(2000, self.autoAnimFunc)
        self.x = 700

    def start(self, frame1, frame2, dif):
        if self.autoAnimation is not None:
            self.win.after_cancel(self.autoAnimation)
        self.frame1 = frame1
        self.frame2 = frame2

        def animator():
            if 0 <= self.x<=1400:                
                self.frame1.place(x=self.x - 700, y=0)
                self.frame2.place(x=self.x if dif == 10 else self.x - 1400, y=0)
                self.x -= dif
                self.loop = self.win.after(5, animator)
            else:
                root.after_cancel(self.loop)
                self.x = 700
                self.autoAnimation = self.win.after(SLIDINGTIME*1000, self.autoAnimFunc)
                self.stop()

        animator()
            

    def stop(self):

        if self.frame1 is not None:
            self.frame1.place_forget()
            self.frame2.place(x=0, y=0)

class Item(CTkFrame):
    
    def __init__(self, win, msg, name, photoPath="./Images/user.png"):

        super().__init__(master=win, width=700, height=350, fg_color="#D6E4E5")
        self.name = name
        quotesImg = CTkImage(Image.open("./Images/quote.png"), size=(30, 30))

        CTkLabel(self, text='', image=quotesImg).place(x=50, y=30)
        CTkLabel(self, text=self.__format_msg(msg), font=CTkFont("Comic Sans MS", 16, "normal")).place(x=90, y=60)
        imageICON = CTkImage(Image.open(photoPath), size=(30, 30))
        CTkLabel(self, text="  "+name, image=imageICON, compound="left").place(x=300, y=300)

    def __format_msg(self, msg):

        msg = msg.replace('\n', '').strip().split()
        newMsg = ""
        for i in msg:
            s = newMsg.split("\n")[-1]
            if len(s) + len(i) > 80:
                newMsg += "\n" + i + " "
            else:
                newMsg += i + " "
            
            if len(newMsg) >= 700:
                return newMsg

        return newMsg
        

class Testimonials:

    def __init__(self, win):

        self.items = []
        self.win = win
        leftArrow = CTkImage(Image.open('./Images/left-arrow.png'), size=(64, 64))
        leftArrowTP = CTkImage(Image.open('./Images/left-arrow TP.png'), size=(64, 64))

        rightArrow = CTkImage(Image.open('./Images/right-arrow.png'), size=(64, 64))
        rightArrowTP = CTkImage(Image.open('./Images/right-arrow TP.png'), size=(64, 64))

        self.right = CTkLabel(master=win, text='', image=rightArrowTP, cursor="hand2")
        self.left = CTkLabel(master=win, text='',  image=leftArrowTP, cursor="hand2")

        self.right.place(x=815, y=175)
        self.left.place(x=25, y=175)

        self.right.bind("<Button-1>", self.toRight)
        self.left.bind("<Button-1>", self.toLeft)
        
        self.right.bind("<Enter>", lambda e: self.right.configure(image=rightArrow))
        self.right.bind("<Leave>", lambda e: self.right.configure(image=rightArrowTP))
        self.left.bind("<Enter>", lambda e: self.left.configure(image=leftArrow))
        self.left.bind("<Leave>", lambda e: self.left.configure(image=leftArrowTP))
    
    def add_item(self, item):
        self.items.append(item)

    def start(self):
        self.animation = Animation(self.win, self.toRight)
        self.items[0].place(x=0, y=0)

    def toRight(self, e=None):
        self.animation.stop()
        self.animation.start(self.items[0], self.items[1], 10)
        self.items = self.items[1:] + self.items[:1]

    def toLeft(self, e=None):
        self.animation.stop()
        self.animation.start(self.items[0], self.items[-1], -10)
        self.items = self.items[-1:] + self.items[:-1]



root = CTk()
root.geometry("900x450")
root.resizable(False, False)

frame = CTkFrame(master=root, width=700, height=350)
frame.place(x=100, y=50)


testimonials = Testimonials(root)
testimonials.add_item(Item(frame, msg="""Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                                         Id ipsa odit veniam aspernatur nobis voluptates ipsum quasi 
                                         velit, enim porro atque quos ea iusto deleniti ducimus distinctio 
                                         nihil possimus minima. Nam, illo maiores cum, alias soluta beatae 
                                         nihil fugiat ut incidunt laborum ab. Corporis omnis, recusandae 
                                         dolorum doloribus repellendus eligendi.""", 
                                  name="Codester_09", 
                                  photoPath="./Images/man1.png"))

testimonials.add_item(Item(frame, msg="""Lorem ipsum dolor sit amet consectetur adipisicing elit. Error, 
                                        esse sed fugiat harum laudantium quaerat laborum corrupti consectetur 
                                        ad omnis repellat inventore quia libero ex magnam dignissimos ea voluptatum 
                                        officia perferendis adipisci aliquid odit soluta voluptatibus. Quos, corrupti 
                                        dicta ex, saepe numquam esse minus qui iure, quo provident eum sit!""", 
                                  name="fakeUser", 
                                  photoPath="./Images/man2.png"))

testimonials.add_item(Item(frame, """Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                                     A veritatis, quos adipisci hic quia sequi corporis non veniam, eveniet voluptates repellendus nisi tenetur? Labore vel eaque voluptatem ipsum corrupti nobis illum, ullam est aliquam ut laudantium alias iure doloremque voluptatibus ipsa repudiandae sunt eligendi incidunt, vitae magni? Enim, mollitia possimus?""", "Fake_09", photoPath="./Images/man3.png", ))

testimonials.add_item(Item(frame, msg="""Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                                         Debitis sint tempora, illo nisi error mollitia. Eius architecto, ad quibusdam non voluptate saepe iure cumque ratione dignissimos mollitia commodi quo rerum?""", 
                                  name="userNotFound",  
                                  photoPath="./Images/men4.png"))

testimonials.add_item(Item(frame, msg="""Lorem, ipsum dolor sit amet consectetLorem, ipsum dLorem, 
                                     ipsum dolor sit amet consectetur adipisicing elit. Neque suscipit perspiciatis et repellendus ipsum, earum perferendis ab, nihil molestiae error esse blanditiis excepturi odio iste nam fugiat eum nobis rerum temporibus minima sapiente illum expedita. Hic sit voluptate inventore unde ad laudantium sapiente placeat, voluptas nisi. Accusamus vero enim odit!Lorem, ipsum dolor sit amet consectetur adipisicing elit. Neque suscipit perspiciatis et repellendus ipsum, earum perferendis ab, nihil molestiae error esse blanditiis excepturi odio iste nam fugiat eum nobis rerum temporibus minima sapiente illum expedita. Hic sit voluptate inventore unde ad laudantium sapiente placeat, voluptas nisi. Accusamus vero enim odit!olor sit amet consectetur adipisicing elit. Neque suscipit perspiciatis et repellendus ipsum, earum perferendis ab, nihil molestiae error esse blanditiis excepturi odio iste nam fugiat eum nobis rerum temporibus minima sapiente illum expedita. Hic sit voluptate inventore unde ad laudantium sapiente placeat, voluptas nisi. Accusamus vero enim odit!ur adipisicing elit. Neque suscipit perspiciatis et repellendus ipsum, earum perferendis ab, nihil molestiae error esse blanditiis excepturi odio iste nam fugiat eum nobis rerum temporibus minima sapiente illum expedita. Hic sit voluptate inventore unde ad laudantium sapiente placeat, voluptas nisi. Accusamus vero enim odit!""", 
                                  name="notUser_09"))
testimonials.start()



root.mainloop()