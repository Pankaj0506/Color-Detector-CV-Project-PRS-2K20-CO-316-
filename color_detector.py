
# SUBMITTED BY - PANKAJ LAHOTI (2K20/CO/316)
# SUBJECT - COMPUTER VISION (CO411) E4
# SUBMITTED TO - Ms. CHING MUAN KIM (DEPT. OF COMP. SCI. & ENGG.)
# PROJECT TOPIC - COLOR DETECTOR IN IMAGE

# Dataset link: https://github.com/codebrainz/color-names/blob/master/output/colors.csv

# In this Program, we are basically finding color from the dataset
# which is nearest to the RGB values of the clicked pixel
import cv2 as cv
import pandas as pd

# storing image path of different images in differnt variable
# IMPORTANT: WE HAVE TO UPDATE FILE PATH OF a,b,c,d,e FOR DIFFERENT DEVICES
a = r'C:\Users\Pankaj Lahoti\Desktop\pankaj\Color Detector CV Project PRS\images\t1.jpg'
b = r'C:\Users\Pankaj Lahoti\Desktop\pankaj\Color Detector CV Project PRS\images\t2.jpg'
c = r'C:\Users\Pankaj Lahoti\Desktop\pankaj\Color Detector CV Project PRS\images\t3.jpg'
d = r'C:\Users\Pankaj Lahoti\Desktop\pankaj\Color Detector CV Project PRS\images\t4.jpg'
e = r'C:\Users\Pankaj Lahoti\Desktop\pankaj\Color Detector CV Project PRS\images\t5.jpg'

# selcting one image from above 5 images for color detection
choice = int(input('enter your choice from 1-5: '))

if choice == 1: image_path = a
elif choice == 2: image_path = b
elif choice == 3: image_path = c
elif choice == 4: image_path = d
else: image_path = e

img = cv.imread(image_path)

# declaring global variables (are used later on)
clicked = False
r = g = b = x_pos = y_pos = 0

# Reading csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
dataset_path = r'C:\Users\Pankaj Lahoti\Desktop\pankaj\Color Detector CV Project PRS\colors.csv'
csv = pd.read_csv(dataset_path, names=index, header=None)


# function to calculate minimum distance from all colors and get the most matching color
def get_color_name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname


# function to get x,y coordinates of mouse double click
def draw_function(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


cv.namedWindow('image')
cv.setMouseCallback('image', draw_function)

while True:

    cv.imshow("image", img)
    if clicked:

        # cv2.rectangle(image, start point, endpoint, color, thickness)-1 fills entire rectangle
        cv.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        # Creating text string to display( Color name and RGB values )
        text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv.LINE_AA)

        # For very light colours we will display text in black colour
        if r + g + b >= 600:
            cv.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv.LINE_AA)

        clicked = False

    # Break the loop when user hits 'esc' key
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()