#coding: utf-8
import tkinter as tk
import tkinter.font as tkFont
from time import sleep
from PIL import ImageTk, Image


################################################################################
# class graphicObject
################################################################################
class graphicObject():
    def __init__(self, num, x, y, col):
        self.num = num
        self.x = x
        self.y = y
        self.col = col


################################################################################
# classe Canevas
################################################################################
class Canevas(tk.Canvas):
    def __init__(self, master, largeur,hauteur):
        tk.Canvas.__init__(self, master, width=largeur, height=hauteur, bg="black", confine=True)
# attributs
        self.master = master #The window host the canvas 
        self.img = {} #To store the images otherwise they are garbagecollected as soon as they are created lol
#         self.obj = {}
        self.lastkey = None #Last Key Down
        self.lastclic = None #Last Click down
        self.lastpos = 0,0 #Last pos mouse

# bindings
        self.bind_all("<Key>", self.eventKeyboard)
        self.bind("<Button-1>", self.eventRightClick)
        self.bind("<Button-3>", self.eventLeftClick)
        self.bind("<Motion>", self.eventMoveMouse)
        self.pack()

################################################################################
# CREATE OBJECT
################################################################################

    def postText(self, txt, x, y, col="white", sizefont=18):
        font = tkFont.Font(family='Helvetica', size=sizefont, weight='normal')
        return graphicObject(self.create_text(x,y,fill=col, text=txt, font=font), x, y, col)

    def drawRectangle(self, x, y, l, h, col):
        return graphicObject(self.create_rectangle(x, y, x+l, y+h, fill=col, width=0), x, y, col)

    def drawLine(self, x, y, x2, y2, col):
        return graphicObject(self.create_line(x, y, x2, y2, fill=col), x, y, col)

    def drawCircle(self, x, y, r, col):
        return graphicObject(self.create_oval(x-r, y-r, x+r, y+r, width=1, outline=col), x, y, col)

    def drawDisc(self, x, y, r, col):
        return graphicObject(self.create_oval(x-r, y-r, x+r, y+r, width=0, fill=col), x, y, col)

    def postImage(self, x, y, filename):
        image = Image.open(filename)
        if not image:
            print("Eror: postImage",filename,": incorrect file")
            return
        img = ImageTk.PhotoImage(image)
        self.img[img] = True
        self.create_rectangle(x, y, x+img.width()-1, y+img.height()-1, outline='')
        return graphicObject(self.create_image(x, y, image=img, anchor="nw"), x, y, None)

################################################################################
# MODIFIERS
################################################################################
    def moveOn(self, obj, x, y):
        obj.x += x
        obj.y += y
        self.move(obj.num,x,y)

    def destroy(self, obj):
        self.delete(obj.num)
        obj = None

    def changeColor(self, obj, col):
        obj.col = col
        self.itemconfigure(obj.num, fill=col)

    def changeText(self, obj, txt):
        self.itemconfigure(obj.num, text=txt)

################################################################################
# EVENTS
################################################################################
    def eventLeftClick(self, event):
#         if event!=self.lastclic:
#             print("Mouse", event)
            self.lastclic = event

    def eventRightClick(self, event):
#         if event!=self.lastclic:
#             print("Mouse", event)
            self.lastclic = event

    def eventKeyboard(self, event):
#         if event.keysym != self.lastkey:
#             print("Keyboard",event.keysym)#event, event.char)
            self.lastkey=event.keysym

    def eventMoveMouse(self, event):
#         print("Move",event)#event, event.char)
        self.lastpos=(event.x, event.y)

    def keyDown(self):
#         print(self.lastkey)
        self.master.focus_force()
        self.update()
        touche = self.lastkey
        self.lastkey = None
        return touche

    def waitKey(self):
        touche = None
        while touche == None:
            self.pause(0.1)
            touche = self.keyDown()
        return touche

    def clickOn(self):
        self.master.focus_force()
        self.update()
        clic = self.lastclic
        self.lastclic = None
        return clic

    def waitClick(self):
        clic = None
        while clic==None:
            self.pause(0.1)
            clic = self.clickOn()
        return clic

    def givePos(self):
        self.master.focus_force()
        self.update()
        posx,posy = self.lastpos[0],self.lastpos[1]
        return posx,posy

################################################################################
# OTHER FUNCTIONS
################################################################################
    def updateStage(self):
        self.update()

    def closeWindow(self):
        self.master.destroy()



def openWindow(x=400, y=200):
    racine = tk.Tk()
    #racine.protocol("WM_DELETE_WINDOW", qtk.quad.master.destroy)
    g = Canevas(racine, x, y)
#     tk.mainloop()
    return g




if __name__ == '__main__':
    openWindow()
    tk.mainloop()
