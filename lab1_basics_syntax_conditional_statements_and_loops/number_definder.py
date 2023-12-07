number = float(input())
out = ""
if number == 0:
    out = "zero"
elif number > 0:
    out = "positive"
else:
    out = "negative"
if 0 < abs(number) < 1:
    print(f"small {out}")
elif abs(number) > 1000000:
    print(f"large {out}")
else:
    print(out)