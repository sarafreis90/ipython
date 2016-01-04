
# coding: utf-8

# In[ ]:

#This one
from Tkinter import Button
from Tkinter import Scale
from Tkinter import *
import os, re, Tkinter, random
from PIL import Image
from PIL import ImageTk
import glob
import csv
from random import shuffle

# original code from: http://stackoverflow.com/questions/10599771/how-to-loop-through-subfolders-showing-jpg-in-tkinter
class SimpleAppTk(Tkinter.Frame):
    
    def __init__(self,*args,**kwargs):
        
        Tkinter.Frame.__init__(self,*args,**kwargs)
        self.filelist = glob.glob("/Volumes/vph-prism5/Sara/observerStudy/test_images/*.png")  #get your files here
        #self.filelist = glob.glob("/Volumes/UNTITLED/observerStudy/test_images/*.png")
        #self.filelist = glob.glob("/Users/sarareis/Documents/observerStudy/test_images/*.png")
        #self.filelist = glob.glob("/Volumes/vph-prism5/Sara/observerStudy/non_histo_test_images/*.tiff")  #get your files here
        
        self.filelist_pairs = []
        '''
        for p1 in range(len(self.filelist)):
                for p2 in range(p1+1,len(self.filelist)):
                        self.filelist_pairs.append([self.filelist[p1],self.filelist[p2]])
        shuffle(self.filelist_pairs)
        '''
        shuffle(self.filelist, lambda: .5)
        self.filelist_pairs = zip(self.filelist, self.filelist[1:])
        #print self.filelist_pairs
        
        self.i = 0
        self.classification = []
        self.maturity_A = []
        self.maturity_B = []
        self.name1 = []
        self.name2 = []
        self.setup()

        #self.display_next()
        #self.mature()
        #self.immature()
        
        #self.quit()

            
    def setup(self):
        self.Label=Tkinter.Label(self) # widget to display the image 1 on the screen
        self.Label.grid(row=0,column=0)
        
        self.Label2=Tkinter.Label(self) # widget to display the image 2 on the screen
        self.Label2.grid(row=0,column=1)
        
        #Slider button
        self.Slider = Tkinter.Scale(self, from_=-1, to=1, length=500,tickinterval=0.25, resolution=0.25, orient=HORIZONTAL) 
        self.Slider.grid(row=1,column=0, columnspan=2)
        
        ## Labels button
        self.Label3=Tkinter.Label(self, text="'A' is more mature than 'B'") # widget to display the text 
        self.Label3.grid(row=2,column=0)
        
        self.Label4=Tkinter.Label(self, text="Same maturity") # widget to display the text
        self.Label4.grid(row=2,column=0, columnspan=2)
        
        self.Label5=Tkinter.Label(self, text="'B' is more mature than 'A'") # widget to display the text
        self.Label5.grid(row=2,column=1)
        
        ## Next button
        self.Button1 = Tkinter.Button(self,text="Next", command = lambda: self.display_next())
        self.Button1.grid(row=3,column=0, columnspan=3)
        
        ## QUIT button
        self.Quit = Tkinter.Button(self,text="QUIT", command = self.quit)
        self.Quit.grid(row=4,column=0, columnspan=3)
        
        ## Maturity buttons
        self.matureA = Tkinter.Button(self, text="Mature", command = lambda: self.mature_A())
        self.matureA.grid(row=4,column=0)  
        
        self.immatureA = Tkinter.Button(self, text="Immature", command = lambda: self.immature_A())
        self.immatureA.grid(row=5,column=0)
        
        self.matureB = Tkinter.Button(self, text="Mature", command = lambda: self.mature_B())
        self.matureB.grid(row=4,column=1) 
        
        self.immatureB = Tkinter.Button(self, text="Immature", command = lambda: self.immature_B())
        self.immatureB.grid(row=5,column=1)
    
    
    def display_next(self):

        if self.i!= len(self.filelist_pairs):
            f1=self.filelist_pairs[self.i][0]
            f2=self.filelist_pairs[self.i][1]
            '''
            f1=random.choice(self.filelist)
            f2=random.choice(self.filelist)

            print (self.Slider.get()) # get slider value
            self.classification.append(self.Slider.get())
            print self.classification
            '''

            (dirname1, filename1) = os.path.split(f1)
            filename1 = str(os.path.basename(f1))
            filename1 = filename1.replace('.png','')
            self.name1.append(filename1)

            (dirname2, filename2) = os.path.split(f2)
            filename2 = str(os.path.basename(f2))
            filename2 = filename2.replace('.png','')
            self.name2.append(filename2)

            #Create PhotoImage here
            image1=Image.open(f1)
            cropped1=image1.crop((0,0,500,500))
            #resized = photoimage.resize((int(photoimage.size[0]*.3),int(photoimage.size[1]*.2)),Image.ANTIALIAS)
            resized = image1.resize((500,500),Image.ANTIALIAS)
            tkpi = ImageTk.PhotoImage(cropped1)
            self.Label.config(image=tkpi, text="A", compound=Tkinter.TOP)
            self.Label.image=tkpi

            #Create PhotoImage here
            image2=Image.open(f2)
            cropped2=image2.crop((0,0,500,500))
            #resized = photoimage.resize((int(photoimage.size[0]*.3),int(photoimage.size[1]*.2)),Image.ANTIALIAS)
            resized = image2.resize((500,500),Image.ANTIALIAS)
            tkpi = ImageTk.PhotoImage(cropped2)
            self.Label2.config(image=tkpi, text="B", compound=Tkinter.TOP)
            self.Label2.image=tkpi

            print self.name1 #List with filenames displayed as image 'A'
            print self.name2 #List with filenames displayed as image 'B'

            print (self.Slider.get()) # get slider value
            self.classification.append(self.Slider.get())
            print self.classification

            self.i=self.i+1

            self.Slider.set(0) #reset slider to 0.0 
    
    def mature_A(self):
        print "You chose mature." 
        self.maturity_A.append('mature')
        
    def immature_A(self):
        print "You chose immature."
        self.maturity_A.append('immature')

    def mature_B(self):
        print "You chose mature." 
        self.maturity_B.append('mature')
        
    def immature_B(self):
        print "You chose immature." 
        self.maturity_B.append('immature')
        
    def quit(self):
        self.master.destroy()
        print (self.Slider.get()) # get slider value
        self.classification.append(self.Slider.get())
        print self.classification
        
