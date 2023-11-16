
# 두 수의 합을 반환하는 함수
def add_two_numbers(a, b):
    return a + b

# 숫자가 짝수인지 확인하는 함수
def is_even(number):
    return number % 2 == 0

# 테스트
num = 6
if is_even(num):
    print(f"{num}은(는) 짝수입니다.")
else:
    print(f"{num}은(는) 홀수입니다.")
