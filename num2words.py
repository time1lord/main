a = 12344432351235123451235
c = []
import math

b = math.ceil(len(str(a)) / 3)

for i in range(b):
    c.append(a % 1000)
    a = math.floor(a / 1000)

ones = {
    0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
    5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
    10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
    15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
}
tens = {
    20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
    60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"
}
words = []

def three_digit_to_words(number):
    """Converts a three-digit number to words.

    Args:
        number: The three-digit number to convert.

    Returns:
        The number in words.
    """

    if number < 20:
        return ones[number]
    elif number < 100:
        return tens[number // 10 * 10] + ("" if number % 10 == 0 else " " + ones[number % 10])
    else:
        return ones[number // 100] + " Hundred" + ("" if number % 100 == 0 else " " + three_digit_to_words(number % 100))

for i in range(len(c)):
    words.append(three_digit_to_words(c[i]))

places = ["", "Thousand", "Million", "Billion", "Trillion", "Quadrillion", "Quintillion", "Sextillion", "Septillion", "Octillion", "Nonillion", "Decillion"]

result = []
for i in range(len(words)):
    if c[i] != 0:  # Only add the place name if the corresponding number is not zero
        if i == 0:
            result.append(words[i])
        else:
            result.append(words[i] + " " + places[i])

result.reverse()

sen = result[0]
for i in range(1, len(result)):
    sen += " " + result[i]

print(sen)
