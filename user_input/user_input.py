def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input('Введите текст: ')
something = something.lower()



forbidden = ('.','?','!',':',';','-','—',' ')
simbol = ' '
if simbol in forbidden:
    if simbol in something:
        something = something.replace(simbol,'')
   
print(something)

if (is_palindrome(something)):
    print('Да это палиндром')
else:
    print('НЕТ это не палиндром')

