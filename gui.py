import  customtkinter
import tkinter
from customtkinter import filedialog
import json
import os
import convert

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.json'), 'r') as json_file: # write the content of the config to the var config
    config = json.load(json_file)
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'file_types.json'), 'r') as json_file: # write the content of file_types.json to file_types
    file_types = json.load(json_file)

def select_file(input_f:bool):
    filetypes = file_types.items()
    if input_f:
        filename = filedialog.askopenfilename(
            title='Select an input file',
            filetypes=filetypes
        )
    else:
        filename = filedialog.asksaveasfilename(
            title='Save',
            filetypes=filetypes
        )
    return filename

files = {'input_file': None, 'output_file': None, 'toc': False}

def button_select_file_command(label, input_f:bool):
    file = select_file(input_f)
    if file == '':
        return

    if input_f:
        files['input_file'] = file
    else:
        files['output_file'] = file

    if files['input_file'] and files['output_file']:
        button_convert.configure(state=customtkinter.NORMAL)
    label.configure(text=file)

def button_convert_command(files):
    try:
        convert.convert(files)
    except FileExistsError:
        label_user_info.configure(text='Pandoc isn\'t installed', text_color='red')
        return
    else:
        label_user_info.configure(text='Successfully converted the file.', text_color='white')
        files['input_file'] = None
        files['output_file'] = None
        label_select_input_file.configure(text='')
        label_select_output_file.configure(text='')
        button_convert.configure(state=customtkinter.DISABLED)

def set_variable(variable_name:str, variable_value, key=None):
    if isinstance(globals()[variable_name], dict) and not (key is None):
        globals()[variable_name][key] = variable_value
    else:
        globals()[variable_name] = variable_value
    

customtkinter.set_appearance_mode('system') # set some styles
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()

toc = customtkinter.BooleanVar(False)


# place the windows in the middle
config['width_screen'] = root.winfo_screenwidth()
config['height_screen'] = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (config['width'], config['height'], (config['width_screen']/2)-(config['width']/2), (config['height_screen']/2)-(config['height']/2)))

frame_starting = customtkinter.CTkFrame(master=root)
frame_starting.pack(pady=10, padx=60, fill='both', expand=True)

label_select_input_file = customtkinter.CTkLabel(master=frame_starting, text='', font=(config['font_style'], config['font_size']))
label_select_input_file.grid(row=0, column=0, pady=20, padx=30)

button_select_input_file = customtkinter.CTkButton(master=frame_starting, text='Select input file', font=(config['font_style'], config['font_size']), command=lambda: button_select_file_command(label_select_input_file, True))
button_select_input_file.grid(row=0, column=1, pady=20, padx=30)


frame_ending = customtkinter.CTkFrame(master=root)
frame_ending.pack(pady=10, padx=60, fill='both', expand=True)

label_select_output_file = customtkinter.CTkLabel(master=frame_ending, text='', font=(config['font_style'], config['font_size']))
label_select_output_file.grid(row=0, column=0, pady=20, padx=30)

button_select_output_file = customtkinter.CTkButton(master=frame_ending, text='Select output file', font=(config['font_style'], config['font_size']), command=lambda: button_select_file_command(label_select_output_file, False))
button_select_output_file.grid(row=0, column=1, pady=20, padx=30)

checkbox_toc = customtkinter.CTkCheckBox(
    master=frame_ending,
    text='Table of content',
    variable=toc,
    onvalue=True,
    offvalue=False,
    command=lambda: set_variable('files', toc.get(), 'toc')
)
checkbox_toc.grid(
    row=1,
    column=0,
    columnspan=2,
    pady=20,
    padx=30
)

frame_convert = customtkinter.CTkFrame(master=root)
frame_convert.pack(pady=20, padx=60, fill='both', expand=True)

label_user_info = customtkinter.CTkLabel(
    master=frame_convert,
    text='',
    font=(config['font_style'], config['font_size'])
)
label_user_info.pack(pady=10, padx=40)

button_convert = customtkinter.CTkButton(
    master=frame_convert,
    text='Convert',
    font=(config['font_style'], config['font_size']),
    state=customtkinter.DISABLED,
    command=lambda: button_convert_command(files)
)
button_convert.pack(pady=20, padx=60)

root.mainloop()

