# -*- encoding:utf-8 -*-

from Tkinter import *
from time import *
from datetime import datetime,timedelta

started = datetime.today()
time_events = [
    ("発表残り時間", 10, 30, 'white'),
    ("Discussion残り時間", 3*60-30, 0, 'yellow'),
    ("交代残り時間", 30, 0, 'green'),
]
def total_time(index):
    r = 0
    for i in range(index):
        r += time_events[i][1]
    return r

def reset(index=0):
    global started
    change_color('white')
    started = datetime.today() - timedelta(seconds=total_time(index))

def update_time():
    show_time()
    root.after(50, update_time)

def show_time():
    global root
    global started
    text_time.set(strftime('%Y/%m/%d(%a) %H:%M'))

    t = datetime.today()
    v = t-started

    time_sum = 0
    for te in time_events:
        time_sum += te[1]
        limit = timedelta(seconds=time_sum)
        if v <= limit:
            vv =  limit - v
            text_msg.set(te[0])
            shows = vv.seconds + 1
            minutes = shows / 60
            seconds = shows % 60
            text_lt.set('%01d:%02d'%(minutes,seconds))
            if shows<te[2]:
                change_color('#ff9999')
            else:
                change_color(te[3])
            return
    reset()

root = Tk()
root.option_add('*font', ('FixedSys', 12))
root.title(u'Lightening Timer')
width = 640
height = 480
root.minsize(width, height)

text_time = StringVar()
text_time.set('clock')
text_lt = StringVar()
text_lt.set('timer')
text_msg = StringVar()
text_msg.set('Message')

labels = []
Label(text='基礎修練発表会 タイマー', font=(u'FixedSys',12)).pack()
Label(textvariable = text_time, font=(u'FixedSys',12)).pack()
Label(textvariable = text_msg, font=(u'FixedSys',36)).pack()
Label(textvariable = text_lt, font=(u'FixedSys',200)).pack()

def change_color(color):
    root.configure(bg=color)
    for l in root.winfo_children():
        l.configure(bg=color)

Button(text='発表', command=lambda:reset(0)).pack(side=LEFT,padx=10)
Button(text='Discuss', command=lambda:reset(1)).pack(side=LEFT,padx=10)
Button(text='交代', command=lambda:reset(2)).pack(side=LEFT,padx=10)
Label(text="Powered by 2009年度 基礎修練発表会実行委員会", font=(u'FixedSys',10)).pack(side=BOTTOM)

reset()
update_time()
root.mainloop()
