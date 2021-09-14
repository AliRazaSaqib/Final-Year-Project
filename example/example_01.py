from check import detect
import tkinter as tk
from tkinter import filedialog
from PIL import Image
#def opneFile():
 #   res = filedialog.askopenfilename()
  #  get_path = res
   # img=get_path
    #set = ('../output/')
    #detect.detect(img, set, 4) #pass at the start after read the imae

#def outputFile():
 #   image = Image.open('../output/')
  #  image.show()

#root=tk.Tk()

# detect original image with image block size of 16
#detect.detect('../assets/lor.PNG', '../output/', 16)

# detect original image with image block size of 32
# detect.detect('../assets/dataset_example.png', '../output/', block_size=32)

# detect attacked image with image block size of 16
# detect.detect('../assets/dataset_example_blur.png', '../output/', block_size=16)

# detect attacked image with image block size of 32
#root.geometry('400x150')
#root.title('Image Forgery Detection By Using Machine Learning')
#label = tk.Label( root, text='Click on insert button and select the image to check the forgery' )
#label.pack()
#button = tk.Button(root, text='Insert Image', width=25,command=opneFile)
#button.pack()
#button = tk.Button(root, text='Output Image', width=25,command=outputFile)
#button.pack()
#root.mainloop()
