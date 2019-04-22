def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input('Введите текст: ')
something = something.lower()
something = "".join(c for c in something if c not in ('!','.',':',' '))
   
print(something)
print(reverse(something))


if (is_palindrome(something)):
    print('Да это палиндром')
else:
    print('НЕТ это не палиндром')

