from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import xml.dom.minidom as mndom
import datetime as waktu
from threading import Timer
class kriteria:
    def simpan(this):
        bobot_c1=float(this.t_c1.get())
        bobot_c2=float(this.t_c2.get())
        bobot_c3=float(this.t_c3.get())
        bobot_c4=float(this.t_c4.get())
        bobot_c5=float(this.t_c5.get())
        bobot_c6=float(this.t_c6.get())
        jenis_c1=this.c_c1.get().split(")")
        jenis_c2=this.c_c2.get().split(")")
        jenis_c3=this.c_c3.get().split(")")
        jenis_c4=this.c_c4.get().split(")")
        jenis_c5=this.c_c5.get().split(")")
        jenis_c6=this.c_c6.get().split(")")
        if((bobot_c1+bobot_c2+bobot_c3+bobot_c4+bobot_c5+bobot_c6)!=100):
            messagebox.showinfo("pesan","Jumlah bobot harus sama dengan 100")
        else:
            this.dbase.getElementsByTagName("kriteria")[0].setAttribute("tipe",jenis_c1[0])
            this.dbase.getElementsByTagName("kriteria")[1].setAttribute("tipe",jenis_c2[0])
            this.dbase.getElementsByTagName("kriteria")[2].setAttribute("tipe",jenis_c3[0])
            this.dbase.getElementsByTagName("kriteria")[3].setAttribute("tipe",jenis_c4[0])
            this.dbase.getElementsByTagName("kriteria")[4].setAttribute("tipe",jenis_c5[0])
            this.dbase.getElementsByTagName("kriteria")[5].setAttribute("tipe",jenis_c6[0])
            this.dbase.getElementsByTagName("kriteria")[0].setAttribute("bobot",str(bobot_c1))
            this.dbase.getElementsByTagName("kriteria")[1].setAttribute("bobot",str(bobot_c2))
            this.dbase.getElementsByTagName("kriteria")[2].setAttribute("bobot",str(bobot_c3))
            this.dbase.getElementsByTagName("kriteria")[3].setAttribute("bobot",str(bobot_c4))
            this.dbase.getElementsByTagName("kriteria")[4].setAttribute("bobot",str(bobot_c5))
            this.dbase.getElementsByTagName("kriteria")[5].setAttribute("bobot",str(bobot_c6))
            isi_file=open("spk.xml","w")
            this.dbase.writexml(isi_file)
            isi_file.close()
            this.cek_kriteria()
    def __init__(this):
        this.dbase=mndom.parse("spk.xml")
        this.win=Tk()
        this.win.title("Data Kriteria")
        jenis_krit=[]
        jenis_krit.append("B)enefit")
        jenis_krit.append("C)ost")
        this.l_c1=Label(this.win,text="Presensi")
        this.l_c2=Label(this.win,text="Ketepatan Waktu")
        this.l_c3=Label(this.win,text="Kreativitas")
        this.l_c4=Label(this.win,text="Target")
        this.l_c5=Label(this.win,text="Pelanggaran")
        this.l_c6=Label(this.win,text="Kerjasama")
        this.t_c1=Entry(this.win)
        this.t_c2=Entry(this.win)
        this.t_c3=Entry(this.win)
        this.t_c4=Entry(this.win)
        this.t_c5=Entry(this.win)
        this.t_c6=Entry(this.win)
        this.c_c1=Combobox(this.win)
        this.c_c2=Combobox(this.win)
        this.c_c3=Combobox(this.win)
        this.c_c4=Combobox(this.win)
        this.c_c5=Combobox(this.win)
        this.c_c6=Combobox(this.win)
        this.c_c1["values"]=jenis_krit
        this.c_c2["values"]=jenis_krit
        this.c_c3["values"]=jenis_krit
        this.c_c4["values"]=jenis_krit
        this.c_c5["values"]=jenis_krit
        this.c_c6["values"]=jenis_krit
        this.b_simpan=Button(this.win,text="Simpan",command=this.simpan)
        this.b_keluar=Button(this.win,text="Keluar",command=this.win.destroy)
        this.l_c1.grid(column=0,row=0)
        this.l_c2.grid(column=0,row=1)
        this.l_c3.grid(column=0,row=2)
        this.l_c4.grid(column=0,row=3)
        this.l_c5.grid(column=0,row=4)
        this.l_c6.grid(column=0,row=5)
        this.c_c1.grid(column=1,row=0)
        this.c_c2.grid(column=1,row=1)
        this.c_c3.grid(column=1,row=2)
        this.c_c4.grid(column=1,row=3)
        this.c_c5.grid(column=1,row=4)
        this.c_c6.grid(column=1,row=5)
        this.t_c1.grid(column=2,row=0)
        this.t_c2.grid(column=2,row=1)
        this.t_c3.grid(column=2,row=2)
        this.t_c4.grid(column=2,row=3)
        this.t_c5.grid(column=2,row=4)
        this.t_c6.grid(column=2,row=5)
        this.c_c1.current(0)
        this.c_c2.current(0)
        this.c_c3.current(0)
        this.c_c4.current(0)
        this.c_c5.current(0)
        this.c_c6.current(0)
        this.b_simpan.grid(column=0,row=6)
        this.b_keluar.grid(column=1,row=6)
        
        this.cek_kriteria()
        this.win.mainloop()
    def cek_kriteria(this):
        t_c1=this.dbase.getElementsByTagName("kriteria")[0].getAttribute("tipe")
        t_c2=this.dbase.getElementsByTagName("kriteria")[1].getAttribute("tipe")
        t_c3=this.dbase.getElementsByTagName("kriteria")[2].getAttribute("tipe")
        t_c4=this.dbase.getElementsByTagName("kriteria")[3].getAttribute("tipe")
        t_c5=this.dbase.getElementsByTagName("kriteria")[4].getAttribute("tipe")
        t_c6=this.dbase.getElementsByTagName("kriteria")[5].getAttribute("tipe")
        b_c1=this.dbase.getElementsByTagName("kriteria")[0].getAttribute("bobot")
        b_c2=this.dbase.getElementsByTagName("kriteria")[1].getAttribute("bobot")
        b_c3=this.dbase.getElementsByTagName("kriteria")[2].getAttribute("bobot")
        b_c4=this.dbase.getElementsByTagName("kriteria")[3].getAttribute("bobot")
        b_c5=this.dbase.getElementsByTagName("kriteria")[4].getAttribute("bobot")
        b_c6=this.dbase.getElementsByTagName("kriteria")[5].getAttribute("bobot")
        if(t_c1=="B"):
            this.c_c1.current(0)
        elif(t_c1=="C"):
            this.c_c1.current(1)
        if(t_c2=="B"):
            this.c_c2.current(0)
        elif(t_c2=="C"):
            this.c_c2.current(1)
        if(t_c3=="B"):
            this.c_c3.current(0)
        elif(t_c3=="C"):
            this.c_c3.current(1)
        if(t_c4=="B"):
            this.c_c4.current(0)
        elif(t_c4=="C"):
            this.c_c4.current(1)
        if(t_c5=="B"):
            this.c_c5.current(0)
        elif(t_c5=="C"):
            this.c_c5.current(1)
        if(t_c6=="B"):
            this.c_c6.current(0)
        elif(t_c6=="C"):
            this.c_c6.current(1)
        if(this.t_c1.get()!=""):
            this.t_c1.delete(0, END)
        if(this.t_c2.get()!=""):
            this.t_c2.delete(0, END)
        if(this.t_c3.get()!=""):
            this.t_c3.delete(0, END)
        if(this.t_c4.get()!=""):
            this.t_c4.delete(0, END)
        if(this.t_c5.get()!=""):
            this.t_c5.delete(0, END)
        if(this.t_c6.get()!=""):
            this.t_c6.delete(0, END)
        this.t_c1.insert(INSERT, b_c1)
        this.t_c2.insert(INSERT, b_c2)
        this.t_c3.insert(INSERT, b_c3)
        this.t_c4.insert(INSERT, b_c4)
        this.t_c5.insert(INSERT, b_c5)
        this.t_c6.insert(INSERT, b_c6)
    



