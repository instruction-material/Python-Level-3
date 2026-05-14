# List of baseball players with random stats
p1 = ["B. Harper", .254, 27, 92]
p2 = ["J. Soler", .256, 36, 91]
p3 = ["C. Yelich", .329, 41, 89]
p4 = ["C. Bellinger", .312, 42, 100]
p5 = ["M. Trout", .299, 41, 99]
p6 = ["F. Lindor", .296, 23, 56]
p7 = ["M. Betts", .285, 21, 67]
p8 = ["A. Rendon", .328, 29, 104]
p9 = ["D. Lemahieu", .331, 22, 87]
p10 = ["R. Acuna", .290, 36, 89]

playerList = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]


# Slightly modified bubblesort to accomodate different areas. Returns the names in correct order rather than the list itself.
def bubbleBaseball(players, stat):
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


def printList(list1):
    for i in range(len(list1)):
        print("\t" + list1[i])


import time

print("Average Leaderboard:")
printList(bubbleBaseball(playerList, "Average"))
time.sleep(2)
print("\nHome Run Leaderboard:")
printList(bubbleBaseball(playerList, "Home Run"))
time.sleep(2)
print("\nRBI Leaderboard:")
printList(bubbleBaseball(playerList, "RBI"))
