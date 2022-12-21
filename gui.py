import  customtkinter
from customtkinter import filedialog
import json
import os
import convert

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.json'), 'r') as json_file: # write the content of the config to the var config
    config = json.load(json_file)


def select_file(input_f:bool):
    filetypes = (
        ('Supported Filetypes', '*.md *.markdown *.docx *.html *.odt *.tex *.epub *.ipynb *.csv *.bib *.bst'),
        ('Markdown files', '*.md *.markdown *.'),
        ('Word files', '*.docx'),
        ('Websites', '*html'),
        ('Open Ofice files', '*.odt'),
        ('LaTeX files', '*tex'),
        ('E-Books', '*.epub'),
        ("Jupyter Notebooks", '*.ipynb'),
        ("CSV", '*.csv'),
        ('BibTeX', '*.bib'),
        ('BibLaTex', '*.bst')
    )
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

files = {'input_file': None, 'output_file': None}
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
    except KeyError:
        label_user_info.configure(text='At least one of the file exstensions isn\'t supportet by this programm and/or by pandoc', text_color='red')
        return
    else:
        label_user_info.configure(text='Successfully converted the file.', text_color='white')
        files = {'input_file': None, 'output_file': None}
        label_select_input_file.configure(text='')
        label_select_output_file.configure(text='')
        button_convert.configure(state=customtkinter.DISABLED)


customtkinter.set_appearance_mode('system') # set some styles
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()

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

