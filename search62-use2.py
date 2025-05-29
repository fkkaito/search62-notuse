import random
# 配列 0 番地未使用
# ランダムな201件のデータを生成し、ソートする
Cod = sorted(random.sample(range(100, 1000), 201))
# 0番地未使用のため、最初の要素は0にする
Cod[0] = 0
print(f'生成されたデータ（最初の10件のみ表示）: {Cod[1:11]}')
n = len(Cod) - 1
print(f'生成されたデータは、{n} 件です')

Str = int(input('数値を入力:'))
Lo = 1
Hi = n
Mid = (Hi + Lo) // 2
print(f'上限:{Hi} 下限:{Lo} 中央:{Mid}中央値:{Cod[Md]} 数値:{str}')

# while Cod[Mid] != Str and Lo <= Hi:
while Lo <= Hi:
  if Cod[Mid] == Str:
    break
  print('データを見つけたよ')

  if Cod[Mid] > Str:
    Hi = Mid - 1
  else:
    Lo = Mid + 1
  Mid = (Hi + Lo) // 2
  print(f'上限:{Hi} 下限:{Lo} 中央値:{Mid} 数値:{Str}')

if Hi >= Lo:
  print("該当データあり")
else:
  print("該当データなし")