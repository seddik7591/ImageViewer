# seddik7591@gmail.com
# This is an image viewer with image resizing

from tkinter import *
from PIL import ImageTk,Image
from resizeimage import resizeimage

app = Tk()
app.title("my app")
app.iconbitmap('palm.ico')

image_name_list = ['img1.jpg', 'img2.jpg', 'img3.jpg', 'img4.jpg', 'img5.jpg']

# an empty list to save resized images objects
image_list  = []

for i in range(5):
	f= open('images/'+image_name_list[i], 'r+b')
	image = Image.open(f)
	resizedImage = resizeimage.resize_cover(image, [900, 300], validate=False)
	resizedImage.save('resized-images/'+image_name_list[i], image.format)
	# to open image to the window add elements to the list image_list
	image_list.append(ImageTk.PhotoImage(resizedImage))

currentImg = 0

# display default image
my_label = Label(image=image_list[0])
my_label.grid(row=0, column=0, columnspan=3)

# display default status bar
StatusBar_label = Label(app, text="Image 1 of "+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

StatusBar_label.grid(row=2, column=0, columnspan=3, sticky=W+E)

# this function will be executed when the next or previews button clicked
def changeImg(step):
	global my_label
	global button_previews
	global button_next
	global currentImg
	global StatusBar_label
	if step == 1 and currentImg == 4:
		currentImg = 0
	elif step == -1 and currentImg == 0:
		currentImg = 4
	else:
		currentImg += step
	my_label.grid_forget()
	my_label = Label(image=image_list[currentImg])
	my_label.grid(row=0, column=0, columnspan=3)
	StatusBar_label.grid_forget()
	StatusBar_label = Label(app, text="Image "+str(currentImg+1)+" of "+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
	StatusBar_label.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_previews = Button(app, text="<<", command=lambda: changeImg(-1))
button_next = Button(app, text=">>", command=lambda: changeImg(1))
button_quit = Button(app, text="Exit the app", command=app.quit)

button_previews.grid(row=1, column=0)
button_next.grid(row=1, column=2) 
button_quit.grid(row=1, column=1, pady=10)

app.mainloop()
