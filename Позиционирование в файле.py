file_name = 'Текстовый документ.txt.'
with open(file_name, mode='r', encoding='utf8') as file:
    file_content = file.read()
    print(file_content)

print(file.closed)
# Использование оператора with open(file_name...) от простого использования file.close() отличается тем, что оператор
# with закрывает файл автоматичски.
