list1 = [123, 345]
print(list1)

list2 = [['a1','a2'],['b1','b2','b3']]

print('\n--------Tạo list với n phần tử--------\n')
a = [i for i in range(30)] #tao list tu 0 -> 29, tang i++ tu 0
print(a) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

b = [[n*1, n*2] for n in range(1,3)] #tạo list với n0 = 1; n -> 2 (< 3)
print(b) #[[1, 2], [2, 4]]

list3 = list([1,2,3])
print(list3) #[1, 2, 3]

print('\n--------Tạo list với từng kí tự của chuỗi--------\n')
list4 = list('ThangKoi')
print(list4) #['T', 'h', 'a', 'n', 'g', 'K', 'o', 'i']

print('\n--------Nhân list lên--------\n')
list5 = ['one','two']
list5 *= 2
print(list5) #['one', 'two', 'one', 'two']

print('\n--------List 2 chiều--------\n')
list6 = [1,2,'3','4',[5,6]]
print(list6[4][1]) #6
print(list6[-1]) #[5, 6] #-1 để lấy thằng cuối
print(list6[0:4]) #[2, '3', '4'] = list[:4]
print(list6[3:]) #lay tu vi tri 4 di #['4', [5, 6]]
print(list6[::-1]) #[[5, 6], '4', '3', 2, 1]

print(list6.index('4')) #3 #tìm vị trí phần tử

print('\n--------Dùng hàm .copy() để gán 2 biến k cùng trỏ 1 --------\n')

list7_1 = [1,2,3,4,5,31,1]
list7_2 = list7_1.clear()
print(list7_1) #[]
print(list7_2) #None

print('\n--------Hàm thêm phần  vào list --------\n')
list8 = [1,2,3]
list8.append([4,[5,6]])
print(list8) #[1, 2, 3, [4, [5, 6]]]

list8.extend([7,8])
print(list8) #[1, 2, 3, [4, [5, 6]], 7, 8]
#hàm append extend k gán được

print('\n--------Hàm thêm phần tử vào 1 vị trí trong list --------\n')
list9 = [1,2,3]
list9.insert(2,4) #2 là vị trí; 4 là giá trị
print(list9)

print('\n--------Hàm lấy ra rồi bỏ phần tử trong list --------\n')
list10= [6,7,8]
print(list10.pop(1)) #7
print(list10) #[6, 8]

print('\n--------Hàm reverse + sắp xếp phần tử trong list --------\n')
list11 = [2,3,4,1]
list11.reverse()
print(list11) #[1, 4, 3, 2]

list11.sort()
print(list11) #[1, 2, 3, 4]

list11.sort(reverse = True)
print(list11) #[4, 3, 2, 1]