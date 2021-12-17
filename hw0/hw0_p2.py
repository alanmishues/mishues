#!/usr/bin/env python
# coding: utf-8

# 資料前處理

# In[72]:


f = open("IMDB-Movie-Data.csv")
lines = f.readlines()
print(type(lines))
for idx in lines:
 print(idx)
fn = 'IMDB-Movie-Data.csv'
movie_data = open(fn)
data = movie_data.read()
movie_data.close()
print(data)
y = []
t = []
for idx in range(len(lines)):
    print(lines[idx].split(','))
    y.append(lines[idx].split(','))
    t.append(lines[idx].split(','))


# ### Problem1
# 
# 將資料變成一個二維list

# In[3]:


print(y)


# 將年份維2016的資料取出來 (取出電影名稱跟排名)

# In[4]:


z = []
for idx in range(len(lines)):
  if y[idx][5] == '2016':
    print(y[idx])
    z.append(y[idx][1])
    z.append(y[idx][7])


# In[5]:


print(z)


# 將電影名稱跟排名放到一個dict裡面

# In[6]:


dict1 = {}
for idx in range(len(y)):
    if y[idx][5] == '2016':
        dict1[y[idx][1]] = eval(y[idx][7])
print(dict1)


# 排序後取出value的值

# In[7]:


sorted_value = sorted(dict1.values())
print(sorted_value)
new_sorted_value = sorted_value[-1:-4:-1]
print(new_sorted_value)


# 用另種方法進行排序

# In[8]:


{x:idx for x, idx in sorted(dict1.items(),key=lambda item: item[1])}


# 排序後取出key的值

# In[9]:


key = list({x:idx for x, idx in sorted(dict1.items(),key=lambda item: item[1])})


# ### Answer1

# In[10]:


print(key[-1:-4:-1])
print(new_sorted_value)
print('2016年評分第一名的電影是',key[-1],'分數是',new_sorted_value[0])
print('2016年評分第二名的電影是',key[-2],'分數是',new_sorted_value[1])
print('2016年評分第三名的電影是',key[-3],'分數是',new_sorted_value[2])


# ### Problem2 
# The actor generating the highest average revenue

# 創造一個新的list把沒有Revenue的電影資料給刪掉

# In[11]:


for idx in range(len(y)):
    if y[idx][9] == "":
        print(y[idx])


# In[12]:


new_y = []
for idx in range(len(y)):
    if y[idx][9] != "":
        new_y.append(y[idx])


# 進行actor的處理

# In[13]:


actor = []
for idx in range(len(new_y)):
    if new_y[idx][4] not in actor:
        actor.append(new_y[idx][4])


# In[14]:


print(actor)


# In[15]:


print(actor[0])
new_actor = []
new_actor1 = []
for idx in range(len(actor)):
    new_actor.append(actor[idx])
print(new_actor)


# In[16]:


for idx in range(len(new_actor)):
    if new_actor[idx].split('|') not in new_actor1:
        new_actor1.append(new_actor[idx].split('|'))


# In[17]:


print(new_actor1)


# In[18]:


for i in range(len(new_actor1)):
    for j in range(len(new_actor1[i])):
        new_actor1[i][j] = new_actor1[i][j].strip()
new_actor2 = new_actor1[1:]         
print(new_actor2)


# In[19]:


new_actor3 = []
for i in range(len(new_actor2)):
    for j in range(len(new_actor2[i])):
        if new_actor2[i][j] not in  new_actor3:
            new_actor3.append(new_actor2[i][j])
print(new_actor3)


# 目前已找出所有的actor了

# In[20]:


print(new_y)


# In[21]:


new_y = new_y[1:]


# In[22]:


for i in range(len(new_y)):
    new_y[i][4]=new_y[i][4].split('|')


# In[23]:


for i in range(len(new_y)):
    for j in range(len(new_y[i][4])):
        new_y[i][4][j]=new_y[i][4][j].strip()


# 分別把每個演員有演過的電影收入丟到然後平均計算出每個演員的平均收入

# In[24]:


revenue_average = []
revenue_actor = []
dict2 = {}
for idx in range(len(new_actor3)):
    average_revenue = []
    revenue_actor.append(new_actor3[idx])    
    for k in range(len(new_y)):
        for i in range(len(new_y[k][4])):
            if new_actor3[idx] in new_y[k][4][i]:
                average_revenue.append(eval(new_y[k][9]))
    dict2[revenue_actor[idx]] = (sum(average_revenue)/len(average_revenue))           
    print(average_revenue)
    print(len(average_revenue))
    print(new_actor3[idx],"的平均收入是",(sum(average_revenue)/len(average_revenue)))
    revenue_average.append(sum(average_revenue)/len(average_revenue))


