import sqlite3

# Initialize SQLite database for caching embeddings
def init_embedding_cache(db_path="embeddings.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS embeddings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            transaction_text TEXT UNIQUE,
            embedding BLOB
        )
    """)
    conn.commit()
    return conn

# Get or generate embedding for a transaction
def get_cached_embedding(conn, transaction_text):
    cursor = conn.cursor()
    cursor.execute("SELECT embedding FROM embeddings WHERE transaction_text = ?", (transaction_text,))
    result = cursor.fetchone()
    if result:
        return np.frombuffer(result[0], dtype=np.float32)
    else:
        embedding = np.array(get_embedding(transaction_text), dtype=np.float32)
        cursor.execute("INSERT INTO embeddings (transaction_text, embedding) VALUES (?, ?)", 
                       (transaction_text, embedding.tobytes()))
        conn.commit()
        return embedding

# Example usage
conn = init_embedding_cache()
transaction = "Payment of $1000 to Vendor A"
embedding = get_cached_embedding(conn, transaction)
