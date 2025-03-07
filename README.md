# **Financial Advice System for Stock Trading (RAG-based)**

**Author:** Team PI  
**Date:** 7/3/2025  
**Version:** 1.0  

---

## **1. Introduction**

### **1.1 Problem Statement**

Trading stocks without accurate and timely information is highly risky. Investors often make uninformed decisions, leading to financial losses. The lack of real-time market insights prevents traders from making optimal buy/sell/hold decisions.  

### **1.2 Solution**

This project implements a **Retrieval-Augmented Generation (RAG) system** that automatically collects stock-related news on NVIDIA (NVDA), Tesla (TSLA), and Alphabet (GOOG) from the internet every **6 hours**, processes it, and uses an **LLM (Large Language Model)** to provide financial advice.  

The system consists of:

- **Web Scraper**: Extracts real-time stock news.
- **Database (StockNews Table)**: Stores news temporarily (24 hours max).
- **Vector Store**: Enables efficient news retrieval for queries.
- **LLM-powered Query System**: Generates stock advice (Buy/Sell/Hold).

---

## **2. System Architecture**

### **2.1 Components Overview**

| **Component** | **Description** |
|--------------|----------------|
| **Web Scraper** | Fetches stock-related news every 6 hours |
| **Database (PostgreSQL/SQLite)** | Temporarily stores news articles for retrieval |
| **Vector Store (ChromaDB)** | Embeds text data for efficient similarity search |
| **Query System (LLM-based)** | Provides stock advice using retrieved news and LLM reasoning |

### **2.2 Data Flow**

1. **Scraper** collects real-time stock news every 6 hours.
2. **News is stored** in the database temporarily (expires after 24 hours).
3. **Vector Store** processes the news into embeddings.
4. **User queries** the system for stock advice.
5. **System retrieves relevant news** and generates advice using an LLM.

---

## **3. Implementation Details**

### **3.1 Web Scraper (20 Marks)**

The **web scraper** uses the **Tavily API** to fetch stock-related news every **6 hours** and stores it in a **PostgreSQL/SQLite database**. The scraper:

- Searches for **“\<Stock Symbol> stock news today”**.
- Extracts **headlines, URLs, and raw content**.
- Stores the results in the **StockNews** table.

**Key Features:**
✅ **Automatic Execution:** Runs every **6 hours** via **APScheduler**.  
✅ **Structured Data Storage:** Saves stock symbol, headline, raw content, and timestamp.  
✅ **Data Cleaning:** Removes duplicate/irrelevant news items.  

### **3.2 Temporary Data Storage (15 Marks)**

✅ **Database:** **PostgreSQL** (supports auto-deletion of expired data) or **SQLite**.  
✅ **Data Deletion:** News articles older than **24 hours** are deleted.  
✅ **Schema:** The `StockNews` table contains:  

| **Field** | **Type** | **Description** |
|-----------|---------|----------------|
| `id` | UUID | Unique identifier |
| `symbol` | String | Stock ticker (NVDA, TSLA, GOOG) |
| `headline` | String | News headline |
| `url` | String | Source link |
| `raw_content` | Text | Full news content |
| `timestamp` | Datetime | Time of storage |

---

### **3.3 Vector Store for Text Retrieval (20 Marks)**

✅ **ChromaDB** stores **vector embeddings** of stock news.  
✅ **Enables quick search** for relevant news.  
✅ **Used by the query system** to retrieve relevant news before generating responses.

**Processing Steps:**

1. Extract text from `StockNews`.
2. Convert text into embeddings.
3. Store embeddings in **ChromaDB** for fast retrieval.
4. When a query is made, search for **similar** news articles.

---

### **3.4 Financial Advice Query System (30 Marks)**

✅ **User Query Input:** Users ask whether to buy, sell, or hold a stock.  
✅ **Retrieves Relevant News:** Uses **ChromaDB** to find matching articles.  
✅ **LLM-Based Response:** Uses **GPT-4** to analyze news and generate advice.  

#### **Query Process**

1. **User asks:** _"Should I buy NVDA stock?"_
2. **System searches ChromaDB** for **relevant news**.
3. **LLM analyzes retrieved news** and generates a **confident answer**.

#### **Example Query**

```python
@router.get("/financial-advice")
async def get_financial_advice(query: str):
    retrieved_news = retrieve_relevant_news(query, top_k=5)

    if not retrieved_news:
        return {"financial_advice": "No relevant stock news found."}

    ai_response = generate_financial_advice(query, retrieved_news)
    
    return {"financial_advice": ai_response}
```

---

### **3.5 Deployment & Usability (15 Marks)**

✅ **FastAPI API** with **CORS enabled** for frontend integration.  
✅ **SQLite/PostgreSQL support** for flexible deployment.  
✅ **Endpoints:**

- `/financial-advice?query=<stock question>` → Returns AI-generated financial advice.

---

## **5. Conclusion**

✅ **Fully Functional RAG System** that provides AI-powered **stock trading advice**.  
✅ **Retrieves and processes real-time financial data** every **6 hours**.  
✅ **Deployable via FastAPI**, allowing integration with **frontends and mobile apps**.  

📌 **Next Steps:**  

- Expand coverage to **all stock symbols**.  
- Improve accuracy by adding **more data sources**.  
- **Integrate live stock price trends** for enhanced decision-making.
