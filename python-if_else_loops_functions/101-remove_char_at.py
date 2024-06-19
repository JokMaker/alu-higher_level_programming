def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str  # If n is out of range, return the original string
    return str[:n] + str[n+1:]
