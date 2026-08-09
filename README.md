# 👋 Hi, I'm Amir Hossain Limon

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&duration=3000&pause=1000&color=00F7FF&center=true&vCenter=true&width=600&lines=Flutter+Developer;Mobile+App+Developer;UI%2FUX+Enthusiast;Building+Modern+Apps" />

<img align="right" width="350" src="https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif"/>


## 🚀 About Me

```dart
class FlutterDeveloper {

  String name = "Amir Hossain Limon";

  String role = "Flutter Developer";

  List<String> skills = [
    "Flutter",
    "Dart",
    "Firebase",
    "REST API",
    "GetX",
    "Provider"
  ];

  String passion =
      "Building modern, scalable and user-friendly applications";

}
<br>
🔭 Currently working on Flutter Applications
🌱 Learning Advanced Flutter Architecture
💡 Interested in Mobile App Development & UI/UX
⚡ Love solving problems with code
🎯 Goal: Build production-level applications
🛠️ Tech Stack
<div align="center"> <img src="https://skillicons.dev/icons?i=flutter,dart,firebase,androidstudio,vscode,git,github,figma,postman,mysql,java,c,cpp" /> </div>
📱 Featured Flutter Projects
<table> <tr> <td width="50%">
🚀 BMI Calculator

📌 Flutter UI + Business Logic

✨ Features:

BMI calculation
Clean UI
Responsive design
</td> <td width="50%">
💬 Chat Application

📌 Modern Chat Interface

✨ Features:

Real-time UI
Firebase Ready
Modern design
</td> </tr> <tr> <td width="50%">
📝 Flashcard Quiz App

📌 Interactive Learning App

✨ Features:

Quiz system
Score tracking
Beautiful animations
</td> <td width="50%">
🛒 E-Commerce App

📌 Shopping Application

✨ Features:

Product listing
Cart system
API integration
</td> </tr> <tr> <td width="50%">
✈️ Travel UI

📌 Responsive Flutter Design

✨ Features:

Modern layouts
Smooth animations
</td> <td width="50%">
📖 Quote Vault

📌 Quote Management App

✨ Features:

Category system
Favorite quotes
</td> </tr> </table>
💻 Development Environment
Mobile Development:
  - Flutter
  - Dart
  - Firebase
  - REST API

State Management:
  - GetX
  - Provider

IDE:
  - Android Studio
  - VS Code

Programming:
  - Java
  - C
  - C++

Database:
  - MySQL
  - Firebase Firestore

Tools:
  - Git
  - GitHub
  - Postman
  - Figma
📊 GitHub Analytics
<p align="center"> <img src="https://github-readme-stats.vercel.app/api?username=Amirhossainlimon&show_icons=true&theme=tokyonight&hide_border=true"/> <img src="https://github-readme-streak-stats.herokuapp.com/?user=Amirhossainlimon&theme=tokyonight&hide_border=true"/> </p>
📈 Most Used Languages
<p align="center"> <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Amirhossainlimon&layout=compact&theme=tokyonight&hide_border=true"/> </p>
🐍 Contribution Snake Animation
<p align="center"> <img src="https://raw.githubusercontent.com/Amirhossainlimon/Amirhossainlimon/output/github-contribution-grid-snake.svg"/> </p>
🌐 Connect With Me
<p align="center"> <a href="https://github.com/Amirhossainlimon"> <img src="https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github"/> </a> <a href="https://linkedin.com"> <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin"/> </a> <a href="mailto:yourmail@gmail.com"> <img src="https://img.shields.io/badge/Email-red?style=for-the-badge&logo=gmail"/> </a> </p>
👀 Profile Views
<img src="https://komarev.com/ghpvc/?username=Amirhossainlimon&label=Profile%20Views&color=0e75b6&style=flat"/>
⚡ Daily Motivation
<img src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=tokyonight"/>
<div align="center">
⭐ Code • Create • Learn • Repeat ⭐
<img src="https://media.giphy.com/media/f3iwJFOVOwuy7K6FFw/giphy.gif" width="300"> </div> ```
Snake Animation কাজ করানোর জন্য .github/workflows/snake.yml বানাতে হবে:
name: Generate Snake

on:
  schedule:
    - cron: "0 */12 * * *"

  workflow_dispatch:


jobs:

  build:

    runs-on: ubuntu-latest

    steps:

      - uses: Platane/snk@v3
        with:

          github_user_name: Amirhossainlimon

          outputs: |
            dist/github-contribution-grid-snake.svg


      - uses: crazy-max/ghaction-github-pages@v4
        with:

          build_dir: dist

        env:

          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
