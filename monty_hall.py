import random


def set_stage():
    stage = ['goat', 'goat', 'Cadillac']
    random.shuffle(stage)
    return stage


def set_montys_stage(stage, player_guess):
    montys_stage = []
    for index, item in enumerate(stage):
        if index == player_guess:
            continue
        else:
            montys_stage.append(index)
    random.shuffle(montys_stage)
    return montys_stage


def play_game_stay(stage):
    player_guess = random.randint(0, 2)
    # montys_stage = set_montys_stage(stage, player_guess)
    # if stage[montys_stage[0]] == 'Cadillac':
    #     montys_door = montys_stage[1]
    # else:
    #     montys_door = montys_stage[0]
    # player stays with initial choice
    if stage[player_guess] == 'Cadillac':
        state = 1
    else:
        state = 0
    # print("Stage: {} Player Guess: {} Monty's Door: {}".format(
    #     stage, player_guess, montys_door))
    return state


def play_game_switch(stage):
    player_guess = random.randint(0, 2)
    montys_stage = set_montys_stage(stage, player_guess)
    if stage[montys_stage[0]] == 'Cadillac':
        montys_door = montys_stage[1]
    else:
        montys_door = montys_stage[0]
    # player switches to the other unopened door
    for index, item in enumerate(stage):
        if player_guess == index:
            continue
        elif montys_door == index:
                continue
        else:
            player_final_guess = index
    if stage[player_final_guess] == 'Cadillac':
        state = 1
    else:
        state = 0
    # print("Stage: {} Player Guess: {} Monty's Door: {}".format(
    #     stage, player_final_guess, montys_door))
    return state


def simulate_stay(trials):
    stay_results = []
    for idx in range(trials):
        stage = set_stage()
        state = play_game_stay(stage)
        stay_results.append(state)
    return stay_results


def simulate_switch(trials):
    switch_results = []
    for idx in range(trials):
        stage = set_stage()
        state = play_game_switch(stage)
        switch_results.append(state)
    return switch_results


def main():
    trials = 1000
    stay_results = simulate_stay(trials)
    print("Stay strategy win percentage: {}%".format(
        round((sum(stay_results) / len(stay_results) * 100), 2)))
    switch_results = simulate_switch(trials)
    print("Switch strategy win percentage: {}%".format(
        round((sum(switch_results) / len(switch_results) * 100), 2)))


if __name__ == '__main__':
    main()
