import faiss
import numpy as np

# Save FAISS index to disk
def save_faiss_index(index, filepath):
    faiss.write_index(index, filepath)

# Load FAISS index from disk
def load_faiss_index(filepath, dimension):
    if os.path.exists(filepath):
        return faiss.read_index(filepath)
    else:
        return faiss.IndexFlatL2(dimension)

# Example usage
dimension = 1536  # OpenAI embedding dimension
faiss_index_path = "faiss_index.idx"
index = load_faiss_index(faiss_index_path, dimension)
