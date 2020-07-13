import matplotlib.pyplot as plt

category = ["Abstract\nStrategy", "Card\nGame", "Children's\nGame", "Dice", "Economic", "Educational",
            "Fantasy", "Fighting", "Miniatures", "Movies/\nTV/Radio\ntheme", "Party\nGame",
            "Print &\nPlay", "Science\nFiction", "Trivia", "Wargame"]

time = [31, 36, 22.643, 44, 101, 41, 64.066, 68.173, 103, 45, 43, 51, 88, 45, 171]

plt.bar(list(range(0, 75, 5)), time, width = 2.5, color = 'dodgerblue')
plt.xticks(list(range(0, 75, 5)), category, fontsize = 10)
plt.xlabel("Category",fontsize = 13)
plt.ylabel("Time (minutes)",fontsize = 13)
for x in range(0, 15):
    plt.text(x * 5, time[x] + 2 ,'%s' %time[x],ha ='center', fontsize = 12)
plt.title("Statistics - Category to Time", fontsize = 20)

#category.reverse()
#time.reverse()
#plt.barh(category, time)

plt.show()


