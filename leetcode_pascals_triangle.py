def pascals_triangle(rows):
    output = []
    if rows == 1:
        output = [[1]]
    elif rows == 2:
        output = [[1,1]]
    elif rows > 2:
        num = 1
        while num <= rows:
            
            output.append(num)
