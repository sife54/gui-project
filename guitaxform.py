"""
File: guitaxform.py
By: Matthew Norloff
"""

from breezypythongui import EasyFrame
import tkinter


class LayoutDemo(EasyFrame):
    """Displays labels in the quadrants."""

    def __init__(self):
        """Sets up the window and the labels."""
        EasyFrame.__init__(self)
        self.addLabel(text="Insert Yearly Income(numbers only):", row=0, column = 0)
        self.income = self.addFloatField(value=0, row=0, column=1)
        self.addLabel(text="Insert Number of Dependents(whole numbers only):", row=1, column=0)
        self.dependents = self.addIntegerField(value=0, row=1, column=1)
        self.addLabel(text="output(if you did not enter numbers correctly it will not output):", row=3, column=1)
        self.output = self.addFloatField(value=0, row=3, column=2, state="readonly")

        self.addButton(text="Compute", row=2, column=2, command=self.num)

    def num(self):
        taxrate = 0.20
        standard = 10000.0
        dependent = 3000.0
        yearly_income = self.income.getNumber()
        depends = self.dependents.getNumber()
        taxableincome = round(yearly_income, 2) - standard - \
                        dependent * depends
        incometax = taxableincome * taxrate
        self.output.setNumber(incometax)


def main():
    """Instantiate and pop up the window."""
    LayoutDemo().mainloop()


if __name__ == "__main__":
    main()
