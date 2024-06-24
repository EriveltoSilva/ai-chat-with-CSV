[MAINTENANCE_BADGE]: https://img.shields.io/badge/Maintained%3F-yes-green.svg
[PYTHON_BADGE]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[LICENSE_BADGE]: https://img.shields.io/pypi/l/ansicolortags.svg


<h1 align="center">AI Chat with CSV</h1>

![PYTHON][PYTHON_BADGE]
![LICENSE][LICENSE_BADGE]


`Content:`
<ul>
  <li><a href="#about">About</a></li>
  <li><a href="#features">Project Features</a></li>
  <li><a href="#gettingStarted">Getting Started</a></li>
    <ul>
      <li><a href="#technologiesUsed">Technologies Used</a></li>
      <li><a href="#preRequisites">Prerequisites</a></li>
    </ul>
  <li><a href="#howToRun">How To Run</a></li>
  <li><a href="#results">Results</a></li>
  <li><a href="#projectVideo">Project Video</a></li>
  <li><a href="#collaborators">Collaborators</a></li>
</ul>

<p align="center">
    <img src="./assets/images/rh-assistant1.PNG" alt="Image Example" width="400px">
</p>

<h2 id="about">📌 About</h2>
This project implements an interactive user interface using Langchain and Streamlit, allowing users to upload a CSV document and ask questions about its content. The goal is to provide an easy and efficient way to interact with CSV files, extracting specific information without the need to manually navigate through the data.

<h2 id="features">✔ Project Features</h2>

- <strong>Upload CSV Documents:</strong> Upload CSV files directly through the Streamlit interface.
- <strong>Interactive Questions:</strong> The application allows users to ask questions in natural language about the uploaded document.

  - <strong>Example questions:</strong>

        "How many rows does the document have?"
        "Who is the employee with ID number 245?"
        "How many records does the file have?"

- <strong>Immediate Responses:</strong> Using AI, the application provides immediate answers based on questions asked by users.

<h2 id="gettingStarted">🚀 Getting Started</h2>

This section describes how to run the project locally.

<h3 id="technologiesUsed">Technologies Used</h3>

- <strong>Langchain:</strong> Used for natural language processing and interpretation of questions asked by the user.
- <strong>Streamlit:</strong> Framework used to build the interactive web interface in a simple and fast way.
- <strong>Python:</strong>Main language of the project, used to integrate Langchain and Streamlit and to manipulate CSV data.

<h3 id="preRequisites">Prerequisites</h3>

Ensure you have the following prerequisites installed:

- [Python 3.x](https://www.python.org/downloads/)
- [Streamlit](https://docs.streamlit.io/)
- [Langchain](https://python.langchain.com/v0.2/docs/introduction/)
- OpenAI API Key

<h2 id="howToRun">How to Run</h2>

- Clone the project repository from GitHub:

```bash
git clone https://github.com/EriveltoSilva/ai-chat-with-CSV.git
```


- Navigate to the project directory and install the required dependencies. 
```bash
pip install -r requirements.txt
```

- Then start the Streamlit app:

```bash
streamlit run app.py
```

<h2 id="results">🤝 Results</h2>

<p align="center">
    <img src="./assets/images/rh-assistant1.PNG" alt="Image Example" />
</p>


<h2 id="projectVideo">▶ Project Video</h2>

<a href="#">
See a short video of how project works on my LinkedIn
</a>

<h2 id="collaborators">🤝 Collaborators</h2>

Special thanks to the project contributor:

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/125351173?v=4" width="100px;" alt="Fernanda Kipper Profile Picture"/><br>
        <sub>
          <b>Erivelto Silva</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<h2 id="contribute">📫 Contribute</h2>

To contribute to this project, follow these steps:

1. `git clone https://github.com/EriveltoSilva/ai-chat-with-CSV.git`
2. `git checkout -b feature/NAME`
3. Follow commit patterns
4. Open a Pull Request explaining the problem solved or feature made. If applicable, include screenshots of visual modifications and wait for the review!

<h2 id="contribute">📫 License</h2>

This project is licensed under the MIT License. See the <a href="./LICENSE">LICENSE file</a> for more information.