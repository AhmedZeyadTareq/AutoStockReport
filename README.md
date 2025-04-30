# 📊 AutoStock Insight

**Generate full financial reports using AI agents – no APIs required.**

AutoStock Insight is a smart, interactive tool that lets you enter stock symbols and receive a full, structured financial report—automatically written and formatted. Built using [Streamlit](https://streamlit.io) and [AutoGen](https://github.com/microsoft/autogen), the app handles everything from data collection to writing and exporting.

---

## 🚀 Features

- ✅ Accepts multiple stock symbols (e.g., AAPL, TSLA, GOOGL)
- 📈 Retrieves price history, financial metrics, and correlation
- 📰 Gathers relevant news headlines (10 per stock)
- 🧠 Uses multiple AI agents for analysis, writing, and review
- 📊 Generates a normalized price chart (`normalized_prices.png`)
- 📝 Saves the final report in Markdown (`report.md`)

---

## ⚙️ How to Run

1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Create `.env` file**
   ```env
   OPENAI_API_KEY=your_openai_key
   ```
4. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## 📂 Output

- `coding/normalized_prices.png`: stock price chart
- `coding/report.md`: final AI-written financial report

---

## 💡 Why Use This?

- No manual research needed
- No API keys for financial/news data
- Uses AutoGen agents with distinct roles for quality
- Clean, well-organized Markdown report
- Easy to extend for other domains (e.g., crypto, sectors, etc.)

---

## 📜 License

MIT License

> For educational and demo purposes only.
