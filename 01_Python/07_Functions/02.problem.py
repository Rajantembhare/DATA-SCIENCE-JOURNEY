def count_vowels(s):
    vowels = "aeiouAEIOU"   # include both lowercase and uppercase
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example usage
text = "Python Programming"
print("Number of vowels:", count_vowels(text))

    
    
    
        
    
    