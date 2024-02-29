from sameNumberException import SameNumberException

equals = None
a = int(input('first number'))
b = int(input('second number'))

try:
    a/b 
    if a == b:
        raise SameNumberException('Error: Same number.')
except BaseException as e:
    print(f'Error muahahaha: {e}')

finally:
    print('the "finally" codeblock always runs even if theres no error.')


print('pero se puede seguir...?')