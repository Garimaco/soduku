
# coding: utf-8

# In[23]:


import numpy as np
from tkinter import*
from tkinter import messagebox
import random
import pickle
box=Tk()
box.title('Soduko 2.0')
box.geometry('250x200')
messagebox.showinfo('Welcome','Welcome to Soduko 2.0')
ask=messagebox.askyesno('Continue','Would you like to continue your last game?')

r00=StringVar()
r01=StringVar()
r02=StringVar()
r03=StringVar()

r10=StringVar()
r11=StringVar()
r12=StringVar()
r13=StringVar()

r20=StringVar()
r21=StringVar()
r22=StringVar()
r23=StringVar()

r30=StringVar()
r31=StringVar()
r32=StringVar()
r33=StringVar()

def contold():
    op=Tk()
    op.title('saving name')
    s=StringVar()
    Label(op,text="Name by which game was saved:").grid(row=1,column=1)
    Entry(op,textvariable=s).grid(row=1,column=2)
    Button(op,text='ok',command=op.destroy).grid(row=2,column=2)
    op.mainloop()
    f=open('game.dat','rb+')
    
    while True:
        try:
            d=pickle.load(f)
            if s.get() in d:
                return d[s.get()]
        except:
            break

l=[[r00,r01,r02,r03],[r10,r11,r12,r13],[r20,r21,r22,r23],[r30,r31,r32,r33]]
if ask:
    game=contold()
    for i in range(4):
        for j in range(4):
            if game[i][j]!=0:
                l[i][j].set(game[i][j])
                
                
else:
    game=np.zeros((4,4),dtype='int')
    game[0][3]=random.randint(1,3) #a
    game[2][0]=random.randint(1,2)#b
    game[1][2]=random.randint(1,3)#c
    game[3][1]=random.randint(3,4)#d
    game[0][0]=random.randint(3,4)#e
    while True:
        if game[2][0]!=game[3][1] and game[0][3]!=game[1][2] and game[0][0]!=game[0][3] and game[0][0]!=game[2][0]:
            break
        else: 
           game[0][3]=random.randint(1,3)
           game[2][0]=random.randint(1,2)
           game[1][2]=random.randint(1,3)
           game[3][1]=random.randint(3,4)
    r00.set(game[0][0])
    r03.set(game[0][3])
    r12.set(game[1][2])
    r20.set(game[2][0])
    r31.set(game[3][1])

"""r1=[e,' ',' ',a]
r2=[' ',' ',c,' ']
r3=[b,' ',' ',' ']
r4=[' ',d,' ',' ']"""

def submit():
    global l
    global game
   
    for i in range(4):
        try:
            for j in range(4):
                if (i==0 and j==0) or (i==0 and j==3) or (i==1 and j==2) or (i==2 and j==0) or (i==3 and j==1):
                    continue     
                else:
                    if int(l[i][j].get()) not in game[i,:4] and int(l[i][j].get()) not in game[:4,j] and int(l[i][j].get())!=0:
                        if (i==0 and j==1) or (i==0 and j==2) or (i==1 and j==0) or (i==3 and j==2) or (i==2 and j==2):
                            if int(l[0][1].get())<int(l[0][0].get()) and int(l[0][2].get())>int(l[1][2].get()) and int(l[1][0].get())>int(l[2][0].get()) and int(l[2][2].get())<int(l[2][3].get()) and int(l[3][1].get())>int(l[3][2].get()):
                                game[i][j]=int(l[i][j].get())
                            else:
                                messagebox.showinfo('error','invalid entry')
                                raise
                        else:
                            game[i][j]=int(l[i][j].get())
                    else:
                        messagebox.showinfo('error','invalid entry')
                        raise

        except:
            break
    else:
        messagebox.showinfo('Congratulations','yaya you win!!')
          
    print(game)

def save():
    global game 
    op=Tk()
    op.title('saving name')
    s=StringVar()
    Label(op,text=" saving name:").grid(row=1,column=1)
    Entry(op,textvariable=s).grid(row=1,column=2)
    Button(op,text='ok',command=op.destroy).grid(row=2,column=2)
    op.mainloop()
    f=open('game.dat','ab+')
    d={}
    d[s.get()]=game
    pickle.dump(d,f)
    
Entry(box,textvariable=r00,width=3,fg='red').grid(row=2,column=2) #e
Entry(box,textvariable=r01,width=3).grid(row=2,column=4)
Entry(box,textvariable=r02,width=3).grid(row=2,column=6)
Entry(box,textvariable=r03,width=3,fg='red').grid(row=2,column=8) #a

Label(box,text='V',fg='blue',font=('arial',10)).grid(row=3,column=6)

Entry(box,textvariable=r10,width=3).grid(row=4,column=2)
Entry(box,textvariable=r11,width=3).grid(row=4,column=4)
Entry(box,textvariable=r12,width=3,fg='red').grid(row=4,column=6) #b
Entry(box,textvariable=r13,width=3).grid(row=4,column=8)

Label(box,text='V',fg='blue',font=('arial',10)).grid(row=5,column=2)

Entry(box,textvariable=r20,width=3,fg='red').grid(row=6,column=2) #c
Entry(box,textvariable=r21,width=3).grid(row=6,column=4)
Entry(box,textvariable=r22,width=3).grid(row=6,column=6)
Entry(box,textvariable=r23,width=3).grid(row=6,column=8)

Label(box,text='<',fg='blue',font=('arial',14)).grid(row=6,column=7)
Label(box,text='>',fg='blue',font=('arial',14)).grid(row=8,column=5)
Label(box,text='>',fg='blue',font=('arial',14)).grid(row=2,column=3)
Label(box,text=' ',fg='blue',font=('arial',9)).grid(row=7,column=3)

Entry(box,textvariable=r30,width=3).grid(row=8,column=2)
Entry(box,textvariable=r31,width=3,fg='red').grid(row=8,column=4) #d
Entry(box,textvariable=r32,width=3).grid(row=8,column=6)
Entry(box,textvariable=r33,width=3).grid(row=8,column=8)


Button(box,text='submit',command=submit).grid(row=12,column=1)            
Button(box,text='save',command=save).grid(row=12,column=4)
Button(box,text='quit',command=box.destroy).grid(row=12,column=9)

box.mainloop()

