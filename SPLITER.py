#!/usr/bin/env python3

'''
Takes array of intigers and groups them by same intiger.
'''
def spliter(dice):
        current, groups = None, [[]]
        for item in sorted(dice):
            current = current or item
            is_equal = item == current
            (groups, groups[-1])[is_equal].append(([item], item)[is_equal])
            current = is_equal and current or item
        return groups


if __name__ == "__main__":

	dice = [10, 20, 20, 10, 10, 30, 50, 10, 20]
	print(spliter(dice))
