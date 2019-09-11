import string
# # học chuỗi
# print('\nChuỗi nhiều dòng:')
# str1 = '''Hello
# I am Thang
# Nice to meet you
# Thank you'''
# print(str1)
#
# print('\nChuỗi trần:')
# print(r'\neu mot ngay nao do') #loai \n bang cach them 'r'
#
# print('\nIn nhiều chuỗi:')
# strA = 'Thang Koi'
# strB = 'oi'
# strC = strA*5
# strD = strB in strA
# print(strC)
# print(strD) #check chuỗi B trong A hay k
# print(strA[3])
# print(strA[-2]) #in đi ngược từ bên phải *only Python bắt đầu từ -1
# print(strA[len(strA) - 1]) #đội dài chcuốiuỗi la len(), syntax này lấy ra phần tử
# print(strA[2:7]) #7 là số kí tự tính từ cái đầu

str1 = 'I am %s %s'%('Thang', 'Koi')
print(str1)
s = '%s %s'
print(str1 + s %(' Hi', 'nek'))

print('%s' %([1,2,3])) #list nhieu ky tu

a = 12.412421
print('%.2f %.3f' %(a,a) )

addStr = 'trainee'
print(f'Thang is {addStr}')

print('\n----------fString--------\n')
name = 'Kim Thoa'
phone = 798277543
info = 'tretrau'
print(f'Ten: {name}\nSDT: {phone}\nInfo: {info}')
print(f'Ten: {{name}}\nSDT: {phone}\nInfo: {info}')

print('\n----------formatString--------\n')

print('stt2: {1}, stt1: {0}, stt3: {2}'.format('one','two','three','four'))
print('1: {one}, 2: {two}'.format(one=1, two = 22))
print('I am{:*<5}Koi'.format('Thang'))

print('\n----------Capitalize--------\n')
cap1 = 'i like playing sports'
cap2 = cap1.capitalize()
cap3 = cap1.upper()
cap4 = cap1.title()
print(cap2 + '\n' + cap3 + '\n' + cap4)

#lower()
#swapcase() chữ viết thường -> hoa và ngược lại

re1 = 'Hom nay troi that dep'
re2 = re1.replace('dep','xau') #replace hàm
print(re2)
print(re1.replace('a','1',2)) #replace 2 kí tự
print('11122223311'.strip('1')) #rstrip & lstrip

print('\n----------Split theo ký tự-----------\n')
spl1 = '1 22 333 4444'
spl2 = spl1.split(' ',2) #2 khoang trang #rsplit & lsplit
print(spl2)
print(spl2[2])

print('\n----------Split theo thành ký tự -----------\n')
part1 = 'i will be superman'
part2 = part1.partition('1') #rpartition & #lpartition
print(part2)

print('\n---------- Đếm ký tự -----------\n')
count1 = 'abcdefffaacvbs'
count2 = count1.count('a',1,30) #1 là điểm bắt đầu #10 là kết thúc
print(count2)

print('\n---------- Kiểm tra suất phải bằng kí tư -----------\n')
start1 = '11222233334444'
start2 = start1.startswith('2',2,9) #endswith
print(start2)

print(start1.find('3')) #return -1 if doesnt find
#hàm  .islower()
#hàm  .isupper()
#hàm  .istitle()
#hàm  .isspace() kiểm tra có phải khoảng trắng hết k
#hàm .isdigit() kiểm tra có phải chuỗi số


