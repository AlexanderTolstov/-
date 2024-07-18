import time
import threading
for i in range(1,9):
    with open(f'example{i}.txt', 'w'):
        pass
def write_words(word_count, file_name):
    for i in range(1, word_count + 1):
        word = f"Какое-то слово № {i}\n"
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(word)
        time.sleep(0.1)
    print(f'Запись завершилась в файл {file_name}')
start = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
finish = time.time()
res = finish - start
print('Время работы:', res)
start = time.time()
th1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
th2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
th3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
th4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
th1.start()
th2.start()
th3.start()
th4.start()
th1.join()
th2.join()
th3.join()
th4.join()
print('Запись в файлы завершена')
finish = time.time()
res = finish - start
print('Время работы:', res)