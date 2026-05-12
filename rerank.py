from sentence_transformers import CrossEncoder
from chroma import collection
from llm_document import gerar_documento_hipotetico

cross_encoder = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)

query_original = "quais são os direitos fundamentais?"

documento_hyde = gerar_documento_hipotetico(
    query_original
)

results = collection.query(
    query_texts=[documento_hyde],
    n_results=10
)

documentos = results["documents"][0]

print("\n== TOP 10 RECUPERADOS ==")

for i, doc in enumerate(documentos, start=1):
    print(f"\n{i}. {doc}")

pares = [
    (query_original, documento)
    for documento in documentos
]

scores = cross_encoder.predict(pares)

documentos_rankeados = sorted(
    zip(documentos, scores),
    key=lambda x: x[1],
    reverse=True
)

print("\n==============================")
print("== TOP 3 APÓS RE-RANKING ==")
print("==============================")

for i, (doc, score) in enumerate(
    documentos_rankeados[:3],
    start=1
):
    print(f"\n{i}. SCORE: {score:.4f}")
    print(doc)