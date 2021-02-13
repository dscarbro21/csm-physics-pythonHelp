print("print function basics:")
print("Each statement prints on a new line")

print("unless I tell it not to with the end= ", end="")
print("parameter")
print("- Because by default end is set to a newline")

print()
print("an empty print still uses the default end parameter")
print()

print("I can end with spaces", end="   ")
print("or dashes", end="---")
print("or anything I need to", end="!!!!!")
print()
print()

print("I can print two things", "together with a comma")
print("- and if they are strings I can " "omit the comma")
print("- or I can use " + "the + operator")
print("-- but not with variables! we'll see that later")
print()

print("If I want something specific between inputs, I can do that:")
print("using the", "sep", "parameter", sep="--")
print("But I have to use commas" " to do so", sep="dskjfas;dk", end="\n\n")

print("As long as I use quotes for strings, I can use an apostrophe ' ")
print('but if I use single quotes, I cannot, but I can use "quotes"')
print("- we'll see how to get around this later")