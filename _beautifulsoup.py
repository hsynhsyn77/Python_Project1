html_doc = """
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>İlk web sayfam</title>
</head>
<body>

<h1 id="header">
    Python
</h1>
    <div class="grup1">
        <h2>
            Programlama
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    <div class="grup2">
         <h2>
            Modüller
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>

    </div>
</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

result = soup.prettify()
result = soup.title
result = soup.head
result = soup.body

result = soup.title.name
result = soup.title.string
result=soup.h1
result=soup.h2
result=soup.h2.name
result=soup.h2.string


result=soup.find_all("h2")
result=soup.find_all("h2")[0]
result=soup.find_all("h2")[1]

result=soup.div

result=soup.find_all("div")[1]
result=soup.find_all("div")[1].ul.find_all("li")


result=soup.div.findChildren()

result=soup.div.findNextSibling()




print(result)
