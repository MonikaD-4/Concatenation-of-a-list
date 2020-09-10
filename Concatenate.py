list1=["Wel", "t", "Py", "wor"]
list2=["come", "o", "thon", "ld"]
lst=[]
s=''
for i in range(len(list1)):
      s=list1[i]+list2[i]
      lst.append(s)
      s=''
print(lst)
