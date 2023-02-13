import datetime


class TimePrinter:
    def Year(self):
        return datetime.date.today().year

    def Month(self):
        return datetime.date.today().month

    def Day(self):
        return datetime.date.today().day

    def Hour(self):
        return datetime.datetime.now().hour

    def Minute(self):
        minute = datetime.datetime.now().minute
        return minute if minute > 9 else ("0" + str(minute))

    def Print1(self):
        print("{0}/{1}/{2} {3}:{4}".format(self.Day(), self.Month(), self.Year(), self.Hour(), self.Minute()))

    def Print2(self):
        print("{0}/{1}/{2} {3}:{4}".format(self.Month(), self.Day(), self.Year(), self.Hour(), self.Minute()))

    def Print3(self):
        if self.Hour() < 12:
            ampm = "am"
        else:
            ampm = "pm"
        print(
            "{0}/{1}/{2} {3}:{4}".format(self.Day(), self.Month(), self.Year(), self.Hour() % 12, self.Minute()) + ampm)


timeprinter = TimePrinter()
timeprinter.Print1()
timeprinter.Print2()
timeprinter.Print3()
