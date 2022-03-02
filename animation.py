from pdf2image import convert_from_path, convert_from_bytes
import os
import imageio

imageio.plugins.freeimage.download()  # download freeimage package

path = str(os.path.abspath(os.getcwd())) # read current work package


images = []
for i in range(1,51):
    images.append(convert_from_path(path + '\\Plots\\'+ str(i) +'.pdf')[0])  # read pdfs and convert them to image
    
imageio.mimsave('movie1.gif', images, 'GIF-FI', fps=6)  # convert images to gif


