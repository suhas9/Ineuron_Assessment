def freq(str):
 
    # break the string into list of words 
    str = str.split()         
    str2 = []
 
    # loop till string values present in list str
    for i in str:             
 
        # checking for the duplicacy
        if i not in str2:
 
            # insert value in str2
            str2.append(i) 
             
    for i in range(0, len(str2)):
 
        # count the frequency of each word(present 
        # in str2) in str and print
        print('Frequency of', str2[i], 'is :', str.count(str2[i]),'And Length is:',len(str2[i]))
 
def main():
    str ='write write write all the number from from from 1 to 100 '

    freq(str)                    
 
if __name__=="__main__":
    main()   