from random import shuffle


class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [None, None,
              "2", "3", "4", "5", "6", "7", "8", "9",
              "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        """両方整数"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            return self.suit < c2.suit
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            return self.suit > c2.suit
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " \
            + self.suits[self.suit]
        return v


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("player1 name: ")
        name2 = input("player2 name: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def print_winner(self, winner):
        w = "{} wins this round"
        print(w.format(winner.name))

    def print_draw(self, p1, p2):
        d = "{} draws {}, {} draws {}"
        print(d.format(p1.name, p1.card, p2.name, p2.card))

    def play_game(self):
        cards = self.deck.cards
        print("Start War!")
        while len(cards) >= 2:
            m = "exit for q, start play for any other key:"
            response = input(m)
            if response == "q":
                break
            self.p1.card = self.deck.draw()
            self.p2.card = self.deck.draw()
            self.print_draw(self.p1, self.p2)
            if self.p1.card > self.p2.card:
                self.p1.wins += 1
                self.print_winner(self.p1)
            else:
                self.p2.wins += 1
                self.print_winner(self.p2)

        win = self.winner(self.p1, self.p2)
        print("game set, {} is win!".format(win))
        print("{} wins {} times, {} wins {} times".format(self.p1.name, self.p1.wins, self.p2.name, self.p2.wins))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "draw!"


if __name__ == "__main__":
    # card1 = Card(11, 3)
    # card2 = Card(11, 2)
    # print(card1 < card2)
    # print(card1)

    # deck = Deck()
    # print(len(deck.cards))
    # for card in deck.cards:
    #     print(card)
    # print(deck.rm_card())
    # print(len(deck.cards))

    game = Game()
    game.play_game()