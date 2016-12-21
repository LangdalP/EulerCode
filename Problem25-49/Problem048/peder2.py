from langint import LangInteger

# This gives correct answer but takes ~5 minutes.
# Need to speed up LangInteger

sum = LangInteger(0)
for i in range(1, 1001):
    ili = LangInteger(i)
    sum = sum.add(ili.to_power_of(i))
    if i % 10 == 0:
        print("Progress: {}".format(i))

print(str(sum)[-10:])