# In[25]:


print(dict2)


# 排序後取前幾個(確認最高不只一個)

# In[26]:


key = list({x:idx for x, idx in sorted(dict2.items(),key=lambda item: item[1])})
print(key[-1:-5:-1])


# In[27]:


sorted_value2 = sorted(dict2.values())
new_sorted_value2 = sorted_value2[-1:-4:-1]
print(new_sorted_value2)


# ### Answer2

# In[28]:


print('收入最高的演員是',key[-1],'和',key[-2],'收入是',new_sorted_value2[0])


# ### Problem3
# The average rating of Emma Watson’s movies

# In[29]:


rating_of_Emma=[]
for idx in range(len(lines)):
    if 'Emma Watson' in y[idx][4]:
        print(y[idx])
        rating_of_Emma.append(eval(y[idx][7]))


# In[30]:


print(rating_of_Emma)
mean_of_Emma = sum(rating_of_Emma)/len(rating_of_Emma)
print(mean_of_Emma)


# ### Answer3

# In[31]:


print(mean_of_Emma)


# ### Problem4
# Top-3 directors who collaborate with the most actors? 

# In[32]:


for i in range(len(t)):
    t[i][4]= t[i][4].split('|')


# In[33]:


for i in range(len(t)):
    for j in range(len(t[i][4])):
        t[i][4][j] =t[i][4][j].strip()


# In[34]:


print(t)


# In[35]:


Director=set()
for i in range(len(t)):
    Director.add(t[i][3])
Director = list(Director)


# In[36]:


list_Director = []
for i in range(len(Director)):
    listXXXX = []
    listXXXX.append(Director[i])
    list_Director.append(listXXXX)


# 將導演名稱變成一個二維list 之後如果導演名稱跟原先的資料一樣，那把不再重複的演員添加到list中
# 如此一來合作的演員數量就是那個list的長度-1

# In[37]:


for i in range(len(t)):
    for j in range(len(list_Director)):
        if list_Director[j][0] == t[i][3] :
            for x in range(len(t[i][4])):
                list_Director[j].append(t[i][4][x])


# In[38]:


print(list_Director)


# In[39]:


for i in range(len(list_Director)):
    if len(list_Director[i]) >5:
        print(len(list_Director[i]))


# 算出合作前三名(數量)

# In[40]:


list_number = []
for i in range(len(list_Director)):
    list_number.append(len(list_Director[i]))
list_number=list((set(list_number)))
list_number = sorted(list_number , reverse = True)


# print出答案

# In[41]:


for i in range(len(list_Director)):
    if len(list_Director[i])  == list_number[0] :
        print('Top-1 directors who collaborate with the most actors','is',list_Director[i][0])
    if len(list_Director[i])  == list_number[1] :
        print('Top-2 directors who collaborate with the most actors','is',list_Director[i][0])
    if len(list_Director[i])  == list_number[2] :
        print('Top-3 directors who collaborate with the most actors','is',list_Director[i][0])


# ### Problem5
# Top-2 actors playing in the most genres of movies? 
# 
# 跟第四題的邏輯一樣，故不解釋

# In[42]:


print(t)


# In[43]:


Actor= []
for i in range(len(t)):
    for j in range(len(t[i][4])):
        Actor.append(t[i][4][j])
print(Actor)


# In[57]:


for i in range(len(t)):
    t[i][2] = t[i][2].split('|')


# In[58]:


for i in range(len(t)):
    for j in range(len(t[i][2])):
        t[i][2][j] =t[i][2][j].strip()


# In[59]:


list_Actor = []
for i in range(len(Actor)):
    listXXXX = []
    listXXXX.append(Actor[i])
    list_Actor.append(listXXXX)


# In[60]:


for i in range(len(t)):
    for j in range(len(list_Actor)):
        for d in range(len(t[i][4])):
            if list_Actor[j][0]== t[i][4][d]:
                for x in range(len(t[i][2])):
                    if t[i][2][x] not in list_Actor[j]:
                        list_Actor[j].append(t[i][2][x])


# In[61]:


print(t[1][2])


# In[62]:


list_Actor = list_Actor[1:]
print(list_Actor)


# In[63]:


