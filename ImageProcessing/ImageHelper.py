import cv2
import numpy


def load_image(path):
    image = cv2.imread(path, 1)
    return image


def display_image(imagevariable):
    if (imagevariable != None):
        cv2.imshow('Image', imagevariable)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def get_height_width(image):
    if image != None:
        height, width = image.shape[0:2]
        return height, width
    else:
        return None, None


def get_image_coordinates(height, width):
    if (height != None and width != None):
        return numpy.float32([[0, 0], [width, 0], [0, height], [width, height]])


def get_cooridnates_as_points(coordinates):
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


def get_perspective_transform_matrix(pt1,pt2):
    return cv2.getPerspectiveTransform(pt1, pt2)


def get_warped_image(srcImage,transformMatrix,(dimX,dimY)):
    return cv2.warpPerspective(srcImage, transformMatrix, (dimX, dimY))
