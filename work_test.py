import math

input_data = input("請問每年減少耗電百分之[多少]的電量?(輸入值為0~100之間)")
input_data = float(input_data)
reduced_rate = input_data / 100
print("減少率為: " + str(reduced_rate))

end_var = 0.75
now_var = 1.0
year = 1
while( (now_var > end_var)  ):
	now_var = math.pow(1 - reduced_rate , year)
	#print(1 - reduced_rate)
	#print(year)
	#print(now_var)
	print("" + str(year) + "年後" + " 減少為原來的 " + str(now_var) + " 倍")
	year += 1
