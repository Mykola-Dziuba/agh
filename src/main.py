from fastapi import FastAPI
from pydantic import BaseModel
from llama_cpp import Llama
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

llm = None

class Prompt(BaseModel):
    prompt: str

@app.post("/generate")
def generate_text(data: Prompt):
    global llm
    if llm is None:
        logger.info("Loading model...")
        llm = Llama(model_path="models/mistral-7b-instruct-v0.1.Q4_0.gguf", n_ctx=256)
        logger.info("Model loaded.")
    logger.info(f"Prompt: {data.prompt}")
    output = llm(data.prompt, max_tokens=32, stop=["</s>"])
    return {"response": output["choices"][0]["text"].strip()}
