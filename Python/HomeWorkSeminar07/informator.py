

# функция для отображения чего либо
def view_data(title, data):
    print(f'{title} = {data}')



# функция для отображения чего либо
def view_list(title, data):
    count = 1
    for element in data:
        print(f'{count}) {title} = {element}')
        count += 1
