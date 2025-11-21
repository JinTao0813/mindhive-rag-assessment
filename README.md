# MindHive - ZUS Coffee AI RAG Agent Assessment

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![Vue 3](https://img.shields.io/badge/Vue-3.5+-brightgreen.svg)](https://vuejs.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-orange.svg)](https://www.langchain.com/)

---

## 👤 Author & Contact Information

**Jin Tao**

- **Email**: jintaoyap@gmail.com
- **GitHub**: [@JinTao0813](https://github.com/JinTao0813)
- **LinkedIn**: [Connect with me](https://www.linkedin.com/in/jin-tao-yap)

---

## 💬 Personal Statement

### To the MindHive Team,

I am pleased to submit this ZUS Coffee AI Agent project, completed to the best of my abilities within a focused **3-day development period** (as evidenced by the commit history).

Throughout this assessment, I have successfully implemented the majority of the functional requirements outlined in the specification, including:

- ✅ Multi-tool ReAct agent with LangChain + LangGraph
- ✅ RAG system with FAISS for product search
- ✅ Text-to-SQL implementation for outlet queries
- ✅ Conversational memory and context management
- ✅ Full-stack integration with Vue 3 frontend
- ✅ Comprehensive testing and documentation

While I acknowledge that I was unable to complete all functional requirements, particularly the production deployment to cloud platforms. I am proud of what has been achieved within the given timeframe. This project has been an invaluable learning experience, marking my first hands-on work with **LangChain and LangGraph technologies**. The challenges encountered and overcome have significantly deepened my understanding of:

- Agent-based architectures and tool orchestration
- Vector databases and semantic search
- Natural language to SQL generation
- Production-ready FastAPI applications
- Modern frontend development with TypeScript

I am grateful for the opportunity to undertake this technical assessment. The experience has not only tested my existing skills but also motivated me to expand my expertise in AI/ML engineering and LLM-based applications.

Thank you for your time and consideration. I look forward to discussing this project and my approach in greater detail.

**Sincerely,**  
**Jin Tao**

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#️-architecture)
- [Tech Stack](#️-tech-stack)
- [Project Structure](#-project-structure)
- [Setup & Installation](#-setup--installation)
- [Implementation Summary](#-implementation-summary)
- [Implementation Details](#-implementation-details)
- [API Documentation](#-api-documentation)
- [Testing](#-testing)
- [Challenges & Solutions](#-challenges--solutions)

---

## 🎯 Overview

Vercel (Frontend): [https://mindhive-rag-assessment.vercel.app/](https://mindhive-rag-assessment.vercel.app/)

This project implements an **intelligent conversational agent** for ZUS Coffee that can:

1. **Answer product questions** using RAG with FAISS vector store
2. **Find outlet locations** using Text-to-SQL with SQLite database
3. **Perform calculations** for pricing and conversions
4. **Maintain conversation context** across multiple turns
5. **Provide a modern chat interface** built with Vue 3 + TypeScript

The system uses **LangChain + LangGraph** for agent orchestration and **Google Gemini 2.5 Flash** as the LLM provider.

---

## ✨ Features

### Backend (FastAPI)

- ✅ **Multi-tool ReAct Agent** - Autonomous decision-making for tool selection
- ✅ **RAG System** - Semantic search over drinkware products using FAISS
- ✅ **Text-to-SQL** - Natural language to SQL query generation for outlet search
- ✅ **Conversation Memory** - Stateful conversations with InMemorySaver
- ✅ **RESTful API** - Clean endpoint design with proper error handling
- ✅ **CORS Support** - Frontend integration ready
- ✅ **Background Loading** - ML models load asynchronously on startup
- ✅ **Data Scraping** - BeautifulSoup scripts for ZUS Coffee website
- ✅ **Data Ingestion** - Pipeline for FAISS index and SQLite database

### Frontend (Vue 3 + TypeScript)

- ✅ **Modern Chat UI** - Clean, responsive chat interface
- ✅ **Real-time Streaming** - Message-by-message conversation flow
- ✅ **Conversation Persistence** - localStorage for session management
- ✅ **Quick Actions** - One-click shortcuts for common queries
- ✅ **Markdown Support** - Rich text rendering with marked.js
- ✅ **Sanitization** - XSS protection with DOMPurify
- ✅ **TypeScript** - Full type safety with interfaces and composables
- ✅ **Keyboard Shortcuts** - Enter to send, Shift+Enter for new line

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Vue 3 Frontend (Vite)                    │
│  ┌───────────┐  ┌───────────┐  ┌──────────────┐           │
│  │ Chat UI   │  │ Quick     │  │ Composables  │           │
│  │ Components│  │ Actions   │  │ (useChat.ts) │           │
│  └─────┬─────┘  └─────┬─────┘  └──────┬───────┘           │
│        └────────────────┴───────────────┘                   │
│                         │                                    │
│                    Axios HTTP Client                        │
└─────────────────────────┼───────────────────────────────────┘
                          │
                          │ POST /chat
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    FastAPI Backend                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              LangGraph ReAct Agent                    │  │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐     │  │
│  │  │ Calculator │  │  Product   │  │   Outlet   │     │  │
│  │  │    Tool    │  │   Search   │  │   Search   │     │  │
│  │  └──────┬─────┘  └──────┬─────┘  └──────┬─────┘     │  │
│  │         │                │                │           │  │
│  │         │          ┌─────▼─────┐    ┌─────▼─────┐   │  │
│  │         │          │   FAISS   │    │  SQLite   │   │  │
│  │         │          │  Vector   │    │  Database │   │  │
│  │         │          │   Store   │    │           │   │  │
│  │         │          └───────────┘    └───────────┘   │  │
│  │         └──────────────┬──────────────────┘         │  │
│  │                        │                             │  │
│  │              Google Gemini 2.5 Flash                │  │
│  │                (LLM Provider)                        │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Agent Flow (ReAct Pattern)

```
User Input
    ↓
[Agent Node] → Analyze query & select tool
    ↓
┌───────────┬──────────────┬──────────────┐
│ calculator│product_search│outlet_search │
└───────────┴──────────────┴──────────────┘
    ↓
Tool Execution → Returns results
    ↓
[Agent Node] → Format natural language response
    ↓
[Memory] → Save to conversation history
    ↓
User Response
```

---

## 🛠️ Tech Stack

### Backend

- **Framework**: FastAPI 0.100+
- **AI/ML**:
  - LangChain + LangGraph (agent orchestration)
  - Google Gemini 2.5 Flash (LLM)
  - Sentence Transformers (embeddings)
  - FAISS (vector search)
- **Database**: SQLite + SQLAlchemy
- **Data Processing**: BeautifulSoup, Pandas
- **Testing**: Pytest, HTTPX

### Frontend

- **Framework**: Vue 3.5 (Composition API)
- **Build Tool**: Vite (Rolldown)
- **Language**: TypeScript 5.9
- **HTTP Client**: Axios
- **Markdown**: Marked.js + DOMPurify
- **Styling**: CSS3 (custom)

### DevOps

- **Version Control**: Git + GitHub
- **Environment**: Python 3.12+ virtual environment
- **Package Manager**: npm (frontend), pip (backend)

---

## 📁 Project Structure

```
mindhive-rag-assessment/
├── backend/
│   ├── app/
│   │   ├── agent/
│   │   │   ├── brain.py              # Agent initialization
│   │   │   └── tools.py              # Tool definitions (calculator, RAG, SQL)
│   │   ├── routers/
│   │   │   ├── chat.py               # /chat endpoint
│   │   │   ├── products.py           # /products endpoint (RAG)
│   │   │   └── outlets.py            # /outlets endpoint (SQL)
│   │   ├── services/
│   │   │   ├── rag_service.py        # FAISS search + summarization
│   │   │   └── sql_service.py        # Text-to-SQL generation
│   │   ├── main.py                   # FastAPI app + startup
│   │   └── schemas.py                # Pydantic models
│   ├── data/
│   │   ├── drinkware.json            # Scraped product data
│   │   ├── outlets.json              # Scraped outlet data
│   │   ├── faiss_index.faiss         # Vector index
│   │   ├── faiss_meta.pkl            # Product metadata
│   │   └── outlets.db                # SQLite database
│   ├── ingestion/
│   │   ├── ingest_products_faiss.py  # Build FAISS index
│   │   └── ingest_outlets_to_sqlite.py # Build SQLite DB
│   ├── scraper/
│   │   ├── scrape_drinkware.py       # Product scraper
│   │   └── scrape_outlets.py         # Outlet scraper
│   ├── tests/
│   │   └── test_phase1.py            # Unit tests
│   ├── dependencies.py               # Shared dependencies (LLM, DB path)
│   ├── requirements.txt              # Python dependencies
│   ├── .env                          # Environment variables
│   ├── README_VISUALIZATION.md       # LangGraph visualization guide
│   └── agent_visualization.mmd       # Mermaid diagram
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatWindow.vue        # Main chat display
│   │   │   ├── Composer.vue          # Message input
│   │   │   ├── AgentMessage.vue      # Agent response bubble
│   │   │   ├── UserMessage.vue       # User message bubble
│   │   │   └── QuickActions.vue      # Action buttons
│   │   ├── composables/
│   │   │   └── useChat.ts            # Chat state management
│   │   ├── services/
│   │   │   └── api.ts                # Backend API client
│   │   ├── types/
│   │   │   └── chat.ts               # TypeScript interfaces
│   │   ├── App.vue                   # Root component
│   │   ├── main.ts                   # Vue app entry
│   │   └── style.css                 # Global styles
│   ├── public/                       # Static assets
│   ├── package.json                  # Node dependencies
│   ├── vite.config.ts                # Vite configuration
│   ├── tsconfig.json                 # TypeScript config
│   ├── SETUP.md                      # Frontend setup guide
│   └── .env.production               # Production environment
│
└── README.md                         # This file
```

---

## 🚀 Setup & Installation

### Prerequisites

- Python 3.12+
- Node.js 18+
- Google API Key (Gemini)

### Backend Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/JinTao0813/mindhive-rag-assessment.git
   cd mindhive-rag-assessment/backend
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv

   # Windows
   .\venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   ```bash
   # Create .env file
   echo "GOOGLE_API_KEY=your_api_key_here" > .env
   ```

5. **Run data ingestion** (if needed)

   ```bash
   # Scrape data (optional, data already included)
   python scraper/scrape_drinkware.py
   python scraper/scrape_outlets.py

   # Build indices
   python ingestion/ingest_products_faiss.py
   python ingestion/ingest_outlets_to_sqlite.py
   ```

6. **Start the server**

   ```bash
   uvicorn app.main:app --reload
   ```

   Server runs at: `http://127.0.0.1:8000`

### Frontend Setup

1. **Navigate to frontend**

   ```bash
   cd ../frontend
   ```

2. **Install dependencies**

   ```bash
   npm install
   ```

3. **Start development server**

   ```bash
   npm run dev
   ```

   Frontend runs at: `http://localhost:5173`

---

### 📊 Implementation Summary

| Phase        | Component              | Status             | Completion | Blocker/Notes                                                                                      |
| ------------ | ---------------------- | ------------------ | ---------- | -------------------------------------------------------------------------------------------------- |
| **Phase 1**  | Agent Foundation       | ✅ Complete        | 100%       | -                                                                                                  |
| **Phase 2**  | RAG System             | ✅ Complete        | 100%       | -                                                                                                  |
| **Phase 3**  | Text-to-SQL            | ✅ Complete        | 100%       | -                                                                                                  |
| **Phase 4**  | Multi-Tool Integration | ✅ Complete        | 100%       | -                                                                                                  |
| **Phase 5**  | Testing & QA           | ✅ Complete        | 100%       | -                                                                                                  |
| **Phase 6A** | Frontend UI            | ✅ Complete        | 100%       | -                                                                                                  |
| **Phase 6B** | Backend Deployment     | ❌ Incomplete      | 0%         | Render "no open ports detected" error; suspected file paths, memory limits, or health check issues |
| **Phase 6C** | Frontend Deployment    | ✅ Complete        | 100%       | Ready to deploy, waiting for backend API endpoint                                                  |
| **Overall**  |                        | ⚠️ Mostly Complete | **87.5%**  | Core functionality complete, deployment troubleshooting needed                                     |

---

## 💡 Implementation Details

### 1. Data Collection & Processing

**Scraping (BeautifulSoup)**

- Scraped ZUS Coffee website for drinkware products and outlet locations
- Extracted: product names, prices, descriptions, images, outlet addresses, hours, facilities
- Stored in JSON format for processing

**Challenges:**

- Website structure variations required flexible parsing
- Handling missing data fields gracefully
- Rate limiting to avoid overwhelming the server

**Solution:**

- Implemented robust error handling and default values
- Added delays between requests
- Stored intermediate results to avoid re-scraping

### 2. RAG System (Products)

**Architecture:**

- **Embeddings**: Sentence Transformers (`all-MiniLM-L6-v2`)
- **Vector Store**: FAISS with L2 distance
- **Chunking**: Product-level granularity (each product = 1 chunk)
- **Retrieval**: Top-k semantic search
- **Summarization**: LLM generates natural language response

**Implementation:**

```python
# Embedding generation
embeddings = embed_model.encode(product_descriptions)

# FAISS index creation
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Search
distances, indices = index.search(query_embedding, k=3)

# LLM summarization
summary = llm.invoke(f"Summarize: {retrieved_docs}")
```

**Challenges:**

- Model loading time (3-5 seconds on startup)
- Balancing retrieval precision vs. recall
- Formatting product data for LLM consumption

**Solutions:**

- Asynchronous background loading (server starts immediately)
- Tuned k=3 for optimal balance
- Structured prompt templates for consistent formatting

### 3. Text-to-SQL (Outlets)

**Architecture:**

- **Database**: SQLite with normalized schema
- **LLM**: Gemini generates SQL from natural language
- **Safety**: Filters non-SELECT queries, limits results
- **Chain**: LangChain's `create_sql_query_chain`

**Implementation:**

```python
# Chain creation
chain = create_sql_query_chain(llm, db)

# Query generation
sql = chain.invoke({"question": user_query})

# Execution with safety checks
if "select" not in sql.lower():
    raise ValueError("Not a SELECT query")
results = db.run(sql)
```

**Challenges:**

- SQL injection risks
- Handling ambiguous queries ("outlets near me")
- Schema awareness by LLM

**Solutions:**

- Strict SELECT-only enforcement
- Clear schema descriptions in prompts
- Example few-shot prompts for common patterns

### 4. Agent Orchestration (LangGraph)

**Architecture:**

- **Pattern**: ReAct (Reasoning + Acting)
- **Tools**: 3 tools (calculator, product_search, outlet_search)
- **Memory**: InMemorySaver for conversation history
- **LLM**: Gemini decides tool selection autonomously

**Implementation:**

```python
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(
    model=llm,
    tools=[calculator, product_search, outlet_search],
    system_prompt=system_message,
    checkpointer=memory
)

# Invoke with session
result = agent.invoke(
    {"messages": [{"role": "user", "content": query}]},
    config={"configurable": {"thread_id": session_id}}
)
```

**Challenges:**

- Tool selection accuracy (agent choosing wrong tool)
- Handling tool errors gracefully
- Memory persistence across server restarts

**Solutions:**

- Clear, descriptive tool docstrings
- Try-catch blocks with fallback responses
- InMemorySaver (noted as limitation - see "Not Implemented")

### 5. Frontend Implementation

**Architecture:**

- **Deployment**: Vercel
- **Composition API**: Reactive state with Vue 3
- **Composables**: Reusable logic in `useChat.ts`
- **TypeScript**: Full type safety
- **localStorage**: Conversation persistence

**Key Features:**

```typescript
// useChat.ts composable
export function useChat() {
  const messages = ref<Message[]>([]);

  // Load from localStorage
  const loadHistory = () => {
    const saved = localStorage.getItem("chat_history");
    if (saved) messages.value = JSON.parse(saved);
  };

  // Send message to backend
  const sendMessage = async (content: string) => {
    const response = await api.post("/chat", {
      message: content,
      session_id: sessionId.value,
    });
    // Update UI
  };

  return { messages, sendMessage, clearHistory };
}
```

**Challenges:**

- Markdown rendering security (XSS risks)
- Managing async API calls and loading states
- Responsive design for mobile

**Solutions:**

- DOMPurify for sanitization + marked.js for rendering
- Reactive loading states with proper error boundaries
- CSS flexbox and media queries

---

## 📡 API Documentation

### Backend Endpoints

#### `POST /chat`

Main agent endpoint for conversational interactions.

**Request:**

```json
{
  "message": "Show me tumblers under RM50",
  "session_id": "user-123"
}
```

**Response:**

```json
{
  "response": "Here are some tumblers under RM50: ..."
}
```

#### `POST /products/`

Direct RAG search over products.

**Request:**

```json
{
  "query": "insulated tumbler",
  "top_k": 3
}
```

**Response:**

```json
{
  "summary": "LLM-generated summary",
  "hits": [
    {
      "id": 1,
      "name": "ZUS Tumbler 500ml",
      "price": "RM 45.00",
      "description": "...",
      "distance": 0.234
    }
  ],
  "top_k": 3
}
```

#### `POST /outlets/`

Direct Text-to-SQL outlet search.

**Request:**

```json
{
  "query": "outlets in Petaling Jaya with WiFi",
  "max_rows": 10
}
```

**Response:**

```json
{
  "sql": "SELECT * FROM outlets WHERE ...",
  "results": [
    {
      "id": 1,
      "name": "ZUS Coffee SS2",
      "address": "...",
      "facilities": "WiFi, Parking"
    }
  ],
  "count": 5
}
```

---

## 🧪 Testing

### Test Coverage

**Backend Tests** (`tests/test_phase1.py`):

- ✅ Root endpoint health check
- ✅ RAG product search (happy path)
- ✅ RAG empty query validation
- ✅ Text-to-SQL outlet search
- ✅ SQL injection attempt blocking

**Run Tests:**

```bash
cd backend
pytest tests/ -v --cov=app
```

**Example Output:**

```
tests/test_phase1.py::test_root PASSED
tests/test_phase1.py::test_products_rag_happy_path PASSED
tests/test_phase1.py::test_outlets_sql_happy_path PASSED
```

---

## 🚧 Challenges & Solutions

As this was my **first project using LangChain and LangGraph**, I encountered several learning curves and technical challenges throughout the development process. Here are the key challenges I faced and how I overcame them:

### Challenge 1: Learning Web Scraping from Scratch

**Problem**: I had no prior experience with web scraping and needed to extract product and outlet data from the ZUS Coffee website.

**Learning Process**:

- Studied BeautifulSoup documentation and tutorials
- Learned how to inspect HTML elements using browser DevTools
- Figured out how to select the proper HTML selectors (classes, IDs, tags) for target data
- Learned to handle edge cases like missing fields and varying page structures

**Solution**:

- Created robust scrapers with error handling for missing data
- Processed scraped data into clean JSON format for downstream use
- Implemented data validation to ensure consistency

### Challenge 2: Understanding Vector Embeddings and FAISS

**Problem**: The concept of embeddings and vector stores was completely new to me.

**Learning Process**:

- Watched YouTube tutorials on semantic search and embeddings
- Used ChatGPT to understand the theory behind vector similarity
- Learned that embeddings capture semantic meaning, not just keyword matching
- Discovered that my dataset was small enough (~50 products) that I didn't need document splitting

**Solution**:

- Successfully implemented FAISS vector store with Sentence Transformers
- Created ingestion pipeline to generate embeddings for all products
- Chose not to use text splitting since my data was already at optimal granularity (product-level)
- Achieved effective semantic search with simple product descriptions

### Challenge 3: SQL Query Cleaning for LLM Outputs

**Problem**: SQLite couldn't parse raw LLM outputs directly. The LLM often returned SQL wrapped in markdown code blocks like ` ```sql SELECT * FROM outlets``` `.

**Learning Process**:

- Learned about regular expressions (regex) for pattern matching
- Understood SQL injection risks and safety measures
- Discovered I needed to sanitize LLM outputs before database execution

**Solution**:

- Implemented regex-based SQL extraction to strip markdown formatting:
  ````python
  # Extract SQL from markdown code blocks
  sql_pattern = r"```sql\s*(.*?)\s*```"
  match = re.search(sql_pattern, llm_output, re.DOTALL)
  if match:
      sql = match.group(1).strip()
  ````
- Added validation to ensure only SELECT queries are executed
- Implemented result limits to prevent data dumps

### Challenge 4: Navigating Deprecated LangChain APIs

**Problem**: ChatGPT often suggested deprecated LangChain functions, causing runtime errors and confusion.

**Learning Process**:

- Realized I needed to read the **official LangChain API documentation** directly
- Learned to identify correct, current function signatures
- Understood key concepts like:
  - `create_react_agent()` for agent creation
  - `InMemorySaver()` for conversation checkpointing
  - Proper message formatting for LangGraph agents

**Solution**:

- Built agent implementation by referencing official docs instead of relying solely on AI assistance
- Correctly configured:

  ```python
  from langgraph.prebuilt import create_react_agent
  from langgraph.checkpoint.memory import InMemorySaver

  agent = create_react_agent(
      model=llm,
      tools=[calculator, product_search, outlet_search],
      checkpointer=InMemorySaver()
  )
  ```

- Learned proper input/output processing for the agent:

  ```python
  # Input format
  input_payload = {"messages": [{"role": "user", "content": query}]}

  # Output extraction
  result = agent.invoke(input_payload, config=config)
  response = result["messages"][-1].content
  ```

### Challenge 5: Backend Deployment Issues on Render

**Problem**: Deployment to Render failed with "no open ports detected" error, despite the application working perfectly locally.

**Investigation**:

- Verified build and start commands were correct
- Ensured `$PORT` environment variable was used in uvicorn
- Checked FAISS-CPU compatibility with platform
- Suspected potential issues:
  1. Relative file paths breaking in production environment
  2. Free-tier memory limitations (~512MB) insufficient for ML models
  3. Model loading taking too long, causing health check timeout
  4. Missing runtime.txt specifying Python version

**Current Status**:

- Application runs flawlessly on localhost
- Deployment remains incomplete due to platform-specific issues
- Created comprehensive deployment guide with troubleshooting steps

**Lessons Learned**:

- Cloud deployment requires different considerations than local development
- File paths must be absolute and environment-aware
- ML model memory footprint matters for tier selection
- Health check timeouts are critical for long-loading services

---

**Built with ❤️ and dedication for the MindHive AI Software Engineer Assessment**
