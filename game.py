"""
@Guess: This class contains the functions for calculating
the score of a game and finally printing the score table
"""


class Game:
    def printTable(self, game, word, status, bad_guesses, missed_letters, score):
        """
        This function is used to printing the table
        :param game: It contains the game list
        :param word: It contains the random word list
        :param status: status of a particular
        :param bad_guesses: it contains the bad guesses list
        :param missed_letters: it contains the missed letters list
        :param score: it contains the score of each game
        """
        titles = ['Game', 'Word', 'Status', 'Bad Guesses', 'Missed Letters', 'Score']
        data = [titles] + list(zip(game, word, status, bad_guesses, missed_letters, score))
        #print(data)
        for i, d in enumerate(data):
            line = '|'.join(str(x).ljust(18) for x in d)
            print(line)
            if i == 0:
                print('-' * len(line))

    def score_calculate(self, word):
        """
        It calculates the score of a word using the frequency
        :param word:random word
        :return: it returns the frequency of the word
        """
        score_map = {"a": 5.53,
                     "b": 12.21,
                     "c": 10.92,
                     "d": 9.45,
                     "e": 1,
                     "f": 11.47,
                     "g": 11.68,
                     "h": 7.61,
                     "i": 6.73,
                     "j": 13.55,
                     "k": 12.93,
                     "l": 9.67,
                     "m": 11.29,
                     "n": 6.95,
                     "o": 6.19,
                     "p": 11.77,
                     "q": 13.6,
                     "r": 7.71,
                     "s": 7.37,
                     "t": 4.64,
                     "u": 10.94,
                     "v": 12.72,
                     "w": 11.34,
                     "x": 13.55,
                     "y": 11.73,
                     "z": 13.63}
        score = 0
        for i in word:
            score = score + score_map[i]
        return int(score)

    def calculate_score_letter(self,score, missed_letter):
        """
        Calculating the score of missed letters
        :param score: total score of the random variable
        :param missed_letter: missed letters list
        :return: It returns the total score of the missed letters
        """
        score1 = 0
        length = len(missed_letter)
        if length!=0:
           score1 = score/length
        return int(score1)

    def calculate_score_guess(self, score, missed_guess):
        """
        Calculating the score of the missed gusses
        :param score: it contains the score
        :param missed_guess: it contains the list of missed gusses
        :return: the score of missed letter
        """
        actual_score = score
        reduce_score = (int(actual_score) * 10 * missed_guess) / 100
        return int(reduce_score)

    def calculate_total_score(self, list):
        """
        Calculate the total score on the basis of the missed letters count
        :param list: list of missed letters
        :return: score of the list
        """
        score = 0
        for i in list:
            score = score + i
        return score
