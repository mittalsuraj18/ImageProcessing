import ImageHelper
import sys



def get_max_width_height(points):
    maximumx = max(points, key=lambda x: float(x[0]))[0]
    maximumxy = max(points, key=lambda x: float(x[1]))[1]
    return maximumx, maximumxy


def main():
    # Sample Image for Testing
    # imagepath = "1.jpg"
    imagepath = raw_input("enter image path")

    # Load the image
    srcImage = ImageHelper.load_image(imagepath)

    # Check if image loaded successfully
    if srcImage != None:
        print "Successfully loaded the image"
    else:
        print "Unable to load the image, Please check the path"
        return

    # Get height and width of soource image and convert it to co-ordinates
    height, width = ImageHelper.get_height_width(srcImage)
    pts1 = ImageHelper.get_image_coordinates(height, width)

    # sample co-ordinate points
    # coord=["955,198,","1071,506","717,281","847,504"]
    coord = raw_input("Please enter coordinates A,B,C,D for image manipulation").split(" ")

    # Convert string input to floating point co-ordinate points
    pts2 = ImageHelper.get_cooridnates_as_points(coord)

    # Get the transform matrix
    perspectiveMatrix = ImageHelper.get_perspective_transform_matrix(pts1, pts2)

    #Get the maximum dimensions of new image
    maxX, maxY = get_max_width_height(pts2)

    #Generate new image
    newimage = ImageHelper.get_warped_image(srcImage, perspectiveMatrix, (maxX, maxY))

    #Display the images
    ImageHelper.display_image(srcImage)
    ImageHelper.display_image(newimage)



if __name__ == "__main__":
    sys.exit(int(main() or 0))
