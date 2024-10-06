N = int(input("請輸入一個正整數: "))

if 1 <= N <= 100000:
    reversed_N = int(str(N)[::-1]) 
    # 將整數轉換為字串，反轉後再轉回整數
    
    print("反轉後的數字是:", reversed_N)
    # 輸出反轉後的整數