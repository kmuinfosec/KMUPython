class Vehicle :
    _ACCELERATION = 5

    def __init__(self):
        self._speed = 0

    def speed_up(self):
        if self._speed + self._ACCELERATION <= 240 :
            self._speed += self._ACCELERATION

    def __str__(self):
        return "현재 속도는 {}입니다.".format(self._speed)
