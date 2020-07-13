import matplotlib.pyplot as plt
import re
import matplotlib
matplotlib.use('Agg')

def draw_dynamic(draw_list, num):
    draw_list.sort()
    category = []
    rates = []
    for i in draw_list:
        split_list = re.split(' |/', i[0])
        length = 0
        first = 1
        temp = ""
        for j in split_list:
            if first:
                first = 0
                length = length + len(j) + 1
                temp = temp + j + ' '
            else:
                length = length + len(j) + 1
                if length >= 10:
                    temp = temp + '\n' + j + ' '
                    length = len(j)
                else:
                    temp = temp + j + ' '
        category.append(temp)
        rates.append(round(i[1], 2))

    plt.figure(figsize=(50, 25))

    plt.bar(list(range(0, 75, 5)), rates, width=2.5, color='dodgerblue')
    plt.xticks(list(range(0, 75, 5)), category, fontsize=30)
    plt.yticks(fontsize=30)
    plt.xlabel("Category", fontsize=45)
    plt.ylabel("Rating", fontsize=45)

    for x in range(0, 15):
        plt.text(x * 5, rates[x] + 0.1, '%s' % rates[x], ha='center', fontsize=30)

    plt.title("Statistics - Category to Rating", fontsize=60)
    plt.savefig('static/IMG/category_to_rating_pictures/category_to_rating_' + str(num) + '.png')

# # For testing
# category = [("Abstract Strategy", 8.5), ("Card Game", 9), ("Children's Game", 6.7), ("Dice", 8.1), ("Economic", 9.2),
#             ("Educational", 8.8), ("Fantasy", 9.0), ("Fighting", 7.6), ("Miniatures", 8.6),
#             ("Movies/TV/Radio theme", 9.5), ("Party Game", 8.3), ("Print & Play", 6.9),
#             ("Science Fiction", 7.5), ("Trivia", 7.9), ("Wargame", 8.4)]
# draw_dynamic(category)
