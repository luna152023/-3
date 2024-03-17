from tkinter import Tk, Label, LabelFrame, Radiobutton, StringVar, Button
from tkinter import colorchooser

root = Tk()
root.title("Параметри автомобіля")

lang1 = StringVar()
lang2 = StringVar()
lang3 = StringVar()
lang4 = StringVar()
lang5 = StringVar()

result_text = ""

frm_model = LabelFrame(root, text='Марка автомобіля')
frm_model.pack(padx=10, pady=5, side='left')
Label(frm_model, text="Оберіть марку автомобіля:").pack(anchor='w')
for i in ['Toyota','BMW','Mercedes-Benz','Ford','Honda','Audi','Hyundai','Volkswagen','Tesla','Ferrari','Porsche']:
    rb = Radiobutton(frm_model, value=i, text=i, variable=lang2)
    rb.pack(anchor='w')

frm_age = LabelFrame(root, text='Скільки років')
frm_age.pack(padx=10, pady=5, side='left')
Label(frm_age, text="Оберіть рік випуску автомобіля:").pack(anchor='w')
for i in ['Нова', 'до 5 років', '6-10 років', '11-15 років', 'більше 15 років']:
    rb = Radiobutton(frm_age, value=i, text=i, variable=lang3)
    rb.pack(anchor='w')

frm_volume = LabelFrame(root, text="Об'єм двигуна")
frm_volume.pack(padx=10, pady=5, side='left')
Label(frm_volume, text="Оберіть об'єм двигуна:").pack(anchor='w')
for i in ['менше 1200', '1200-1500', '1501-2200', 'більше 2200']:
    rb = Radiobutton(frm_volume, value=i, text=i, variable=lang4)
    rb.pack(anchor='w')

frm_motor = LabelFrame(root, text='Вид палива')
frm_motor.pack(padx=10, pady=5, side='left')
Label(frm_motor, text="Оберіть вид палива:").pack(anchor='w')
for i in ['Дизель', 'Бензин','Газ','Електромобіль']:
    rb = Radiobutton(frm_motor, value=i, text=i, variable=lang5)
    rb.pack(anchor='w')

def choose_color():
    color_code = colorchooser.askcolor(title="Виберіть колір")
    if color_code[1]:
        color_frame.config(bg=color_code[1])

color_button = Button(root, text="Обрати колір", command=choose_color)
color_button.pack(pady=5)

color_frame = LabelFrame(root, text="Колір")
color_frame.pack(pady=5)
color_frame.config(width=50, height=20)
color_frame.pack_propagate(False)

def add_to_list():
    global result_text
    result_text = ""
    result_text += f"Марка автомобіля: {lang2.get()}\n"
    result_text += f"Рік випуску автомобіля: {lang3.get()}\n"
    result_text += f"Об'єм двигуна: {lang4.get()}\n"
    result_text += f"Вид палива: {lang5.get()}\n"
    result_text += f"Колір: {color_frame.cget('bg')}\n"
    result_display.config(text=result_text)

add_button = Button(root, text="Додати", command=add_to_list)
add_button.pack(pady=5)

result_label = Label(root, text="Результат вибору", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

result_display = Label(root, text=result_text, relief="solid", width=50, height=10, justify="left")
result_display.pack(pady=5)

root.mainloop()