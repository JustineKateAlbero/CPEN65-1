print("What is the type of given measurement?   ", "\n", "\t", "Press 1 for Radius", "\n", "\t", "Press 2 for Diameter",
      "\n", "\t", "Press 3 for Circumference")

class Circle:
    def __init__(self, given):
        self.given = given

    def area(self):
        pi = 3.14
        self.measurement = measurement

        if self.given == 1:
            print("The area of the circle is:" + " ", + self.measurement ** 2 * pi)
        elif self.given == 2:
            print("The area of the circle is:" + " ", +  ((self.measurement ** 2) * pi) / 4)
        elif self.given == 3:
            print("The area of the circle is " + " ", + (self.measurement ** 2) / (4 * pi))
        else:
            print("Select a valid option")


given = int(input("Select the measurement type:  "))
measurement = float(input("Enter the value: "))
Given = Circle(given)
Given.area()
