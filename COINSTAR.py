one_yen = int(input())
five_yen = int(input())
ten_yen = int(input())
fifty_yen = int(input())
hundred_yen = int(input())
five_hundred_yen = int(input())

one_yen_amt = one_yen * 1
five_yen_amt = five_yen * 5
ten_yen_amt = ten_yen * 10
fifty_yen_amt = fifty_yen * 50
hundred_yen_amt = hundred_yen * 100
five_hundred_yen_amt = five_hundred_yen * 500

total_yen = (one_yen_amt + five_yen_amt + ten_yen_amt + fifty_yen_amt + hundred_yen_amt + five_hundred_yen_amt)

print(f'Total Yen: {total_yen}')
