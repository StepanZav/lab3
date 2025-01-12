# Задание 1
def create_example_file():
    with open('lab3.txt', 'w') as file:
        file.write("Первая строка текста.\n")
        file.write("Вторая строка текста.\n")
        file.write("Третья строка текста.\n")

def read_file(file_name, mode='all'):
    try:
        with open(file_name, 'r') as file:
            if mode == 'all':
                content = file.read()
                print("Содержимое файла:\n", content)
            elif mode == 'line':
                print("Содержимое файла построчно:")
                for line in file:
                    print(line, end='')
            else:
                print("Неверный режим чтения. Используйте 'all' или 'line'.")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_name}' не найден.")

# Задание 2
def write_user_input():
    user_input = input("Введите текст для записи в файл user_input.txt: ")
    with open('user_input.txt', 'w') as file:
        file.write(user_input)

    user_input = input("Введите текст для добавления в файл user_input.txt: ")
    with open('user_input.txt', 'a') as file:
        file.write("\n" + user_input)


if __name__ == "__main__":
    create_example_file()

    # Читаем файл example.txt
    read_file('example.txt', 'all')
    read_file('example.txt', 'line')

    write_user_input()

    read_file('non_existent_file.txt', 'all')