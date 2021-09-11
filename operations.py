import numpy
import cv2
import imutils
import random
import pyautogui
from PIL import ImageGrab

class Operations:
    @staticmethod
    def check_match(screen, template, threshold):
        chan, w, h = template.shape[::-1]
        filtered_point = numpy.where(
            cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED) >= threshold)
        for point in zip(*filtered_point[::-1]):
            rect = (point[0], point[1], w, h)
            return rect
        return False

    @staticmethod
    def multiscale_template_match(pic, template, threshold, suggested_size=1.0):
        found = None
        for size in numpy.linspace(0.2, 1.0, 20):
            scaled_template = imutils.resize(template, width=int(template.shape[1] * size))
            ratio = template.shape[1] / scaled_template.shape[1]

            if scaled_template.shape[0] > pic.shape[0] or scaled_template.shape[1] > pic.shape[1]:
                break

            result = cv2.matchTemplate(pic, scaled_template, cv2.TM_CCOEFF_NORMED)
            (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
            if found == None or maxVal > found[0]:
                found = (maxVal, maxLoc, ratio)

        if found[0] >= threshold:
            rect = (found[1][0],
                    found[1][1],
                    template.shape[1],
                    template.shape[0])
            return rect
        return False

    @staticmethod
    def random_mouse(rect):
        print('clicked')
        pyautogui.moveTo(rect[0] + random.randrange(rect[2]), rect[1] + random.randrange(rect[3]))
        pyautogui.click()

    @staticmethod
    def grab_screen():
        screen = cv2.cvtColor(numpy.array(ImageGrab.grab()), cv2.COLOR_BGR2RGB)
        return screen
