def iq_test(numbers):
    odd_count=0
    even_count=0
    num_dict={0:'First',1:'Second',2:'Third',3:'Fourth',4:'Fifth',5:'Sixth',6:'Seventh',7:'Eight',8:'Ninth',9:'Tenth'} #using dictionary to let the user know the index position which is odd or even
    
    number_list=list(map(int,numbers.split())) #making use of map method to split the string and convert it to integers.
    
    for num in number_list: #for loop for deciding whether our list of number is odd majority or even majority
        if num%2==0:
            even_count+=1 
        else:
            odd_count+=1
    
    #print(odd_count)
    #print(even_count)
    
    if odd_count < even_count:
        for num in number_list: #picking out the odd man out
            if num%2!=0:
                return "{} number is odd, while rest of the numbers are even".format(num_dict[number_list.index(num)]) #making use of the dictionary
    else:
        for num in number_list: #picking out the odd man out
            if num%2==0:
                return "{} number is even, while rest of the numbers are odd".format(num_dict[number_list.index(num)]) #making use of dictionary
      
            
            
    

