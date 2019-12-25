import xml.dom.minidom as mndom
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import datetime as waktu
from threading import Timer

class Karyawan:
	def save_data(this):
		this.dbase=mndom.parse("spk.xml")
		new_data=this.dbase.createElement("karyawan")
		new_data.setAttribute("kode_karyawan",this.t_kode.get())
		new_data.setAttribute("kode_karyawan",this.t_nama.get())
		jenis_kelamin=this.c_jk.get()
		jekel=jenis_kelamin.split("_")
		new_data.setAttribute("kd_kar",this.t_kode.get())
		new_data.setAttribute("nm_kar",this.t_nama.get())
		new_data.setAttribute("jekel",jekel[0])
		new_data.setAttribute("alt",this.t_alt.get())
		this.dbase.getElementsByTagName("dbspk")[0].appendChild(new_data)
		isi_file=open("spk.xml","w")
		this.dbase.writexml(isi_file)
		isi_file.close()
		this.t_kode.delete(0, END)
		this.t_nama.delete(0, END)
		this.t_alt.delete(0, END)
		this.c_jk.current(0)
	def check_code(this,aaa):
		this.dbase=mndom.parse("spk.xml")
		i=0
		ii=0
		av=0
		kode_item=this.dbase.getElementsByTagName("karyawan")
		for kd in kode_item:
			if (kd.getAttribute("kd_kar")==this.t_kode.get()):
				ii=i
				av=1
			i=i+1
		if (av==1):
			this.t_nama.insert(INSERT,kode_item[ii].getAttribute("nm_kar"))
			this.t_alt.insert(INSERT,kode_item[ii].getAttribute("alt"))
			if(kode_item[ii]=="L"):
				this.c_jk.current(0)
			else:
				this.c_jk.current(1)
		else:
			this.t_nama.focus()

	def __init__(this):
		this.jekel=[]
		this.jekel.append("L_laki-laki")
		this.jekel.append("P_perempuan")
		this.win=Tk()
		this.l_kode=Label(this.win,text="Kode Karyawan")
		this.l_nama=Label(this.win,text="Nama Karyawan")
		this.l_jk=Label(this.win,text="Jenis Kelamin")
		this.l_alt=Label(this.win,text="Alamat")
		this.t_kode=Entry(this.win,text="")
		this.t_nama=Entry(this.win,text="")
		this.c_jk=Combobox(this.win)
		this.c_jk['values']=this.jekel
		this.t_alt=Entry(this.win,text="")
		this.b_simpan=Button(this.win,text="Simpan",command=this.save_data)
		this.b_edit=Button(this.win,text="Edit")
		this.b_hapus=Button(this.win,text="Hapus")
		this.b_batal=Button(this.win,text="Batal")
		this.b_keluar=Button(this.win,text="Keluar",command=this.win.destroy)
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
		this.b_keluar.grid(column=0,row=6)
		this.t_kode.bind('<Return>',this.check_code)
		this.win.mainloop()

karyawan=Karyawan()
karyawan()
