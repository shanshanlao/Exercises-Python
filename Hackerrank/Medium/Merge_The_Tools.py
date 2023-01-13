from collections import OrderedDict

def merge_the_tools(string, k):
    n = len(string)
    for i in range(0,n,k):
        key = string[i:i+k]
        print("".join(list(OrderedDict.fromkeys(key))))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
