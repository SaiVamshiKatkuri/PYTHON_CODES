def longest_string(s):
     a=s.split(" ")
     print(a)
     max=0
  #to find the length of max letter word
     for i in a:
         l=len(i)
         if l>max:
             max=l
             max_word=i
    #logic to print the max letter words
     for i in a:
         if len(i)==max:
             print(i)
k=input("enter")

longest_string(k)