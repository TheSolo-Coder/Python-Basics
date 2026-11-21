# Variables

## Objective

Learn how to create variables, store values, and use them in Python.

## Concepts

- Variables store values using names.
- Use `=` to assign values.
- Strings store text, while integers store whole numbers.
- Use `print()` to display variable values.
- Use commas in `print()` to display multiple values with spaces.
- Use `+` to join strings together.
- Use `str()` to convert a value into a string.
- Use `type()` to check a value's data type.

## Code

```python
language = "Python"
print(language)

year = 2026
print(year)

name = "Ali"
goal = "AI Engineer"

print("My name is", name, "and I want to become an", goal)

first = "AI"
second = "Engineer"
print(first + " " + second)

age = 15
print("My age is", age)

year_text = str(year)
print("My learning year is " + year_text)

print(type(year))
print(type(year_text))
```

## Output

```text
Python
2026
My name is Ali and I want to become an AI Engineer
AI Engineer
My age is 15
My learning year is 2026
<class 'int'>
<class 'str'>
```

## What I Learned

- Create and use variables.
- Store text and numbers.
- Print variable values.
- Join strings using `+`.
- Display multiple values using commas.
- Convert integers into strings using `str()`.
- Check data types using `type()`.
