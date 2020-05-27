def is_palindrome(string):
    if len(string) == 0:
        return False
    if len(string) == 1:
        return True

    start_index = 0
    end_index = len(string)-1

    while start_index < end_index:
        strart_c = string[start_index]
        end_c = string[end_index]
        if strart_c != end_c:
            return False
        start_index += 1
        end_index -= 1

    return True


print(is_palindrome("adffvbddvddbvffda"))