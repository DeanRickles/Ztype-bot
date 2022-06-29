import cv2
import numpy as np

# Screen Shot Point
class imagePosition:

    # declare self variables.
    def __init__(self, path):
        self.path = path
        self.scale_percent = 100
        self.scale_lock = True
        self.coord_x = None
        self.coord_y = None

    # sets the size of the show scale.
    def scale(self, percent):
        if isinstance(percent, int):
            # checks if inputed int is within parameters, 1 to 100.
            if percent >= 1 and percent <= 100 or self.scale_lock != True:
                self.scale_percent = percent
            else:
                return print(f"Warning: Scale value not set. {str(percent)} is not greater then 1 and less then 100 percent.")
                
        else:
            return print("Warning: Scale value not set. Arg percent not int type.")

    def scalelock(self, boolean):
        # Allow values outside of the preset scale percentage.
        # enable = True || Disable = False
        if isinstance(boolean, bool):
            print(f"Scale lock has been changed to {str(boolean)}.")
            self.scale_lock = boolean
        else:
            return print(f"Warning: scale_lock value not set. Arg boolean not bool type.")  

    def get(self):
        # path = string path to image file.

        img = cv2.imread(self.path)  
        cv2.namedWindow('image') # do I need this?

        # bind select_point function to a window that will capture the mouse click
        cv2.setMouseCallback('image', self.select_point)
        cv2.imshow('image', 
            cv2.resize(
                img,
                (
                    int(img.shape[1] * self.scale_percent / 100),
                    int(img.shape[0] * self.scale_percent / 100)
                )
            )
        )

        print("Double left click on location, then press a key.")
        # waits for key 'k' to be pressed before closing the image.
        k = cv2.waitKey(0) & 0xFF
        if k == ord('a'):
            pass
        # cv2.waitKey(0) # not needed.
        cv2.destroyAllWindows()
        print("run yourVariable.json() to get image coordinates.")

    def select_point(self, event,x,y,flags,param):
        # stores double mouse click position for x and y coordinate.

        if event == cv2.EVENT_LBUTTONDBLCLK: # captures left button double-click
            
            # scales up the coords to match with screen.
            self.coord_x = int(x / self.scale_percent * 100) 
            self.coord_y = int(y / self.scale_percent * 100)

            img = cv2.imread(self.path)
            cv2.namedWindow('image') 

            # displaying the coordinates on the image.
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(
                img,
                '. ' + str(self.coord_x) + ',' + str(self.coord_y), 
                (self.coord_x,self.coord_y),
                font, 1, (0, 255, 255), 2
            )

            cv2.imshow(
                'image',
                cv2.resize(
                    img,
                    (
                        int(img.shape[1] * self.scale_percent / 100),
                        int(img.shape[0] * self.scale_percent / 100)
                    )
                )
            )

    def json(self):
        if self.coord_x:
            return {"x": self.coord_x, "y": self.coord_y }
        else:
            return print("warning: Need to run .img_cood() first.")


# TODO: Check if needed class or add to auto class.
class AdjustImage():
    def showBW(img):
        # Converting BGR to RGB
        return cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2GRAY) 

    def show(img):
        # Converting BGR to BW.
        return cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2RGB) 
        
    def imshow(img):
        return cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2RGB) # Converting BGR to RGB
        
    def imshowBW(img):
        return cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2GRAY) # Converting BGR to RGB

    def maskWhite(img):
        
        # look at removing numpty.
        #set the lower and upper bounds
        lower = np.array([100,100,100])
        upper = np.array([255,255,255])
        
        #create a mask for green colour using inRange function
        mask = cv2.inRange(img, lower, upper)

        #perform bitwise and on the original image arrays using the mask
        return cv2.bitwise_and(img, img, mask=mask)

    
class auto():
    
    def __init__(self, path):
        self.path = path
    
    # TODO: run  
    print("To be filled in")