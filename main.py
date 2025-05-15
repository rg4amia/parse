import re
import csv
import pandas as pd

# Motif pour détecter le début d'un message WhatsApp
MESSAGE_PATTERN = re.compile(r'^(\d{2}/\d{2}/\d{2}), (\d{1,2}:\d{2}\s?[ap]m) - (.*)$')

input_file = 'chat.txt'
output_file = 'chat.csv'

rows = []
current = {'date': '', 'time': '', 'author': '', 'message': ''}

with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n')
        match = MESSAGE_PATTERN.match(line)
        if match:
            # Sauvegarder le message précédent
            if current['date']:
                rows.append(current)
            date, time, rest = match.groups()
            # Séparer auteur et message si possible
            if ': ' in rest:
                author, message = rest.split(': ', 1)
            else:
                author, message = '', rest
            current = {
                'date': date,
                'time': time,
                'author': author,
                'message': message
            }
        else:
            # Ligne de continuation du message précédent
            current['message'] += '\n' + line
    # Ajouter le dernier message
    if current['date']:
        rows.append(current)

# Écriture dans le CSV
with open(output_file, 'w', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['date', 'time', 'author', 'message']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

print(f'Export terminé : {output_file}')

# Conversion en Excel (XLSX)


df = pd.read_csv(output_file)
df.to_excel('chat.xlsx', index=False)
print('Export Excel terminé : chat.xlsx')
