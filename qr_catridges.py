# lpoptions -d RT200 -l
# * is active options
# lpadmin utilites for configuring printers
from tkinter import *
import subprocess
import qrcode
import os


def form_data():
    return (f'https://glpi.crh.local/front/{select_type()}.form.php?id={get_id()}')

def get_id():
    return ent_id.get()

def select_type():
    return val.get()

def gen_qr(data):
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=7,
        border=1,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img_qr = qr.make_image()
    img_qr.save('qr_code.png')

def print_btn():
    value = form_data()
    gen_qr(value)
    subprocess.run(["lp", "-d", "RT200", '-o', 'fit-to-page', 'qr_code.png'])
    if os.path.exists("qr_code.png"):
        os.remove("qr_code.png")

root = Tk()
root.title('Qrcode Print')

#Problem when two display
#scr_width = int(root.winfo_screenwidth()/2)
scr_height = int(root.winfo_screenheight()/2)

root.geometry(f'325x130+{540}+{scr_height}')
root.resizable(False, False)

lb_id = Label(root, text='Enter --> id ')
lb_id.grid(row=0, column=0, padx=10, pady=10)

ent_id = Entry(root, width=15)
ent_id.grid(row=0, column=1, padx=10, pady=10)

val = StringVar()
val.set('printer')

rb_cartridge = Radiobutton(root, text='Printer', variable=val, value='printer', command=select_type)
rb_cartridge.grid(row=1, column=0, padx=5, pady=5, sticky='w')

rb_printer = Radiobutton(root, text='Computer', variable=val, value='computer', command=select_type)
rb_printer.grid(row=1, column=1, padx=5, pady=5, sticky='w')

print_btn = Button(root, text='Print', command=print_btn)
print_btn.grid(row=2, columnspan=2, padx=5, pady=5, sticky='we')

root.mainloop()



