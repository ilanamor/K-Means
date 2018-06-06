import tkFileDialog
import tkMessageBox

from CleanData import *
from Clustering import *
import pandas as pd
from Tkinter import *


class KmeansClustering:

    #data member
    file_path= ""
    n_clusters = 0
    n_init = 0
    df = None
    clustering = None
    cleanData = None

    # Initialize the GUI
    def __init__(self, master):
        self.master = master
        master.title("K Means Clustering")
        master.geometry("1000x650")

        # <editor-fold desc="init buttons, labels and entries">
        self.labelPath = Label(master, text="File Path:")
        self.entryPath = Entry(master, width=70)
        self.browse_button = Button(master, text="Browse", width=10, command=self.choosefile)
        self.browse_button.pack()

        self.labelClusterNum = Label(master, text="Num of cluster k:")
        self.entryClusterNum = Entry(master, width=20, validate="key")

        self.labelInitNum = Label(master, text="Num of runs:")
        self.entryInitNum = Entry(master, width=20, validate="key")

        self.clean_button = Button(master, text="Pre-process", width=20, command=self.clean)
        self.clean_button.pack()

        self.cluster_button = Button(master, text="Cluster", width=20, command=self.cluster, state=DISABLED)
        self.cluster_button.pack()

        self.close_button = Button(master, text="Exit", width=10, command=master.quit)
        self.close_button.pack()
        # </editor-fold>
        # Define grid
        self.gridDefinition(master)
        # layout the controls in the grid
        self.controlsLayout()

        # <editor-fold desc="Gui Functions">
    def controlsLayout(self):
        self.labelPath.grid(row=1, column=0, sticky=E)
        self.entryPath.grid(row=1, column=1, columnspan=2, sticky=W)
        self.browse_button.grid(row=1, column=3, sticky=W)
        self.labelClusterNum.grid(row=2, column=0, sticky=E)
        self.entryClusterNum.grid(row=2, column=1, sticky=W)
        self.labelInitNum.grid(row=3, column=0, sticky=E)
        self.entryInitNum.grid(row=3, column=1, sticky=W)
        self.clean_button.grid(row=5, column=1, columnspan=2)
        self.cluster_button.grid(row=6, column=1, columnspan=2)
        self.close_button.grid(row=7, column=1, columnspan=2)

    def gridDefinition(self, master):
        master.grid_rowconfigure(0, weight=2)
        master.grid_rowconfigure(1, weight=1)
        master.grid_rowconfigure(2, weight=1)
        master.grid_rowconfigure(3, weight=1)
        master.grid_rowconfigure(4, weight=1)
        master.grid_rowconfigure(5, weight=1)
        master.grid_rowconfigure(6, weight=1)
        master.grid_rowconfigure(7, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)
        master.grid_columnconfigure(2, weight=1)
        master.grid_columnconfigure(3, weight=2)
        # </editor-fold>

    def choosefile(self):
        self.file_path = tkFileDialog.askopenfilename()
        self.entryPath.delete(0, END)
        self.entryPath.insert(0, self.file_path)

        if (not self.file_path):
            #tkMessageBox.showinfo("K Means Clustering", "insert a file")
            return

        if( not (self.file_path[-5:]==".xlsx" or self.file_path[-4:]==".xls")):
            tkMessageBox.showinfo("K Means Clustering", "insert an excel file")
            return

        self.df = pd.read_excel(self.file_path)

        if self.df.empty:
            tkMessageBox.showinfo("K Means Clustering", "invalid file!")
            return


    def clean(self):
        if self.validate(self.entryClusterNum.get(), self.entryInitNum.get(), self.file_path):
            self.dataCleaner = CleanData(self.df).Clean()
            tkMessageBox.showinfo("K Means Clustering", "Preprocessing completed successfully!")
            self.cluster_button.config(state=NORMAL)
    def cluster(self):
        return

    def validate(self, cluster, init, path):
        if  (path==""):  # the field is being cleared
            tkMessageBox.showinfo("K Means Clustering", "Please enter path")
            return False
        if not cluster and not init:  # the field is being cleared
            tkMessageBox.showinfo("K Means Clustering", "Please enter values")
            return False
        if not cluster:  # the field is being cleared
            tkMessageBox.showinfo("K Means Clustering", "Please enter number of clusters")
            return False
        if not init:  # the field is being cleared
            tkMessageBox.showinfo("K Means Clustering", "Please enter number of runs")
            return False
        try:
            self.n_clusters = int(cluster)
            self.n_init = int(init)
            # check validate number
            if self.n_clusters < 1:
                tkMessageBox.showinfo("K Means Clustering", "The number for clusters should be bigger than 0")
                return False
            elif self.n_clusters > len(self.df.columns):
                tkMessageBox.showinfo("K Means Clustering", "Num of clusters shouldn't be higher then the number of columns")
                return False
            elif self.n_init < 1:
                tkMessageBox.showinfo("K Means Clustering", "The number for runs should be bigger than 0")
                return False
            else:
                return True

        except ValueError:
            tkMessageBox.showinfo("K Means Clustering",
                                  "Invalid input - Please enter a number")
            return False

    '''df = pd.read_excel("data.xlsx")
    dataCleaner = CleanData(df).Clean()
    clustering = Clustering(dataCleaner,6,3)
    table=clustering.calcKmeans()
    clustering.horoplethMap()
    print "xxxx"'''

root = Tk()
my_gui = KmeansClustering(root)
root.mainloop()