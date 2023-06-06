from bs4 import BeautifulSoup

with open("pie.html", "r") as f: 
    doc = BeautifulSoup(f, "html.parser")

title = doc.find("title")

print(title.string)

print("Existing external links in this webpage")

print()

tags = doc.find_all("a")

for tag in tags:
    href = tag.get('href')

    if href: 
        print("href: ", href)
    
    p_tag = tag.find("p")

    if p_tag: 
        print(p_tag.string)
    
    print()