# function1.py
#함수정의
def times(a,b):
    return a+b, a*b

#함수호출
result = times(3,4)
print(result)    

#함수정의
def setValue(newVal):
    x = newVal
    print("함수내부:",x)

#호출
result = setValue(5)
printf(result)    

#교집함 리턴
def intersect(prelist,postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result 

#호출
#             