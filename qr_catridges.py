# lpoptions -d RT200 -l
# * is active options
# lpadmin utilites for configuring printers
from tkinter import *
import subprocess
from pprint import pprint
import qrcode
#
# def x():
#     return print(num_ent.get())

def form_data():
    print(f'https://my_site/{select_type()}/{get_id()}')

def get_id():
    return ent_id.get()

def select_type():
    return val.get()


root = Tk()
root.title('Qrcode Print')

scr_width = int(root.winfo_screenwidth()/2)
scr_height = int(root.winfo_screenheight()/2)

root.geometry(f'325x130+{scr_width}+{scr_height}')
root.resizable(False, False)

lb_id = Label(root, text='Enter --> id ')
lb_id.grid(row=0, column=0, padx=10, pady=10)

ent_id = Entry(root, width=15)
ent_id.grid(row=0, column=1, padx=10, pady=10)

val = StringVar()
val.set('catridges')

rb_cartridge = Radiobutton(root, text='Cartridge', variable=val, value='catridges', command=select_type)
rb_cartridge.grid(row=1, column=0, padx=5, pady=5)

rb_printer = Radiobutton(root, text='Printer', variable=val, value='printers', command=select_type)
rb_printer.grid(row=1, column=1, padx=5, pady=5)

print_btn = Button(root, text='Print', command=form_data)
print_btn.grid(row=2, columnspan=2, padx=5, pady=5, sticky='we')

root.mainloop()


def gen_qr():

    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=7,
        border=1,
        )

    url = 'https://glpi.crh.local/front/printer.form.php?id=71'
    qr.add_data(url)
    qr.make(fit=True)

    img_qr = qr.make_image()
    img_qr.save('qr_code.png')

#subprocess.run(["lp", "-d", "RT200", '-o', 'fit-to-page', 'qr_code.png'])

