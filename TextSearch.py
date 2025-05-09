'''
    Text  search  with  Binary search algorithm
'''

#Algorithm,  BS -> Binary  search
def BS(words,word):
    '''
        finding word index  in a list of strings
        inefficient approach, different style  and  works with unsorted list,  O(N^2)
        Args:
            words : list[string]
            word  : word  to find  =  str

        Returns  word  index if  found  else -1
    '''
    l = 0#first word
    r = len(words)-1 #last word
    while  l <= r:
        mid = (l+r)//2  #get middle word index
        if  mid == words.index(word):#compare middle and  word  index  from  list
            return mid#  return if   mid  is  index
        elif words.index(words[mid])<words.index(word): #compare word index and  middle word index from  list
            l = mid+1 # if word  index is greater then, first word = word after  middle word
        else:
            r = mid-1# last word = string  before  middle word
    return -1


#approach 2
def bs2(words,word):
    '''
        efficient approach
        O(log N)
        for sorted  list

    '''
    words  =  sorted(words)# sort first so  list becomes  -> ['book','girl','groceries','man']
    l = 0
    r = len(words)-1
    while  l <= r:
        mid = (l+r)//2
        if  words[mid] == word:
            return mid
        elif words[mid] < word:
            l = mid+1
        else:
            r = mid-1
    return -1



if __name__ == '__main__':
    words = ['book','man','groceries','girl']# list demo
    word1=  input('Enter for 1 : ')# word  to   search for approach 1
    word2 = input('Enter for 2 :')#word  to   search for approach 2

    result =  BS(words,word1)
    if  result != -1:
        print(f'[Approach1] Found at  index  {result}')
    else:
        print('word not  in  list')

    result =  bs2(words,word2)
    if  result != -1:
        print(f'[Approach2] : Found at  index  {result}')
    else:
        print('word not  in  list')
