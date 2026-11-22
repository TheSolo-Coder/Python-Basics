# User Input

## Objective

Learn how to receive information from users and convert input into different data types.

## Concepts

- `input()` receives information from the user.
- `input()` returns a string.
- `int()` converts input into a whole number.
- `float()` converts input into a decimal number.
- `type()` checks the data type.
- f-strings display variables inside text.

## Code

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
price = float(input("Enter product price: "))

print(f"Hello {name}, you are {age} years old.")
print(f"The product price is {price}.")

print(type(age))
print(type(price))
```

## What I Learned

- Receive user input with `input()`.
- Convert input into integers and floats.
- Display variables using f-strings.
- Check data types using `type()`.
