def char_frequency(string_name):
    dict = {}
    for number in range(len(string_name)):
        for char in  string_name:
            if char in string_name:
                return dict.append(char,number)


print(char_frequency("google.com"))
sample = "google.com"
print({value: sample.count(value) for value in sample})
