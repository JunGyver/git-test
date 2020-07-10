def get_even_number(num):
    if num % 2 == 0:
        return f"{num}은 짝수입니다."
    return f"{num}은 홀수입니다."

print(get_even_number(3453))
