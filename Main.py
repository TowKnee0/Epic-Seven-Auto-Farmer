import cv2
import content_logic


farm = content_logic.Content('Hunt')

inPlay = True
while inPlay:
    farm.Repeat()

    cv2.waitKey(30000)
