st = int(input("Vnesi število: "))
najmanjse_stevilo = st
while True:
    if st < najmanjse_stevilo and st > 0 :
        najmanjse_stevilo = st
    st = int(input("Vnesi število: "))
    if st==0:
        break
print(f"Najmanjše pozitivno število je: {najmanjse_stevilo}")
