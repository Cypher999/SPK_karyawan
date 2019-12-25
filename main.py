from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import xml.dom.minidom as dbase
import hasil_penilaian as hasil_pen
import karyawan as kar
import kriteria as krit
import normalisasi as norm
import penilaian as pen
import perangkingan as rank
import cetak_lap as cetak
win=Tk()
win.title("SPK Kinerja Karyawan")
win.geometry("640x320")
mn=Menu(win)
mn_file=Menu(mn,tearoff=0)
mn_res=Menu(mn,tearoff=0)
mn_ctk=Menu(mn,tearoff=0)
mn_file.add_command(label="Data Karyawan",command=kar.karyawan)
mn_file.add_separator()
mn_file.add_command(label="Data Kriteria",command=krit.kriteria)
mn_res.add_command(label="Penilaian",command=pen.penilaian)
mn_res.add_separator()
mn_res.add_command(label="Normalisasi",command=norm.normalisasi)
mn_res.add_separator()
mn_res.add_command(label="Hasil penilaian",command=hasil_pen.hasil_penilaian)
mn_res.add_separator()
mn_res.add_command(label="Perangkingan",command=rank.perangkingan)
mn_res.add_separator()
mn_res.add_command(label="Print laporan",command=cetak.open_file)
mn.add_cascade(label="Menu Data",menu=mn_file)
mn.add_cascade(label="Menu Penilaian",menu=mn_res)
win.config(menu=mn)
mn.mainloop()