if __name__ == "__main__":
    root=Tkinter.Tk()
    app=SimpleAppTk(root)
    app.grid(row=0,column=0)
    root.mainloop()
    #app.classification.pop([0])
    print app.classification
    
    print app.name1
    print app.name2
    
    dirname = '/Volumes/vph-prism5/Sara/observerStudy/test_images/'
    # dirname = '/Volumes/UNTITLED/observerStudy/test_images/'
    # dirname = '/Volumes/vph-prism5/Sara/observerStudy/non_histo_test_images/'
    image_names = 'image_list.csv'
    classif_rate = 'maturity_rate.csv'
    A_filename = 'image_A.csv'
    B_filename = 'image_B.csv'
    maturity_A_filename = 'maturity_A.csv'
    maturity_B_filename = 'maturity_B.csv'
    
    filelist_csv = os.path.join(dirname, image_names)
    file = open(filelist_csv, "wb")
    writer = csv.writer(file)
    writer.writerow(app.filelist)
    file.close()
    
    rating_csv = os.path.join(dirname, classif_rate)
    file = open(rating_csv, "wb")
    writer = csv.writer(file)
    writer.writerow(app.classification)
    file.close()
    
    A_csv = os.path.join(dirname, A_filename)
    file = open(A_csv, "wb")
    writer = csv.writer(file)
    writer.writerow(app.name1)
    file.close()
    
    B_csv = os.path.join(dirname, B_filename)
    file = open(B_csv, "wb")
    writer = csv.writer(file)
    writer.writerow(app.name2)
    file.close()
    
    class_A_csv = os.path.join(dirname, maturity_A_filename)
    file = open(class_A_csv, "wb")
    writer = csv.writer(file)
    writer.writerow(app.maturity_A)
    file.close()
    
    class_B_csv = os.path.join(dirname, maturity_B_filename)
    file = open(class_B_csv, "wb")
    writer = csv.writer(file)
    writer.writerow(app.maturity_B)
    file.close()

