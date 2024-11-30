def count_upper_and_lower(string):
    count_upper=0
    count_lower=0
    for ch in string:
        if ch.isupper():
            count_upper+=1
        elif ch.islower():
            count_lower+=1
    return count_upper,count_lower

sentence=input("Enter a sentence:")
upper_count,lower_count = count_upper_and_lower(sentence)
print(f"Count of uppercase characters in the sentence: {upper_count}")
print(f"Count of lowercase characters in the sentence: {lower_count}")
