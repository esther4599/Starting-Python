#slice에서 조건주기
list1 = list(range(20))
print(list1)

print(list1[5:15]) #[5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# 아래의 2, 3 = step 이다. (for (a = 5; a < 15; a+=step))
print(list1[5:15:2]) #[5, 7, 9, 11, 13]

print(list1[5:15:3]) #[5, 8, 11, 14]

#step은 음수일 수 있다.
print(list1[5:15:-1]) #[] => 5에서 -1를 반복하여 더해서 15가 될 수 없음
# 아래 예시 주의하기
print(list1[15-1:5-1:-1]) #[14, 13, 12, 11, 10, 9, 8, 7, 6, 5]
print(list1[15:5:-1]) #[15, 14, 13, 12, 11, 10, 9, 8, 7, 6]

#전체 영역에서 step 사용. 두 경우 수가 같지 않음
print(list1[::3]) #[0, 3, 6, 9, 12, 15, 18]
print(list1[::-3]) #[19, 16, 13, 10, 7, 4, 1]
