
COIN_VALUES = [1,2,5,10,20,50,100,200]

def count_combinations(target_sum, highest_allowed_coin):
    if target_sum == 0:
        return 1
    lower_or_eq_coins = filter(lambda x: True if x <= highest_allowed_coin else False, COIN_VALUES)
    combinations = 0
    for chosen_coin in lower_or_eq_coins:
        if target_sum - chosen_coin >= 0:
            combinations += count_combinations(target_sum - chosen_coin, chosen_coin)
    return combinations

print(count_combinations(200, 200))

