# from (Book) OpenCV-Python으로 배우는 영상 처리 및 응용
import header_area as mod
from header_area import write

mod.say()                                       # 함수 호출 – 인수없음, 반환값 없음
ret = mod.calc_area(type=1, a=5, b=5)			# 함수 호출 – 튜플 반환
write(ret[0], ret[1])


