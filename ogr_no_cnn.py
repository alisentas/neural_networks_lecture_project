from tkinter import *
import os
from keras.models import load_model
from PIL import Image
import numpy
import sqlite3


class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()

        self.numl1 = Label(self.root, text="#")
        self.numl1.grid(row=0, column=1)

        self.numl2 = Label(self.root, text="#")
        self.numl2.grid(row=0, column=2)

        self.numl3 = Label(self.root, text="#")
        self.numl3.grid(row=0, column=3)

        self.numl4 = Label(self.root, text="#")
        self.numl4.grid(row=0, column=4)

        self.numl5 = Label(self.root, text="#")
        self.numl5.grid(row=0, column=5)

        self.numl6 = Label(self.root, text="#")
        self.numl6.grid(row=0, column=6)

        self.numl7 = Label(self.root, text="#")
        self.numl7.grid(row=0, column=7)

        self.numl8 = Label(self.root, text="#")
        self.numl8.grid(row=0, column=8)

        self.numl9 = Label(self.root, text="#")
        self.numl9.grid(row=0, column=9)

        self.num1 = Canvas(self.root, bg='white', width=140, height=140)
        self.num1.grid(row=1, column=1)

        self.num2 = Canvas(self.root, bg='white', width=140, height=140)
        self.num2.grid(row=1, column=2)

        self.num3 = Canvas(self.root, bg='white', width=140, height=140)
        self.num3.grid(row=1, column=3)

        self.num4 = Canvas(self.root, bg='white', width=140, height=140)
        self.num4.grid(row=1, column=4)

        self.num5 = Canvas(self.root, bg='white', width=140, height=140)
        self.num5.grid(row=1, column=5)

        self.num6 = Canvas(self.root, bg='white', width=140, height=140)
        self.num6.grid(row=1, column=6)

        self.num7 = Canvas(self.root, bg='white', width=140, height=140)
        self.num7.grid(row=1, column=7)

        self.num8 = Canvas(self.root, bg='white', width=140, height=140)
        self.num8.grid(row=1, column=8)

        self.num9 = Canvas(self.root, bg='white', width=140, height=140)
        self.num9.grid(row=1, column=9)

        self.ogrenci_no = Label(self.root, text="#########")
        self.ogrenci_no.grid(row=2, column=1)

        self.ogrenci_adi = Label(self.root, text="numaralı öğrenci: yok")
        self.ogrenci_adi.grid(row=2, column=2)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.model = load_model("model_cnn.h5")
        self.ogr_nos = [140201037,
                        140201001,
                        140201002,
                        140201004,
                        140201005,
                        140201008,
                        140201009,
                        140201011,
                        140201012,
                        140201015,
                        140201018,
                        140201020,
                        140201031,
                        140201032,
                        140201034,
                        140201035,
                        140201040,
                        140201041,
                        140201044,
                        140201047,
                        140201050,
                        140201051,
                        140201052,
                        140201053,
                        140201054,
                        140201055,
                        140201056,
                        140201062,
                        140201064,
                        140201069,
                        140201070,
                        140201072,
                        140201074,
                        140201075,
                        140201076,
                        140201077,
                        140201078,
                        140201079,
                        140201080,
                        140201081,
                        140201082,
                        140201083,
                        140201085,
                        140201091,
                        140201093,
                        140201098,
                        140201106,
                        140201003,
                        140201013,
                        140201014,
                        140201016,
                        140201019,
                        140201025,
                        140201026,
                        140201027,
                        140201036,
                        140201038,
                        140201039,
                        140201042,
                        140201043,
                        140201057,
                        140201061,
                        140201067,
                        140201071,
                        140201073,
                        140201084,
                        140201099,
                        140201100,
                        140201101,
                        140201103,
                        140201105,
                        140201107,
                        140201119,
                        140201134,
                        140201134,
                        ]
        self.ogr_names = ["Ali Şentaş",
                          "Hüsnü Mert Polat",
                          "Ahmet Niyazi Eyiokur",
                          "Tolunay Tezcan",
                          "Umut Kaymak",
                          "Yunus Dönmez",
                          "Zeliha Solmaz",
                          "Kevser Sertel",
                          "Doğukan Polat",
                          "Mahiye Büsra Gökle",
                          "Furkan Hasan Şekerci",
                          "Ayegül Veyisoğlu",
                          "Gürkan Akdeniz",
                          "İsmail Yıldırım",
                          "Tuğba Seven",
                          "Fatmanur Küçükayvaz",
                          "Gülsüm Kök",
                          "Emine Turğay",
                          "Yasin Talha Akman",
                          "Bahar Kılıç",
                          "Çiller Taş",
                          "Onur Karakaya",
                          "Can Özer",
                          "Elif Bilge Şahin",
                          "Hilal Arslan",
                          "Muhammet Seymen",
                          "Ayşenur Kayabaşı",
                          "Hüseyin Emre Özhan",
                          "Mücahit Talha Baki",
                          "Kübra Surat",
                          "Miraç Arslan",
                          "İmdat Enes Yılmaz",
                          "Gamze Çalışkan",
                          "Hatize Zeren",
                          "Dilek Şaylan",
                          "Arda Şahin",
                          "Çağrı Kızılkan",
                          "Gökay Gök",
                          "Oğuzhan Mevsim",
                          "Fatma Yılmaz",
                          "Sümeyra Çakmak",
                          "Melek Pazarbaşı",
                          "Mert Can Balcı",
                          "Ömürcan Aktemur",
                          "Barış Alpaydın",
                          "Kutluhan Aygür",
                          "Hasan Kandil",
                          "Ozan Meral",
                          "Emircan Uzel",
                          "Emin Yıldız",
                          "Onurkan Eyüboğlu",
                          "Neslihan Usta",
                          "Berat Can Topal",
                          "Metin Işık",
                          "Umut Canbolat",
                          "İnanç Yücel",
                          "Halil Arslan",
                          "Muhammed Ensar Özer",
                          "Furkan Topuz",
                          "Uğur Avcı",
                          "Ahmet Salih Elibol",
                          "İlker Aksu",
                          "Dabut Eryılmaz",
                          "Murat Akçam",
                          "Utkı Güler",
                          "Yasemir Büşra Nur Uyanık",
                          "Hakan Yerlikaya",
                          "Emrah Gümüş",
                          "Nursel Akay",
                          "Fatih Dindarol",
                          "Renas Salman",
                          "Selman Akbulut",
                          "Cafer Avcı",
                          "Hasan Basri Şahin"
                          ]
        self.changed = [False, False, False, False, False, False, False, False, False, False]
        self.old_x1 = None
        self.old_y1 = None
        self.old_x2 = None
        self.old_y2 = None
        self.old_x3 = None
        self.old_y3 = None
        self.old_x4 = None
        self.old_y4 = None
        self.old_x5 = None
        self.old_y5 = None
        self.old_x6 = None
        self.old_y6 = None
        self.old_x7 = None
        self.old_y7 = None
        self.old_x8 = None
        self.old_y8 = None
        self.old_x9 = None
        self.old_y9 = None
        self.line_width = 10
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.num1.bind('<B1-Motion>', self.paint1)
        self.num1.bind('<ButtonRelease-1>', self.reset)
        self.num1.bind('<ButtonRelease-3>', self.clear1)
        self.num2.bind('<B1-Motion>', self.paint2)
        self.num2.bind('<ButtonRelease-1>', self.reset)
        self.num2.bind('<ButtonRelease-3>', self.clear2)
        self.num3.bind('<B1-Motion>', self.paint3)
        self.num3.bind('<ButtonRelease-1>', self.reset)
        self.num3.bind('<ButtonRelease-3>', self.clear3)
        self.num4.bind('<B1-Motion>', self.paint4)
        self.num4.bind('<ButtonRelease-1>', self.reset)
        self.num4.bind('<ButtonRelease-3>', self.clear4)
        self.num5.bind('<B1-Motion>', self.paint5)
        self.num5.bind('<ButtonRelease-1>', self.reset)
        self.num5.bind('<ButtonRelease-3>', self.clear5)
        self.num6.bind('<B1-Motion>', self.paint6)
        self.num6.bind('<ButtonRelease-1>', self.reset)
        self.num6.bind('<ButtonRelease-3>', self.clear6)
        self.num7.bind('<B1-Motion>', self.paint7)
        self.num7.bind('<ButtonRelease-1>', self.reset)
        self.num7.bind('<ButtonRelease-3>', self.clear7)
        self.num8.bind('<B1-Motion>', self.paint8)
        self.num8.bind('<ButtonRelease-1>', self.reset)
        self.num8.bind('<ButtonRelease-3>', self.clear8)
        self.num9.bind('<B1-Motion>', self.paint9)
        self.num9.bind('<ButtonRelease-1>', self.reset)
        self.num9.bind('<ButtonRelease-3>', self.clear9)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint1(self, event):
        paint_color = 'black'
        if self.old_x1 and self.old_y1:
            self.num1.create_line(self.old_x1, self.old_y1, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
            self.changed[1] = True
        self.old_x1 = event.x
        self.old_y1 = event.y

    def paint2(self, event):
        paint_color = 'black'
        if self.old_x2 and self.old_y2:
            self.num2.create_line(self.old_x2, self.old_y2, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
            self.changed[2] = True
        self.old_x2 = event.x
        self.old_y2 = event.y

    def paint3(self, event):
        paint_color = 'black'
        if self.old_x3 and self.old_y3:
            self.num3.create_line(self.old_x3, self.old_y3, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
            self.changed[3] = True
        self.old_x3 = event.x
        self.old_y3 = event.y

    def paint4(self, event):
        paint_color = 'black'
        if self.old_x4 and self.old_y4:
            self.num4.create_line(self.old_x4, self.old_y4, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
            self.changed[4] = True
        self.old_x4 = event.x
        self.old_y4 = event.y

    def paint5(self, event):
        paint_color = 'black'
        if self.old_x5 and self.old_y5:
            self.num5.create_line(self.old_x5, self.old_y5, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
            self.changed[5] = True
        self.old_x5 = event.x
        self.old_y5 = event.y

    def paint6(self, event):
        paint_color = 'black'
        if self.old_x6 and self.old_y6:
            self.num6.create_line(self.old_x6, self.old_y6, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
            self.changed[6] = True
        self.old_x6 = event.x
        self.old_y6 = event.y

    def paint7(self, event):
        paint_color = 'black'
        if self.old_x7 and self.old_y7:
            self.num7.create_line(self.old_x7, self.old_y7, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
            self.changed[7] = True
        self.old_x7 = event.x
        self.old_y7 = event.y

    def paint8(self, event):
        paint_color = 'black'
        if self.old_x8 and self.old_y8:
            self.num8.create_line(self.old_x8, self.old_y8, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
            self.changed[8] = True
        self.old_x8 = event.x
        self.old_y8 = event.y

    def paint9(self, event):
        paint_color = 'black'
        if self.old_x9 and self.old_y9:
            self.num9.create_line(self.old_x9, self.old_y9, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
            self.changed[9] = True
        self.old_x9 = event.x
        self.old_y9 = event.y

    def clear1(self, event):
        self.num1.delete('all')
        self.numl1.config(text="#")
        self.reset(False)

    def clear2(self, event):
        self.num2.delete('all')
        self.numl2.config(text="#")
        self.reset(False)

    def clear3(self, event):
        self.num3.delete('all')
        self.numl3.config(text="#")
        self.reset(False)

    def clear4(self, event):
        self.num4.delete('all')
        self.numl4.config(text="#")
        self.reset(False)

    def clear5(self, event):
        self.num5.delete('all')
        self.numl5.config(text="#")
        self.reset(False)

    def clear6(self, event):
        self.num6.delete('all')
        self.numl6.config(text="#")
        self.reset(False)

    def clear7(self, event):
        self.num7.delete('all')
        self.numl7.config(text="#")
        self.reset(False)

    def clear8(self, event):
        self.num8.delete('all')
        self.numl8.config(text="#")
        self.reset(False)

    def clear9(self, event):
        self.num9.delete('all')
        self.numl9.config(text="#")
        self.reset(False)

    def reset(self, event):
        self.old_x1, self.old_y1 = None, None
        self.old_x2, self.old_y2 = None, None
        self.old_x3, self.old_y3 = None, None
        self.old_x4, self.old_y4 = None, None
        self.old_x5, self.old_y5 = None, None
        self.old_x6, self.old_y6 = None, None
        self.old_x7, self.old_y7 = None, None
        self.old_x8, self.old_y8 = None, None
        self.old_x9, self.old_y9 = None, None

        if self.changed[1]:
            self.num1.postscript(file="sayi.ps", colormode='color')
            os.system("convert sayi.ps sayi.jpg")
            os.system("convert -negate -resize 28x28 sayi.jpg sayi.jpg")
            jpg = Image.open("sayi.jpg")
            os.system("rm sayi.ps sayi.jpg")
            input = numpy.array([numpy.array([numpy.array(list(jpg.getdata())) / 255], dtype='float32').reshape((28,28,1))])
            self.numl1.config(text=str(self.get_answer(self.model.predict(input)[0])))
            self.changed[1] = False

        if self.changed[2]:
            self.num2.postscript(file="sayi.ps", colormode='color')
            os.system("convert sayi.ps sayi.jpg")
            os.system("convert -negate -resize 28x28 sayi.jpg sayi.jpg")
            jpg = Image.open("sayi.jpg")
            os.system("rm sayi.ps sayi.jpg")
            input = numpy.array([numpy.array([numpy.array(list(jpg.getdata())) / 255], dtype='float32').reshape((28,28,1))])
            self.numl2.config(text=str(self.get_answer(self.model.predict(input)[0])))
            self.changed[2] = False

        if self.changed[3]:
            self.num3.postscript(file="sayi.ps", colormode='color')
            os.system("convert sayi.ps sayi.jpg")
            os.system("convert -negate -resize 28x28 sayi.jpg sayi.jpg")
            jpg = Image.open("sayi.jpg")
            os.system("rm sayi.ps sayi.jpg")
            input = numpy.array([numpy.array([numpy.array(list(jpg.getdata())) / 255], dtype='float32').reshape((28,28,1))])
            self.numl3.config(text=str(self.get_answer(self.model.predict(input)[0])))
            self.changed[3] = False

        if self.changed[4]:
            self.num4.postscript(file="sayi.ps", colormode='color')
            os.system("convert sayi.ps sayi.jpg")
            os.system("convert -negate -resize 28x28 sayi.jpg sayi.jpg")
            jpg = Image.open("sayi.jpg")
            input = numpy.array([numpy.array([numpy.array(list(jpg.getdata())) / 255], dtype='float32').reshape((28,28,1))])
            self.numl4.config(text=str(self.get_answer(self.model.predict(input)[0])))
            self.changed[4] = False

        if self.changed[5]:
            self.num5.postscript(file="sayi.ps", colormode='color')
            os.system("convert sayi.ps sayi.jpg")
            os.system("convert -negate -resize 28x28 sayi.jpg sayi.jpg")
            jpg = Image.open("sayi.jpg")
            os.system("rm sayi.ps sayi.jpg")
            input = numpy.array([numpy.array([numpy.array(list(jpg.getdata())) / 255], dtype='float32').reshape((28,28,1))])
            self.numl5.config(text=str(self.get_answer(self.model.predict(input)[0])))
            self.changed[5] = False

        if self.changed[6]:
            self.num6.postscript(file="sayi.ps", colormode='color')
            os.system("convert sayi.ps sayi.jpg")
            os.system("convert -negate -resize 28x28 sayi.jpg sayi.jpg")
            jpg = Image.open("sayi.jpg")
            os.system("rm sayi.ps sayi.jpg")
            input = numpy.array([numpy.array([numpy.array(list(jpg.getdata())) / 255], dtype='float32').reshape((28,28,1))])
            self.numl6.config(text=str(self.get_answer(self.model.predict(input)[0])))
            self.changed[6] = False

        if self.changed[7]:
            self.num7.postscript(file="sayi.ps", colormode='color')
            os.system("convert sayi.ps sayi.jpg")
            os.system("convert -negate -resize 28x28 sayi.jpg sayi.jpg")
            jpg = Image.open("sayi.jpg")
            os.system("rm sayi.ps sayi.jpg")
            input = numpy.array([numpy.array([numpy.array(list(jpg.getdata())) / 255], dtype='float32').reshape((28,28,1))])
            self.numl7.config(text=str(self.get_answer(self.model.predict(input)[0])))
            self.changed[7] = False

        if self.changed[8]:
            self.num8.postscript(file="sayi.ps", colormode='color')
            os.system("convert sayi.ps sayi.jpg")
            os.system("convert -negate -resize 28x28 sayi.jpg sayi.jpg")
            jpg = Image.open("sayi.jpg")
            os.system("rm sayi.ps sayi.jpg")
            input = numpy.array([numpy.array([numpy.array(list(jpg.getdata())) / 255], dtype='float32').reshape((28,28,1))])
            self.numl8.config(text=str(self.get_answer(self.model.predict(input)[0])))
            self.changed[8] = False

        if self.changed[9]:
            self.num9.postscript(file="sayi.ps", colormode='color')
            os.system("convert sayi.ps sayi.jpg")
            os.system("convert -negate -resize 28x28 sayi.jpg sayi.jpg")
            jpg = Image.open("sayi.jpg")
            os.system("rm sayi.ps sayi.jpg")
            input = numpy.array([numpy.array([numpy.array(list(jpg.getdata())) / 255], dtype='float32').reshape((28,28,1))])
            self.numl9.config(text=str(self.get_answer(self.model.predict(input)[0])))
            self.changed[9] = False

        ogr_no = ""
        ogr_no += self.numl1['text']
        ogr_no += self.numl2['text']
        ogr_no += self.numl3['text']
        ogr_no += self.numl4['text']
        ogr_no += self.numl5['text']
        ogr_no += self.numl6['text']
        ogr_no += self.numl7['text']
        ogr_no += self.numl8['text']
        ogr_no += self.numl9['text']
        self.ogrenci_no.config(text=ogr_no)

        if '#' not in ogr_no:
            for i in range(len(self.ogr_nos)):
                if self.ogr_nos[i] == int(ogr_no):
                    self.ogrenci_adi.config(text=self.ogr_names[i])
        else:
            self.ogrenci_adi.config(text="numaralı öğrenci: yok")

    def get_answer(self, nparray):
        max_i = 0
        max_v = nparray[0]
        for i in range(1, 10):
            if nparray[i] > max_v:
                max_v = nparray[i]
                max_i = i
        return max_i


if __name__ == '__main__':
    Paint()
