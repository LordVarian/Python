def div42by(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print("Can't divide by zero")

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))