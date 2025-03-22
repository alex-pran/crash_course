first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}"
print(message)

#format() method
full_name = "{} {}".format(first_name.upper(), last_name.upper())
print(full_name)

print("Python")

# \t - whitespace(like TAB button)
print("\tPython")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = 'python '
print(favorite_language)

print(favorite_language.rstrip())

universe_age = 14_000_000
print(universe_age)