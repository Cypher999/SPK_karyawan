import xml.dom.minidom as mndom
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import datetime as waktu
from threading import Timer
class karyawan:
    def __init__(this):
        this.dbase=mndom.parse("spk.xml")
        this.win=Tk()
        this.win.title("Data Karyawan")
        jekel=[]
        jekel.append("L)aki-laki")
        jekel.append("P)erempuan")
        this.l_kode=Label(this.win,text="Kode Karyawan")
        this.l_nama=Label(this.win,text="Nama Karyawan")
        this.l_jk=Label(this.win,text="Jenis Kelamin")
        this.l_alt=Label(this.win,text="Alamat")
        this.t_kode=Entry(this.win)
        this.t_nama=Entry(this.win)
        this.c_jk=Combobox(this.win)
        this.t_alt=Entry(this.win)
        this.c_jk['values']=jekel
        this.b_simpan=Button(this.win,text="Simpan",command=this.save)
        this.b_edit=Button(this.win,text="Edit",command=this.edit)
        this.b_hapus=Button(this.win,text="Hapus",command=this.hapus)
        this.b_batal=Button(this.win,text="Batal",command=this.batal)
        this.b_daftar=Button(this.win,text="Daftar",command=this.list_data)
        this.b_keluar=Button(this.win,text="Keluar",command=this.win.destroy)
        this.c_jk.current(0)
        this.l_kode.grid(column=0,row=0)
        this.l_nama.grid(column=0,row=1)
        this.l_jk.grid(column=0,row=2)
        this.l_alt.grid(column=0,row=3)
        this.t_kode.grid(column=1,row=0)
        this.t_nama.grid(column=1,row=1)
        this.c_jk.grid(column=1,row=2)
        this.t_alt.grid(column=1,row=3)
        this.b_simpan.grid(column=0,row=4)
        this.b_edit.grid(column=1,row=4)
        this.b_hapus.grid(column=0,row=5)
        this.b_batal.grid(column=1,row=5)
        this.b_keluar.grid(column=1,row=6)
        this.b_daftar.grid(column=0,row=6)
        this.t_kode.bind('<Return>',this.cari)
        this.begin_text()
        this.begin_cmd()
        this.win.mainloop()
    def begin_text(this):
        this.t_kode.configure(state=NORMAL)
        this.t_nama.configure(state=DISABLED)
        this.c_jk.configure(state=DISABLED)
        this.t_alt.configure(state=DISABLED)
    def list_data(this):
        win_dt=Tk()
        win_dt.title("Daftar Karyawan")
        i=0
        list_dt=mndom.parse("spk.xml")
        data_contain=list_dt.getElementsByTagName("Karyawan")
        l_kd=Label(win_dt,text="Kode karyawan")
        l_p1=Label(win_dt,text=" | ")
        l_nm=Label(win_dt,text="Nama Karyawan")
        l_p2=Label(win_dt,text=" | ")
        l_jk=Label(win_dt,text="Jenis Kelamin")
        l_p3=Label(win_dt,text=" | ")
        l_alt=Label(win_dt,text="Alamat")
        l_kd.grid(column=0,row=0)
        l_p1.grid(column=1,row=0)
        l_nm.grid(column=2,row=0)
        l_p2.grid(column=3,row=0)
        l_jk.grid(column=4,row=0)
        l_p3.grid(column=5,row=0)
        l_alt.grid(column=6,row=0)
        for data_ct in data_contain:
            k_kd=data_ct.getAttribute("kd_kar")
            k_nm=data_ct.getAttribute("nm_kar")
            if(data_ct.getAttribute("jekel")=="L"):
                kd_jk=Label(win_dt,text="Laki-Laki")
            else:
                kd_jk=Label(win_dt,text="Perempuan")
            k_alt=data_ct.getAttribute("alt")
            kd_kd=Label(win_dt,text=k_kd)
            kd_p1=Label(win_dt,text=" | ")
            kd_nm=Label(win_dt,text=k_nm)
            kd_p2=Label(win_dt,text=" | ")
            kd_alt=Label(win_dt,text=k_alt)
            kd_p3=Label(win_dt,text=" | ")
            kd_kd.grid(column=0,row=i+1)
            kd_p1.grid(column=1,row=i+1)
            kd_nm.grid(column=2,row=i+1)
            kd_p2.grid(column=3,row=i+1)
            kd_jk.grid(column=4,row=i+1)
            kd_p3.grid(column=5,row=i+1)
            kd_alt.grid(column=6,row=i+1)
            i=i+1
        win_dt.mainloop()
    def batal(this):
        this.new_data_text()
        this.t_kode.configure(state=NORMAL)
        this.bersih()
        this.begin_cmd()
    def bersih(this):
        this.t_kode.delete(0, END)
        this.t_nama.delete(0, END)
        this.t_alt.delete(0, END)
        this.c_jk.current(0)
    def save(this):
        if((this.t_kode.get()=="")or(this.t_nama.get()=="")or(this.t_alt.get()=="")):
            messagebox.showinfo("Pesan","Data tidak lengkap")
        else:
            new_data=this.dbase.createElement("Karyawan")
            new_data.setAttribute("kd_kar",this.t_kode.get())
            new_data.setAttribute("nm_kar",this.t_nama.get())
            new_data.setAttribute("alt",this.t_alt.get())
            jekel=(this.c_jk.get().split(")"))
            new_data.setAttribute("jekel",jekel[0])
            this.dbase.getElementsByTagName("spk")[0].appendChild(new_data)
            file=open("spk.xml","w")
            this.dbase.writexml(file)
            file.close()
            this.new_data_text()
            this.t_kode.configure(state=NORMAL)
            this.bersih()
            this.begin_text()
            this.begin_cmd()
    def new_data_text(this):
        this.t_kode.configure(state=DISABLED)
        this.t_nama.configure(state=NORMAL)
        this.t_alt.configure(state=NORMAL)
        this.c_jk.configure(state=NORMAL)
    def cari(this,aaa):
        i=0
        ii=0
        present=0
        items=this.dbase.getElementsByTagName("Karyawan")
        for it in items:
            if(this.t_kode.get()==it.getAttribute("kd_kar")):
                present=1
                ii=i
            i=i+1
        if(present==1):
            this.new_data_text()
            if((this.t_nama.get()!="")or(this.t_alt.get()!="")):
                this.t_nama.delete(0, END)
                this.t_alt.delete(0, END)
            this.t_nama.insert(INSERT, items[ii].getAttribute("nm_kar"))
            this. t_alt.insert(INSERT, items[ii].getAttribute("alt"))
            if(items[ii].getAttribute("jekel")=="L"):
                this.c_jk.current(0)
            else:
                this.c_jk.current(1)
            this.edit_data_cmd()
        else:
            this.new_data_text()
            this.new_data_cmd()
        this.t_nama.focus()
    def edit(this):
        i=0
        ii=0
        present=0
        items=this.dbase.getElementsByTagName("Karyawan")
        for it in items:
            if(this.t_kode.get()==it.getAttribute("kd_kar")):
                present=1
                ii=i
            i=i+1
        data_edit=this.dbase.getElementsByTagName("Karyawan")[ii]
        data_edit.setAttribute("nm_kar",this.t_nama.get())
        data_edit.setAttribute("alt",this.t_alt.get())
        jekel=(this.c_jk.get().split(")"))
        data_edit.setAttribute("jekel",jekel[0])
        file=open("spk.xml","w")
        this.dbase.writexml(file)
        file.close()
        this.new_data_text()
        this.t_kode.configure(state=NORMAL)
        this.bersih()
        this.begin_text()
        this.begin_cmd()
    def hapus(this):
        i=0
        ii=0
        j=0
        jj=0
        items=this.dbase.getElementsByTagName("Karyawan")
        items_nilai=this.dbase.getElementsByTagName("nilai")
        for it in items:
            if(this.t_kode.get()==it.getAttribute("kd_kar")):
                ii=i
            i=i+1
        if(len(items_nilai)!=0):
            for it_nil in items_nilai:
                if(this.t_kode.get()==it_nil.getAttribute("kd_kar")):    
                    jj=j
                j=j+1    
        data_edit=this.dbase.getElementsByTagName("Karyawan")[ii]
        data_nilai=this.dbase.getElementsByTagName("nilai")[jj]
        this.dbase.documentElement.removeChild(data_edit)
        this.dbase.documentElement.removeChild(data_nilai)
        file=open("spk.xml","w")
        this.dbase.writexml(file)
        file.close()
        this.new_data_text()
        this.t_kode.configure(state=NORMAL)
        this.bersih()
        this.begin_text()
        this.begin_cmd()
    def new_data_cmd(this):
        this.b_simpan.configure(state=NORMAL)
        this.b_batal.configure(state=NORMAL)
        this.b_edit.configure(state=DISABLED)
        this.b_hapus.configure(state=DISABLED)
        this.b_keluar.configure(state=DISABLED)
    def begin_cmd(this):
        this.b_simpan.configure(state=NORMAL)
        this.b_batal.configure(state=DISABLED)
        this.b_edit.configure(state=DISABLED)
        this.b_hapus.configure(state=DISABLED)
        this.b_keluar.configure(state=NORMAL)
    def edit_data_cmd(this):
        this.b_simpan.configure(state=DISABLED)
        this.b_batal.configure(state=NORMAL)
        this.b_edit.configure(state=NORMAL)
        this.b_hapus.configure(state=NORMAL)
        this.b_keluar.configure(state=DISABLED)

