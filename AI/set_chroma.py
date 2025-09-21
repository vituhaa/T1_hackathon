import chromadb
from openai import OpenAI
import uuid
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

client = OpenAI(api_key="sk-qAVtgeSNioNomveOtt17ZQ", base_url="https://llm.t1v.scibox.tech/v1")
chroma_client = chromadb.PersistentClient(path="./chroma_db")

# Коллекции
kb_collection = chroma_client.get_or_create_collection("knowledge_base")
chat_collection = chroma_client.get_or_create_collection("chat_history")


def embed_text(text: str):
    emb = client.embeddings.create(
        model="bge-m3",
        input=[text],
    )
    return emb.data[0].embedding

def reset_collection():
    """Очистка коллекции полностью"""
    print("Очистка коллекции Chroma")
    # Получаем все id
    all_docs = kb_collection.get()
    all_ids = all_docs.get("ids", [])
    print(all_ids)

    if all_ids:
        kb_collection.delete(ids=all_ids)
        print(f"Удалено {len(all_ids)} элементов")
    else:
        print("Коллекция пустая")



def add_item_to_chroma(item_id, text, metadata):
    embedding = embed_text(text)
    kb_collection.add(
        ids=[item_id],
        documents=[text],
        embeddings=[embedding],
        metadatas=[metadata]
    )

def print_collection():
    print(kb_collection.get())

def query_chroma(query: str, n: int = 5):
    query_emb = embed_text(query)
    results = kb_collection.query(
        query_embeddings=[query_emb],
        n_results=n
    )

    out = []
    for i in range(len(results["ids"][0])):
        out.append({
            "id": results["ids"][0][i],
            "document": results["documents"][0][i],
            "metadata": results["metadatas"][0][i],
            "score": 1 - results["distances"][0][i]
        })
    return out


# --- Сохранение сообщений чата ---
def add_chat_message(employee_id, role, message):
    embedding = embed_text(message)
    chat_collection.add(
        ids=[str(uuid.uuid4())],
        documents=[message],
        metadatas={"employee_id": employee_id, "role": role},
        embeddings=[embedding]
    )

# --- Получение истории чата ---
def get_chat_history(employee_id, limit=10):
    results = chat_collection.get(where={"employee_id": employee_id})
    history = list(zip(results["metadatas"], results["documents"]))
    # Берём последние N в порядке добавления
    return [{"role": meta["role"], "content": doc} for meta, doc in history[-limit:]]

def semantic_search(query: str, top_k: int = 3):
    """Поиск по positions и courses."""
    embedding = embed_text(query)

    res = kb_collection.query(query_embeddings=[embedding], n_results=top_k)

    matches = []
    for doc, meta, score in zip(
        res["documents"][0],
        res["metadatas"][0],
        res["distances"][0]
    ):
        matches.append({
            "id": meta.get("id"),
            "type": meta.get("type"),
            "title": meta.get("title"),
            "score": round(float(score), 3),
            "content": doc,
            "metadata": meta
        })

    return matches

# --- Общение с ИИ ---



