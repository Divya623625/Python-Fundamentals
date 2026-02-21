# Count the number of i's in the word artificial intelligence."
word="artificial intelligence"
#count the number of i's => 5
count=0
for ch in word:
    if(ch=='i'):
      count+=1

print("count of i=", count)
