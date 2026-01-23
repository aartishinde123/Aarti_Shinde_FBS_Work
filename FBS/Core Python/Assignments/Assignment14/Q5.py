# Write a Python program to find the longest common prefix of all strings. Use the Python set.

strings = ["flower", "flow", "flight"]

# if list is empty
if not strings:
    print("No common prefix")
else:
    prefix = ""
    min_len = min(len(s) for s in strings)

    for i in range(min_len):
        # collect characters at position i from all strings
        chars = set(s[i] for s in strings)

        # if more than one unique character, stop
        if len(chars) == 1:
            prefix += chars.pop()
        else:
            break

    print("Longest Common Prefix:", prefix)
