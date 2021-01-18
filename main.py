#wordorder
#@codingwithec

n = int(input())#how many word will be entered

count = {}#dic to save word occurances
word = []#list to hold words

for i in range(n):
    w = input()#enter the words 
    word.append(w)#adding words to the list
    if w in count:#if entered word is already in dic
        count[w] += 1#add 1 to the number
    else:
        count[w] = 1#else just add the word and its occurance
        
        
print(len(count))#printing the len of dic wich has distinct words

#printing each occurance
print(' '.join([str(count[word]) for word in count]))
