# AutoStock Insight - AI Financial Report Generator

A Streamlit web application powered by AutoGen agents that generates comprehensive financial reports for requested stock symbols, including historical performance, key financial ratios, recent news analysis, and a normalized price chart.

---

## ✨ Features

- **AI-Powered Reports**: Utilizes AutoGen agents to perform financial analysis, research news, and generate a cohesive report.
- **Multi-Stock Analysis**: Analyze multiple stock symbols simultaneously by entering a comma-separated list.
- **Key Financial Metrics**: Includes important ratios like P/E, Forward P/E, Dividends, Price to Book, Debt/Equity, and ROE.
- **Historical Performance**: Reports on the percentage change in stock price over the past 6 months.
- **Normalized Price Chart**: Generates and displays a normalized price chart for easy comparison.
- **News Analysis**: Gathers recent news headlines to provide context for stock performance.
- **Markdown Report Output**: The final report is presented in a clear, readable Markdown format.
- **Automated Export**: Automatically saves the final report to a Markdown file.

---

## ⚙️ Installation

Before running the application, ensure you have the necessary dependencies installed.

### 1. Clone the Repository

```bash
git clone https://github.com/AhmedZeyadTareq/AutoStockReport.git
cd AutoStockReport
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### 2. Create a Virtual Environment (Recommended)
```Bash
python -m venv venv
source venv/bin/activate   # On Windows use `.\venv\Scripts\activate`
```

### 3. Install Python Libraries
```Bash
pip install -r requirements.txt
```
(Note: You will need to create a requirements.txt file containing the required libraries: streamlit, autogen, python-dotenv, pandas, yfinance, matplotlib - based on the code's likely dependencies for fetching/plotting stock data, although not all are explicitly imported in the provided snippet, they are necessary for the tasks described).

### 4. Set up Environment Variables
Create a .env file in the root directory of the project and add your OpenAI API key:

Code snippet
```
OPENAI_API_KEY="your_openai_api_key"
```
Replace "your_openai_api_key" with your actual OpenAI API key.

## 🚀 How It Works
The application uses a multi-agent system orchestrated by AutoGen to perform the financial analysis and reporting:

User Input: The user enters stock symbols into the Streamlit interface.
Initialization: Upon clicking "Start Analysis", the application initializes various AutoGen agents with specific roles.
Financial Analysis: A Financial_Assistant agent fetches current stock prices, calculates historical performance, retrieves key financial ratios (P/E, Forward P/E, etc.), and generates a normalized price chart.
Research: A Researcher agent gathers recent news headlines related to the specified stocks using search tools (simulated via prompts in this code).
Writing: A Writer agent, acting as a professional financial report writer, compiles all the gathered data and news into a comprehensive report in Markdown format. This agent is guided by a Critic and a team of reviewers (Legal_Reviewer, Consistency_Reviewer, Text_Alignment_Reviewer, Completion_Reviewer, Meta_Reviewer) to ensure the report's quality and accuracy.
Export: An Exporter agent saves the final Markdown report to a file.
Display: The Streamlit application displays the normalized price chart and the final generated report to the user.
## 📁 Project Structure
Bash
```
AutoStockReport/
├── .env                   # Environment variables (for API keys)
├── AutoStockReport.py     # The main Streamlit application code
├── requirements.txt       # Python dependencies
└── coding/                # Directory for code execution and generated files (like plots)
    └── normalized_prices.png # Generated plot file (example)
```
## ▶️ How to Use
Ensure you have completed the installation steps, including setting up the .env file and installing dependencies.

Run the Streamlit application from your terminal:

```Bash
streamlit run AutoStockReport.py
```
The application will open in your web browser.
Enter the stock symbols you want to analyze in the text input field, separated by commas (e.g., AAPL, GOOGL, TSLA).

Click the "🚀 Start Analysis" button.

The application will display a spinner while the AI agents are running.

Once the analysis is complete, the normalized price chart and the generated financial report will appear on the page.

A Markdown file containing the report will also be saved in the coding/ directory.

## 💡 Why This Project is Useful
Automated Reporting: Quickly generate detailed financial reports without manual data gathering.
Holistic View: Combines historical data, key financial metrics, and recent news for a comprehensive analysis.
AI-Powered Insights: Leverages the power of large language models via AutoGen for sophisticated analysis and report generation.
Customizable: Easily adaptable to include more financial metrics, different time periods, or additional data sources by modifying agent tasks.


## 👨‍💻 Developed By
**Eng. Ahmed Zeyad Tareq**  
📌 Data Scientist | 🎓 Master of AI Engineering
- 📞 WhatsApp: +905533333587
- 📷 Instagram: [@adlm7](https://instagram.com/adlm7)
- 🔗 LinkedIn: [AhmedZeyadTareq](https://www.linkedin.com/in/ahmed-zeyad-tareq)
- 📊 Kaggle: [AhmedZeyadTareq](https://www.kaggle.com/ahmedzeyadtareq)


## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details. (You should create a LICENSE file with the MIT license text if you don't have one).

## ⭐ Support and Contribution
If you find this project helpful, please consider giving it a star ⭐ on GitHub!

Contributions are welcome! If you have ideas for improvements or find issues, feel free to open a Pull Request or create an Issue on the GitHub repository.
