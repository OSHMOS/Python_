class Clock:
    def __init__(self, hour, min, sec):
        self.hour = hour
        self.min = min
        self.sec = sec
    

    def tick():
        sec += 1
        if sec == 60:
            sec = 0
            min += 1
        elif min == 60:
            min = 0
            hour += 1
        elif hour == 24:
            hour = 0