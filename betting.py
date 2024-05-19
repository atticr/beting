def set_print(g, t, money, bet):
  print("All : ", g)
  print("temp : ", t)
  print(money)
  print(bet)


def round(p):
  ground = p
  temp = 1

  for i in range(p):
    money[i] -= 1
    bet[i] = 1

  set_print(ground, temp, money, bet)

  for i in range(4):

    print("BET : ", i)

    x = 0
    w = 0
    x = x % p
    while bet[x] != bet[x - 1] or x == 0:
      y = 0
      while True:
        y = int(input())
        if y > money[x]:
          print("잔액이 부족합니다.")
          continue
        else:
          break

      if y <= temp and w != 1:
        bet[x] += temp
        ground += temp
        money[x] -= temp
      else:
        temp = y
        bet[x] += y
        ground += y
        money[x] -= temp
      x += 1
      z = x
      x = z % p
      if x != z:
        w = 1
      set_print(ground, temp, money, bet)
      print(x)

    set_print(ground, temp, money, bet)


print("player : ")
play_num = int(input())
print("basic_money : ")
bm = int(input())

money = []
bet = []
temp = 0
ground = 0

for i in range(play_num):
  money.append(bm)
  bet.append(0)

round(play_num)
