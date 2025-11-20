import os
import pickle
import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sentence_transformers import SentenceTransformer
import faiss

from app.routers import products, outlets, chat
from dependencies import DB_PATH

# Global dictionary to hold ML models
ml_models = {}

# ==============================
# Background loading function
# ==============================
async def load_ml_models():
    try:
        print("Loading SentenceTransformer model...")
        ml_models["embed_model"] = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        print("SentenceTransformer loaded.")

        FAISS_INDEX_PATH = os.path.join("data", "faiss_index.faiss")
        META_PATH = os.path.join("data", "faiss_meta.pkl")

        if os.path.exists(FAISS_INDEX_PATH):
            ml_models["faiss_index"] = faiss.read_index(FAISS_INDEX_PATH)
            print("FAISS index loaded.")

        if os.path.exists(META_PATH):
            with open(META_PATH, "rb") as f:
                ml_models["meta"] = pickle.load(f)
            print("Meta loaded.")

        print("All models loaded successfully.")

    except Exception as e:
        print("Error loading ML models:", e)

# ==============================
# FastAPI app setup
# ==============================
app = FastAPI()

# Attach the ml_models dict to app state
app.state.ml_models = ml_models

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite dev
        "http://localhost:3000",  # alternative dev
        "https://mindhive-rag.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(outlets.router, prefix="/outlets", tags=["Outlets"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])

# ==============================
# Startup event
# ==============================
@app.on_event("startup")
async def startup_event():
    # Load models in the background so the server starts immediately
    asyncio.create_task(load_ml_models())
    print("Server started! ML models are loading in the background...")

# ==============================
# Root endpoint
# ==============================
@app.get("/")
def root():
    return {"message": "ZUS Coffee Agent API is running"}
