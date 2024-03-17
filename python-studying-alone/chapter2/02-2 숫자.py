# ----------------- 숫자의 종류

# - 그냥 숫자를 입력하면 됨.
print(273) # 정수 - integer
print(2019.08) # 실수 (부동소수점) - float

print(type(273))
print(type(2019.08))

# 출력물
# 273
# 2019.08
# <class 'int'>
# <class 'float'>

# ----------------- 숫자 연산자

## 1. 사칙연산자 + - * /
##      - 정수와 실수를 완전히 구분하는 자바와 달리, 정수와 정수의 나숫셈이여도 실수를 반환한다.
## 2. 정수 연산자 // (Java에서의 / 구나)
## 3. 나눗셈 연산자 %
## 4. 제곱 연산자
##      - 자바에서는 Math 클래스를 불러와서 pow였나 sqrt 메소드를 써줬어야 했는데. 더 간단하구나.

print("5 + 7 =", 5 + 7)
print("5 - 7 =", 5 - 7)
print("5 * 7 =", 5 * 7)
print("5 / 7 =", 5 / 7)
print("7 // 5 =", 7 // 5)
print("7 % 5 =", 7 % 5)
print("7 ** 3 =", 7 ** 3)

# 출력물
# 5 + 7 = 12
# 5 - 7 = -2
# 5 * 7 = 35
# 5 / 7 = 0.7142857142857143
# 7 // 5 = 1
# 7 % 5 = 2
# 7 ** 3 = 343

# ----------------- 연산자의 우선순위
# 1. 괄호가 없을 때는, 곱셈과 나눗셈이 덧셈과 뺄셈보다 우선
# 2. 괄호가 있을 때는, 괄호부터!

# ----------------- TypeError 예외
# 서로 다른 자료를 연산하면 TypeError가 발생한다.

string = "문자열"
number = 273

# `string + number` 을 실행했을 떄의 오류
# Traceback (most recent call last):
#   File "C:\IntelliJ\python-studying-alone\python-studying-alone\chapter2\02-2 숫자.py", line 52, in <module>
#     string + number
# TypeError: can only concatenate str (not "int") to str

# 자바에서는 숫자 -> 문자로 알아서 형변환이 되었었는데 여기선 또 다르구나!





