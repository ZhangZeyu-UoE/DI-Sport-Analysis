import pandas as pd
import numpy as np
import os

NUM_PLAYER = 16


def find_same(p1, p2):
    # A relation between p1 and p2 is how many same attributes they have
    count = 0
    start_year = 2  # Omit early years
    for i in range(start_year, len(p1)):
        if p1[i].split()[0] == p2[i].split()[0]:
            count += 1
    return count


rlt = np.zeros((NUM_PLAYER, NUM_PLAYER))
dp = np.zeros((NUM_PLAYER, 1 << NUM_PLAYER))
choice = np.zeros((NUM_PLAYER+1, 1 << NUM_PLAYER), dtype=np.uint8)
L = []


def clear():
    # Clear DP data
    global rlt
    global dp
    global choice
    global L
    rlt = np.zeros((NUM_PLAYER, NUM_PLAYER))
    dp = np.zeros((NUM_PLAYER, 1 << NUM_PLAYER))
    choice = np.zeros((NUM_PLAYER+1, 1 << NUM_PLAYER), dtype=np.uint8)
    L = []


# dp[i, status]: End with i-th player and have chosen "status" players
# dp[i, status] = max_j{ dp[j, status | (1<<j)] + relation(i, j)}
def search(i, status):
    # Dynamic Planning
    if status == ((1 << NUM_PLAYER) - 1):
        choice[i+1, status] = -1
        return 0
    if i != -1 and dp[i, status] > 0:
        return dp[i, status]

    max_res = 0
    for j in range(NUM_PLAYER):
        if (status & (1 << j)) == 0:
            if i == -1:
                res = search(j, status | (1 << j))
            else:
                res = search(j, status | (1 << j)) + rlt[i, j]
            if res > max_res:
                max_res = res
                choice[i+1, status] = j+1
    if i != -1:
        dp[i, status] = max_res
    return max_res


def print_list(i, status, cnt=0):
    global L
    L.append(i)
    if status == ((1 << NUM_PLAYER) - 1):
        return
    j = choice[i, status]
    print_list(j, status | (1 << (j-1)), cnt+1)


if __name__ == "__main__":
    top_list = ['ManchesterCityFC', 'LiverpoolFC', 'ChelseaFC']
    # end_list = ['CardiffCityFC', 'FulhamFC', 'HuddersfieldTownFC']
    for team_name in top_list:
        clear()
        folder = '../Data_Selected/'+team_name+'_2019'
        person_path = os.path.join(folder, '/person_'+team_name+'_2019.csv')
        career_path = os.path.join(
            folder, '/careerPath_'+team_name+'_2019.csv')

        person_data = pd.read_csv(person_path)
        career_data = pd.read_csv(career_path)

        for i in range(NUM_PLAYER):
            for j in range(i+1, NUM_PLAYER):
                rlt[i, j] = find_same(
                    career_data.loc[i].to_numpy(), career_data.loc[j].to_numpy())
                if person_data['nationality'][i] == person_data['nationality'][j]:
                    # If two players have same nationality, keep them together
                    rlt[i, j] += 100
                rlt[j, i] = rlt[i, j]
        print(search(-1, 0))
        print_list(0, 0)
        print(L)
        for i in range(1, len(L)):
            print(person_data['matchName'][L[i]-1])
