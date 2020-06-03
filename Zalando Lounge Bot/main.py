import tkinter as tk
from scr import bot

height = 200
width = 400

root = tk.Tk()
root.title('ZLBOT')

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

filtersLabels = ['Kod:', 'Kategorie:', 'Brandy:', 'Kolor:', 'Rozmiar:']
labels = []
entries = []
# LABELS
mailLabel = tk.Label(canvas, text='Email:', font=("Courier", 13))
passLabel = tk.Label(canvas, text='Hasło:', font=("Courier", 13))
for i in range(len(filtersLabels)):
    labels.append(tk.Label(canvas, text=filtersLabels[i], font=("Courier", 13), anchor='e'))

# ------
# ENTRIES
mailEntry = tk.Entry(canvas, bg='#D3D3D3')
passEntry = tk.Entry(canvas, bg='#D3D3D3', show='*')
for i in range(len(filtersLabels)):
    entries.append(tk.Entry(canvas, bg='#D3D3D3'))
# ------

# PLACE
mailLabel.place(relwidth=0.25, relheight=0.1, relx=0.2, rely=0.01)
passLabel.place(relwidth=0.25, relheight=0.1, relx=0.2, rely=0.11)
mailEntry.place(relwidth=0.3, relheight=0.1, relx=0.4, rely=0.01)
passEntry.place(relwidth=0.3, relheight=0.1, relx=0.4, rely=0.11)

for i in range(len(filtersLabels)):
    labels[i].place(relwidth=0.25, relheight=0.1, relx=0.15, rely=0.26 + i * 0.1)
    entries[i].place(relwidth=0.3, relheight=0.1, relx=0.4, rely=0.26 + i * 0.1)


def start_bot():
    mail = mailEntry.get()
    password = passEntry.get()
    code = entries[0].get()
    categories = entries[1].get().split(',')
    brands = entries[2].get().split(',')
    color = entries[3].get().split(',')
    size = entries[4].get().split(',')
    bot(mail, password, code, categories, brands, color, size)


button = tk.Button(canvas, text='SZUKAJ', bg='red', command=start_bot)
button.place(relwidth=0.3, relheight=0.2, relx=0.35, rely=0.77)

# -------
root.mainloop()
