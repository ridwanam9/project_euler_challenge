ones = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine"
}

teens = {
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
    14: "fourteen", 15: "fifteen", 16: "sixteen",
    17: "seventeen", 18: "eighteen", 19: "nineteen"
}

tens = {
    20: "twenty", 30: "thirty", 40: "forty",
    50: "fifty", 60: "sixty",
    70: "seventy", 80: "eighty", 90: "ninety"
}

def number_to_words(n):
    if n == 1000:
        return "one thousand"
    
    words = ""
    
    if n >= 100:
        words += ones[n // 100] + " hundred"
        remainder = n % 100
        if remainder != 0:
            words += " and "
        n = remainder
    
    if 10 <= n <= 19:
        words += teens[n]
    else:
        if n >= 20:
            words += tens[(n // 10) * 10]
            if n % 10 != 0:
                words += " "
        if n % 10 != 0:
            words += ones[n % 10]
    
    return words


total = 0
for i in range(1, 1001):
    word = number_to_words(i)
    word = word.replace(" ", "")
    total += len(word)

print(total)

print(number_to_words(342))
print(len(number_to_words(342).replace(" ", "")))