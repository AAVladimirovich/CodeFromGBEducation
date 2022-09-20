# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import utils_v3 as hh  # hh - homework helper

print(
    '***PyCharm***\n'
    'Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.\n'
    'Входные и выходные данные хранятся в отдельных текстовых файлах.\n'
    '\n'
     + '*' * 16 + 'РЕШЕНИЕ' + '*' * 16 + '\n'
    )

string = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEEdddddddddFFFFFFFFFFFFFFEEEEEEEEEEEEXXXXXXXXXXXXXXXXXXXxxxxxxxxxxxx'
hh.write_to_file("HWS05_06_01_RLE_initial.txt", string, 'w')  # запись во входной текстовый файл
string_for_encode = hh.read_from_file("HWS05_06_01_RLE_initial.txt", True)  # чтение из файла
encoded_string = hh.rle_encode(string_for_encode)  # применяем RLE кодирование получаем строку encoded
hh.write_to_file("HWS05_06_01_RLE_encoded.txt", encoded_string, 'w')  # запись во входной текстовый файл строки encoded
string_for_decode = hh.read_from_file("HWS05_06_01_RLE_encoded.txt", True)  # чтение из файла для декодирования
decoded_string = hh.rle_decode(string_for_decode)  # применяем RLE декодирование получаем строку decoded
hh.write_to_file("HWS05_06_01_RLE_decoded.txt", decoded_string, 'w')  # записываем результат в файл decoded
hh.read_from_file("HWS05_06_01_RLE_decoded.txt")   # читаем с файла результат декодирования
