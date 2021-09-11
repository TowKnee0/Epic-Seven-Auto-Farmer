from operations import Operations
import cv2
import random
import constants



class Content:
    def __init__(self, content):
        self.content = content
        self.start = cv2.imread('Images\Start.PNG', 1)
        self.repeat_end = cv2.imread('Images\RepeatEnd.PNG', 1)
        self.confirm = cv2.imread('Images\Confirm.PNG', 1)
        self.try_again = cv2.imread('Images\TryAgain.PNG', 1)
        self.buy = cv2.imread('Images\Buy.PNG', 1)
        self.energy = cv2.imread('Images\Energy.PNG', 1)

    def Repeat(self):

        if self.content == "Hunt":
            current_screen = Operations.grab_screen()
            repeat_stopped = Operations.multiscale_template_match(current_screen, self.repeat_end,
                                                                  constants.GLOBAL_THRESH)

            if repeat_stopped != False:
                confirm_visible = Operations.multiscale_template_match(current_screen, self.confirm,
                                                                       constants.GLOBAL_THRESH)
                if confirm_visible != False:
                    Operations.random_mouse(confirm_visible)
                    cv2.waitKey(random.randint(constants.DELAY_MIN, constants.DELAY_MAX))
                current_screen = Operations.grab_screen()
                try_again_visible = Operations.multiscale_template_match(current_screen, self.try_again,
                                                                         constants.GLOBAL_THRESH)
                if try_again_visible != False:
                    Operations.random_mouse(try_again_visible)

            cv2.waitKey(random.randint(constants.DELAY_MIN, constants.DELAY_MAX))

            current_screen = Operations.grab_screen()
            start_battle = Operations.multiscale_template_match(current_screen, self.start,
                                                                constants.GLOBAL_THRESH)
            if start_battle != False:
                Operations.random_mouse(start_battle)
                cv2.waitKey(random.randint(constants.DELAY_MIN, constants.DELAY_MAX))
                current_screen = Operations.grab_screen()
                buy_btn = Operations.multiscale_template_match(current_screen, self.buy, constants.GLOBAL_THRESH)
                if buy_btn != False:
                    Operations.random_mouse(buy_btn)
                    cv2.waitKey(random.randint(constants.DELAY_MIN, constants.DELAY_MAX))
                    current_screen = Operations.grab_screen()
                    start_battle = Operations.multiscale_template_match(current_screen, self.start,
                                                                        constants.GLOBAL_THRESH)
                    if start_battle != False:
                        Operations.random_mouse(start_battle)
