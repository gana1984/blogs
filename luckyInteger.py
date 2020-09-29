"""
Created on Tue Sep 29 10:55:38 2020

@author: natarajang
"""

def luckyInteger(arr):
    '''
    Parameters
    ----------
        arr : list
        A list of positive integers.
    '''
    #Creating an empty dictionary to hold the frequency counts
    freq_count = {}
    #Looping over the array to build dictionary
    for num in arr:
        freq_count[num] = 1 + freq_count.get(num,0)
    #Return largest lucky number looping
    #over the array and looking up from the dictionary
    return max([num for num in arr if freq_count[num] == num],default = -1)

    #Alternate solution. You may uncomment
#    for num in arr:
#        #Initially the dictionary is empty and does not 
#        #have any keys. Trying to access a non-existent 
#        #key will throw an error. So we will check if 
#        #the key exists. If it exists we increment
#        #the value by 1.
#        if num in freq_count:
#            freq_count[num] += 1
#        #If the key does not already exist, we will create 
#        #the key and initialize the value as 1.
#        else:
#            freq_count[num] = 1
#    #The list that will hold all lucky numbers
#    result = []
#    #Looping through the dictionary we made before
#    for key, value in freq_count.items():
#        #Bingo! Lucky number.
#        #Add the element to our list of results.
#        if key == value:
#            result.append(key)
#    return max(result,default = -1)


#Driver Code
if __name__ == "__main__":
    arr = [2,2,3,3,3,4,5,6,8]
    arr1 = [2,3,3,3,3,4,5,6]
    arr2 = [1,5,4,3,4,4,5,4]
    print("For original array:",luckyInteger(arr))
    print("For arr1:",luckyInteger(arr1))
    print("For arr2:",luckyInteger(arr2))
