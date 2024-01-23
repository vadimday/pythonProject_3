def display_line(symbol, length, direction):
    if direction.lower() == 'горизонтальная':
        print(symbol * length)
    elif direction.lower() == 'вертикальная':
        for _ in range(length):
            print(symbol)
    else:
        print("выберите.")
display_line('*', 10, 'горизонтальная')
display_line('#', 5, 'вертикальная')
