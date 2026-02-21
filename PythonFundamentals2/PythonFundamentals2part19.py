# Count the number of vowels in the word artificial
word_1="artificial"
count=0
for ch in word_1:
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        count+=1
print("Ans = ",count)