from itertools import groupby

def parse_fig(fig):
    if fig.isdigit():
        return int(fig)
    elif fig == "T":
        return 10
    elif fig == "J":
        return 11
    elif fig == "Q":
        return 12
    elif fig == "K":
        return 13
    elif fig == "A":
        return 14
    else:
        raise Exception('UNRECOGNIZED CARD')


class Hand(object):
    def __init__(self, hand):
        self.figs = [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]]
        self.figs = sorted([parse_fig(x) for x in self.figs])
        self.colors = [hand[0][1], hand[1][1], hand[2][1], hand[3][1], hand[4][1]]
        self.sorted_figs = sorted(self.figs)

        self.pair = None
        self.pair1 = None
        self.pair2 = None
        self.three = None
        self.full = None

        self.score = None

        if self.royal_flush():
            self.score = 9
        elif self.straight_flush():
            self.score = 8
        elif self.four_of_a_kind():
            self.score = 7
        elif self.full_house():
            self.score = 6
        elif self.flush():
            self.score = 5
        elif self.straight():
            self.score = 4
        elif self.three_of_a_kind():
            self.score = 3
        elif self.two_pairs():
            self.score = 2
        elif self.one_pair():
            self.score = 1
        else:
            self.score = 0

    def royal_flush(self):
        return len(set(self.colors)) == 1 and self.sorted_figs[4]-self.sorted_figs[0] == 4 and self.sorted_figs[4] == 14

    def straight_flush(self):
        return len(set(self.colors)) == 1 and self.sorted_figs[4] - self.sorted_figs[0] == 4 and len(set(self.figs)) == 5

    def four_of_a_kind(self):
        return any([len(list(group)) == 4 for key, group in groupby(self.figs)])

    def full_house(self):
        if any([len(list(group)) == 3 for key, group in groupby(self.figs)]) and \
               any([len(list(group)) == 2 for key, group in groupby(self.figs)]):
            self.full = [key for key, group in groupby(self.figs) if len(list(group)) == 3][0]
            return True

    def flush(self):
        return len(set(self.colors)) == 1

    def straight(self):
        return len(set(self.figs)) == 5 and self.sorted_figs[4] - self.sorted_figs[0] == 4

    def three_of_a_kind(self):
        if any([len(list(group)) == 3 for key, group in groupby(self.figs)]):
            self.three = [key for key, group in groupby(self.figs) if len(list(group)) == 3][0]
            return True

    def two_pairs(self):
        if len(set(self.figs)) == 3 and not any([len(list(group)) == 3 for key, group in groupby(self.figs)]):
            pairs = ([[key, list(group)] for key, group in groupby(self.figs) if len(list(group)) == 2])
            print pairs
            self.pair1 = pairs[1]
            self.pair2 = pairs[0]
            return True

    def one_pair(self):
        if any([len(list(group)) == 2 for key, group in groupby(self.figs)]):
            self.pair = [key for key, group in groupby(self.figs) if len(list(group)) == 2][0]
            return True

    def get_hand(self):
        return zip(self.figs, self.colors)

    def get_figs(self):
        return self.sorted_figs

    def did_i_win(self, oponent):
        if self.score > oponent.score:
            return True
        elif self.score < oponent.score:
            return False
        else:
            if self.score == 1:
                if self.pair > oponent.pair:
                    return True
                elif self.pair < oponent.pair:
                    return False
                else: return self.compare_high_card(oponent)
            elif self.score == 2:
                if self.pair1 > oponent.pair1:
                    return True
                elif self.pair1 < oponent.pair1:
                    return False
                else:
                    if self.pair2 > oponent.pair2:
                        return True
                    elif self.pair2 < oponent.pair2:
                        return False
                    else:
                        return self.compare_high_card(oponent)
            elif self.score == 3:
                if self.three > oponent.three:
                    return True
                elif self.three < oponent.three:
                    return False
            elif self.score == 6:
                if self.full > oponent.full:
                    return True
                elif self.full < oponent.full:
                    return False
                else: return self.compare_high_card(oponent)
            else:
                return self.compare_high_card(oponent)

    def compare_high_card(self, oponent):
        if self.get_figs()[4] > oponent.get_figs()[4]:
            return True
        elif self.get_figs()[4] < oponent.get_figs()[4]:
            return False
        else:
            if self.get_figs()[3] > oponent.get_figs()[3]:
                return True
            elif self.get_figs()[3] < oponent.get_figs()[3]:
                return False
            else:
                if self.get_figs()[2] > oponent.get_figs()[2]:
                    return True
                elif self.get_figs()[2] < oponent.get_figs()[2]:
                    return False
                else:
                    if self.get_figs()[1] > oponent.get_figs()[1]:
                        return True
                    elif self.get_figs()[1] < oponent.get_figs()[1]:
                        return False
                    else:
                        if self.get_figs()[0] > oponent.get_figs()[0]:
                            return True
                        elif self.get_figs()[0] < oponent.get_figs()[0]:
                            return False
                        else:
                            raise Exception('DRAW!!!')

if __name__ == '__main__':
    # hand = (['AC', 'KC', 'AS', '2D', '3D'])
    # P1 = Hand(hand)
    # print P1.figs, P1.score, P1.pair, P1.pair1, P1.pair2, P1.three, P1.full
    P1_wins = 0
    P2_wins = 0
    with open("p054_poker.txt", "r") as f:
        for line in f:
            hand1 = line.rstrip().split(" ")[:5]
            hand2 = line.rstrip().split(" ")[5:]
            P1 = Hand(hand1)
            P2 = Hand(hand2)
            print P1.get_figs(), P1.score, "   ", P2.get_figs(), P2.score, P1.did_i_win(P2)
            if P1.did_i_win(P2):
                P1_wins += 1
            if P2.did_i_win(P1):
                P2_wins += 1
    print P1_wins
    print P2_wins


