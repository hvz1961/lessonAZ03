import csv

# Путь к вашему входному и выходному CSV-файлам
input_file = 'prices.csv'
output_file = 'prices_cleaned.csv'

# Открываем входной файл для чтения и выходной файл для записи
with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Считываем заголовки и записываем их в выходной файл
    headers = next(reader)
    writer.writerow(headers)

    for row in reader:
        processed_row = []
        for value in row:
            # Убираем "руб." независимо от регистра и пробелов
            cleaned_value = value.replace('руб.', '').replace('Руб.', '').strip()
            # Пробуем преобразовать в число
            try:
                processed_value = float(cleaned_value)
                processed_row.append(processed_value)
            except ValueError:
                processed_row.append(cleaned_value)  # Если не число, добавляем как есть

        # Записываем обработанную строку в выходной файл
        writer.writerow(processed_row)

print(f'Обработка завершена. Результаты записаны в {output_file}.')
