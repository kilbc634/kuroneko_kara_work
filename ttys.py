str_input = input("請輸入英文:")
lib = {}
#if(str_input[0] > str_input[-1]):
#	print(str(str_input[0]) + ">" + str(str_input[-1]))
	
#elif(str_input[0] < str_input[-1]):
#	print(str(str_input[0]) + "<" + str(str_input[-1]))
	
#else:
#	print("unknow")

#print(ord(str_input[0]))

#str_to_int_list = []
for text in str_input:
	if(lib.__contains__(text) == True):
		lib[text] = lib[text] + 1
	else:
		lib[text] = 1
	
#print(lib)
selcet_keys = []

def getMAX_keys():
	keys = list(lib.keys())   
	if(keys):                 
		v_max = lib[keys[0]]   
		#print(keys , v_max)
		selcet_keys.clear()    
		for key in lib:       
			if(lib[key] == v_max):      #
				selcet_keys.append(key)
			if(lib[key] > v_max):
				v_max = lib[key]
				selcet_keys.clear()
				selcet_keys.append(key)
	return len(keys)
	
def bubble_sort(list):
    for i in range(0,len(list)-1): 
        for j in range(0,len(list)-1-i): 
            if list[j] < list[j+1]: 
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp

#print(selcet_keys , lib[selcet_keys[0]])
while(getMAX_keys() > 0):
	if(len(selcet_keys) == 1):
		print(selcet_keys[0] *lib[selcet_keys[0]])
		#print('del ' + selcet_keys[0])
		del lib[selcet_keys[0]]
		
	if(len(selcet_keys) > 1):
		bubble_sort(selcet_keys)
		for text in selcet_keys:
			print(text *lib[text])
			#print('del ' + text)
			del lib[text]
			
		
		
		
	

	
	
	
