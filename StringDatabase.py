import random

"""
This class takes care of the file I/O operations and returns the randomword
"""


class StringDatabaseClass:

    def __init__(self):
        self.file = open('four_letters.txt')
        self.file_data = []

    def get_random_word(self):
        """
        This funtion returns the random variable
        :return: the random variable
        """
        string = self.file.read()
        data = string.split()
        random_word = random.choice(data)
        # print(random_word)
        return random_word

# sd=StringDatabaseClass()
# set=sd.get_random_word()
# print(set)
