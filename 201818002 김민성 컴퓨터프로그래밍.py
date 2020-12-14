#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1번
print(5/3)
#5/3의 값을 출력하기위해 print라는 용어를 사용한다.


# In[3]:


#2번
#에어컨값 월 48,584 무이자 36개월이므로 총금액은 월금액과 개월수를 곱해줘야한다.
print(48584*36)


# In[5]:


#3번
#결과 의 값은 = abcd 가 나올 것이다.
#string은 문자열인데 변경할 수가 없기 때문에
string = 'abcd'
print(string)
#값이 그대로 나온다.


# In[11]:


#4번
data = " 삼성전자 "
example = data.strip()
print(example)
#strip을 사용하여 공백을 제거 할 수 있다.


# In[15]:


#5번
data = "039490  "
data = data.rstrip()
print(data)
#rstrip방법을 이용하면 오른쪽 공백이 포함된 문자열이 나온다.


# In[21]:


#6번
nums = [1, 2, 3, 4, 5]
평균 = sum(nums) / len(nums)
print(평균)
#sum은 모든 원소의 합을 구하는 것이고 len는 행에대한 열의 갯수 이므로 나눠주면 평균이다.


# In[23]:


#7번
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
#sort는 크기 순으로 정렬해주는 기능이 있으므로 오름차순으로 정렬된다. 


# In[32]:


#8번
import numpy as np
np.arange(2,100,2)
#괄호안의 첫번째가 시작하는수, 두번째가 마지막수 이며 세번째 수가 증가량이므로 이렇게 표현할수 있다.


# In[ ]:


#9번
#저 코드 안에 누가바라는 키 밸류 값이 정해져 있지 않아서 오류가 난 것이다.


# In[45]:


#10번
data = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(data, close_price))
print(close_table)
#list를 set로 바꿀때와 비슷한 방법으로 dict로 바꿀때 앞에 dict를 넣어주고 zip으로 키와 밸류 값을 합쳐준다


# In[ ]:


#11번
정답은 3과 5과 출력된다
#If True 이므로 true가 출력됨. 아래 False 이므로 1,2는 출력이되지않고 False 아래에 else이므로 3 출력되고,
#그 아래 else는 true에 대한 else 이므로 4도 출력되지않고 True 맨아래에 연결되잇는 프린트 안의 5가 출력됨


# In[46]:


#12번
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
a = input("좋아하는 과일은?")
if a in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")
#두 가지로 출력을 해야 하므로 if else 조건문을 이용해서 만들어주면 값을 구할 수 있다.
#그리고 밸류 값을 구해야 하므로 .values를 붙여줘야 key의 값을 제외한 value값이 출력된다.


# In[49]:


#13번
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")
#변동폭은 최고가에서 최저가를 뺀 값이고 변동폭에 시가를 더한값이 최고가와 비교되는 대상이 될 수 있다.


# In[54]:


#14번
for a in range(4):
    print("-------")
#7개의 하이푼을 4가지 연속 되게 출력해야 하므로 정렬을 사용해야한다.


# In[55]:


#15번
a = ["가", "나", "다", "라"]
for i in a[: :-1]:
    print(i)
#조건문 리스트 안의 앞에 공백은 줄바꾸는 띄우는것을 나타내고 뒤에는 열의 순서인 -1이므로 뒤에 수부터 출력이 된다


# In[56]:


#16번
a = ['spiderman.s', 'batman.b', 'ironman.i', 'suicidesquad.s']
for i in a:
    split = i.split(".")
    if (split[1] == "b") or (split[1] == "i"):
        print(i)
#b 혹은 i 두 개 의 변수를 내기위해서 or을 사용하고 split을 사용하면 리스트로 변환된다.


# In[59]:


#17번
result = 1
for i in range(1,11):
    result *= i
print(result)
#range방법을 이용해서 1부터 10까지의 수를 표현한후 곱셈을 넣어서 1부터10까지의 수를 모두 곱하게 함.


# In[60]:


#18번
low_prices = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []
for i in range(5):
    diff = high_prices[i] - low_prices[i]
    volatility.append(diff)
print(volatility)
#5일간의 변동폭이므로 range값을 5로 정하고 큰값에서 작은값을 빼주는 변동폭을 구해주면 된다.
#append는 뒤에 추가되는 기능이있기 때문이다.


# In[61]:


#19번
apart = [ [101, 102], [201, 202], [301, 302] ]
for a in apart:
    for b in a:
        print(b, "호")
print("-----")
#순서대로 뒤에 호를 붙여 마지막에 -----만 붙여주면 세로로 나온다.


# In[64]:


#20번
ohlc = [["open", "high", "low", "close"],
       [100, 110, 70, 100],
       [200, 210, 180, 190],
       [300, 310, 300, 310]]
money = 0
for a in ohlc[1:]:
    money += (a[3] - a[0])
#결국 남은 수익금은 0원이고 4번째 원소에서 1번째 원소를 빼서 더한 값을 나타내었다.

#21번
def message1():
    print("A")
    
def message2():
    print("B")
    
def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()
    
message3()

#맨마지막에 있는 메세지3 때문에 3번째 for문이 있는 곳부터 출력 되기 시작하는데 range(3) 이므로 총 세번 순환한다
# 처음에 메세지2 이므로 B를 출력하고 그다음 프린트 C 로 C를 출력하고 이것을 3번 반복후에
#마지막에 메세지1의 A를 출력하므로 B C B C B C A가 된다.
# In[73]:


#22번
def print_max(a, b, c) :
    max_val = 0
    if a > max_val :
        max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c
    print(max_val)
    
#if문 사용하여 수를 비교하기위해서 0으로 놓고 시작한다


# In[ ]:


#23번
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)
    
my_print(b=100, a=200)
#(1번,2번) 1번과 2번부분이 프린트 되는데 왼쪽: 오른쪽: 이렇게 잇으므로 a와 b가 왼쪽 오른쪽 옆으로 출력되서 나온다.


# In[ ]:


#24번
#처음에 아래에있는 함수2가 출력되고 함수2로 가서 12가 되고 그다음 함수1로 가서 +2 14가 되서 그다음
#함수0으로 호출되어 28이되고 리턴되어 리턴된 값이 나온다.


# In[70]:


#25번
import numpy as np
np.arange(0, 5, 0.1)
#arange에서 (시작수, 마지막수(포함안됌), 상승하는량) 이므로 채워주면 된다.


# In[ ]:


#26번


# In[75]:


#27번
종목 = []

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)

for i in 종목:
    print(i.code, i.per)


# In[ ]:


#28번


# In[ ]:


#29번
#super()를 이용해서 바로 부모클래스를 생성할 수 있다.


# In[ ]:


#30번

