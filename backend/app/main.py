from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sentence_transformers import SentenceTransformer
import faiss
import pickle
import os

from app.routers import products, outlets, chat
from dependencies import DB_PATH

# Global state dictionary to hold ML models
ml_models = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        print("Loading FAISS Index and Embeddings...")

        FAISS_INDEX_PATH = os.path.join("data", "faiss_index.faiss")
        META_PATH = os.path.join("data", "faiss_meta.pkl")
        
        ml_models["embed_model"] = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        print("Model loaded.")

        if os.path.exists(FAISS_INDEX_PATH):
            ml_models["faiss_index"] = faiss.read_index(FAISS_INDEX_PATH)
            print("FAISS loaded.")

        if os.path.exists(META_PATH):
            with open(META_PATH, "rb") as f:
                ml_models["meta"] = pickle.load(f)
            print("META loaded.")

    except Exception as e:
        print("Startup error:", e)

    yield
    ml_models.clear()


app = FastAPI(lifespan=lifespan)

# CORS Configuration for Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite development server
        "http://localhost:3000",  # Alternative dev port
        "https://mindhive-rag.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.state.ml_models = ml_models


app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(outlets.router, prefix="/outlets", tags=["Outlets"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])

@app.get("/")
def root():
    return {"message": "ZUS Coffee Agent API is running"}

