import matplotlib.pyplot as plt

year_published = ["1951\n~1955", "1956\n~1960", "1961\n~1965", "1966\n~1970", "1971\n~1975",
                  "1976\n~1980", "1981\n~1985", "1986\n~1990", "1991\n~1995", "1996\n~2000",
                  "2001\n~2005", "2006\n~2010", "2011\n~2015", "2016\n~2020"]

card_game = [67, 66, 104, 117, 132, 175, 324, 420, 614, 1124, 2320, 3704, 6876, 2604]
wargame = [4, 9, 32, 78, 375, 756, 795, 718, 908, 1014, 1635, 2352, 2758, 1000]
childrens_game = [106, 182, 182, 207, 246, 322, 408, 569, 650, 865, 1352, 1908, 1913, 396]
dice = [52, 65, 58, 85, 166, 174, 232, 343, 389, 501, 757, 1276, 2071, 802]
fantasy = [4, 7, 6, 8, 33, 121, 174, 212, 267, 336, 874, 1365, 2948, 1321]
abstract_strategy = [26, 33, 64, 158, 294, 300, 379, 356, 357, 448, 927, 1161, 1541, 385]
miniatures = [1, 0, 19, 26, 78, 162, 105, 208, 280, 417, 781, 1162, 2193, 939]
educational = [63, 68, 69, 121, 149, 160, 208, 330, 333, 479, 800, 1178, 959, 234]
party_game = [41, 25, 24, 55, 50, 36, 131, 334, 386, 378, 798, 1151, 1780, 695]
science_fiction = [13, 5, 18, 22, 42, 211, 307, 284, 290, 380, 664, 820, 2094, 848]
fighting = [2, 4, 9, 12, 35, 80, 101, 167, 213, 300, 813, 1182, 1954, 762]
trivia = [39, 28, 35, 42, 44, 55, 287, 433, 441, 468, 819, 1295, 712, 80]
economics = [18, 28, 49, 56, 116, 177, 252, 296, 233, 406, 679, 1033, 1137, 336]
#Movies/TV/Radio Theme
mtr_theme = [58, 135, 225, 130, 134, 196, 294, 289, 326, 356, 767, 875, 969, 323]
print_and_play = [0, 0, 1, 3, 3, 5, 12, 14, 31, 128, 787, 1430, 1753, 414]

plt.plot(year_published, card_game, 'o-', label = 'Card Game', color = 'lightcoral')
plt.plot(year_published, wargame, 'o-', label = 'WarGame', color = 'darkred')
plt.plot(year_published, childrens_game, 'o-', label = "Children's Game", color = 'red')
plt.plot(year_published, dice, 'o-', label = 'Dice', color = 'chocolate')
plt.plot(year_published, fantasy, 'o-', label = 'Fantasy', color = 'darkorange')
plt.plot(year_published, abstract_strategy, 'o-', label = 'Abstract Strategy', color = 'saddlebrown')
plt.plot(year_published, miniatures, 'o-', label = 'Miniatures', color = 'olive')
plt.plot(year_published, educational, 'o-', label = 'Educational', color = 'y')
plt.plot(year_published, party_game, 'o-', label = 'Party Game', color = 'green')
plt.plot(year_published, science_fiction, 'o-', label = 'Science Fiction', color = 'turquoise')
plt.plot(year_published, fighting, 'o-', label = 'Fighting', color = 'dodgerblue')
plt.plot(year_published, trivia, 'o-', label = 'Trivia', color = 'blueviolet')
plt.plot(year_published, economics, 'o-', label = 'Economics', color = 'royalblue')
plt.plot(year_published, mtr_theme, 'o-', label = 'Movies/TV/Radio Theme', color = 'gold')
plt.plot(year_published, print_and_play, 'o-', label = 'Print & Play', color = 'crimson')

plt.legend(loc = "best", fontsize = 10)
plt.title("Statistics - Circulation to Published Time", fontsize = 20)
plt.xlabel("Published Year", fontsize = 13)
plt.ylabel("Circulations", fontsize = 13)
plt.show()
