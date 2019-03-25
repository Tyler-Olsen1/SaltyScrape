from bs4 import BeautifulSoup

html_doc = """
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Salty Scrape</title>
  <meta name="Salty Scrape" content="Addresses for BB & Rob">
  <meta name="Tyler Olsen" content="SaltyScrape">
  <link rel="stylesheet" href="./styles.css">
</head>

<body>
  <script src="js/scripts.js"></script>
  <h3 data-hello="hi">Fight the Power</h3>
  <ul class='items'>
    <li class="item" id="000">
        <a href='#'>
        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quaerat pariatur exercitationem iste reiciendis, reprehenderit qui voluptates perspiciatis cumque expedita, aut a accusamus quas fugiat sed perferendis non rem neque quod.</p>
    </li>
    <li class="item" id="xxx">
        <a href='#'>
        <p>BeetlejuiceBeetlejuiceBeetlejuice, sit amet consectetur adipisicing elit. Quaerat pariatur exercitationem iste reiciendis, reprehenderit qui voluptates perspiciatis cumque expedita, aut a accusamus quas fugiat sed perferendis non rem neque quod.</p>
    </li>
    <li class="item" id="section1">
        <a href='#'>
        <p>this is section1, sit amet consectetur adipisicing elit. Quaerat pariatur exercitationem iste reiciendis, reprehenderit qui voluptates perspiciatis cumque expedita, aut a accusamus quas fugiat sed perferendis non rem neque quod.</p>
    </li>
    <li class="item">
        <a href='#'>
        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quaerat pariatur exercitationem iste reiciendis, reprehenderit qui voluptates perspiciatis cumque expedita, aut a accusamus quas fugiat sed perferendis non rem neque quod.</p>
    </li>
    <li class="forTheHorde">
        <a href='#'>
        <p>This is for Tyler, sit amet consectetur adipisicing elit. Quaerat pariatur exercitationem iste reiciendis, reprehenderit qui voluptates perspiciatis cumque expedita, aut a accusamus quas fugiat sed perferendis non rem neque quod.</p>
    </li>
  </ul>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

#direct
#print(soup.body)
#print(soup.head)
#print(soup.head.title)

#find()
#el = soup.find('li')

# find_all() or findAll()
#el = soup.find_all('li')
# el = soup.find_all('li')[0]
# el = soup.find(id='xxx')
#el = soup.find(class_='forTheHorde')
# el = soup.find(attrs={"data-hello": "hi"})
 
#select
#el = soup.select('#section1')[0]
#putting the array [0] asks for the first index it finds and doesn't return a list

#get_text()
#el = soup.find(class_="xxx").get_text()
#line 66 didn't work. I wonder why.

# for item in soup.select('.item'):
#     print(item.get_text())
# I like this one

#Navigation
el = soup.body.contents 
#return with a \n all over (linebreaks)

print(el)

