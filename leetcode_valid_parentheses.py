def valid_paren(str):
    i = 1
    while i < len(str):
        #if str[0] == '(' or str[0] == '{' or str[0]=='[':
        if i % 2 == 1:
            if str[i-1] == '(' and str[i] != ')':
                return False
            if str[i-1] == '{' and str[i] != '}':
                return False
            if str[i-1] == '[' and str[i] != ']':
                return False
        elif i % 2 == 0:
            if str[i] != '(' or str[i] != '{' or str[i] != '[':
                return False
        else: 
            return False
        i += 1
    return True

print(valid_paren('()'))
print(valid_paren('()[]{}'))
print(valid_paren('(]'))