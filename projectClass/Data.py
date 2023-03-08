
class Data:

    def __init__(self, id:int, value:int):
        self.id = id
        self.value = value

    def __str__(self):
        return f'Data id: {self.id} | value: {self.value}'

    def __add__(self, other):
        return self.value + other.value
