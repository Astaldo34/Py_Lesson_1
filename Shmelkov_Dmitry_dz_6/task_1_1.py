import requests


responce = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

with open('text.txt', 'w+', encoding='utf-8') as f:
    f.write(responce.text)
    f.seek(0)
    result = []
    for line in f:
        addres = line[:line.index(' ')]
        metod = line[line.index('"'):line.index(' /')].replace('/', '').replace('"', '')
        src = line[line.index(' /'):line.index(' HTTP')].replace(' ', '')
        result.append((addres, metod, src))

# print(*(res for res in result), sep='\n')
print(result[:10])
