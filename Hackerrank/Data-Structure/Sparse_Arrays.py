
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries

def matchingStrings(stringList, queries):
    result = [None] * len(queries)
    
    for i in range(len(queries)):
        result[i] = stringList.count(queries[i])

    return result

