def is_palindrome_valid(s: str) -> bool:
    cleaned_chars = []
    for char in s:
        if char.isalnum():
            cleaned_chars.append(char.lower())

    processed_s = "".join(cleaned_chars)

    if not processed_s or len(processed_s) == 1:
        return True

    left = 0
    right = len(processed_s) - 1

    while left < right:
        if processed_s[left] != processed_s[right]:
            return False
        left += 1
        right -= 1

    return True
