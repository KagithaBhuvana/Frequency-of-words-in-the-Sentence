input_list=input().split()
word_count_dict={}
for i in sorted(input_list):
    key=i 
    count=input_list.count(i)
    word_count_dict[key]=count 
for key,value in word_count_dict.items():
    strr="{}: {}".format(key,value)
    print(strr)
