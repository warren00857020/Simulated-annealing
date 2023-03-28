# Simulated-annealing
作業2-2

#SA特色<br>
會在一「設定的機率」下，接受看似不佳的狀態 ，並以此狀態為基礎，進行下一個尋找最佳解的動作。此一尋找最佳解的路線有可能找到最佳解。<br><br>

SA的最大特色，即是在尋找最佳解的過程中若發生某一狀態較前一狀態惡化時，SA會以一設定的機率決定是否接受此一状態，而不是直接放棄。<br><br>

#code介紹<br>
total_valu_size():看現在的背包有沒有符合規則<br>
adjacent():隨機換一個物品的狀態<br>
solve():用SA解決此背包問題
<br><br><br>
為了找出最佳解，在main函式裡窮舉退火溫度，結果在start_temperature=3591000時迭代250次的時後衝出了區域最佳解
