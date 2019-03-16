from tkinter import *
import random
import string
import sys
from tkinter import messagebox
import math
import sqlite3
import enchant
from PIL import Image
import os
class wuzzle:
    def done1(self):
        finalbox=Tk()
        finalbox.title("final_box")
        finalbox.config(bg="red")
        finalbox.geometry("500x380")
        u1=Label(finalbox,text="Username:",bg="red",fg="white",width=10,height=1)
        u1.config(font=('times',15,'bold'))
        u1.place(x=50,y=30)
        u2=Label(finalbox,text="UserId:",bg="red",fg="white",width=10,height=1)
        u2.config(font=('times',15,'bold'))
        u2.place(x=50,y=70)
        u1_value=Label(finalbox,bg="blue",width=20,height=1,relief=RIDGE)
        u1_value.config(font=('times',15,'bold'))
        u1_value.place(x=190,y=30)
        u2_value=Label(finalbox,bg="blue",width=20,height=1,relief=RIDGE)
        u2_value.config(font=('times',15,'bold'))
        u2_value.place(x=190,y=70)
        u1_value.config(text=str(self.q[0][0]))
        u2_value.config(text=str(self.q[0][1]))
        s1=Label(finalbox,text="Score:",bg="red",fg="white",width=10,height=1)
        s1.config(font=('times',15,'bold'))
        s1.place(x=50,y=110)
        s1_value=Label(finalbox,bg="blue",width=20,height=1,relief=RIDGE)
        s1_value.config(font=('times',15,'bold'))
        s1_value.place(x=190,y=110)
        s2=Label(finalbox,text="Gender:",bg="red",fg="white",width=10,height=1)
        s2.config(font=('times',15,'bold'))
        s2.place(x=50,y=150)
        s2_value=Label(finalbox,bg="blue",width=20,height=1,relief=RIDGE)
        s2_value.config(font=('times',15,'bold'))
        s2_value.place(x=190,y=150)
        s3=Label(finalbox,text="Words made:",bg="red",fg="white",width=10,height=1)
        s3.config(font=('times',15,'bold'))
        s3.place(x=50,y=190)
        s3_value=Label(finalbox,bg="blue",width=20,height=1,relief=RIDGE)
        s3_value.config(font=('times',15,'bold'))
        s3_value.place(x=190,y=190)
        s4=Label(finalbox,text="Level:",bg="red",fg="white",width=10,height=1)
        s4.config(font=('times',15,'bold'))
        s4.place(x=50,y=230)
        s4_value=Label(finalbox,bg="blue",width=20,height=1,relief=RIDGE)
        s4_value.config(font=('times',15,'bold'))
        s4_value.place(x=190,y=230)
        s2_value.config(text=str(self.q[0][6]))
        s3_value.config(text=len(self.wordmadelist))
        s4_value.config(text=self.it.get())
        labellast=Label(finalbox,text="!!!YOUR DATA IS RECORDED SUCCESSFULLY!!!",width=50,bg="blue",fg="white")
        labellast.config(font=('courier',13,'bold'))
        labellast.place(x=0,y=0)
        labellast=Label(finalbox,text="HOPE YOU ENJOYED PLAYING, THANK U!!!!!",bg="blue",fg="white")
        labellast.config(font=('courier',13,'bold'))
        labellast.place(x=50,y=280)
        con=sqlite3.connect("wuzzle.db")
        sco=self.total_score
        print([sco])
        sc=[sco]
        con.execute("update wuzzle set score=(?) where Userid='"+str(self.q[0][1])+"'",(sc))
        con.commit()   
        s1_value.config(text=sc)
        def newblock():
            for i in range(self.box):
                for j in range(self.box):
                    self.b[i][j].destroy()
                    self.r[i][j].destroy()
            self.b.clear()
            self.r.clear()
            self.root.destroy()
            finalbox.destroy()
            self.game()
        def quitlast():
            self.root.destroy()
            finalbox.destroy()        
        remove1=Button(finalbox,text="Quit",bg="white",fg="blue",width=20,height=1,activebackground="red",command=quitlast)
        remove1.place(x=80,y=330)
        b1=Button(finalbox,text="Play Again",bg="white",width=20,height=1,activebackground="green",command=newblock)   
        b1.place(x=290,y=330)
