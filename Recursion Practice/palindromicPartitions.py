# prints all possible palindromic partitions of a word

def palindromicPartitions(s):
    if(len(s) == 1):
        return s 
    
    if(s != s[::-1]):
        return palindromicPartitions(s[:len(s) - 1])
    else:
        print(s)
        return palindromicPartitions(s[1:])

print(palindromicPartitions("nitin"))
