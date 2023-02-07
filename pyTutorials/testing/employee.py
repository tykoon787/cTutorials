import requests

class Employee:
    """A class to represent Employees"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        self.month = month
        response = requests.get(f'http://company.com/{self.last}/{self.month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'