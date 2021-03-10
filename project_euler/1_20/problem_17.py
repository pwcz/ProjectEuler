
numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
           11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
           18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
           70: "seventy", 80: "eighty", 90: "ninety", 100: "one hundred", 1000: "one thousand"}


def get_number_string(number: int) -> str:
    if number in numbers:
        return numbers[number]
    elif number < 100:
        return f"{numbers[(number//10)*10]}-{numbers[number%10]}"
    elif number < 1000:
        sub_hundred = f" and {get_number_string(number%100)}" if number % 100 != 0 else ""
        return f"{numbers[number//100]} hundred{sub_hundred}"


def count_number_letters(number: str) -> int:
    return len(number.replace(" ", "").replace("-", ""))


print(sum(count_number_letters(get_number_string(x)) for x in range(1, 1001)))
