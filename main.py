class stringCheck:
    @staticmethod
    def inverser_chaine(chaine):
        return chaine[::-1]

    @staticmethod
    def est_palindrome(chaine):
        return chaine == chaine[::-1]

    @staticmethod
    def compter_lettres(chaine):
        return len(chaine)