#============================================================================================================================================================
    def game(self):
        self.root=Tk()
        self.root.title("Wuzzle")
        self.root.config(bg="orange")
        if(self.it.get()==self.droplist[0]):
             self.root.geometry("1175x730")
        if(self.it.get()==self.droplist[1]):
             self.root.geometry("1175x750")
        if(self.it.get()==self.droplist[2]):
             self.root.geometry("1220x770")
        if(self.it.get()==self.droplist[3]):
             self.root.geometry("1310x760")    
        note=Label(self.root,bg='black',text="NOTE: information regarding this block will be updated here",fg="white",width=56,height=2)
        l0=Label(self.root,text="Word:",bg="orange",width=12,height=1)
        l0.config(font=('times',20,'bold'))
        word_label=Label(self.root,bg='white',width=40,height=1,relief=RIDGE)
        swapallowance=[]
        border=Label(self.root,bg="red",height=57)
        player=Label(self.root,text="Player:",bg="crimson",width=12,height=1,relief=RIDGE)
        player.config(font=("times",16,"bold"))
        playername=Label(self.root,bg="crimson",width=13,height=1,relief=RIDGE)
        playername.config(font=("times",16,"bold"))
        playername.config(text=str(self.q[0][0]))
        idlab=Label(self.root,text="Player ID:",bg="crimson",width=12,height=1,relief=RIDGE)
        idlab.config(font=("times",16,"bold"))
        idname=Label(self.root,bg="crimson",width=13,height=1,relief=RIDGE)
        idname.config(font=("times",16,"bold"))
        idname.config(text=str(self.q[0][1]))  
        levellab=Label(self.root,text="Level:",bg="crimson",width=12,height=1,relief=RIDGE)
        levellab.config(font=("times",16,"bold"))
        levelval=Label(self.root,bg="crimson",width=13,height=1,relief=RIDGE)
        levelval.config(font=("times",16,"bold"))
        levelval.config(text=self.it.get())
        def infobox():
            myimage=Image.open("direct1.png")
            myimage.show()
        inforouter=Button(self.root,text="DIRECTION'S FOR MAKING A WORD",bg="cyan",width=35,height=1,command=infobox)
        inforouter.config(fon=("times",14,"bold"))
        def functions(self,i,j):
            print("r[i][j]= ",self.r[i][j])
            if(len(self.text)!=0):
                print(self.text)
                op=0
                for self.text[op] in self.text:
                    self.text[0]["bg"]="blue"
                self.text.clear()
                self.text1.clear()
                self.word_list.clear()
            word_label.config(text="")
            def index_finder(swapallowance,g):
                for i,x in enumerate(self.r):
                    if g in x:
                        return(i,x.index(g))
            print("positions: ")
            y=True
            z=True
            try:
                self.r[i+1][j] not in self.r
            except:
                print("r[i+1][j] does not exists")
                y=False
            try:
                self.r[i][j+1] not in self.r
            except:
                print("r[i][j+1] does not exists")
                z=False
            p1=index_finder(swapallowance,self.r[i][j])
            p2=index_finder(swapallowance,self.r[i-1][j])
            if(y is False):
                print("r[i+1][j] does not exists")
            else:
                p3=index_finder(swapallowance,self.r[i+1][j])
            if(z is False):
                print("r[i][j+1] does not exists")
            else:
                p4=index_finder(swapallowance,self.r[i][j+1])
            p5=index_finder(swapallowance,self.r[i][j-1])
            print("r[i][j]: ",p1)
            print("r[i-1][j]: ",p2)
            if(y is False):
                pass
            else:
                print("r[i+1][j]: ",p3)
            if(z is False):
                pass
            else:
                print("r[i][j+1]: ",p4)
            print("r[i][j-1]: ",p5)
            if(p1[1] is 0):
                v=self.r[i][j-1]
                print("v = ",v["text"])
                self.r[i][j-1]=0  
            if(p1[0] is 0):
                m=self.r[i-1][j]
                print("m = ",m["text"])
                self.r[i-1][j]=0
            if(y is False):
                self.mainright=0
            else:    
                self.mainright=self.r[i+1][j]
            if(z is False):
                self.maindown=0
            else:
                self.maindown=self.r[i][j+1]
            self.main=self.r[i][j]    
            self.mainup=self.r[i][j-1]    
            self.mainleft=self.r[i-1][j]    
            print("main: ",self.main)
            print("mainup: ",self.mainup)
            print("maindown: ",self.maindown)
            print("mainleft: ",self.mainleft)
            print("mainright: ",self.mainright)
            if(len(self.whitelist)!=0):
                if(self.r[i][j] is not self.whitelist[0] or self.r[i][j] is self.whitelist[0]):
                    self.whitelist[0]["bg"]="blue"
                    self.whitelist[0]["relief"]=RAISED
                    self.whitelist.clear()
            else:
                print("whitelist is empty")
            if(len(swapallowance)!=0):
                counter=1
                counter+=1
            else:
                counter=0
                counter+=1
            print("counter value= ",counter)    
            def call_possible(self,i,j):
                print("r[i][j] in call_possible= ",self.r[i][j])
                self.r[i][j]["relief"]=RAISED                            # or RIDGE
                if(len(swapallowance)==0):
                    swapallowance.append(self.main)
                    swapallowance.append(self.mainup)
                    swapallowance.append(self.maindown)
                    swapallowance.append(self.mainleft)
                    swapallowance.append(self.mainright)
                    print("values in swapallowance")
                    print("swapallowance= ",swapallowance)
                print("text")
                print("main= ",self.main["text"])
                if(self.mainup!=0):
                    print(self.mainup["text"])
                if(self.mainleft!=0):
                    print(self.mainleft["text"])
                if(self.maindown!=0):
                    print(self.maindown["text"])
                if(self.mainright!=0):
                    print(self.mainright["text"])
                self.main["bg"]="green"
                if(self.mainup!=0):
                    self.mainup["bg"]="green"
                    self.mainup["relief"]=SUNKEN
                    a1=self.mainup["text"]
                else:
                    a1="--"
                if(self.maindown!=0):    
                    self.maindown["bg"]="green"
                    self.maindown["relief"]=SUNKEN
                    a2=self.maindown["text"]
                else:
                    a2="--"  
                if(self.mainleft!=0):
                    self.mainleft["bg"]="green"
                    self.mainleft["relief"]=SUNKEN
                    a3=self.mainleft["text"]
                else:
                    a3="--"  
                if(self.mainright!=0):
                    self.mainright["bg"]="green"
                    self.mainright["relief"]=SUNKEN 
                    a4=self.mainright["text"]
                else:
                    a4="--"  
                note.config(text="Command Swap\n'"+self.main["text"]+"' can be swaped to: '"+a1+"','"+a2+"','"+a3+"','"+a4+"'")
                if(p1[1] is 0):
                    self.r[i][j-1]=v
                    print("v= ",v)
                if(p1[0] is 0):
                    self.r[i-1][j]=m
                    print("m= ",m)
            def delcall_possibleandswap(self,swapallowance,i,j):
                print("r[i][j] in deleteand swap fun.= ",self.r[i][j]["text"])
                if(self.r[i][j] in swapallowance):
                    swapvar1_value=swapallowance[0]["text"]
                    swapvar2_value=self.r[i][j]["text"]
                    swapvar1=swapallowance[0]
                    swapvar2=self.r[i][j]
                    print("swapvar1_value: ",swapvar1_value)
                    print("swapvar2_value: ",swapvar2_value)
                    def indexfinder(mylist, a):
                        for sub_list in mylist:
                            if a in sub_list:
                                return (mylist.index(sub_list), sub_list.index(a))
                    x=index_finder(self.r,swapvar1)
                    print("index value of 1'nd clicked button swapallowance[0]: ",x)
                    print(x[0])
                    print(x[1])
                    y=index_finder(self.r,swapvar2)
                    print("index value of 2'st clicked button r[i][j]: ",y)
                    print(y[0])
                    print(y[1])
                    print("before swap")
                    print("in r: ",self.r[x[0]][x[1]]["text"])
                    print("in r: ",self.r[y[0]][y[1]]["text"])
                    self.r[x[0]][x[1]]["text"]=swapvar2_value
                    self.r[y[0]][y[1]]["text"]=swapvar1_value
                    print("after swap")
                    print("in r: ",self.r[x[0]][x[1]]["text"])
                    print("in r: ",self.r[y[0]][y[1]]["text"])
                    note.config(text="swap done for: '"+self.r[y[0]][y[1]]["text"]+"','"+self.r[x[0]][x[1]]["text"]+"'--->'"+self.r[x[0]][x[1]]["text"]+"','"+self.r[y[0]][y[1]]["text"]+"'")
                    op=0
                    for swapallowance[op] in swapallowance:
                        if(swapallowance[op]!=0):
                            swapallowance[op]["bg"]="blue"
                            swapallowance[op]["relief"]=RAISED
                    swapallowance.clear()         
                    self.whitelist.append(self.r[i][j])
                    self.whitelist[0]["bg"]="white"
                    self.whitelist[0]["relief"]=RIDGE
                    print("whitelist= ",self.whitelist)
                    if(p1[1] is 0):
                        self.r[i][j-1]=v
                        print("v= ",v)
                    if(p1[0] is 0):
                        self.r[i-1][j]=m
                        print("m= ",m)    
                else:
                    #Update swapallowance
                    op=0
                    for swapallowance[op] in swapallowance:
                        if(swapallowance[op]!=0):
                            swapallowance[0]["bg"]="blue"
                            swapallowance[0]["relief"]=RAISED
                    swapallowance.clear()        
                    call_possible(self,i,j)
            if (counter==1):
                call_possible(self,i,j)
            if(counter==2):
                delcall_possibleandswap(self,swapallowance,i,j)
    
        def makemyword(self,swapallowance,i,j):
            m=self.r[i][j]
            def index_finderinwordmake(g):
                for i,x in enumerate(self.r):
                    if g in x:
                        return(i,x.index(g))
            q1=index_finderinwordmake(m)
            if(q1[1] is 0):
                h=self.r[i][j-1]
                self.r[i][j-1]=0  
            if(q1[0] is 0):
                p=self.r[i-1][j]
                self.r[i-1][j]=0
            print("coordinates of r[i][j]",q1)
            a=True
            b=True
            c=True
            d=True
            e=True
            f=True
            try:
                self.r[i+1][j] not in self.r
            except:
                print("r[i+1][j] does not exists")
                a=False
            try:
                self.r[i][j+1] not in self.r
            except:
                print("r[i][j+1] does not exists")
                b=False
            try:
                self.r[i+1][j+1] not in self.r
            except:
                print("r[i+1][j+1] does not exists")
                c=False
            try:
                self.r[i-1][j-1] not in self.r
            except:
                print("r[i-1][j-1] does not exists")
                d=False
            try:
                self.r[i+1][j-1] not in self.r
            except:
                print("r[i+1][j-1] does not exists")
                e=False
            try:
                self.r[i-1][j+1] not in self.r
            except:
                print("r[i-1][j+1] does not exists")
                f=False    
            if(a is False):
                up=0
            else:
                up=self.r[i+1][j]
            if(b is False):
                right=0
            else:
                right=self.r[i][j+1]
            if(c is False):
                plus2=0
            else:
                plus2=self.r[i+1][j+1]
            if(d is False):
                sub2=0
            else:
                sub2=self.r[i-1][j-1]
            if(e is False):
                plussub=0
            else:
                plussub=self.r[i+1][j-1]
            if(f is False):
                subplus=0
            else:
                subplus=self.r[i-1][j+1]
            down=self.r[i-1][j]
            left=self.r[i][j-1]
            
            if(len(self.whitelist)!=0):
                if(self.r[i][j] is not self.whitelist[0] or self.r[i][j] is self.whitelist[0]):
                    self.whitelist[0]["bg"]="blue"
                    self.whitelist[0]["relief"]=RAISED
                    self.whitelist.clear()
            else:
                print("whitelist is empty")     
                self.r[i][j]["relief"]=RAISED
            if(len(self.word_list)==0):
                count=0
                count+=1
            else:
                count=1
                count+=1
            print("count value= ",count) 
            if(len(self.text)!=0):
                if(self.r[i][j] in self.text):
                    self.text.append(self.r[i][j])
                    messagebox.showwarning('note','You have pressed the same button')
                    op=0
                    for self.text[op] in self.text:
                        self.text[op]["bg"]="blue"
                    self.text.clear()
                    self.word_list.clear()
                    self.text1.clear()
                    word_label.config(text="")
            def labelupdate(self,i,j):
                letter=self.r[i][j]["text"]
                if(letter==""):
                    messagebox.showwarning('note','text in the button does not exists cannot make the word')
                    op=0
                    for self.text[op] in self.text:
                        self.text[0]["bg"]="blue"
                    self.text.clear()
                    self.text1.clear()
                    word_label.config(text="")
                    print("letter= ",letter)
                    self.word_list.clear()
                else:
                    self.text1.append(letter)
                    print("values in text1: ",self.text1)
                    word_label.config(text=self.text1)
                    note.config(text="COMMAND:- Make word\n Selected'"+letter+"'")
                if(q1[1] is 0):
                    self.r[i][j-1]=h
                    print("h= ",h)
                if(q1[0] is 0):
                    self.r[i-1][j]=p
                    print("p= ",p)    
            def counter1(self,swapallowance):
                if(len(swapallowance)!=0):
                    swapallowance[0]["bg"]="blue"
                    swapallowance[0]["relief"]=RAISED
                    if(self.mainup!=0):
                        swapallowance[1]["bg"]="blue"
                        swapallowance[1]["relief"]=RAISED
                    if(self.maindown!=0):
                        swapallowance[2]["bg"]="blue"
                        swapallowance[2]["relief"]=RAISED
                    if(self.mainleft!=0):
                        swapallowance[3]["bg"]="blue"
                        swapallowance[3]["relief"]=RAISED
                    if(self.mainright!=0):
                        swapallowance[4]["bg"]="blue"
                        swapallowance[4]["relief"]=RAISED
                    print("values in swapallowance")
                    print(swapallowance)
                    swapallowance.clear()
                    print("value in swapallowance")
                    print(swapallowance)
                self.r[i][j]["bg"]="crimson" 
                self.text.append(self.r[i][j])
                print("length of text: ",len(self.text))
                print("text= ",self.text)
                self.word_list.append(m)
                self.word_list.append(up)
                self.word_list.append(down)
                self.word_list.append(right)
                self.word_list.append(left)
                self.word_list.append(plus2)
                self.word_list.append(sub2)
                self.word_list.append(plussub)
                self.word_list.append(subplus)
                labelupdate(self,i,j)
                print("word_list:= ",self.word_list)
                print("word_list: ",m,up,down,left,right,plus2,sub2,plussub,subplus)

            def counter2(self):
                print("wordlist:- ",self.word_list)
                print("r[i][j]= ",self.r[i][j]["text"])
                print("r[i][j]= ",self.r[i][j])
                print("up: ",up)
                print("down: ",down)
                print("left: ",left)
                print("right: ",right)
                print("plus2: ",plus2)
                print("sub2: ",sub2)
                print("plussub: ",plussub)
                print("subplus: ",subplus)
                if(up==0):
                    u=0
                else:
                    u=up["text"]
                if(down==0):
                    d=0
                else:
                    d=down["text"]
                if(left==0):
                    l=0
                else:
                    l=left["text"]
                if(right==0):
                    r=0
                else:
                    r=right["text"]
                if(plus2==0):
                    plus=0
                else:
                    plus=plus2["text"]
                if(sub2==0):
                    sub=0
                else:
                    sub=sub2["text"]
                if(plussub==0):
                    ps=0
                else:
                    ps=plussub["text"]
                if(subplus==0):
                    sp=0
                else:
                    sp=subplus["text"]
                print("up,down plus2,sub2,plussub,subplus",u,d,l,r,plus,sub,ps,sp)
                print("wordlist:- ",self.word_list)
                if(self.r[i][j] in self.word_list and self.r[i][j]!=0):
                    self.r[i][j]["bg"]="crimson"
                    self.text.append(self.r[i][j])
                    print("length of text: ",len(self.text))
                    print("text= ",self.text)
                    if(len(self.text)==2):
                        if(self.r[i][j] is self.word_list[1]):
                            self.word_list.clear()
                            self.word_list.append(up)
                        elif(self.r[i][j] is self.word_list[2]):
                            self.word_list.clear()
                            self.word_list.append(down)
                        elif(self.r[i][j] is self.word_list[3]):
                            self.word_list.clear()
                            self.word_list.append(right)
                        elif(self.r[i][j] is self.word_list[4]):
                            self.word_list.clear()
                            self.word_list.append(left)
                        elif(self.r[i][j] is self.word_list[5]):
                            self.word_list.clear()
                            self.word_list.append(plus2)
                        elif(self.r[i][j] is self.word_list[6]):
                            self.word_list.clear()
                            self.word_list.append(sub2)
                        elif(self.r[i][j] is self.word_list[7]):
                            self.word_list.clear()
                            self.word_list.append(plussub)
                        elif(self.r[i][j] is self.word_list[8]):
                            self.word_list.clear()
                            self.word_list.append(subplus)
                        else: 
                            print("exit len==2")
                        self.lo.clear()    
                        self.lo.append(up)
                        self.lo.append(down)
                        self.lo.append(left)
                        self.lo.append(right)
                        self.lo.append(plus2)
                        self.lo.append(sub2)
                        self.lo.append(plussub)
                        self.lo.append(subplus)
                        print("lo: ",self.lo)
                        print("lo= ",u,d,l,r,plus,sub,ps,sp)
                    else:
                        print("len!=2")
                    print("lo= ",u,d,l,r,plus,sub,ps,sp)    
                    if(len(self.text)>2):
                        if(self.word_list[0] is self.lo[0]):
                            self.word_list.clear()
                            self.word_list.append(up)
                        elif(self.word_list[0] is self.lo[1]):
                            self.word_list.clear()
                            self.word_list.append(down)
                        elif(self.word_list[0] is self.lo[2]):
                            self.word_list.clear()
                            self.word_list.append(left)
                        elif(self.word_list[0] is self.lo[3]):
                            self.word_list.clear()
                            self.word_list.append(right)
                        elif(self.word_list[0] is self.lo[4]):
                            self.word_list.clear()
                            self.word_list.append(plus2)
                        elif(self.word_list[0] is self.lo[5]):
                            self.word_list.clear()
                            self.word_list.append(sub2)
                        elif(self.word_list[0] is self.lo[6]):
                            self.word_list.clear()
                            self.word_list.append(plussub)
                        elif(self.word_list[0] is self.lo[7]):
                            self.word_list.clear()
                            self.word_list.append(subplus)
                        else: 
                            print("len>2")    
                        self.lo.clear()
                        self.lo.append(up)
                        self.lo.append(down)
                        self.lo.append(left)
                        self.lo.append(right)
                        self.lo.append(plus2)
                        self.lo.append(sub2)
                        self.lo.append(plussub)
                        self.lo.append(subplus)
                        print("lo= ",self.lo)
                        print("lo= ",u,d,l,r,plus,sub,ps,sp)
                    else:
                        print("exit len>2")
                    print("wordlist: ",self.word_list)        
                    labelupdate(self,i,j) 
                    if(len(swapallowance)!=0):
                        counter1(self,swapallowance)
                else:
                    messagebox.showwarning('note','invalid selection')
                    self.r[i][j]["bg"]="blue"
                    self.r[i][j]["relief"]=RAISED
                    if(q1[1] is 0):
                        self.r[i][j-1]=h
                        print("h= ",h)
                    if(q1[0] is 0):
                        self.r[i-1][j]=p
                        print("p= ",p)
            if(count==1):
                counter1(self,swapallowance)
            if(count==2):
                counter2(self)
    
        def blocks():
            self.wordmadelist=[]
            self.text=[]
            self.text1=[]
            self.r=[]
            self.word_list=[]
            self.whitelist=[]
            self.lo=[]
            self.total_score=0
            note.config(text="note")
            self.box=self.w
            self.fon=self.d
            print("box:w= ",self.box)
            print("font:d= ",self.fon)   
            self.b=self.box*[self.box*[0]]
            def fun():
                self.root.iconify()
                #self.root.deiconify()
                self.done1()
            self.done=Button(self.root,text="Done",bg="blue",fg="white",activebackground="green",width=20,command=fun)
            def des():
                self.root.destroy()
            self.quitbut=Button(self.root,text="Quit",bg="blue",fg="white",activebackground="red",width=20,command=des)
            self.gameframe=Frame(self.root,bg="green")
            self.gameframe.place(x=0,y=0)
            frame=Frame(self.gameframe,bg="green")
            for i in range(self.box):
                c=[]
                for j in range(self.box):
                    self.b[i][j]=Button(frame,text=random.choice(string.ascii_letters.upper()),width=5,height=2,bg="blue",fg="black")
                    self.b[i][j].config(font=('times',self.fon,'bold'))
                    self.b[i][j].grid(column=i,row=j)
                    self.b[i][j].bind('<Button-1>',lambda event,i=i,j=j:functions(self,i,j))
                    self.b[i][j].bind('<Button-3>',lambda event,i=i,j=j:makemyword(self,swapallowance,i,j))
                    c.append(self.b[i][j])
                self.r.append(c)
            frame.place(x=19,y=60)
            self.c=0
            self.la=Label(self.root,text="Words you made: ",bg="green",height=2,relief=RIDGE)
            self.la.config(font=('times',12,'bold'))
            self.lb=Listbox(self.root,width=30,height=10,relief=RIDGE,bg="white")
            self.lb.insert(1,"start making words")
            self.lb.config(font=('times',11,'bold'))  
            self.di=Label(self.root,text="Only words present in en_US Dictionary",bg="red",fg="white",relief=RIDGE)
            self.di.config(font=('courier',12,'bold'))
            self.countlabel=Label(self.root,text="Word's Count: ",bg="red",relief=RIDGE)
            self.countlabel.config(font=('times',12,'bold'))
            self.countwords=Label(self.root,text="0",width=10,bg="white",relief=RIDGE)
            self.countwords.config(font=('times',12,'bold'))
            def verify():
                if(word_label["text"]==""):
                    note.config(text="word not found")
                    messagebox.showwarning('note','no word made')
                    self.valofscore=0
                else:
                    print("word_label: ",word_label["text"])
                    score_value=0
                    def concatenate_list_data(list):
                        result=''
                        for element in list:
                            result += str(element)
                        return result
                    dict_box=enchant.Dict("en_US")
                    checker=concatenate_list_data(self.text1)
                    print("word after concate of list is: ",checker)
                    print("check")
                    r=dict_box.check(checker)
                    print("r: ",r)
                    print(dict_box.suggest(checker))
                    print(len(checker))
                    if(len(checker)==1 or len(checker)==2):
                        messagebox.showinfo('invalid','Sorry there is no score for a single and two letter word')
                    else:
                        if(r is True):
                            self.wordmadelist.append(checker)
                            print(self.wordmadelist)
                            self.countwords.config(text=len(self.wordmadelist))
                            for i in range(self.c,len(self.wordmadelist)):
                                if(self.c==0):
                                    self.lb.delete(0,END)
                                self.lb.insert(i+1,self.wordmadelist[i])
                                self.c+=1  
                            if(score["text"]==""):
                                self.total_score=0
                            else:
                                s=score["text"]
                                self.total_score=s
                            l=len(word_label["text"])
                            print(l)
                            n=math.floor(l/2)
                            v=l-n
                            print("n: ",n)
                            print("v= ",v)
                            if(self.it.get()==self.droplist[0]):
                                if(v==3):
                                    score_value=30
                                if(v==4):
                                    score_value=40
                                if(v==5):
                                    score_value=50
                                if(v>=6):
                                    score_value=100
                            if(self.it.get()==self.droplist[1]):
                                if(v==3):
                                    score_value=60
                                if(v==4):
                                    score_value=80
                                if(v==5):
                                    score_value=100
                                if(v>=6):
                                    score_value=150
                            if(self.it.get()==self.droplist[2]):
                                if(v==3):
                                    score_value=20
                                if(v==4):
                                    score_value=30
                                if(v==5):
                                    score_value=40
                                if(v>=6):
                                    score_value=50
                            if(self.it.get()==self.droplist[3]):
                                if(v==3):
                                    score_value=10
                                if(v==4):
                                    score_value=15
                                if(v==5):
                                    score_value=20
                                if(v>=6):
                                    score_value=25
                            self.total_score+=score_value
                            score.config(text=self.total_score) 
                            note.config(text="word made")
                            if(self.total_score==400):
                                messagebox.showinfo('note','doing well')
                            op=0    
                            for self.text[op] in self.text:
                                self.text[0]["bg"]="blue"
                                self.text[0]["text"]=""
                                self.text[0]["relief"]=RAISED
                        else:
                            messagebox.showinfo('error',"word '"+str(checker)+"' is not defines in en_US dictionary")

                    op=0
                    for self.text[op] in self.text:
                        self.text[0]["bg"]="blue"
                        self.text[0]["relief"]=RAISED                 
                    self.text.clear()
                    self.text1.clear()   
                    self.word_list.clear()
                    print("text=",self.text)
                    print("text1: ",self.text1)
                    print("wordlist= ",self.word_list)
                    word_label.config(text="")
            self.button_verify=Button(self.root,text="Verify",bg="blue",width=10,height=1,command=verify)
            def clearword():
                word_label.config(text="")  
                op=0
                for self.text[op] in self.text:
                    self.text[0]["bg"]="blue"
                self.text.clear()
                self.text1.clear()
                self.word_list.clear()
                print("text=",self.text)
                print("text1: ",self.text1)
                print("wordlist= ",self.word_list)
            self.b0=Button(self.root,text="clear word",bg="blue",width=10,height=1,command=clearword)
        blocks()
        header=Label(self.root,text="WUZZLE\nWORD + PUZZLE",bg="red",fg="white")
        score_label=Label(self.root,text="Score board:",width=10,height=1,bg="orange")
        score_label.config(font=('times',20,'bold'))
        score=Label(self.root,width=8,height=1,bg="white",relief=RIDGE)
        score.config(font=('times',14,'bold'))  
        ts=0
        score.config(text=ts)  
        if(self.it.get()==self.droplist[0]):
            score_label.place(x=820,y=190)
            player.place(x=820,y=305)
            score.place(x=990,y=200)
            self.b0.place(x=1050,y=140)
            self.button_verify.place(x=910,y=140)
            note.place(x=770,y=9)
            l0.place(x=710,y=72)
            word_label.place(x=830,y=110)
            border.place(x=756,y=0)
            header.config(font=('times',13,'bold'),width=60)
            header.place(x=70,y=0)
            self.done.place(x=800,y=690)
            self.quitbut.place(x=1000,y=690)
            playername.place(x=980,y=305)
            idlab.place(x=820,y=350)
            idname.place(x=980,y=350)
            inforouter.place(x=770,y=250)
            levellab.place(x=820,y=395)
            levelval.place(x=980,y=395)
            self.la.place(x=770,y=440)
            self.lb.place(x=910,y=440)
            self.di.place(x=770,y=630)
            self.countlabel.place(x=770,y=510)
            self.countwords.place(x=800,y=550)
            self.gameframe.config(width=756,height=900)
        if(self.it.get()==self.droplist[1]):
            score_label.place(x=820,y=195)
            player.place(x=820,y=305)
            score.place(x=990,y=200)
            self.b0.place(x=1050,y=140)
            self.button_verify.place(x=910,y=140)
            note.place(x=770,y=9)
            l0.place(x=710,y=72)
            word_label.place(x=830,y=110)
            border.place(x=756,y=0)
            header.config(font=('times',13,'bold'),width=60)
            header.place(x=70,y=0)
            self.done.place(x=800,y=700)
            self.quitbut.place(x=1000,y=700)
            playername.place(x=980,y=305)
            idlab.place(x=820,y=350)
            idname.place(x=980,y=350)
            inforouter.place(x=770,y=250)
            levellab.place(x=820,y=395)
            levelval.place(x=980,y=395)
            self.la.place(x=770,y=440)
            self.lb.place(x=910,y=440)
            self.di.place(x=770,y=630)
            self.countlabel.place(x=770,y=510)
            self.countwords.place(x=800,y=550)
            self.gameframe.config(width=756,height=900)
        if(self.it.get()==self.droplist[2]):
            score_label.place(x=820,y=195)
            player.place(x=870,y=305)
            score.place(x=990,y=200)
            self.b0.place(x=1050,y=140)
            self.button_verify.place(x=910,y=140)
            note.place(x=815,y=9)
            l0.place(x=750,y=72)
            word_label.place(x=870,y=110)
            border.place(x=800,y=0)
            header.config(font=('times',13,'bold'),width=65)
            header.place(x=70,y=0)
            self.done.place(x=850,y=710)
            self.quitbut.place(x=1030,y=710)
            playername.place(x=1025,y=305)
            idlab.place(x=870,y=350)
            idname.place(x=1025,y=350)
            inforouter.place(x=820,y=250)
            levellab.place(x=866,y=395)
            levelval.place(x=1025,y=395)
            self.la.place(x=810,y=440)
            self.lb.place(x=950,y=440)
            self.di.place(x=820,y=640)
            self.countlabel.place(x=810,y=510)
            self.countwords.place(x=830,y=550)
            self.gameframe.config(width=800,height=900)
        if(self.it.get()==self.droplist[3]):
            score_label.place(x=900,y=195)
            player.place(x=950,y=305)
            score.place(x=1070,y=200)
            self.b0.place(x=1180,y=140)
            self.button_verify.place(x=1070,y=140)
            note.place(x=905,y=9)
            l0.place(x=835,y=72)
            word_label.place(x=950,y=110)
            border.place(x=890,y=0)
            header.config(font=('times',13,'bold'),width=75)
            header.place(x=70,y=0)
            self.done.place(x=930,y=700)
            self.quitbut.place(x=1100,y=700)
            playername.place(x=1109,y=305)
            idlab.place(x=950,y=350)
            idname.place(x=1109,y=350)
            inforouter.place(x=910,y=250)
            levellab.place(x=950,y=395)
            levelval.place(x=1110,y=395)
            self.la.place(x=910,y=440)
            self.lb.place(x=1050,y=440)
            self.di.place(x=910,y=640)
            self.countlabel.place(x=910,y=510)
            self.countwords.place(x=940,y=550)
            self.gameframe.config(width=890,height=900)
