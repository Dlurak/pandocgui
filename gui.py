import  customtkinter
from customtkinter import filedialog
import json
import os

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.json'), 'r') as json_file: # write the content of the config to the var config
    config = json.load(json_file)


def select_file():
    filetypes = (
        ('All files', '*.*'),
        ('Markdown files', '*.md *.markdown *.'),
        ('Word files', '*.docx'),
        ('Websites', '*html'),
        ('Open Ofice files', '*.odt'),
        ('LaTeX files', '*tex'),
        ('E-Books', '*.epub')
    )
    filename = filedialog.askopenfilename(
        title='Select an input file',
        filetypes=filetypes
    )
    return filename

def button_select_file_command(label):
    label.configure(text=select_file())

customtkinter.set_appearance_mode('system') # set some styles
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()

# place the windows in the middle
config['width_screen'] = root.winfo_screenwidth()
config['height_screen'] = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (config['width'], config['height'], (config['width_screen']/2)-(config['width']/2), (config['height_screen']/2)-(config['height']/2)))

frame_starting = customtkinter.CTkFrame(master=root)
frame_starting.pack(pady=20, padx=60, fill='both', expand=True)

label_select_input_file = customtkinter.CTkLabel(master=frame_starting, text='', font=(config['font_style'], config['font_size']))
label_select_input_file.grid(row=0, column=0, pady=20, padx=30)

button_select_input_file = customtkinter.CTkButton(master=frame_starting, text='Select input file', font=(config['font_style'], config['font_size']), command=lambda: button_select_file_command(label_select_input_file))
button_select_input_file.grid(row=0, column=1, pady=20, padx=30)


frame_ending = customtkinter.CTkFrame(master=root)
frame_ending.pack(pady=20, padx=60, fill='both', expand=True)

label_select_output_file = customtkinter.CTkLabel(master=frame_ending, text='', font=(config['font_style'], config['font_size']))
label_select_output_file.grid(row=0, column=0, pady=20, padx=30)

button_select_output_file = customtkinter.CTkButton(master=frame_ending, text='Select output file', font=(config['font_style'], config['font_size']), command=lambda: button_select_file_command(label_select_output_file))
button_select_output_file.grid(row=0, column=1, pady=20, padx=30)

root.mainloop()

