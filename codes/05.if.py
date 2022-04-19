# from (Book) OpenCV-Python으로 배우는 영상 처리 및 응용
year = 2020

if (year%4==0) and (year % 100 != 0):
    print(year, '는 윤년입니다.')
elif year%400==0:
    print(year , '는 윤년입니다.')
else:
    print(year , '는 윤년이 아닙니다.')