import cv2
import numpy


def loadImage(path):
    image = cv2.imread(path, 1)
    return image


def DisplayImage(imagevariable):
    if (imagevariable != None):
        cv2.imshow('Image', imagevariable)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def GetHeightAndWidth(image):
    if image != None:
        height, width = image.shape[0:2]
        return height, width
    else:
        return None, None


def GetImageCoordinates(height, width):
    if (height != None and width != None):
        return numpy.float32([[0, 0], [width, 0], [0, height], [width, height]])


def GetCoorinatesaspoints(coordinates):
    list_coordinates=list(coordinates)
    if list_coordinates!=None:
        p1=(str(list_coordinates[0]).split(","))
        p2=str(list_coordinates[1]).split(",")
        p3=str(list_coordinates[2]).split(",")
        p4=str(list_coordinates[3]).split(",")
        return numpy.float32([
            [float(p1[0]), p1[1]],
            [p2[0],p2[1]],
            [p3[0],p3[1]],
            [p4[0],p4[1]]
        ])
    else:
        return None

def GetPerspectiveTransform(pt1,pt2):
    return cv2.getPerspectiveTransform(pt1, pt2)


