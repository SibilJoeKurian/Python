import StringDatabase as sd
import game as gs
"""
This class represents the game
"""


class Guess:
    random_word = ""
    current_word = "****"
    missed_letters_stars = []
    game_count = 1
    game_list = []
    word_list = []
    game_status = ""
    status_list = []
    bad_guess = 0
    bad_guess_list = []
    missed_letters = 0

    missed_letters_list = []
    score_missed_letters = []
    current_score = 0
    score_list = []
    score_count = 1
    score_guess_reduction = 0

    def get_random_word(self):
        """
        This function calls the StringDatabaseClass and get the random word
        """
        self.obj = sd.StringDatabaseClass()
        Guess.random_word = self.obj.get_random_word()

    def calculate_score(self):
        """
                This function calculates the score of the random word
        """
        Guess.current_score = gs.Game().score_calculate(Guess.random_word)
        Guess.score_guess_reduction = gs.Game().calculate_score_guess(Guess.current_score, Guess.bad_guess)
        Guess.current_score = Guess.current_score - Guess.score_guess_reduction
        reduce_letter_score = gs.Game().calculate_score_letter(Guess.current_score,Guess.score_missed_letters)
        Guess.current_score = Guess.current_score - reduce_letter_score
        Guess.score_list.append(Guess.current_score)
        Guess.score_missed_letters.clear()

    def get_game_count(self):
        """
        This function keeps track of the game count and save it to the variable game_list
        """
        temp_value = Guess.game_list[-1]
        temp_value = temp_value + 1
        Guess.game_list.append(temp_value)

    def start_game(self):
        """
                This function keeps track of the game count and save it to the variable game_list
        """
        Guess.bad_guess = 0
        Guess.game_list.append(Guess.game_count)
        self.get_random_word()
        Guess.word_list.append(Guess.random_word)
        self.print_menu()

    def new_game(self):
        Guess.bad_guess_list.append(Guess.bad_guess)
        Guess.bad_guess = 0
        Guess.missed_letters_list.append(Guess.missed_letters)
        Guess.missed_letters = 0
        Guess.missed_letters_stars.append(Guess.current_word.count("*"))
        Guess.current_word = "****"
        self.get_game_count()
        self.get_random_word()
        Guess.word_list.append(Guess.random_word)
        self.print_menu()

    def check_word(self, checkword):
        """
        :param checkword: To check the word
        :return: It returns a 0 for correct check and 1 for wrong check
        """
        if checkword == Guess.random_word:
            return 0
        else:
            return 1

    def get_table(self):
        """
        This function prints the result as a table
        """
        game = Guess.game_list
        word = Guess.word_list
        status = Guess.status_list
        bad_guesses = Guess.bad_guess_list
        missed_letters = Guess.missed_letters_stars
        score = Guess.score_list
        obje = gs.Game()
        obje.printTable(game, word, status, bad_guesses, missed_letters, score)

    def guess_fun(self):
        """
        This function is called when g is pressed and do the processing of guess
        """
        print("Enter the word to guess")
        guessword = input()
        if self.check_word(guessword) == 0:
            print("Correct Guess ")
            Guess.status_list.append("Success")
            self.calculate_score()
            self.new_game()
        else:
            print("Wrong Guess")
            Guess.bad_guess = Guess.bad_guess + 1
            self.print_menu()

    def letter_fun(self):
        """
        This function is called when l is pressed and do the processing of a letter
        """
        print("Enter a letter")
        letter = input()
        new_word = ""
        new_temp_word = ""
        if letter in Guess.random_word:
            for check_letter in Guess.random_word:
                if letter == check_letter:
                    new_word = new_word + letter
                else:
                    new_word = new_word + "*"
            for i in range(0, 4):
                if Guess.current_word[i] == "*" and new_word[i] == "*":
                    new_temp_word = new_temp_word + "*"
                elif Guess.current_word[i] != "*":
                    new_temp_word = new_temp_word + Guess.current_word[i]
                else:
                    new_temp_word = new_temp_word + new_word[i]
            Guess.current_word = new_temp_word
            if Guess.current_word == Guess.random_word:
                print("Correct Word")
                Guess.status_list.append("Success")
                self.calculate_score()
                self.new_game()
            else:
                print("Correct Letter")
                self.print_menu()
        else:
            print("Wrong Letter")
            Guess.score_missed_letters.append(letter)
            Guess.missed_letters = Guess.missed_letters + 1
            self.print_menu()

    def tell_me_fun(self):
        """
        This function is called when t is pressed and shows the current value of the random variable
        """
        print("Your Word : " + Guess.random_word)
        Guess.status_list.append("Gave Up")
        # score
        Guess.current_score = gs.Game().score_calculate(Guess.random_word)
        temp=gs.Game().score_calculate(Guess.random_word)
        Guess.score_guess_reduction = gs.Game().calculate_score_guess(Guess.current_score, Guess.bad_guess)
        Guess.current_score = Guess.current_score - Guess.score_guess_reduction
        reduce_letter_score = gs.Game().calculate_score_letter(Guess.current_score,Guess.score_missed_letters)
        Guess.current_score = reduce_letter_score
        Guess.current_score=Guess.current_score-temp
        Guess.score_list.append(Guess.current_score)
        Guess.current_score=0
        self.new_game()

    def quit_fun(self):
        """
        This function is called when q is pressed and exit the program
        """
        Guess.status_list.append("Quit")
        Guess.bad_guess_list.append(Guess.bad_guess)
        Guess.missed_letters_list.append(Guess.missed_letters)
        # score
        temp = gs.Game().score_calculate(Guess.random_word)
        Guess.current_score = gs.Game().score_calculate(Guess.random_word)
        Guess.score_guess_reduction = gs.Game().calculate_score_guess(Guess.current_score, Guess.bad_guess)
        Guess.current_score = Guess.current_score - Guess.score_guess_reduction
        reduce_letter_score = gs.Game().calculate_score_letter(Guess.current_score, Guess.score_missed_letters)
        Guess.current_score = Guess.current_score - reduce_letter_score
        Guess.current_score = Guess.current_score - temp
        Guess.score_list.append(Guess.current_score)
        Guess.missed_letters_stars.append(Guess.current_word.count("*"))
        self.get_table()
        score = gs.Game().calculate_total_score(Guess.score_list)
        string_score = str(score)
        print("Final Score : " + string_score)
        exit()

    def print_menu(self):
        print("Guessing Word : " + Guess.random_word)
        print("Current guess : " + Guess.current_word)
        print("** The great guessing game **")
        print("g=guess, t=tell me, l for a letter, q for quit")
        print("Enter a letter")
        letter = input()
        if letter == "g":
            self.guess_fun()
        elif letter == "t":
            self.tell_me_fun()
        elif letter == "l":
            self.letter_fun()
        elif letter == "q":
            self.quit_fun()
        else:
            print("enter a correct letter")
            self.print_menu()


def main():
    """
    Main Function it calls the guess function and calls the start function
    """
    g = Guess()
    g.start_game()


if __name__ == "__main__":
    main()
