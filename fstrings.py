# Used for string formatting

letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harshada"

# print(letter.format(name, country))
print(letter.format(country, name))
# print(letter.format)

print(f"Hey my name is {name} and I am from {country}")

txt = "For only {price: .2f} dollars!"
print(txt.format(price = 49.099))

print(f"Hey my name is {{name}} and I am from {{India}}")