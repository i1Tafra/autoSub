from tkinter.filedialog import askdirectory

def gui_get_folder(initial_dir):
    initial_dir =  initial_dir if initial_dir else '.'
    return askdirectory(title='Select folder to download subtitles', initialdir=initial_dir, mustexist=True)



