from tkinter import *
from tkinter.ttk import *
import xml.dom.minidom as mndom
from threading import Timer
from tkinter import messagebox
import datetime as waktu

class penilaian:
    def __init__(this):
        this.dbase=mndom.parse("spk.xml")
        this.win=Tk()
        nama_karyawan=[]
        spk=this.dbase.getElementsByTagName("spk")[0]
        insert_name=spk.getElementsByTagName("Karyawan")
        for in_nm in insert_name:
            nama_karyawan.append(in_nm.getAttribute("kd_kar")+" | "+in_nm.getAttribute("nm_kar"))
        
        this.c_nama=Combobox(this.win)
        this.c_c1=Combobox(this.win)
        this.c_c2=Combobox(this.win)
        this.c_c3=Combobox(this.win)
        this.c_c4=Combobox(this.win)
        this.c_c5=Combobox(this.win)
        this.c_c6=Combobox(this.win)
        nilai_combo=[]
        i=1
        while(i<=10):
            nilai_combo.append(i)
            i=i+1
        this.c_nama["values"]=nama_karyawan
        this.c_c1["values"]=nilai_combo
        this.c_c2["values"]=nilai_combo
        this.c_c3["values"]=nilai_combo
        this.c_c4["values"]=nilai_combo
        this.c_c5["values"]=nilai_combo
        this.c_c6["values"]=nilai_combo
        this.l_nama=Label(this.win,text="Nama Karyawan")
        this.l_c1=Label(this.win,text="Presensi")
        this.l_c2=Label(this.win,text="Ketepatan waktu")
        this.l_c3=Label(this.win,text="Kreativitas")
        this.l_c4=Label(this.win,text="Target")
        this.l_c5=Label(this.win,text="Pelanggaran")
        this.l_c6=Label(this.win,text="Kerjasama")
        this.b_simpan=Button(this.win,text="Simpan",command=this.simpan)
        this.b_edit=Button(this.win,text="Edit",command=this.edit)
        this.b_hapus=Button(this.win,text="Hapus",command=this.hapus)
        this.b_batal=Button(this.win,text="Batal",command=this.batal)
        this.b_keluar=Button(this.win,text="Keluar",command=this.win.destroy)
        this.b_daftar=Button(this.win,text="Daftar",command=this.daftar)
        this.c_nama.bind("<<ComboboxSelected>>",this.cari)
        this.l_nama.grid(column=0,row=0)
        this.l_c1.grid(column=0,row=1)
        this.l_c2.grid(column=0,row=2)
        this.l_c3.grid(column=0,row=3)
        this.l_c4.grid(column=0,row=4)
        this.l_c5.grid(column=0,row=5)
        this.l_c6.grid(column=0,row=6)
        this.c_nama.grid(column=1,row=0)
        this.c_c1.grid(column=1,row=1)
        this.c_c2.grid(column=1,row=2)
        this.c_c3.grid(column=1,row=3)
        this.c_c4.grid(column=1,row=4)
        this.c_c5.grid(column=1,row=5)
        this.c_c6.grid(column=1,row=6)
        this.b_simpan.grid(column=0,row=7)
        this.b_edit.grid(column=1,row=7)
        this.b_hapus.grid(column=2,row=7)
        this.b_batal.grid(column=0,row=8)
        this.b_daftar.grid(column=1,row=8)
        this.b_keluar.grid(column=2,row=8)
        this.first_combo()
        this.command_first()
        this.nonactive_combo()
        this.win.mainloop()
    def cari(this,event):
        i=0
        ii=0
        present=0
        kode_karyawan=this.dbase.getElementsByTagName("nilai")
        for kd_kar in kode_karyawan:
            combo_value=this.c_nama.get().split(" | ")
            if((kd_kar.getAttribute("kd_kar"))==combo_value[0]):
                ii=i
                present=1
            i=i+1
        if (present==1):
            this.active_combo()
            this.c_c1.delete(0, END)
            this.c_c2.delete(0, END)
            this.c_c3.delete(0, END)
            this.c_c4.delete(0, END)
            this.c_c5.delete(0, END)
            this.c_c6.delete(0, END)
            this.c_c1.insert(INSERT, kode_karyawan[ii].getAttribute("c1"))
            this.c_c2.insert(INSERT, kode_karyawan[ii].getAttribute("c2"))
            this.c_c3.insert(INSERT, kode_karyawan[ii].getAttribute("c3"))
            this.c_c4.insert(INSERT, kode_karyawan[ii].getAttribute("c4"))
            this.c_c5.insert(INSERT, kode_karyawan[ii].getAttribute("c5"))
            this.c_c6.insert(INSERT, kode_karyawan[ii].getAttribute("c6"))
            this.command_edit()
        else:
            this.active_combo()
            this.command_new()
    def edit(this):
        i=0
        ii=0
        present=0
        kode_karyawan=this.dbase.getElementsByTagName("nilai")
        for kd_kar in kode_karyawan:
            combo_value=this.c_nama.get().split(" | ")
            if((kd_kar.getAttribute("kd_kar"))==combo_value[0]):
                ii=i
                present=1
            i=i+1
        
        kode_karyawan[ii].setAttribute("c1",this.c_c1.get())
        kode_karyawan[ii].setAttribute("c2",this.c_c2.get())
        kode_karyawan[ii].setAttribute("c3",this.c_c3.get())
        kode_karyawan[ii].setAttribute("c4",this.c_c4.get())
        kode_karyawan[ii].setAttribute("c5",this.c_c5.get())
        kode_karyawan[ii].setAttribute("c6",this.c_c6.get())
        file=open("spk.xml","w")
        this.dbase.writexml(file)
        file.close()
        this.first_combo()
        this.command_first()
        this.nonactive_combo()
    def daftar(this):
        daftar=Tk()
        list_nilai=this.dbase.getElementsByTagName("nilai")
        l_p1=Label(daftar,text=" | ")
        l_p2=Label(daftar,text=" | ")
        l_p3=Label(daftar,text=" | ")
        l_p4=Label(daftar,text=" | ")
        l_p5=Label(daftar,text=" | ")
        l_p6=Label(daftar,text=" | ")
        l_nama=Label(daftar,text="Nama Karyawan")
        l_c1=Label(daftar,text="Presensi")
        l_c2=Label(daftar,text="Ketepatan waktu")
        l_c3=Label(daftar,text="Kreativitas")
        l_c4=Label(daftar,text="Target")
        l_c5=Label(daftar,text="Pelanggaran")
        l_c6=Label(daftar,text="Kerjasama")
        l_nama.grid(column=0,row=0)
        l_p1.grid(column=1,row=0)
        l_c1.grid(column=2,row=0)
        l_p2.grid(column=3,row=0)
        l_c2.grid(column=4,row=0)
        l_p3.grid(column=5,row=0)
        l_c3.grid(column=6,row=0)
        l_p4.grid(column=7,row=0)
        l_c4.grid(column=8,row=0)
        l_p5.grid(column=9,row=0)
        l_c5.grid(column=10,row=0)
        l_p6.grid(column=11,row=0)
        l_c6.grid(column=12,row=0)
        i=1
        j=0
        jj=0
        for ls_ni in list_nilai:
            j=0
            jj=0
            kode_kar=ls_ni.getAttribute("kd_kar")
            nm_kar=this.dbase.getElementsByTagName("Karyawan")
            for n_k in nm_kar:
                if(kode_kar==n_k.getAttribute("kd_kar")):
                    jj=j
                j=j+1
            
            t_nama=Label(daftar,text=nm_kar[jj].getAttribute("nm_kar"))
            
            t_c1=Label(daftar,text=ls_ni.getAttribute("c1"))
            t_c2=Label(daftar,text=ls_ni.getAttribute("c2"))
            t_c3=Label(daftar,text=ls_ni.getAttribute("c3"))
            t_c4=Label(daftar,text=ls_ni.getAttribute("c4"))
            t_c5=Label(daftar,text=ls_ni.getAttribute("c5"))
            t_c6=Label(daftar,text=ls_ni.getAttribute("c6"))
            t_nama.grid(column=0,row=i)
            t_c1.grid(column=2,row=i)
            t_c2.grid(column=4,row=i)
            t_c3.grid(column=6,row=i)
            t_c4.grid(column=8,row=i)
            t_c5.grid(column=10,row=i)
            t_c6.grid(column=12,row=i)
            i=i+1
        daftar.mainloop()
        
    def hapus(this):
        i=0
        ii=0
        present=0
        kode_karyawan=this.dbase.getElementsByTagName("nilai")
        for kd_kar in kode_karyawan:
            combo_value=this.c_nama.get().split(" | ")
            if((kd_kar.getAttribute("kd_kar"))==combo_value[0]):
                ii=i
                present=1
            i=i+1
        this.dbase.documentElement.removeChild(kode_karyawan[ii])
        file=open("spk.xml","w")
        this.dbase.writexml(file)
        file.close()
        this.first_combo()
        this.command_first()
        this.nonactive_combo()
    def first_combo(this):
        this.c_nama.current(0)
        this.c_c1.current(0)
        this.c_c2.current(0)
        this.c_c3.current(0)
        this.c_c4.current(0)
        this.c_c5.current(0)
        this.c_c6.current(0)
    def active_combo(this):
        this.c_nama.configure(state=DISABLED)
        this.c_c1.configure(state=NORMAL)
        this.c_c2.configure(state=NORMAL)
        this.c_c3.configure(state=NORMAL)
        this.c_c4.configure(state=NORMAL)
        this.c_c5.configure(state=NORMAL)
        this.c_c6.configure(state=NORMAL)
    def nonactive_combo(this):
        this.c_nama.configure(state=NORMAL)
        this.c_c1.configure(state=DISABLED)
        this.c_c2.configure(state=DISABLED)
        this.c_c3.configure(state=DISABLED)
        this.c_c4.configure(state=DISABLED)
        this.c_c5.configure(state=DISABLED)
        this.c_c6.configure(state=DISABLED)
    def simpan(this):
        new_data=this.dbase.createElement("nilai")
        kd_kar=this.c_nama.get().split(" | ")
        new_data.setAttribute("kd_kar",kd_kar[0])
        new_data.setAttribute("c1",this.c_c1.get())
        new_data.setAttribute("c2",this.c_c2.get())
        new_data.setAttribute("c3",this.c_c3.get())
        new_data.setAttribute("c4",this.c_c4.get())
        new_data.setAttribute("c5",this.c_c5.get())
        new_data.setAttribute("c6",this.c_c6.get())
        this.dbase.getElementsByTagName("spk")[0].appendChild(new_data)
        write_file=open("spk.xml","w")
        this.dbase.writexml(write_file)
        write_file.close()
        this.first_combo()
        this.command_first()
        this.nonactive_combo()
    def command_first(this):
        this.b_simpan.configure(state=DISABLED)
        this.b_edit.configure(state=DISABLED)
        this.b_hapus.configure(state=DISABLED)
        this.b_batal.configure(state=DISABLED)
        this.b_keluar.configure(state=NORMAL)
        this.b_daftar.configure(state=NORMAL)
    def command_new(this):
        this.b_simpan.configure(state=NORMAL)
        this.b_edit.configure(state=DISABLED)
        this.b_hapus.configure(state=DISABLED)
        this.b_batal.configure(state=NORMAL)
        this.b_keluar.configure(state=DISABLED)
        this.b_daftar.configure(state=DISABLED)
    def command_edit(this):
        this.b_simpan.configure(state=DISABLED)
        this.b_edit.configure(state=NORMAL)
        this.b_hapus.configure(state=NORMAL)
        this.b_batal.configure(state=NORMAL)
        this.b_keluar.configure(state=DISABLED)
        this.b_daftar.configure(state=DISABLED)
    def batal(this):
        this.first_combo()
        this.nonactive_combo()
        this.command_first()
        

