import time
n = int(input("자연수 >"))
start_time = time.time()
for i in range(2,n):
    if n % i == 0:
        print("소수가 아닙니다.")
        break
else:
    print("소수입니다.")
end_time = time.time()
print(f"실행 시간: {end_time - start_time}초")