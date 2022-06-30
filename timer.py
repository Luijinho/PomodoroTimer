import datetime
from doctest import testfile
import tkinter
from tkinter import messagebox, Label, Entry, Button

window = tkinter.Tk()
window.title("Pomodoro Timer")
window.geometry('400x650')

def checkValues():
    try:
        studySeconds = int(studyTime.get()) * 60
        breakSeconds = int(breakTime.get()) * 60
    except:
        messagebox.showwarning('', 'Invalid Value, insert integers')
    
    if(studySeconds > 0 and breakSeconds > 0):
        startBtn["state"] = "disabled"
        restartBtn["state"] = "active"
        studyTimer(studySeconds, breakSeconds)
    else:
        messagebox.showwarning('', 'Insert values bigger than 0.')

def studyTimer(studySeconds, breakSeconds):
    actualState.config(text = "STUDY TIME")

    global afterValue
    if studySeconds > 0:
        timer = datetime.timedelta(seconds = studySeconds)
        timeLeft.config(text = timer)
        afterValue = window.after(1000, lambda: studyTimer(studySeconds-1, breakSeconds))

    else:
        window.after_cancel(afterValue)
        breakTimer(studySeconds, breakSeconds)
    
def breakTimer(studySeconds, breakSeconds):    
    actualState.config(text = "BREAK TIME")

    global afterValue
    if breakSeconds > 0:
        timer = datetime.timedelta(seconds = breakSeconds)
        timeLeft.config(text = timer)
        afterValue = window.after(1000, lambda: breakTimer(studySeconds, breakSeconds-1))
    else:
        window.after_cancel(afterValue)
        startBtn["state"] = "active"
        restartBtn["state"] = "disabled"
        messagebox.showwarning('', 'End of Pomodoro!')

def restartTimer():
    window.after_cancel(afterValue)
    timeLeft.config(text = '0:00:00')
    actualState.config(text = 'Pomodoro Timer')
    startBtn["state"] = "active"
    restartBtn["state"] = "disabled"

actualState = Label(window, text='Pomodoro Timer', font=('Helvetica', 20), width=30, height=2)
actualState.pack()

timeLeft = Label(window, text='0:00:00', font=('Helvetica', 30), fg='red', width=30, height=4)
timeLeft.pack()

studyLabel = Label(window, text='Study Minutes: ',  width=12, height=1)
studyLabel.pack()
studyTime = Entry(window, width = 20)
studyTime.pack()

breakLabel = Label(window, text='Break Minutes: ',  width=12, height=1)
breakLabel.pack()
breakTime = Entry(window, width = 20)
breakTime.pack()

startBtn = Button(window,text="Start Timer", width=10, height=2, command = checkValues)
startBtn.pack()

restartBtn = Button(window, text="Stop Timer", state= "disabled", width=10, height=2, command = restartTimer )
restartBtn.pack()

window.mainloop()