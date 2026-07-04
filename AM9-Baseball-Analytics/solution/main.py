###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

# List of baseball players with random stats
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

player_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]


# Slightly modified bubblesort to accomodate different areas. Returns the names in correct order rather than the list itself.
def bubble_baseball(players, stat):
    num = 0
    if stat == "Average":
        num = 1
    elif stat == "Home Run":
        num = 2
    elif stat == "RBI":
        num = 3

    names = []
    for i in range(0, len(players)):
        for j in range(0, len(players) - 1):
            if players[j][num] > players[j + 1][num]:
                temp = players[j]
                players[j] = players[j + 1]
                players[j + 1] = temp
        names.append(players[len(players) - i - 1][0])
    return names


def print_list(list1):
    for i in range(len(list1)):
        print("\t" + list1[i])


import time

print("Average Leaderboard:")
print_list(bubble_baseball(player_list, "Average"))
time.sleep(2)
print("\nHome Run Leaderboard:")
print_list(bubble_baseball(player_list, "Home Run"))
time.sleep(2)
print("\nRBI Leaderboard:")
print_list(bubble_baseball(player_list, "RBI"))
