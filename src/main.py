import cv2

from hand_detector import HandDetector
from finger_counter import count_fingers

from calculator import add
from calculator import subtract

cap = cv2.VideoCapture(0)

detector = HandDetector()

operation = "+"

while True:

    success, img = cap.read()

    if not success:
        break

    img = cv2.flip(img, 1)

    hands, img = detector.find_hands(img)

    left_num = 0
    right_num = 0

    if len(hands) >= 1:
        left_num = count_fingers(hands[0])

    if len(hands) >= 2:
        right_num = count_fingers(hands[1])

    if operation == "+":
        result = add(left_num, right_num)
    else:
        result = subtract(left_num, right_num)

    cv2.rectangle(
        img,
        (10,10),
        (520,260),
        (50,50,50),
        -1
    )

    cv2.putText(
        img,
        "KID LEARN MATH",
        (25,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,255),
        3
    )

    cv2.putText(
        img,
        f"Left Hand : {left_num}",
        (25,100),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255,255,255),
        2
    )

    cv2.putText(
        img,
        f"Right Hand : {right_num}",
        (25,140),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255,255,255),
        2
    )

    cv2.putText(
        img,
        f"Operation : {operation}",
        (25,180),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,0),
        2
    )

    cv2.putText(
        img,
        f"Result : {result}",
        (25,230),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,0,255),
        3
    )

    cv2.putText(
        img,
        "A = Add | S = Subtract",
        (20,460),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255,255,0),
        2
    )

    cv2.imshow(
        "Kid Learn Math",
        img
    )

    key = cv2.waitKey(1)

    if key == ord('a'):
        operation = "+"

    elif key == ord('s'):
        operation = "-"

    elif key == 27:
        break

cap.release()

cv2.destroyAllWindows()
