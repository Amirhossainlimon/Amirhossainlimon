import os
import requests

username = "AmirhossainLimon"

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
    url = repo["languages_url"]

    data = requests.get(
        url,
        headers=headers
    ).json()

    for lang, value in data.items():
        languages[lang] = languages.get(lang, 0) + value


total = sum(languages.values())

svg = """
<svg width="500" height="300" xmlns="http://www.w3.org/2000/svg">

<rect width="100%" height="100%" fill="#0d1117"/>

<text x="30" y="40" fill="white" font-size="24">
🔥 Most Used Languages
</text>
"""


y = 80

for lang, value in sorted(
    languages.items(),
    key=lambda x:x[1],
    reverse=True
)[:6]:

    percent = round(value / total * 100, 1)

    svg += f"""
    <text x="30" y="{y}" fill="white" font-size="18">
    {lang}: {percent}%
    </text>
    """

    y += 35


svg += "</svg>"


os.makedirs("assets", exist_ok=True)

with open(
    "assets/languages.svg",
    "w"
) as f:
    f.write(svg)
