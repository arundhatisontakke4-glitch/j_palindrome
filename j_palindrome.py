def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome, ignoring case and non-alphanumeric characters."""
    # Clean the string: keep only alphanumeric characters and convert to lowercase
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    # Compare the cleaned string with its reverse
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    # Sample test cases
    test_strings = ["racecar", "Hello", "A man, a plan, a canal: Panama", "12321"]
    
    for s in test_strings:
        result = is_palindrome(s)
        status = "IS" if result else "is NOT"
        print(f"'{s}' {status} a palindrome.")