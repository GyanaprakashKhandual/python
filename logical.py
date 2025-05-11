# Truth table for OR and AND
print("A  B  A OR B  A AND B")
print("-----------------------")
for A in [0, 1]:
    for B in [0, 1]:
        print(f"{A}  {B}     {A or B}       {A and B}")


print(not(True));
print(not(False));