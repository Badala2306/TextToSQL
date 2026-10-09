
import streamlit as st
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from database import create_database, execute_query

load_dotenv()
create_database()

st.set_page_config(page_title="Text-to-SQL AI", page_icon="🗄️")

st.title("🗄️ Text-to-SQL AI")
st.write("Ask questions about your e-commerce data.")

# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0
)

parser = StrOutputParser()

schema = """
customers(customer_id, customer_name, city, state, signup_date)
products(product_id, product_name, category, unit_price)
orders(order_id, customer_id, order_date, order_status, payment_method)
order_items(order_item_id, order_id, product_id, quantity, selling_price)

Relationships:
customers.customer_id = orders.customer_id
orders.order_id = order_items.order_id
products.product_id = order_items.product_id

Revenue = quantity * selling_price
"""

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for messages in st.session_state.messages:
    role = messages["role"]
    content = messages["content"]

    with st.chat_message(role):
        st.markdown(content)

        if messages.get("sql"):
            st.code(messages["sql"], language="sql")

# User input
question = st.chat_input("Ask a question about your sales data...")

if question:
    # Store and display user question
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    # Generate SQL query
    sql_prompt = f"""
    Generate one SQLite SQL query for this question.

    Schema:
    {schema}

    Question: {question}

    Return only the SQL query without Markdown.
    """

    sql_response = llm.invoke(sql_prompt)
    sql_query = parser.invoke(sql_response).strip()
    sql_query = sql_query.replace("```sql", "").replace("```", "").strip()

    # Execute SQL query
    result = execute_query(sql_query)

    # Generate natural-language answer
    answer_prompt = f"""
    Answer the user's question in simple natural language.

    Question: {question}
    SQL result: {result}
    If the result is in numbers like some value you are calcultion then use the currency symbol Rs in front of the number. If the result is empty then say "No data found for this query.".
    Use only the given result. Do not invent facts or numbers.
    """

    answer_response = llm.invoke(answer_prompt)
    answer = parser.invoke(answer_response)

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown("**Generated SQL**")
        st.code(sql_query, language="sql")

        st.markdown("**Answer**")
        st.markdown(answer)

    # Store answer and SQL in history
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "sql": sql_query
    })
