import requests
import json
from bs4 import BeautifulSoup

res = requests.get("https://projetos.digitalinnovation.one/blog")
res.encoding = 'utf-8'  #  garante a correta formatação dos caracteres retornados por 'res.text'

soup = BeautifulSoup(res.text, 'html.parser')  #  separará os conteúdos do código html

links = soup.find(class_="pagination").find_all('a')  #  separará os links da paginação do blog

all_pages = []
for link in links:
    page = requests.get(link.GET('href'))
    all_pages.append(BeautifulSoup(page.text, 'html.parser'))

print(len(all_pages))  #  contarpa o número de páginas

posts = soup.find_all(class_="post")  #  para pegar os posts de um determinado tipo; o class precisa ver seguido do '_' para o python não reconhecer como classe. Tem que ver o código fonte e se virar

all_posts = []

for posts in all_pages:
    posts = posts.find_all(class_="post")
    for post in posts:
        info = post.find(class_="post-concent")
        title = info.h2.text
        preview = info.p.text
        author = info.find(class_="post-author").text
        time = info.footer.date['datetime']
        img = info.find(class_="wp-post-image")['src']
        all_posts.append({
            'title': title,
            'preview': preview,
            'author': author,
            'img': img,
            'time':time
        })


print(all_posts)
with open('posts.json', 'w') as json_file:
    json.dump(all_posts, json_file, ident=3, ensure_ascii=False)

# print(post.find('h2').text)
# print(all_posts[0])
#print(res)  #  Retorna 200 se a página estiver funcionando e 400 se der erro
# print(res.text)  #  retorna o conteúdo html da página
# print(soup)