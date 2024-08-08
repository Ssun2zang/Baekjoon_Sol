def solution(phone_book):
    phone_book.sort()
    prev = 'a'
    for p in phone_book:
        if prev == p[:len(prev)]:
            return False        
        prev = p
    return True