#input : i am software engineer and i always like to learn new things
#output: i ma erawtfos reenigne dna i syawla ekil ot nrael wen sgniht

stringToConvert='i am software engineer and i always like to learn new things'
outSentence=''
temp=''

for char in stringToConvert:
    if char!=' ':
        temp=temp+char  #This logic work as split by space, it will take each word till space
    else:
        for ch in range(len(temp)-1, -1,-1):
            outSentence=outSentence+temp[ch]
        outSentence=outSentence+' '
        temp=''
print(outSentence)