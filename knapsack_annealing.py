# simulated annealing

#會在一「設定的機率」下，接受看似不佳的状態xk ，並以此状態為基礎，進行下一個尋優動作。此一尋優路線有可能找到最佳解。

#SA的最大特色，即是在尋優過程中若發生某一状態較前一状態惡化時，SA會以一設定的機率決定是否接受此一状態，而不是直接放棄。

import numpy as np
import matplotlib.pyplot as plt
def total_valu_size(packing, valus, sizes, max_size): #看現在的背包有沒有符合規則
  v = 0.0  # value總數
  s = 0.0  # size總數
  n = len(packing)
  for i in range(n):
    if packing[i] == 1:
      v += valus[i]
      s += sizes[i]
  if s > max_size:  #如果超過最大重量限制
    v = 0.0 #價值設0
  return (v, s)

def adjacent(packing, rnd): #隨機換一個物品的狀態
  n = len(packing)
  result = np.copy(packing)
  i = rnd.randint(n) 
  if result[i] == 0:
    result[i] = 1
  elif result[i] == 1:
    result[i] = 0
  return result

def solve(n_items, rnd, valus, sizes, max_size, max_iter, start_temperature, alpha): #數量，隨機數，價值，重量，最大重量，最大迭代次數，初始溫度，機率
  # solve using simulated annealing
  curr_temperature = start_temperature
  #curr_packing = np.ones(n_items, dtype=np.int64) #初始設成全部1
  curr_packing = np.array([1,1,0,0,1,1,1,1,1,0,0,1,0,1,1]) #初始設成全部1 optimial:1,0,1,0,1,0,1,1,1,0,0,0,0,1,1
  #print("Initial guess: ")
  #print(curr_packing)

  (curr_valu, curr_size) = total_valu_size(curr_packing, valus, sizes, max_size) #計算現在狀態
  iteration = 0
  interval = (int)(max_iter / 10) #50
  
  x=[]
  y=[]
  
  while iteration <= max_iter: # 0<500
    adj_packing = adjacent(curr_packing, rnd)#隨機換一個物品的狀態
    (adj_v, _) = total_valu_size(adj_packing, valus, sizes, max_size) #計算調整後的value
    if adj_v > curr_valu:  # 調整過後的value大於現在的value的話就取代
      curr_packing = adj_packing; curr_valu = adj_v
    else:
      accept_p = np.exp( (adj_v - curr_valu ) / curr_temperature ) #波茲曼函數
      p = rnd.random() #隨機產生一個機率
      if p < accept_p:  # 小於accept_p就接受調整後的狀態
        curr_packing = adj_packing; curr_valu = adj_v 
      # else 放棄調整後的狀態 維持現況

    if iteration % interval == 0: # 印出此iteration次數的最佳解
      x.append((int)(iteration)) #圖的x軸
      y.append((int)(curr_valu)) #圖的y軸
      print("iter = %6d : curr value = %7.0f : curr temp = %10.2f " % (iteration, curr_valu, curr_temperature))
    if curr_temperature < 0.00001:
      curr_temperature = 0.00001
    else:
      curr_temperature *= alpha
    iteration += 1
  if curr_valu == 1458: #最佳解時作圖
    plt.title("simulated annealing")
    plt.xlabel("iteration")
    plt.ylabel("value")
    plt.plot(x,y)
    plt.show()
  print("/////////////////////")
  return curr_packing       

def main():
  valus = np.array([135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240])
  sizes = np.array([70,  73,  77,  80,  82,  87,  90,  94,  98,  106, 110, 113, 115, 118, 120])
  max_size = 750

  print("\nItem values: ")
  print(valus)
  print("\nItem sizes: ")
  print(sizes)
  print("\nMax total size = %d " % max_size)

  rnd = np.random.RandomState(4)
  max_iter = 500 #迭代次數
  start_temperature = 10000.0
  alpha = 0.95

  print("\nSettings: ")
  print("max_iter = %d " % max_iter)
  print("start_temperature = %0.1f " % start_temperature)
  print("alpha = %0.2f " % alpha)
  # best = 100
  # goal = 11
  while start_temperature < 12220000 :
    packing = solve(15, rnd, valus, sizes, max_size, max_iter, start_temperature, alpha)
    (v,s) = total_valu_size(packing, valus, sizes, max_size)
    if v == 1458:
      break
    #   best = v
    #   goal = start_temperature
    start_temperature = start_temperature+1000
  print("Finished solve() ")
  
  print("\nBest packing found: ")
  print(packing)
  (v,s) = total_valu_size(packing, valus, sizes, max_size)
  print("\nTotal value of packing = %0.1f " % v)
  print("Total size  of packing = %0.1f " % s)
  print("\nEnd demo ")

if __name__ == "__main__":
  main()