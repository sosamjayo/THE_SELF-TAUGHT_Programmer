from random import shuffle


class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = [None, None,
              "2", "3", "4", "5", "6", "7", "8", "9",
              "10", "Jack", "Queen", "King", "Ace"]
    
    def __init__(self, v, s) -> None:
        self.value = v
        self.suit = s
    
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
    
    def __repr__(self) -> str:
        return Card.values[self.value] + "of" + Card.suits[self.suit]


class Deck:
    def __init__(self) -> None:
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)
        
    def rm_cards(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()


class Player:
    def __init__(self, name) -> None:
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self) -> None:
        name1 = input("player1's name:")
        name2 = input("player2's name:")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
    
    def wins(self, winner) -> None:
        print("このラウンドは{}が勝ちました．".format(winner))
    
    def draw(self, p1n, p1c, p2n, p2c) -> None:
        print("{}は{}を，{}は{}を引きました．".format(p1n, p1c, p2n, p2c))
    
    def play_game(self):
        cards = self.deck.cards
        print("戦争を始めます．")
        while len(cards) >= 2:
            response = input("qで終了，それ以外のキーでplay")
            if response == 'q':
                break
            p1c = self.deck.rm_cards()
            p2c = self.deck.rm_cards()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(p1n)
            else:
                self.p2.wins += 1
                self.wins(p2n)
        self.winner(self.p1, self.p2)
    
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            print("{}の勝ちデース！".format(p1.name))
        elif p1.wins < p2.wins:
            print("{}の勝ちデース！".format(p2.name))
        else:
            print("引き分け")



game = Game()
game.play_game()
