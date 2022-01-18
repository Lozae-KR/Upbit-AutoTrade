import pyupbit

access = "1Ka5DkKNO4J3DrAV2F82q0GxqRYzG2ax50ZTl4Qn"          # 엑세스코드
secret = "AiMr67LEj37G1xvzRzpWajgvxLW0yZAZ8XXCuuoj"          # 시크릿코드
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회