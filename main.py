from tkinter import Tk, PhotoImage, Canvas, Label, Button, Entry, filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

font_path = '/home/jan/anaconda3/fonts/Ubuntu-B.ttf'
original_path = "/home/jan/Desktop/pict_app/original"

def search():
    filename = filedialog.askopenfilename(initialdir=original_path)
    path_entry.insert(0, filename)


def upload():
    try:
        path_original = path_entry.get()
        watermark = watermark_entry.get()
        font_size = int(font_size_entry.get())
        watermark_place_x = float(watermark_place_entry_x.get())
        watermark_place_y = float(watermark_place_entry_y.get())
        watermark_place =tuple([watermark_place_x, watermark_place_y])
        watermark_color = watermark_color_entry.get()
        font = ImageFont.truetype(font_path, size=font_size)
        image = Image.open(path_original).resize((500,500))
        draw = ImageDraw.Draw(image)
        draw.text(watermark_place, watermark, watermark_color, font)
        image.save('/home/jan/Desktop/pict_app/changed/new_image.jpg')
        original_image = Image.open(path_original).resize((500,500))
        tk_original_image_modif = ImageTk.PhotoImage(original_image)
        tk_original_image = Label(window, image=tk_original_image_modif)
        tk_original_image.grid(row=8, column=0)
        new_image = Image.open('/home/jan/Desktop/pict_app/changed/new_image.jpg')
        tk_new_image_modif = ImageTk.PhotoImage(new_image)
        tk_new_image = Label(window, image=tk_new_image_modif)
        tk_new_image.grid(row=8, column=1)
        path_new_image = Label(window,text=f'You can find your new image under following path "/home/jan/Desktop/pict_app/changed/new_image.jpg"')
        path_new_image.grid(row=9, column=0)
        window.mainloop()
    except:
        pass

window = Tk()
window.title('Watermark inserter')
window.configure(padx=20, pady=20)

question_path = Label(window, text='Please chose your picture location:')
question_path.grid(row=0, column=0)

path_entry = Entry(width=50)
path_entry.grid(row=0, column=1)

search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=0, column=2)

question_watermark = Label(window, text='Please insert watermark text:')
question_watermark.grid(row=1, column=0)

watermark_entry = Entry(window, width=50)
watermark_entry .grid(row=1, column=1)

question_font_size = Label(window, text='Please insert font size:')
question_font_size.grid(row=2, column=0)
font_size_entry = Entry(window, width=50)
font_size_entry.insert(0, '14')
font_size_entry .grid(row=2, column=1)

question_watermark_place = Label(window, text='Please insert place of watermark in range (x=500, y=500):')
question_watermark_place.grid(row=3, column=0)
watermark_place_entry_x = Entry(window, width=50)
watermark_place_entry_x.insert(0, 'For example in the middle of x axis: 250')
watermark_place_entry_x .grid(row=3, column=1)
watermark_place_entry_y = Entry(window, width=50)
watermark_place_entry_y.insert(0, 'For example in the middle of y axis: 250')
watermark_place_entry_y .grid(row=4, column=1)

question_watermark_color = Label(window, text='Please insert place of watermark color:')
question_watermark_color.grid(row=5, column=0)
watermark_color_entry = Entry(window, width=50)
watermark_color_entry.insert(1, 'blue')
watermark_color_entry .grid(row=5, column=1)

question = Label(window, text='Upload the picture with watermark:')
question.grid(row=6, column=0)

upload_button = Button(text="Upload", width=15, command=upload)
upload_button.grid(row=6, column=1)

question = Label(window, text='Your original picture:')
question.grid(row=7, column=0)

question = Label(window, text='Your picture with watermark:')
question.grid(row=7, column=1)

window.mainloop()