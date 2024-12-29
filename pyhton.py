# arr_org = ['a', 'b', 'b', 'a', 'b', 'a', 'a', 'b']
# arr_new = []
# for i in range(0,len(arr_org)):
#     if i>0 and arr_org[i]=='a':
#         x = len(arr_new)
#         if arr_new[x-1]=='b':
#             arr_new.remove(arr_new[x-1])
#         else:
#             arr_new.append(arr_org[i])
#     else:
#         arr_new.append(arr_org[i])
# print(arr_new)

# s1 = 'india'
# s2 = 'super'
# s3=''
# for i in range(0, max(len(s1), len(s2))):
#     s3= s3+s1[i]+s2[i]
# print(s3)

# s='india'
# srev = s[::-1]
# print(srev)


def fun(s1,s2):
    list1 = list(s1)
    list2 = list(s2)

    for t in range(len(list1)):
        for q in range(len(list2)):
            if list1[t] == list2[q]:
                list1.remove(list1[t])
                list2.remove(list2[q])
    if len(list1) == 0 and len(list2) == 0:
        print("Ana")
    else:
        print("noo")

q1 = input()
q2 = input()

fun(q1, q2)