genre_number = []
for i in range(len(list_Actor)):
    genre_number.append(len(list_Actor[i]))
genre_number=list((set(genre_number)))
genre_number = sorted(genre_number , reverse = True)
print(genre_number)


# In[64]:


Top2 = []
Top1 = []
for i in range(len(list_Actor)):
    if len(list_Actor[i])  == genre_number[0] :
        Top1.append(list_Actor[i][0])
       # print('Top-1 actors playing in the most genres of movies','is',list_Actor[i][0])
    if len(list_Actor[i])  == genre_number[1] :
        Top2.append(list_Actor[i][0])
       # print('Top-2 actors playing in the most genres of movies','is',list_Actor[i][0])
Top1 = list(set(Top1))
Top2 = list(set(Top2))
for i in range(len(Top1)):
    print('Top-1 actors playing in the most genres of movies','is',Top1[i])
for i in range(len(Top2)):
    print('Top-2 actors playing in the most genres of movies','is',Top2[i])


# ### Problem6
# Top-1 actors whose movies lead to the largest maximum gap of years? 
# 
# 跟第五題邏輯一樣，但時間不夠了先不寫解釋

# In[73]:


new_actor = []
new_actor1 = []
for i in range(len(Actor)):
    list1 = []
    list1.append(Actor[i])
    new_actor.append(list1)
    new_actor1.append(list1)
new_actor = new_actor[1:]
new_actor1 = new_actor1[1:]
print(new_actor)


# In[74]:


yy = y[1:]
for i in range(len(yy)):
    yy[i][5] = int(yy[i][5])


# In[75]:


print(yy)


# In[76]:


for i in range(len(yy)):
    yy[i][4] = yy[i][4].split('|')


# In[77]:


for i in range(len(yy)):
    for j in range(len(yy[i][4])):
        yy[i][4][j] = yy[i][4][j].strip()


# In[78]:


for i in range(len(yy)):
    for j in range(len(yy[i][4])):
        for k in range(len(new_actor)):
            if new_actor[k][0] == yy[i][4][j]:
                new_actor[k].append(yy[i][5])


# In[79]:


print(new_actor)


# In[80]:


for k in range(len(new_actor)):
    new_actor[k] = new_actor[k][1:]


# In[81]:


gapyear = []
for k in range(len(new_actor)):
    print(max(new_actor[k])-min(new_actor[k]))
    gapyear.append(max(new_actor[k])-min(new_actor[k]))


# In[82]:


gapyear = sorted(list(set(gapyear)),reverse=True)
print(gapyear)


# In[83]:


actorrrr = []
for k in range(len(new_actor)):
    if (max(new_actor[k])-min(new_actor[k])) == gapyear[0]:
        actorrrr.append(new_actor1[k][0])
actorrrr = list(set(actorrrr))
for k in range(len(actorrrr)):
     print('Top-1 actors whose movies lead to the largest maximum gap of years','is',actorrrr[k])


# ### Problem7
# Find all actors who collaborate with Johnny Depp in direct and indirect ways 

# In[84]:


for i in range(len(yy)):
    for k in range(len(yy[i][4])):
        if yy[i][4][k] == 'Johnny Depp':
            print(yy[i])


# 先把跟Johnny_Depp有直接相關的人找出來

# In[104]:


Johnny_Depp = []
for i in range(len(yy)):
    for k in range(len(yy[i][4])):
        if 'Johnny Depp' in yy[i][4]:
            if yy[i][4][k] not in Johnny_Depp:
                Johnny_Depp.append(yy[i][4][k])


# In[105]:


print(Johnny_Depp)


# In[127]:


Johnny_Depp1 = []
while True:  #用WHILE迴圈
    if len(Johnny_Depp1) == len(Johnny_Depp1): #如果這兩個長度一樣代表沒有新的加入所以可以停止
        break
    for i in range(len(Johnny_Depp)):
        for k in range(len(yy)):
            for l in range(len(yy[i][4])):
                if Johnny_Depp[i] in yy[i][4]:   #用WHILE迴圈不斷找跟Johnny_Depp有間接關係的人
                    if yy[i][4][k] not in Johnny_Depp:  #如果還沒被加進去LIST，就把它加進去
                        Johnny_Depp.append(yy[i][4][k])
                        Johnny_Depp1 = list(len(Johnny_Depp))  #用一個新的LIST確保沒有重複   


# In[126]:


print(len(Johnny_Depp1))
print(len(Johnny_Depp))


# 總共有1575個
