# 處理首頁自動出現top-rating桌遊要用的list
def home_top_rating_list(old_list):
    newList = []
    for row in old_list:
        newRow = []
        # 放入桌遊名稱
        newRow.append(row[0])
        # 放入適合玩家範圍
        if row[1] == row[2]:
            newRow.append(row[1])
        else:
            if row[1] < row[2]:
                newRow.append(str(row[1]) + '~' + str(row[2]))
            else:
                newRow.append(str(row[2]) + '~' + str(row[1]))
        # 放入遊戲時長範圍
        if row[3] == row[4]:
            newRow.append(row[3])
        else:
            if row[3] < row[4]:
                newRow.append(str(row[3]) + '~' + str(row[4]))
            else:
                newRow.append(str(row[4]) + '~' + str(row[3]))
        newList.append(newRow)
    return newList


def filter_search_list(old_list):
    newList = []
    for row in old_list:
        newRow = []
        # 放入桌遊名稱
        newRow.append(row[0])
        # 放入category
        newRow.append(row[1])
        # 放入players
        if row[2] == row[3]:
            newRow.append(row[2])
        else:
            if row[2] < row[3]:
                newRow.append(str(row[2]) + '~' + str(row[3]))
            else:
                newRow.append(str(row[3]) + '~' + str(row[2]))
        # 放入playtime
        if row[4] == row[5]:
            newRow.append(row[4])
        else:
            if row[4] < row[5]:
                newRow.append(str(row[4]) + '~' + str(row[5]))
            else:
                newRow.append(str(row[5]) + '~' + str(row[4]))
        # 放入rating
        newRow.append(str(row[6]))
        # 放入rating_players
        newRow.append(str(row[7]))
        newList.append(newRow)
    return newList
