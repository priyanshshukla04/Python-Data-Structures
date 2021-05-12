dictionary = {"January": 2200, "February": 2350, "March": 2600, "April": 2130, "May": 2190}
lst_months = []
lst_expense = []
for k, v in dictionary.items():
    lst_months.append(k)
    lst_expense.append(v)

# 1
print(abs(dictionary["February"] - dictionary["January"]))

# 2
print(abs(dictionary["January"] + dictionary["February"] + dictionary["March"]))

# 3
print(2000 in lst_expense)

# 4
dictionary["June"] = 1980
lst_months.append("June")
lst_expense.append(1980)

# 5
dictionary["April"] -= 200
index_april = lst_months.index("April")
lst_expense[index_april] -= 200

print(lst_expense)
print(lst_months)
print(dictionary)
