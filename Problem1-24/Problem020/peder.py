from langint import LangInteger

fac = LangInteger(1)
for i in range(2, 101):
    fac = fac.multiply(LangInteger(i))

print(fac.sum_digits())
