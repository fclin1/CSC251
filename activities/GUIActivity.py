# Lecture 22 Activity
# A description of your assignment will be provided in class
# Complete each section as indicated to compute the quantity indicated

import tkinter as tk
import tkinter.messagebox

class MyGUI:
    def __init__(self):
    
        self.main_window = tk.Tk()
        self.main_window.geometry("400x200")

        #Create 3 frames (2 are done for you)
        self.top_frame = tk.Frame(self.main_window)
        self.mid_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        #Update text of label and add a second label and entry box
        self.miles_label = tk.Label(self.top_frame,  text= 'Enter miles driven:')
        self.miles_entry = tk.Entry(self.top_frame, width = 10)
        self.gallons_label = tk.Label(self.top_frame, text= 'Enter gallons used:')
        self.gallons_entry = tk.Entry(self.top_frame, width = 10)

        
        #Call all pack methods
        self.miles_label.pack()
        self.miles_entry.pack()
        self.gallons_label.pack()
        self.gallons_entry.pack()


        #Update label appropriately
        self.descrip_label = tk.Label(self.mid_frame, text = 'Miles per gallon:')
        self.value = tk.StringVar()
        self.value_label = tk.Label(self.mid_frame, textvariable = self.value)
        
        self.descrip_label.pack()
        self.value_label.pack()
        
        #Create 2 button widgets for bottom frame, one to perform the calculation, one to quit
        self.calc_button = tk.Button(self.bottom_frame, text = 'Calculate MPG', command = self.compute)
        self.quit_button = tk.Button(self.bottom_frame, text = 'Quit', command = self.main_window.quit)
    
        #Pack the button widgets
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        #Pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
    


        #Change window Title
        self.main_window.title("MPG Calculator")

        tk.mainloop()

    #Compute the quantity specified in the class instructions
    def compute(self):
        try:
            miles = float(self.miles_entry.get())
            gallons = float(self.gallons_entry.get())
            
            if gallons == 0:
                tkinter.messagebox.showerror("Error", "Gallons cannot be zero!")
                return
            
            mpg = miles / gallons
            
            self.value.set(f"{mpg:.2f}")
            
        except ValueError:
            tkinter.messagebox.showerror("Error", "Please enter valid numbers for miles and gallons!")
        
if __name__ == "__main__":
    my_gui = MyGUI()



