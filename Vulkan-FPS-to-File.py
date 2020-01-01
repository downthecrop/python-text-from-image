from PIL import Image
from pytesseract import image_to_string
import re
 
def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    #cropped_image.show()
 
 
if __name__ == '__main__':
    r = re.compile(r"^\d*[.,]?\d*$") # check if numbers
    f= open("framerate.txt","w+")
    savedVal = "";
    i = 40 #starting image
    while i < 1241: #ending image
        image = (str(i)+'.png')
        crop(image, (40, 50, 90, 65), 'cropped.png') ## Vulkan FPS Counter
        #crop(image, (1210, 0, 1232, 12), 'cropped.png') #League FPS Counter
        # Provide the target width and height of the image
        im = Image.open("cropped.png")
        (width, height) = (200, 60)
        #(width, height) = (88, 48)
        im_resized = im.resize((width, height), Image.ANTIALIAS)
        #im_resized.show()
        #img=Image.open('5.png')
        print(image_to_string(im_resized))
        if r.match(image_to_string(im_resized)) and image_to_string(im_resized) != "" and float(image_to_string(im_resized))<241: 
            f.write(image_to_string(im_resized)+"\n")
            savedVal = image_to_string(im_resized)
        else: 
            print("skipped, using"+savedVal)
            f.write(savedVal+"\n")
        i += 1
    f.close()
    print("Done!")

#Left, Top