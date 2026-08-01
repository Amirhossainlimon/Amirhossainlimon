import os
import requests


username = "Amirhossainlimon"

token = os.getenv("GITHUB_TOKEN")


headers = {
    "Authorization": f"Bearer {token}"
}


repos = requests.get(
    f"https://api.github.com/users/{username}/repos?per_page=100",
    headers=headers
).json()



languages = {}


for repo in repos:

    data = requests.get(
        repo["languages_url"],
        headers=headers
    ).json()


    for lang, value in data.items():

        languages[lang] = languages.get(lang,0)+value



total = sum(languages.values())


top_languages = sorted(
    languages.items(),
    key=lambda x:x[1],
    reverse=True
)[:6]



svg = """

<svg width="600" height="360"
xmlns="http://www.w3.org/2000/svg">


<style>

.title{
font-family:Arial;
font-size:24px;
font-weight:bold;
fill:white;
}


.text{
font-family:Arial;
font-size:18px;
fill:white;
}


.bar{

animation:grow 2s ease;

}


@keyframes grow{

from{
width:0;
}

to{
width:100%;
}

}


</style>



<rect width="100%" height="100%" rx="20" fill="#0d1117"/>



<text x="30" y="45" class="title">

🔥 Most Used Languages

</text>

"""


y = 90



for lang,value in top_languages:


    percent = round(
        (value/total)*100,
        1
    )


    width = percent * 4



    svg += f"""


<text x="30" y="{y}" class="text">

{lang} - {percent}%

</text>


<rect

x="220"

y="{y-18}"

height="16"

width="{width}"

rx="8"

fill="#02569B"

class="bar"

/>


"""

    y += 45



svg += """

</svg>

"""



os.makedirs(
    "assets",
    exist_ok=True
)



with open(
    "assets/languages.svg",
    "w"
) as file:

    file.write(svg)



print("Language SVG Generated Successfully")
