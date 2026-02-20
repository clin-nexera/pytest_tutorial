import time

class FakeRobot:
    def __init__(self):
        self._is_connected = False

    def connect(self):
        print("Robot is connecting")
        time.sleep(1)
        self._is_connected = True
        print("Robot connected")

    def disconnect(self):
        print("Robot is disconnecting")
        time.sleep(1)
        self._is_connected = False
        print("Robot disconnected")

    def move(self):
        print("Robot is moving")
        time.sleep(2)
        print("Robot moved")
