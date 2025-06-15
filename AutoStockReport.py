import streamlit as st
import os
import autogen
from dotenv import load_dotenv
from datetime import datetime

# Get API key - handle both local and Streamlit Cloud environments
try:
    openai_key = st.secrets["OPENAI_API_KEY"]
except:
    from dotenv import load_dotenv
    load_dotenv()
    openai_key = os.getenv("OPENAI_API_KEY")


# llm_config = {
#     "model": "gpt-4.1",
#     "api_key": openai_key
# }



llm_config = {
    "config_list": [  # This is the required top-level key
        {
            "model": "gpt-4.1-mini",  # Must be a valid model name
            "api_key": openai_key,   # Your actual API key
            "base_url": None,        # Optional: if using a different endpoint
            "api_type": "open_ai",  # Optional: "azure" if using Azure OpenAI
            "api_version": None     # Optional: for Azure
        }
    ],
    "temperature": 0.3,             # Optional parameters
    "timeout": 120,
    "max_retries": 3,
    "cache_seed": 42
}



st.set_page_config(page_title="📊 AutoStock Insight", layout="centered")
st.title("📊 AI Financial Report Generator")
st.markdown("**Enter stock symbols (e.g., AAPL, GOOGL) and generate a full financial report powered by AI.**")
user_input = st.text_input("🧾 Stock Symbols", placeholder="AAPL, GOOGL, TSLA")
start = st.button("🚀 Start Analysis")

if start and user_input.strip():
    stocks = [s.strip().upper() for s in user_input.split(",") if s.strip()]
    stock_str = ", ".join(stocks)
    today = datetime.now().strftime("%Y-%m-%d")

    financial_tasks = [f"""
        Today is {today}.
        What are the current stock prices of {stock_str}, and how is the performance over the past 6 months in terms of percentage change?
        Start by retrieving the full name of each stock and use it for all future requests.
        Prepare a figure of the normalized price of these stocks and save it to a file named normalized_prices.png.
        Include info about P/E, Forward P/E, Dividends, Price to Book, Debt/Equity, ROE.
        Analyze the correlation between the stocks.
        Do not use API keys.
        If the data is wrong (e.g., price = 0), retry with a better query.
    """]

    research_tasks = ["""
        Investigate possible reasons of the stock performance using news headlines from Bing or Google.
        Retrieve 10 headlines per stock.
        Use full names.
        Do not use sentiment analysis or APIs.
    """]

    writing_tasks = ["""
        Write a full financial report using all data and normalized_prices.png.
        Include a comparison table for all metrics and recent news.
        Explain each ratio, compare stocks, and summarize the news.
        Offer future scenarios based on news and performance.
        Only return the final report in Markdown (no comments).
    """]

    exporting_task = ["Save the final report (only the report) to a .md file using a Python script."]

    def create_agent(name, role_description="", termination_condition=None):
        return autogen.AssistantAgent(
            name=name,
            llm_config=llm_config,
            is_termination_msg=termination_condition or (lambda x: False),
            system_message=role_description
        )

    financial_assistant = create_agent("Financial_Assistant")
    researcher = create_agent("Researcher")

    writer = create_agent("Writer", role_description="""
        You are a professional writer for financial reports.
        Write in Markdown without block indicators or comments.
        Only return final work.
    """)

    export_agent = create_agent("Exporter")

    critic = create_agent("Critic", role_description="You are a critic. Provide final improvement feedback.",
                          termination_condition=lambda x: "TERMINATE" in x.get("content", ""))

    reviewers = [
        create_agent("Legal_Reviewer", "Ensure content is legally compliant. 3 bullet points max."),
        create_agent("Consistency_Reviewer", "Check consistency of numbers and facts."),
        create_agent("Text_Alignment_Reviewer", "Ensure text matches data."),
        create_agent("Completion_Reviewer", "Ensure all required elements are present."),
        create_agent("Meta_Reviewer", "Aggregate all feedback into one recommendation.")
    ]

    def reflection_message(recipient, messages, sender, config):
        return f"Review the following content:\n\n{recipient.chat_messages_for_summary(sender)[-1]['content']}"

    review_chats = [
                       {
                           "recipient": reviewers[i],
                           "message": reflection_message,
                           "summary_method": "reflection_with_llm",
                           "summary_args": {"summary_prompt": "{'reviewer': '', 'review': ''}"},
                           "max_turns": 1
                       } for i in range(4)
                   ] + [{
        "recipient": reviewers[4],
        "message": "Aggregate feedback from all reviewers and give final suggestions on the writing.",
        "max_turns": 1
    }]

    critic.register_nested_chats(review_chats, trigger=writer)

    user_proxy_auto = autogen.UserProxyAgent(
        name="User_Proxy_Auto",
        human_input_mode="NEVER",
        is_termination_msg=lambda x: False,
        code_execution_config={"last_n_messages": 3, "work_dir": "coding", "use_docker": False}
    )

    with st.spinner("🔍 Running AI agents... please wait..."):
        results = autogen.initiate_chats([
            {
                "sender": user_proxy_auto,
                "recipient": financial_assistant,
                "message": financial_tasks[0],
                "summary_method": "reflection_with_llm",
                "summary_args": {
                    "summary_prompt": "Return the stock prices, performance, and financial metrics in JSON. Include figure filenames."
                },
                "carryover": "Proceed to the next step automatically."
            },
            {
                "sender": user_proxy_auto,
                "recipient": researcher,
                "message": research_tasks[0],
                "summary_method": "reflection_with_llm",
                "summary_args": {
                    "summary_prompt": "Return news headlines per stock as JSON. Be precise and exclude vague headlines."
                },
                "carryover": "Proceed to the next step automatically."
            },
            {
                "sender": critic,
                "recipient": writer,
                "message": writing_tasks[0],
                "carryover": "Ensure a table and figure are included in the final report.",
                "max_turns": 2,
                "summary_method": "last_msg"
            },
            {
                "sender": user_proxy_auto,
                "recipient": export_agent,
                "message": exporting_task[0],
                "carryover": "Proceed to the next step automatically."
            }
        ])

    final_report = writer.chat_messages_for_summary(critic)[-1]["content"]
    st.markdown("---")
    st.markdown("### 📈 Final Report")
    if os.path.exists("coding/normalized_prices.png"):
        st.markdown("### 📊 Normalized Price Chart")
        st.image("coding/normalized_prices.png", caption="Normalized Prices", use_column_width=True)
    st.markdown(final_report)
