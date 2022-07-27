class Hiker:

    #helpers
    def count(self, dice, number):
        return len([y for y in dice if y == number])

    def highest_repeated(self, dice, minRepeats):
        unique = set(dice)
        repeats = [x for x in unique if self.count(dice, x) >= minRepeats]
        return max(repeats) if repeats else 0

    def of_a_kind(self, dice, n):
        return self.highest_repeated(dice,n) * n
        
    def two_pairs(self,hand):
         pairs = []
         hands = self.spliter(hand)
         for i in hands:
            if len(i) == 3:
               sm = i[0]+i[1]
               pairs.append(sm)
            elif len(i) == 2:
               sm = sum(i)
               pairs.append(sm)
         return sum(pairs) 
    
    def spliter(self,hand):
        current, groups = None, [[]]
        for item in sorted(hand):
            current = current or item
            is_equal = item == current
            (groups, groups[-1])[is_equal].append(([item], item)[is_equal])
            current = is_equal and current or item
        return groups

    #bets
    def chance(self,dice):
        return sum(dice)

    def pair(self,dice):
        return self.of_a_kind(dice, 2)

    def three_of_kind(self,dice):
        return self.of_a_kind(dice, 3)

    def four_of_kind(self,dice):
        return self.of_a_kind(dice, 4)

    def small_straight(self,dice):
        return 15 if tuple(sorted(dice)) == (1,2,3,4,5) else 0

    def large_straight(self,dice):
        return 20 if tuple(sorted(dice)) == (2,3,4,5,6) else 0
        
    def full_house(self, states):
        return [len(group) for group in self.spliter(states)] in [[2, 3], [3, 2]] and sum(states) or 0

    def yahtzee(self,dice):
        return 50 if len(dice) == 5 and len(set(dice)) == 1 else 0

import unittest

class TestHiker(unittest.TestCase):

    douglas = Hiker()

    tests = (  
        ((1,2,3,4,5), 0, douglas.pair), # no pairs found
        ((1,5,3,4,5), 10, douglas.pair), # one pair found
        ((2,2,6,6,4), 12, douglas.pair), # picks highest
        ((2,3,1,3,3), 6, douglas.pair), # only counts two
        ((5,1,2,1,5), 12, douglas.two_pairs),
        ((5,3,2,1,6), 0, douglas.two_pairs),
        ((1,5,5,5,1), 12, douglas.two_pairs),
        ((2,2,6,6,6), 18, douglas.three_of_kind), 
        ((2,2,4,6,6), 0, douglas.three_of_kind), # no threes found
        ((5,5,5,5,5), 15, douglas.three_of_kind), # only counts three
        ((6,2,6,6,6), 24, douglas.four_of_kind), 
        ((2,6,4,6,6), 0, douglas.four_of_kind), # no fours found
        ((5,5,5,5,5), 20, douglas.four_of_kind), # only counts four
        ((1,2,5,4,3), 15, douglas.small_straight),
        ((1,2,5,1,3), 0, douglas.small_straight),
        ((6,2,5,4,3), 20, douglas.large_straight),
        ((1,2,5,1,3), 0, douglas.large_straight),
        ((1,5,5,5,1), 17, douglas.full_house),
        ((1,5,2,5,1), 0, douglas.full_house),
        ((5,5,5,5,5), 50, douglas.yahtzee),
        ((1,5,5,5,5), 0, douglas.yahtzee), 
        ((1,2,3,4,5), 15, douglas.chance),
        )

    def testRunAll(self):
        for (dice, expected, bet) in self.tests:
            score = bet(dice)
            self.assertEqual(expected, score, "got {} expected {}, testing with {} on {}".format(score, expected, bet.__name__, dice))
        print ('ran {0} test cases'.format(len(self.tests)))


if __name__ == '__main__':
    unittest.main() # pragma: no cover