#==============================================================================================================================================================            
    def termsandconditions(self):
        tacbox=Tk()
        tacbox.title("terms_conditions")
        tacbox.config(bg="black")
        tacbox.geometry("730x400")  
        head=Label(tacbox,text="Rules And Regulations",bg="black",fg="white")
        head.config(font=('times',15,'underline'))
        head.pack()
        p1=Label(tacbox,text="--> If you want to Swap the Letter then use the left Button of the mouse",bg="black",fg="white")
        p1.config(font=('times',11,'bold'))
        p1.place(x=8,y=50)
        p2=Label(tacbox,text="--> If you want to Make a word then use the right Button of the mouse",bg="black",fg="white")
        p2.config(font=('times',11,'bold'))
        p2.place(x=8,y=90)
        p3=Label(tacbox,text="--> If you do not press the done button in the main window the score will not be updated into your database",bg="black",fg="white")
        p3.config(font=('times',11,'bold'))
        p3.place(x=8,y=130)
        p4=Label(tacbox,text="--> The Raised one can be only switched to compressed one ",bg="black",fg="white")
        p4.config(font=('times',11,'bold'))
        p4.place(x=8,y=170)
        p5=Label(tacbox,text="--> After making the WORD press the VERIFY button for verification ",bg="black",fg="white")
        p5.config(font=('times',11,'bold'))
        p5.place(x=8,y=210)
        self.droplist=['Default','Easy','Medium','Hard']
        self.it=StringVar()
        lab=Label(tacbox,text="Difficulty Level : ",bg="black",fg="white")
        lab.config(font=('courier',15,'bold'))
        lab.place(x=10,y=280)
        self.drop=OptionMenu(tacbox,self.it,*self.droplist)
        self.drop.config(width=25)
        self.it.set(self.droplist[0])
        print(self.it.get())
        self.drop.place(x=260,y=280)
        def destroy1():
            if(var.get()==1):
                if(self.it.get()==self.droplist[0]):
                    self.w=16
                    self.d=10
                if(self.it.get()==self.droplist[1]):
                    self.w=13    
                    self.d=12
                if(self.it.get()==self.droplist[2]):
                    self.w=17
                    self.d=10
                if(self.it.get()==self.droplist[3]):
                    self.w=19
                    self.d=8   
                tacbox.destroy()
                print(self.it.get())
                con=sqlite3.connect("wuzzle.db")
                dropvalue=self.it.get()
                con.execute("update wuzzle set Level=(?) where Userid='"+str(self.q[0][1])+"'",([dropvalue]))    #dropvalue,
                con.commit()
                self.game()
            else:
                warlabel=Label(tacbox,text="please accept rules and regulations ",bg="black",fg="yellow")
                warlabel.place(x=40,y=360)
        destroybutton=Button(tacbox,text="Done",bg="green",width=20,command=destroy1)
        destroybutton.place(x=430,y=350)
        var=IntVar()
        t=Checkbutton(tacbox,text="I accept all rules and regulations",variable=var)
        t.place(x=30,y=330)
