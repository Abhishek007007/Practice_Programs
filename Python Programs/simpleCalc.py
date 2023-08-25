import tkinter as tk


lightGray = "#F5F5F5"
labelColour = "#25265E"
smallFontStyle = ("Arial",16)
largeFontStyle = ("Arial",40,"bold")
white = "#FFFFFF"
digitFontStyle = ("Arial",24,"bold")
defaultFontStyle =("Arial",20)
offWhite = "#F8FAFF"
lightBlue = "#CCEDFF"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Simple Calculator")
        self.window.geometry("360x540")
        self.window.resizable(0,0)
        self.totalExpression = ""
        self.currentExpression = ""
       
        self.displayFrame = self.createDisplayFrame()
        self.totalLabel,self.currLabel = self.createDisplayLabels()
        self.digit = {
            7:(1,1),8:(1,2),9:(1,3),
            4:(2,1),5:(2,2),6:(2,3),
            1:(3,1),2:(3,2),3:(3,3),
            '.':(4,1), 0:(4,2)
        }
        self.operators= {
            "/" : "\u00F7", "*" : "\u00D7","-":"-","+":"+"
        }
        self.buttonsFrame= self.createButtonsFrame()

        for x in range(1,5):
            self.buttonsFrame.rowconfigure(x,weight=1)
            self.buttonsFrame.columnconfigure(x,weight=1)
        self.createDigitButtons()
        self.createOperatorButtons()
        self.createSpecialButton()
        self.bindKeys()

    def run(self):
        self.window.mainloop()

    def createDisplayFrame(self):
        frame = tk.Frame(self.window,height=170,bg=lightGray)
        frame.pack(expand=True,fill="both")
        return frame
    
    def createButtonsFrame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True,fill="both")
        return frame
    
    def createDisplayLabels(self):
        totalLabel = tk.Label(self.displayFrame,text = self.totalExpression,anchor=tk.E,bg=lightGray,fg=labelColour,padx=24,font=smallFontStyle)
        totalLabel.pack(expand=True,fill="both")

        Label = tk.Label(self.displayFrame,text = self.currentExpression,anchor=tk.E,bg=lightGray,fg=labelColour,padx=24,font=largeFontStyle)
        Label.pack(expand=True,fill="both")

        return totalLabel,Label
    def createOperatorButtons(self):
        i = 0
        for op,symbol in self.operators.items():
            button = tk.Button(self.buttonsFrame,text=symbol,bg=offWhite,fg=labelColour,font=defaultFontStyle,borderwidth=0,command=lambda x=op:self.appendOp(x))
            button.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1

    def createDigitButtons(self):
        for digit,gridValue in self.digit.items():
            buttons = tk.Button(self.buttonsFrame,text=str(digit),bg=white,fg=labelColour,font=digitFontStyle,borderwidth=0,command= lambda x = digit : self.addToExpression(x))
            buttons.grid(row=gridValue[0],column=gridValue[1],sticky=tk.NSEW)
            
    def clearButton(self):
        button = tk.Button(self.buttonsFrame,text='C',bg=offWhite,fg=labelColour,font=defaultFontStyle,borderwidth=0,command=lambda:self.clear())
        button.grid(row=0,column=1,sticky=tk.NSEW)
    
    def square(self):
        try:
            self.currentExpression = str(eval(f"{self.currentExpression}**2"))
        except:
            self.currentExpression = "Error"
        finally:
            self.updateLabel()

    def createSquareButton(self):
        button = tk.Button(self.buttonsFrame,text='x\u00b2',bg=offWhite,fg=labelColour,font=defaultFontStyle,borderwidth=0,command=lambda:self.square())
        button.grid(row=0,column=2,sticky=tk.NSEW)

    def squareRoot(self):
        try:
            self.currentExpression = str(eval(f"{self.currentExpression}**0.5"))
        except:
            self.currentExpression = "Error"
        finally:
            self.updateLabel()

    def createSquareRootButton(self):
        button = tk.Button(self.buttonsFrame,text='\u221ax',bg=offWhite,fg=labelColour,font=defaultFontStyle,borderwidth=0,command=lambda:self.squareRoot())
        button.grid(row=0,column=3,sticky=tk.NSEW)
    
    
    def equalsButton(self):
        button = tk.Button(self.buttonsFrame,text='=',bg=lightBlue,fg=labelColour,font=defaultFontStyle,borderwidth=0,command=lambda:self.evaluate())
        button.grid(row=4,column=3,columnspan=2,sticky=tk.NSEW)

    def createSpecialButton(self):
        self.clearButton()
        self.equalsButton()
        self.createSquareButton()
        self.createSquareRootButton()
    

    def updateTotalLabel(self):
        expression = self.totalExpression
        for op,symbol in self.operators.items():
            expression = expression.replace(op,symbol)
        self.totalLabel.config(text=expression)

    def updateLabel(self):
        self.currLabel.config(text=self.currentExpression[:10])

    def addToExpression(self,value):
        self.currentExpression += str(value)
        self.updateLabel()

    def appendOp(self,op):
        self.currentExpression += str(op)
        self.totalExpression += self.currentExpression
        self.currentExpression = ""
        self.updateLabel()
        self.updateTotalLabel()

    def clear(self):
        self.totalExpression = ""
        self.currentExpression = ""
        self.updateLabel()
        self.updateTotalLabel()
    def evaluate(self):
        self.totalExpression += self.currentExpression
        self.updateTotalLabel()
        try:
            self.currentExpression = str(eval(self.totalExpression))
            self.totalExpression = ""
        except:
            self.currentExpression = "Error"
        finally:
            self.updateLabel()

    def bindKeys(self):
        self.window.bind("<Return>",lambda event : self.evaluate())
        for key in self.digit:
            self.window.bind(str(key),lambda event,digit=key:self.addToExpression(digit))
        for key in self.operators:
            self.window.bind((key),lambda event,operator=key:self.appendOp(operator))

if __name__ == "__main__":
    calc = Calculator()
    calc.run()