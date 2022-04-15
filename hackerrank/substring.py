#first approach
def count_substring(string,sub_string):
    for i in range(len(string)-len(sub_string)+1):#so that we can avoid going at end.
        if string[i:i+len(sub_string)]==sub_string:
            count=count+1
        print(count)
        #match word by word
        return
#2nd approach
#use regex(re)
# import re
# a = raw_input()
# b = raw_input()
# match = re.findall('(?='+b+')',a)
# print len(match)
        

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)