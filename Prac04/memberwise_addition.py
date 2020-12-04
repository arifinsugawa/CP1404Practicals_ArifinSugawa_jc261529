def add_memberwise(list1,list2):
    new_list = []
    list1_len = len(list1) 
    list2_len = len(list2) 
    
    for x in range(max(list1_len,list2_len)):
        num1 = 0
        num2 = 0
        if x < list1_len:
            num1 = list1[x]

        if x < list2_len:
            num2 = list2[x]

        new_list.append(num1+num2)
    return new_list

def main():
    list1 = [1,2,3]
    list2 = [1,2,3,4]
    new_list = add_memberwise(list1,list2)
    print(new_list) 

main()
