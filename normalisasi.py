from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import xml.dom.minidom as mndom
import datetime as waktu
from threading import Timer

class normalisasi:
    def __init__(this):
        daftar=Tk()
        daftar.title("Normalisasi")
        this.dbase=mndom.parse("spk.xml")
        c1_max=0.0
        c2_max=0.0
        c3_max=0.0
        c4_max=0.0
        c5_max=0.0
        c6_max=0.0
        nilai_c1=0.0
        nilai_c2=0.0
        nilai_c3=0.0
        nilai_c4=0.0
        nilai_c5=0.0
        nilai_c6=0.0
        type_c1=this.dbase.getElementsByTagName("kriteria")[0].getAttribute("tipe")
        type_c2=this.dbase.getElementsByTagName("kriteria")[1].getAttribute("tipe")
        type_c3=this.dbase.getElementsByTagName("kriteria")[2].getAttribute("tipe")
        type_c4=this.dbase.getElementsByTagName("kriteria")[3].getAttribute("tipe")
        type_c5=this.dbase.getElementsByTagName("kriteria")[4].getAttribute("tipe")
        type_c6=this.dbase.getElementsByTagName("kriteria")[5].getAttribute("tipe")
        list_nilai_max=this.dbase.getElementsByTagName("nilai")
        for ls_ni_m in list_nilai_max:
            if(type_c1=="C"):
                if(c1_max==0.0):
                    c1_max=ls_ni_m.getAttribute("c1")
                else:
                    if(ls_ni_m.getAttribute("c1")<c1_max):
                        c1_max=ls_ni_m.getAttribute("c1")
            elif(type_c1=="B"):
                if(c1_max==0.0):
                    c1_max=ls_ni_m.getAttribute("c1")
                else:
                    if(ls_ni_m.getAttribute("c1")>c1_max):
                        c1_max=ls_ni_m.getAttribute("c1")
            if(type_c2=="C"):
                if(c2_max==0.0):
                    c2_max=ls_ni_m.getAttribute("c2")
                else:
                    if(ls_ni_m.getAttribute("c2")<c2_max):
                        c2_max=ls_ni_m.getAttribute("c2")
            elif(type_c2=="B"):
                if(c2_max==0.0):
                    c2_max=ls_ni_m.getAttribute("c2")
                else:
                    if(ls_ni_m.getAttribute("c2")>c2_max):
                        c2_max=ls_ni_m.getAttribute("c2")
            if(type_c3=="C"):
                if(c3_max==0.0):
                    c3_max=ls_ni_m.getAttribute("c3")
                else:
                    if(ls_ni_m.getAttribute("c3")<c3_max):
                        c3_max=ls_ni_m.getAttribute("c3")
            elif(type_c3=="B"):
                if(c3_max==0.0):
                    c3_max=ls_ni_m.getAttribute("c3")
                else:
                    if(ls_ni_m.getAttribute("c3")>c3_max):
                        c3_max=ls_ni_m.getAttribute("c3")
            if(type_c4=="C"):
                if(c4_max==0.0):
                    c4_max=ls_ni_m.getAttribute("c4")
                else:
                    if(ls_ni_m.getAttribute("c4")<c4_max):
                        c4_max=ls_ni_m.getAttribute("c4")
            elif(type_c4=="B"):
                if(c4_max==0.0):
                    c4_max=ls_ni_m.getAttribute("c4")
                else:
                    if(ls_ni_m.getAttribute("c4")>c4_max):
                        c4_max=ls_ni_m.getAttribute("c4")
            if(type_c5=="C"):
                if(c5_max==0.0):
                    c5_max=ls_ni_m.getAttribute("c5")
                else:
                    if(ls_ni_m.getAttribute("c5")<c5_max):
                        c5_max=ls_ni_m.getAttribute("c5")
            elif(type_c5=="B"):
                if(c5_max==0.0):
                    c5_max=ls_ni_m.getAttribute("c5")
                else:
                    if(ls_ni_m.getAttribute("c5")>c5_max):
                        c5_max=ls_ni_m.getAttribute("c5")
            if(type_c6=="C"):
                if(c6_max==0.0):
                    c6_max=ls_ni_m.getAttribute("c6")
                else:
                    if(ls_ni_m.getAttribute("c6")<c6_max):
                        c6_max=ls_ni_m.getAttribute("c6")
            elif(type_c6=="B"):
                if(c6_max==0.0):
                    c6_max=ls_ni_m.getAttribute("c6")
                else:
                    if(ls_ni_m.getAttribute("c6")>c6_max):
                        c6_max=ls_ni_m.getAttribute("c6")
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
            if(type_c1=="B"):
                nilai_c1=(float(ls_ni.getAttribute("c1"))/float(c1_max))
            elif(type_c1=="C"):
                nilai_c1=(float(c1_max)/float(ls_ni.getAttribute("c1")))
            if(type_c2=="B"):
                nilai_c2=(float(ls_ni.getAttribute("c2"))/float(c2_max))
            elif(type_c2=="C"):
                nilai_c2=(float(c2_max)/float(ls_ni.getAttribute("c2")))
            if(type_c3=="B"):
                nilai_c3=(float(ls_ni.getAttribute("c3"))/float(c3_max))
            elif(type_c3=="C"):
                nilai_c3=(float(c3_max)/float(ls_ni.getAttribute("c3")))
            if(type_c4=="B"):
                nilai_c4=(float(ls_ni.getAttribute("c4"))/float(c4_max))
            elif(type_c4=="C"):
                nilai_c4=(float(c4_max)/float(ls_ni.getAttribute("c4")))
            if(type_c5=="B"):
                nilai_c5=(float(ls_ni.getAttribute("c5"))/float(c5_max))
            elif(type_c5=="C"):
                nilai_c5=(float(c5_max)/float(ls_ni.getAttribute("c5")))
            if(type_c6=="B"):
                nilai_c6=(float(ls_ni.getAttribute("c6"))/float(c6_max))
            elif(type_c6=="C"):
                nilai_c6=(float(c6_max)/float(ls_ni.getAttribute("c6")))
            t_c1=Label(daftar,text=('{:.2f}'.format(nilai_c1)))
            t_c2=Label(daftar,text=('{:.2f}'.format(nilai_c2)))
            t_c3=Label(daftar,text=('{:.2f}'.format(nilai_c3)))
            t_c4=Label(daftar,text=('{:.2f}'.format(nilai_c4)))
            t_c5=Label(daftar,text=('{:.2f}'.format(nilai_c5)))
            t_c6=Label(daftar,text=('{:.2f}'.format(nilai_c6)))
            t_nama.grid(column=0,row=i)
            t_c1.grid(column=2,row=i)
            t_c2.grid(column=4,row=i)
            t_c3.grid(column=6,row=i)
            t_c4.grid(column=8,row=i)
            t_c5.grid(column=10,row=i)
            t_c6.grid(column=12,row=i)
            i=i+1
        daftar.mainloop()



