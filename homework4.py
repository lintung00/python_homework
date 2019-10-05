#輸入五個數字找到最大值

nums_str = input('請輸入五個數，數字之間加入空格：').split()
nums = [] 

# 用while迴圈應付數字少於五個的情況。
while True:
    for n in nums_str:
        if n.isdigit():   # 檢查是不是整數。
            nums += [int(n)]

        # 如果已經得到5個數字，就離開迴圈。
        if len(nums) == 5:
            break;

    # 如果數字少於三個，提示使用者繼續輸入。
    if len(nums) < 5:
        nums_str = input('請繼續輸入：').split()
    else:
        break;

max_value= 0    #初始化數值    
for i in nums:
    #找到五個數值中的最大值
    if i > max_value :  
       max_value = i;
                 
print(nums) #列出數列
print("得到最大數字")
print(max_value) # 印出最大值