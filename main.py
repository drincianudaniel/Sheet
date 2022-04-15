from tkinter import *
import sys

def start(): # function to start the program
    global window
    window = Tk()
    window.title("Sheet")
    window.geometry("600x400")
    window.resizable(False, False)
    text_var = []
    entries = []


    # function to get the matrix
    def get_mat():
        matrix = []
        for i in range(int(rows.get())):
            matrix.append([])
            for j in range(int(cols.get())):
                matrix[i].append(text_var[i][j].get())

        return matrix

    # function for sum
    def sumZone(stringDate):
        rez = stringDate.split(":")
        parametrii = []
        for elem in rez:
            parametrii.append(translate(elem[1]))
            parametrii.append(translate(elem[0]))
        sum = int(0)
        matrix = get_mat()
        for i in range(parametrii[0], int(parametrii[2])+1):
            for j in range(parametrii[1], int(parametrii[3])+1):
                if (matrix[i][j] == ''):
                    temp = 0
                else:
                    temp = int(matrix[i][j])
                sum += temp
        return sum

    # function for max
    def maxSheet(stringDate):
        rez = stringDate.split(":")
        parametrii = []
        for elem in rez:
            parametrii.append(translate(elem[1]))
            parametrii.append(translate(elem[0]))
        matrix = get_mat()
        largest = 0
        count = 0
        for i in range(parametrii[0], int(parametrii[2])+1):
            for j in range(parametrii[1], int(parametrii[3])+1):
                if (matrix[i][j] == ''):
                    temp = 0
                else:
                    temp = int(matrix[i][j])
                    if count == 0:
                        largest = temp
                        count = 1
                    if temp > largest:
                        largest = temp
        return largest

    # function for min
    def minSheet(stringDate):
        rez = stringDate.split(":")
        parametrii = []
        for elem in rez:
            parametrii.append(translate(elem[1]))
            parametrii.append(translate(elem[0]))
        matrix = get_mat()
        smallest = 0
        count = 0
        for i in range(parametrii[0], int(parametrii[2])+1):
            for j in range(parametrii[1], int(parametrii[3])+1):
                    if (matrix[i][j] == ''):
                        temp = 0
                    else:
                        temp = int(matrix[i][j])
                        if count == 0:
                            smallest = temp
                            count = 1
                        if temp < smallest:
                            smallest = temp
        return smallest

    #function for avg
    def avgSheet(stringDate):
        rez = stringDate.split(":")
        parametrii = []
        for elem in rez:
            parametrii.append(translate(elem[1]))
            parametrii.append(translate(elem[0]))
        matrix = get_mat()
        avgsum = 0
        count = 0
        for i in range(parametrii[0], int(parametrii[2])+1):
            for j in range(parametrii[1], int(parametrii[3])+1):
                if (matrix[i][j] == ''):
                    temp = 0
                else:
                    temp = int(matrix[i][j])
                    avgsum = (avgsum + temp)
        avgsum = avgsum / ((abs(parametrii[2] - parametrii[0]) + 1) * (abs(parametrii[3] - parametrii[1]) + 1))
        return avgsum


    # function to translate matrix index
    def translate(caract):
        if str.isdecimal(caract):
            return int(caract) - 1
        else:
            return ord(caract) - ord("A")


    # function to create the sheet
    def Sheet(rows, cols):
        nrcrt = 1
        letter = 'A'
        x2 = 0
        y2 = 0
        for i in range(rows):
            text_var.append([])
            entries.append([])
            Label(window, text=nrcrt).place(x=45 + x2, y=47 + y2)
            nrcrt = nrcrt + 1
            for j in range(cols):
                text_var[i].append(StringVar())
                entries[i].append(Entry(window, textvariable=text_var[i][j],width=4))
                entries[i][j].place(x=60 + x2, y=50 + y2)
                x2 += 30
                if i == 0:
                    Label(window, text=letter).place(x=32 + x2, y=28 + y2)
                    letter = chr(ord(letter) + 1)


            y2 += 30
            x2 = 0


    # calling functions from entries
    def call_function(arg):
        if arg == 1:
            label_text.set(int(sumZone(entry_text.get())))
        elif arg == 2:
            label_text.set(int(maxSheet(entry_text.get())))
        elif arg == 3:
            label_text.set(int(minSheet(entry_text.get())))
        elif arg == 4:
            label_text.set(float(avgSheet(entry_text.get())))

    def call_sheet():
        if (int(rows.get()) < 11 and int(cols.get())):
            Sheet(int(rows.get()), int(cols.get()))
        else:
            print("Rows and cols max 10")



    # entries
    entry_text = StringVar()
    entry = Entry(window, width=18, font=('arial', 12, 'bold'), textvariable=entry_text).place(x=375, y=100)
    rows= StringVar()
    entry2= Entry(window, width= 5, textvariable=rows).place(x=200, y=10)
    cols= StringVar()
    entry3= Entry(window, width= 5, textvariable=cols).place(x=240, y=10)
    # buttons
    button_sum = Button(window, text="sumZone()", width=15, command=lambda: call_function(1)).place(x=400, y=130)
    button_create= Button(window, text="Create", width=10, command=call_sheet).place(x=280, y=7)
    button_restart= Button(window, text="Restart", width=10, command=refresh).place(x=370, y=7)
    button_max = Button(window, text="maxZone()", width=15, command=lambda: call_function(2)).place(x=400, y=160)
    button_min = Button(window, text="minZone()", width=15, command=lambda: call_function(3)).place(x=400, y=190)
    button_avg = Button(window, text="avgZone()", width=15, command=lambda: call_function(4)).place(x=400, y=220)
    # labels
    Label(window, text="Enter sheet's rows and cols:", font=('arial', 10, 'bold')).place(x=20, y=10)
    Label(window, text="Enter the zone you want to calculate", font=('arial', 10, 'bold')).place(x=340, y=50)
    Label(window, text="EXAMPLE: A1:B3 ", font=('arial', 10, 'bold')).place(x=395, y=70)
    label_text = StringVar()
    label = Label(window, width=15, font=('arial', 12, 'bold'), textvariable=label_text). place(x=380, y= 250)


    window.mainloop()

if __name__ == '__main__':
    def refresh(): # function to restart the program
        window.destroy()
        start()

    start()