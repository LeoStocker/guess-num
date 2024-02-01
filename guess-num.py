import random
print('歡迎加入猜數字遊戲!')
num_low = input('請輸入猜數字遊戲最小值: ')
num_high = input('請輸入猜數字遊戲最大值: ')
print('本次猜數字遊戲的範圍為:',num_low,'~',num_high)
print('開始遊戲!')
num_low = int(num_low)
num_high = int(num_high)
correct_answer = random.randint(num_low,num_high)
i=0
while True:
	i = i+1
	ans = input('請輸入數字: ')
	ans = int(ans)
	if ans == correct_answer:
		print('終於猜對了!')
		print('你猜了',i,'次')
		break
	else:
		if ans > correct_answer:
			print('比答案大')
		else:
			print('比答案小')
