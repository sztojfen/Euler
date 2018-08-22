target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]

ways = [1] + [0] * target

for coin in coins:
    for i in range(coin, target + 1):
        ways[i] += ways[i - coin]

print ways[200]

############# HOW MANY COINS IN OPTIMAL SOLUTION AND WHAT COINS SET FOR TARGET ###############

# available_coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]
# target = 8762
# number_of_coins = [0] * (target + 1)
# first_coin = [0] * (target + 1)
#
# for t in range(1, target+1):
#         min = 100000
#         for coin in available_coins:
#             if coin <= t:
#                 if 1 + number_of_coins[t-coin] < min:
#                     min = 1 + number_of_coins[t-coin]
#                     temp_coin = coin
#         number_of_coins[t] = min
#         first_coin[t] = temp_coin
#
# print number_of_coins
# print first_coin
#
# while target > 0:
#     print first_coin[target]
#     target = target - first_coin[target]