#============================================================================================================================================================
    def loginwuzz(self):
        login_box=Tk()
        login_box.title("login_box")
        info=Label(login_box,text="Information regarding this block will be updated here",bg="red",fg="white",width=66)
        info.config(font=('times',10,'bold'))
        info.place(x=0,y=0)
        login_box.geometry('465x650')
        login_box.config(bg="blue")
        def directaccess():
            x=os.path.exists("wuzzle.db")
            print("database exists: ",x)
            if(x is True):
                info.config(text="WORK BY: CHILUKURI VINAY KUMAR")
                messagebox.showinfo('login',"welcome Default user")
                con=sqlite3.connect("wuzzle.db")
                searchfordefault=con.execute("select * from wuzzle where Username='Default'")
                valueinsearch=searchfordefault.fetchall()
                print("valuein search for default: ",valueinsearch)
                con.commit()
                if(len(valueinsearch)==0):
                    con=sqlite3.connect("wuzzle.db")
                    con.execute("insert into wuzzle(Username,Userid)values('Default','default@123')")
                    con.commit()
                else:
                    print("default user exists in database")
                con=sqlite3.connect("wuzzle.db")
                p=con.execute("select * from wuzzle where Username='Default'")
                self.q=p.fetchall()
                print("values in q",self.q)
                login_box.destroy()
                self.termsandconditions()
            else:
                messagebox.showinfo('invalid',"To use direct access there should be atleast one entry in the database")    
        photo=PhotoImage(file="rsz_1client-wuzzle-1.png")
        labelbuyy=Label(login_box,image=photo,relief=RAISED)
        labelbuyy.image=photo
        labelbuyy.place(x=10,y=30)
        yellowbtn=Button(login_box,text="Word + Puzzle",bg="gold",width=20,activebackground="gold",relief=RIDGE,command=directaccess)
        yellowbtn.config(font=('courier',10,'bold'))
        yellowbtn.place(x=145,y=250)
        login=Label(login_box,text="LOGIN",bg="blue",fg="red")
        login.config(font=('courier',20,'bold'))
        login.place(x=30,y=330)
        loginid=StringVar()
        loginpassword=StringVar()
        useridl=Label(login_box,text="USERNAME ID : ",bg="blue")
        useridl.config(font=('times',12,'bold'))
        useridl.place(x=60,y=370)
        userid_textl=Entry(login_box,bd=2,textvar=loginid,width=25,justify="center")
        userid_textl.place(x=200,y=370)
        log_pass=Label(login_box,text="PASSWORD : ",bg="blue")
        log_pass.config(font=('times',12,'bold'))
        log_pass.place(x=60,y=400)
        logpass_text=Entry(login_box,bd=2,textvar=loginpassword,width=25,show="*",justify="center")
        logpass_text.place(x=200,y=400)
        register=Label(login_box,text="REGISTER",bg="blue",fg="red")
        register.config(font=('courier',20,'bold'))
        register.place(x=30,y=450)
        registeruser=StringVar()
        registerid=StringVar()
        registerpassword=StringVar()
        usernamer=Label(login_box,text="USERNAME : ",bg="blue")
        usernamer.config(font=('times',12,'bold'))
        usernamer.place(x=60,y=490)
        username_textr=Entry(login_box,bd=2,textvar=registeruser,width=25,justify="center")
        username_textr.place(x=200,y=490)
        useridr=Label(login_box,text="USERNAME ID : ",bg="blue")
        useridr.config(font=('times',12,'bold'))
        useridr.place(x=60,y=515)
        userid_textr=Entry(login_box,bd=2,textvar=registerid,width=25,justify="center")
        userid_textr.place(x=200,y=515)
        reg_pass=Label(login_box,text="PASSWORD : ",bg="blue")
        reg_pass.config(font=('times',12,'bold'))
        reg_pass.place(x=60,y=540)
        regpass_text=Entry(login_box,bd=2,textvar=registerpassword,width=25,show="*",justify="center")
        regpass_text.place(x=200,y=540)
        genderlabel=Label(login_box,text="GENDER : ",bg="blue")
        genderlabel.config(font=('times',12,'bold'))
        genderlabel.place(x=60,y=565)
        gen=StringVar()
        radiomale=Radiobutton(login_box,text="Male",bg="white",variable=gen,value="male",width=11)
        radiomale.place(x=200,y=565)
        radiofemale=Radiobutton(login_box,text="Female",bg="white",variable=gen,value="female",width=10)
        radiofemale.place(x=300,y=565)
        age=IntVar()
        agelabel=Label(login_box,text="AGE(optional): ",bg="blue")
        agelabel.config(font=('times',12,'bold'))
        agelabel.place(x=60,y=595)
        age_text=Entry(login_box,bd=2,textvar=age,width=25,justify="center")
        age_text.place(x=200,y=598)
        def login():
            con=sqlite3.connect("wuzzle.db")
            p=con.execute("select * from wuzzle where Userid='"+userid_textl.get()+"'and Password='"+logpass_text.get()+"'")
            if(userid_textl.get()=="" or logpass_text.get()==""):
                info.config(text="please fill the required details")
            else:
                self.q=p.fetchall()
                print("q= ",self.q)
                if(len(self.q)==0):
                    info.config(text="Invalid details")
                    userid_textl.delete(0,"end")
                    logpass_text.delete(0,"end")
                else:
                    g=con.execute("select Username from wuzzle where Userid='"+userid_textl.get()+"'")
                    k=g.fetchall()
                    print("q= ",self.q)
                    print("q= ",str(self.q[0][0]))
                    info.config(text="access granted '"+str(self.q[0][0])+"'")
                    messagebox.showinfo('login',"access granted '"+str(self.q[0][0])+"'")
                    login_box.destroy()
                    self.termsandconditions()  
            con.commit()        
        def register():
            reguser=registeruser.get()
            regid=registerid.get()
            regpass=registerpassword.get()
            gend=gen.get()
            m=False
            try:
                age.get()==0
            except:
                m=True
            if(m==False):
                agef=age.get()
            if(m==True):
                agef=0    
            con=sqlite3.connect("wuzzle.db")
            #con.execute("create table wuzzle(Username varchar(30),Userid varchar(30),Password varchar(20),score int,Level varchar(20),Age int,Gender varchar(10))")
            z=con.execute("select Userid from  wuzzle where Userid='"+regid+"'")
            y=z.fetchall()
            if(len(y)==0):
                if(username_textr.get()=="" or regpass_text.get()=="" or userid_textr.get()==""):
                    info.config(text="please fill the required details")
                else:
                    msg=messagebox.askquestion('register','Allow us to store your data this may be useful further')
                    if(msg=='yes'):
                        con.execute("insert into wuzzle(Username,Userid,Password,Age,Gender)values(?,?,?,?,?)",(reguser,regid,regpass,agef,gend))
                        info.config(text="account created successfully")
                        messagebox.showinfo('register','account created succesfully')
                        username_textr.delete(0,"end")
                        userid_textr.delete(0,"end")
                        regpass_text.delete(0,"end")
                        age_text.delete(0,"end")
                    else:
                        username_textr.delete(0,"end")
                        userid_textr.delete(0,"end")
                        regpass_text.delete(0,"end")
                        radiomale.deselect()
                        radiofemale.deselect()
                        age_text.delete(0,"end")
                        info.config(text="Account not created")
            else:
               info.config(text="UserId already exists please change the UserId")    
            con.commit()        
        logingo=Button(login_box,text="Done",bg="green",width=10,height=1,activebackground="cyan",command=login)
        logingo.place(x=370,y=400)
        registergo=Button(login_box,text="Register",bg="green",width=10,height=1,command=register)
        registergo.place(x=370,y=600)   
        borderhor=Label(login_box,bg="black",fg="red",width=65)
        borderhor.config(text="####################################################################")
        borderhor.place(x=2,y=430)        
        login_box.mainloop()   
w=wuzzle()
w.loginwuzz()
#===========================================================================================================================================================
#==========================================================================================================================================================#
                                                                                                                                                           #
                   #=======================================================================================================#                               #
                   #                                                                                                       #                               #
                   #                                  CREATED BY :- CHILUKURI VINAY KUMAR                                  #                               #                  
                   #                                                                                                       #                               #                   
                   #=======================================================================================================#                               #
                                                                                                                                                           #
#==========================================================================================================================================================# 