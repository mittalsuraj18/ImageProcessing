import ImageHelper
import sys
import matplotlib
import cv2

def main():
    # imagepath=raw_input("enter image path")
    imagepath = "1.jpg"
    image = ImageHelper.loadImage(imagepath)
    if image != None:
        print "Successfully loaded the image"
    else:
        print "Unable to load the image, Please check the path"
        return
    # image_dimensions = image.shape
    height, width = ImageHelper.GetHeightAndWidth(image)
    pts1 = ImageHelper.GetImageCoordinates(height, width)
    #coord = raw_input("Please enter coordinates A,B,C,D for image manipulation").split(" ")
    coord=["955,198,","1071,506","717,281","847,504"]
    pts2=ImageHelper.GetCoorinatesaspoints(coord)
    pts3=pts2-pts1
    perspectiveimage=ImageHelper.GetPerspectiveTransform(pts1,pts2)
    newimage=cv2.warpPerspective(image,perspectiveimage,(300,300))

    #cv2.resize()
    ImageHelper.DisplayImage(image)
    ImageHelper.DisplayImage(newimage)


    # raw_input()
    # ImageHelper.DisplayImage(image)


if __name__ == "__main__":
    sys.exit(int(main() or 0))
