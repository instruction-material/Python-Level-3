"""Bubble-sort leaderboards over the original synthetic player records."""

import math

# List of baseball players with random stats: avg, home run, RBI
p1 = ["B. Harper", 0.254, 27, 92]
p2 = ["J. Soler", 0.256, 36, 91]
p3 = ["C. Yelich", 0.329, 41, 89]
p4 = ["C. Bellinger", 0.312, 42, 100]
p5 = ["M. Trout", 0.299, 41, 99]
p6 = ["F. Lindor", 0.296, 23, 56]
p7 = ["M. Betts", 0.285, 21, 67]
p8 = ["A. Rendon", 0.328, 29, 104]
p9 = ["D. Lemahieu", 0.331, 22, 87]
p10 = ["R. Acuna", 0.290, 36, 89]

playerList = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
player_list = playerList


def bubble_baseball(players, stat):
    """Rank validated records descending by stat; return fresh names, retaining ties."""
    if stat not in ("Average", "Home Run", "RBI"):
        raise ValueError("stat must be Average, Home Run or RBI")
    if not isinstance(players, list):
        raise ValueError("players must be a list of four-field records")
    for number, record in enumerate(players, 1):
        if not isinstance(record, (list, tuple)) or len(record) != 4:
            raise ValueError("record " + str(number) + " must have four fields")
        name, average, home_runs, rbi = record
        if not isinstance(name, str) or not name.strip():
            raise ValueError("record " + str(number) + " must have a nonblank name")
        if (type(average) not in (int, float) or not 0 <= average <= 1
                or not math.isfinite(average)):
            raise ValueError("record " + str(number) + " average must be finite in [0, 1]")
        if any(type(value) is not int or value < 0 for value in (home_runs, rbi)):
            raise ValueError("record " + str(number) + " counts must be nonnegative integers")
    field = {"Average": 1, "Home Run": 2, "RBI": 3}[stat]
    ranked = players.copy()
    for end in range(len(ranked) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if ranked[index][field] < ranked[index + 1][field]:
                ranked[index], ranked[index + 1] = ranked[index + 1], ranked[index]
                swapped = True
        if not swapped:
            break
    return [record[0] for record in ranked]


def print_list(names):
    """Print one tab-indented name per line; return None."""
    if not isinstance(names, list) or not all(isinstance(name, str) for name in names):
        raise ValueError("names must be a list of strings")
    for name in names:
        print("\t" + name)


def main():
    """Display the three leaderboards without changing playerList."""
    for number, stat in enumerate(("Average", "Home Run", "RBI")):
        print(("\n" if number else "") + stat + " Leaderboard:")
        print_list(bubble_baseball(playerList, stat))


if __name__ == "__main__":
    main()
