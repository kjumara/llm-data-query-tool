# 📌 LLM-Powered Data Query Tool
**LLM-Powered Data Query Tool**: Ask natural language questions about your data and get instant answers, along with charts and data tables. 

<p align="center">
    <img src="outputs/Initial%20View.png" alt="Initial View" width="600" height="400">
</p>

# 🛠 Tech Stack
**Languages & Frameworks:** Python, Pandas, Matplotlib, Streamlit  
**APIs & Tools:** OpenAI API, Git, Jupyter Notebook (for testing queries)

# 🎯 Project Overview
This tool bridges the gap between business users and raw datasets by using an LLM to interpret natural language questions. It generates structured Pandas queries, executes them, and return visual insights and tabular results in real-time.

# 📂 Dataset
- **Source**: [Kaggle Sample Sales Data](https://www.kaggle.com/datasets/kyanyoga/sample-sales-data)
- **Size**: 25 Columns x 2,823 Rows
- **License**: [Creative Commons Attribution-Noncommercial-Share Alike 3.0 Unported License](https://creativecommons.org/licenses/by-nc-sa/3.0/)

# 🧠 AI/ML Approach
- **Model:** OpenAI GPT-4o-mini (via API)
- **Prompt Engineering:** Converts natural language questions into executable pandas queries
- **Data Handling:** Queries the loaded dataset in real-time without storing user data
- **Visualization:** Generates charts automatically based on query results using Matplotlib

# 💻 How to Run

```bash
# Clone the repository
git clone https://github.com/kjumara/llm-data-query-tool.git
cd llm-data-query-tool

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
# 1. Copy .env.example to .env in the project root
# 2. Replace "your_key_here" with your OpenAI API key

# Run the Streamlit app 
streamlit run [app.py]
```

# 📊 Example Output

Below are sample outputs from the **LLM-Powered Data Query Tool**:
- **Screenshots** 

<p align="center">
    <img src="outputs/Bar%20Chart.png" alt="Bar Chart Example" width="45%">
    <img src="outputs/Line%20Chart.png" alt="Line Chart Example" width="45%">
</p>

Bar Chart and Line Chart shown above, generated from natural language queries.

- **Demo Video:** Watch a 30-45 second walkthrough of the app in action

<p align="center">
    <video src="https://private-user-images.githubusercontent.com/26746712/482400201-6a0355f7-fe41-4137-ae0c-60ef0796e75c.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTYyNDk0NzgsIm5iZiI6MTc1NjI0OTE3OCwicGF0aCI6Ii8yNjc0NjcxMi80ODI0MDAyMDEtNmEwMzU1ZjctZmU0MS00MTM3LWFlMGMtNjBlZjA3OTZlNzVjLm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA4MjYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwODI2VDIyNTkzOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTBiODIxOWFlZjdhMjlkNzRiYzNjYmZhZmYxOTg4Mzc0ZWQ3ZDExMjQ0NDM5MTU2ZTJiYzExNjE4Y2Q2NmY4N2QmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.UOGTn8N2qD9axi_XzQnoEfKrfWi2U6gQEdQg5Fx4wkU" controls width="700">
    your browser does not support the video tag
    </video>
</p>

> Example questions to try in the app:
> - "What are total sales per year"
> - "Which product line had the highest revenue in 2004"
> - "Show the top 5 customers by total sales"

# 📈 Results
The **LLM-Powered Data Query Tool** is evaluated based on its ability to:
- Generate correct Pandas queries from natural language questions
- Auto-generate informative charts for numeric and categorical data
- Provide an intuitive Streamlit interface for end-to-end interaction

# 🔮 Future Improvements
-  Add support for user-uploaded datasets
- Enhance LLM query robustness with additional prompt templates
- Include more chart types and customization options
- Deploy as a hosted web app for broader access

# 📜 License
This project is licensed under the MIT License.

# 👩🏽‍💻 Author
Kathryn Jumara

- LinkedIn: [Kathryn Jumara](https://www.linkedin.com/in/kathrynjumara/)
- Portfolio: [URL of Portfolio]
- Email: [Yahoo Email](kjumara@yahoo.com)
