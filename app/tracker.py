import cv2
import socket
from cvzone.HandTrackingModule import HandDetector


class HandTracker:
    def __init__(self, width: int = 1280, height: int = 720, port: int = 5052):
        self.height = height
        self.width = width
        self.port = port

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, self.width)
        self.capture.set(4, self.height)

        self.detector = HandDetector(maxHands=1, detectionCon=0.8)

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address_port = ("127.0.0.1", 5052)

        self.finger_tips_indexes = [8, 12, 16, 20]

    def process_capture(self):
        success, img = self.capture.read()

        if not success:
            return

        hands, img = self.detector.findHands(img)
        data = []
        if hands:
            hand = hands[0]
            landmarks = hand["lmList"]
            hand_type = hand["type"]
            data.append(hand_type)
            data.append(self.height)
            for lm in landmarks:
                data.extend([lm[0], lm[1], lm[2]])
        else:
            data.append("NoHand")
            data.append(0)
            data.extend([0 for i in range(21*3)])

        return img, data

    def capture_and_send(self, display_video=True):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            while True:
                img, data = self.process_capture()
                if data:
                    s.sendto(str.encode(str(data)), self.server_address_port)

                if display_video:
                    # Reducimos el tamano a la mitad para que no estorbe mucho en la pantalla
                    img = cv2.resize(img, (self.width // 2, self.height // 2))
                    cv2.imshow("Image", img)
                    cv2.waitKey(1)
