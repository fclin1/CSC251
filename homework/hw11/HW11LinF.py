"""
Author: Frank Lin
Email: fclin@ncsu.edu
Class: CSC 251 Fall 2025
Program: Homework 11
Purpose: Calculates weighted course grades using a GUI.
Bugs: None
Acknowledgements: None.
"""

import tkinter
import tkinter.messagebox

class GradeCalculator:
    """
    A GUI-based grade calculator for CSC 251 course that computes weighted averages
    based on class activities, homework, projects, and exam scores.
    """
    
    def __init__(self):
        """
        Initialize the Grade Calculator GUI with all necessary widgets and layout.
        """
        # Main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Grade Calculator")
        
        # Customization: Changed background color to light blue
        self.main_window.config(bg='light blue')
        
        # Frames
        self.top_frame = tkinter.Frame(self.main_window, bg='light blue')
        self.middle_frame = tkinter.Frame(self.main_window, bg='light blue')
        self.bottom_frame = tkinter.Frame(self.main_window, bg='light blue')
        
        # Title label
        self.title_label = tkinter.Label(self.top_frame, 
                                         text='Grade Calculator', 
                                         font=('Arial', 16, 'bold'), 
                                         bg='light blue', 
                                         fg='dark blue')
        
        # Labels and entries for each grade category
        self.activity_label = tkinter.Label(self.top_frame, 
                                           text='Class Activity Average (15%):',
                                           bg='light blue')
        self.activity_entry = tkinter.Entry(self.top_frame, width=15)
        
        self.homework_label = tkinter.Label(self.top_frame, 
                                           text='Homework Average (15%):',
                                           bg='light blue')
        self.homework_entry = tkinter.Entry(self.top_frame, width=15)
        
        self.project_label = tkinter.Label(self.top_frame, 
                                          text='Project Average (20%):',
                                          bg='light blue')
        self.project_entry = tkinter.Entry(self.top_frame, width=15)
        
        self.exam1_label = tkinter.Label(self.top_frame, 
                                        text='Exam 1 Grade (15%):',
                                        bg='light blue')
        self.exam1_entry = tkinter.Entry(self.top_frame, width=15)
        
        self.exam2_label = tkinter.Label(self.top_frame, 
                                        text='Exam 2 Grade (15%):',
                                        bg='light blue')
        self.exam2_entry = tkinter.Entry(self.top_frame, width=15)
        
        self.final_label = tkinter.Label(self.top_frame, 
                                        text='Final Exam Grade (20%):',
                                        bg='light blue')
        self.final_entry = tkinter.Entry(self.top_frame, width=15)
        
        # Checkbox for final exam completion
        self.final_taken = tkinter.BooleanVar()
        self.final_checkbox = tkinter.Checkbutton(self.top_frame, 
                                                  text='Final Exam Completed', 
                                                  variable=self.final_taken,
                                                  bg='light blue')
        
        # Additional widget: Scale slider for target grade
        self.target_label = tkinter.Label(self.middle_frame, 
                                         text='Target Grade:', 
                                         bg='light blue')
        self.target_scale = tkinter.Scale(self.middle_frame, 
                                         from_=0, 
                                         to=100, 
                                         orient=tkinter.HORIZONTAL, 
                                         length=200,
                                         bg='light blue')
        self.target_scale.set(90)
        
        # Output label
        self.output_label = tkinter.Label(self.middle_frame, 
                                         text='Course Grade:', 
                                         bg='light blue', 
                                         font=('Arial', 12, 'bold'))
        
        self.result = tkinter.StringVar()
        self.result_label = tkinter.Label(self.middle_frame, 
                                         textvariable=self.result,
                                         bg='white',
                                         fg='black',
                                         relief='sunken',
                                         font=('Arial', 14, 'bold'), 
                                         width=15)
        
        # Buttons
        self.compute_button = tkinter.Button(self.bottom_frame, 
                                            text='Compute Grade', 
                                            command=self.calculate_grade,
                                            fg='black', 
                                            font=('Arial', 11, 'bold'))
        
        self.quit_button = tkinter.Button(self.bottom_frame, 
                                         text='Quit', 
                                         command=self.main_window.destroy,
                                         fg='black',
                                         font=('Arial', 11, 'bold'))
        
        # Pack all the widgets
        self.title_label.pack(pady=10)
        
        self.activity_label.pack(pady=5)
        self.activity_entry.pack(pady=5)
        
        self.homework_label.pack(pady=5)
        self.homework_entry.pack(pady=5)
        
        self.project_label.pack(pady=5)
        self.project_entry.pack(pady=5)
        
        self.exam1_label.pack(pady=5)
        self.exam1_entry.pack(pady=5)
        
        self.exam2_label.pack(pady=5)
        self.exam2_entry.pack(pady=5)
        
        self.final_label.pack(pady=5)
        self.final_entry.pack(pady=5)
        
        self.final_checkbox.pack(pady=10)
        
        self.target_label.pack(pady=5)
        self.target_scale.pack(pady=5)
        
        self.output_label.pack(pady=10)
        self.result_label.pack(pady=5)
        
        self.compute_button.pack(side='left', padx=10, pady=10)
        self.quit_button.pack(side='left', padx=10, pady=10)
        
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
        
        tkinter.mainloop()
    
    def calculate_grade(self):
        """
        Calculate the weighted course grade based on user input.
        Also handles cases where the final exam hasn't been taken yet.
        """
        try:
            activity = float(self.activity_entry.get())
            homework = float(self.homework_entry.get())
            project = float(self.project_entry.get())
            exam1 = float(self.exam1_entry.get())
            exam2 = float(self.exam2_entry.get())
            
            # Calculate weighted grade
            if self.final_taken.get():
                final = float(self.final_entry.get())
                total = (activity * 0.15 + homework * 0.15 + project * 0.20 + 
                        exam1 * 0.15 + exam2 * 0.15 + final * 0.20)
            else:
                total = (activity * 0.15 + homework * 0.15 + project * 0.20 + 
                        exam1 * 0.15 + exam2 * 0.15) / 0.80
            
            total = round(total, 2)
            
            self.result.set(f'{total:.2f}%')
            
            # Check against target grade
            target = self.target_scale.get()
            if total >= target:
                tkinter.messagebox.showinfo('Congratulations!', 
                                        'You have met or exceeded your target grade of ' 
                                        + str(target) + '%!')
            
        except ValueError:
            tkinter.messagebox.showerror('Input Error', 
                                        'Please enter valid numeric values for all grades.')

# Main
if __name__ == '__main__':
    my_gui = GradeCalculator()