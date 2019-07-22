import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def plot_pics(images=[], title=[]):
    rows, columns = 1, len(images)
    fig, plot_array = plt.subplots(rows, columns, figsize=(20,10))
    
    for index, plot in enumerate(plot_array.ravel()):
        plot.imshow(images[index], cmap='gray')
        if len(title) == 0 or len(title) != len(images):
            plot.set_title(index)
        else:
            plot.set_title(title[index])
    
    plt.draw()
    
def plot_pics2(images=[], title=[]):
    rows, columns = 2, len(images)//2
    fig, plot_array = plt.subplots(rows, columns, figsize=(20,10))
    
    for index, plot in enumerate(plot_array.ravel()):
        if index < len(images):
            plot.imshow(images[index], cmap='gray')
            if len(title) == 0 or len(title) != len(images):
                plot.set_title(index)
            else:
                plot.set_title(title[index])
        else:
            plot.axis('off')
            
    
    plt.draw()