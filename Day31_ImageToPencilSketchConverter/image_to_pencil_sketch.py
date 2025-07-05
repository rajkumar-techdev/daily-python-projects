import cv2

def image_to_sketch(image_path,output_name="sketch.png"):
    #Load the image
    img=cv2.imread(image_path)
    if img is None:
        print("Error:File not Found or Invalid Image Path. ")
        return

    #convert to grayscale
    gray=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)

    #Invert the grayscale image
    inverted=255-gray

    #Apply Gaussian blur
    blurred=cv2.GaussianBlur(inverted,(21,21),0)

    #Inverted the blur image
    inverted_blur=255-blurred

    #Create a pencil sketch
    sketch=cv2.divide(gray,inverted_blur,scale=256.0)

    #save the result
    cv2.imwrite(output_name,sketch)
    print(f"Pencil sketch saved as {output_name}" )

path=input("Enter the path of your image: ")
image_to_sketch(path)

