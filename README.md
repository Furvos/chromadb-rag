# Sistema RAG com ChromaDB, HyDE e Re-ranking | v1.0

## Sobre a aplicação

Esta aplicação implementa um pipeline de Retrieval-Augmented Generation (RAG) voltado para documentos técnicos de Direito Constitucional. O sistema utiliza o ChromaDB como banco vetorial com índice HNSW para recuperação eficiente de documentos semanticamente relevantes.

A aplicação aplica a técnica HyDE (Hypothetical Document Embeddings), onde uma query coloquial do usuário é transformada por um LLM em um documento técnico hipotético. Esse documento é utilizado como âncora semântica para melhorar a recuperação vetorial.

Após a recuperação inicial dos documentos via HNSW, um modelo Cross-Encoder realiza um re-ranking semântico profundo para selecionar os documentos mais relevantes que seriam posteriormente enviados ao contexto de um LLM.

---

# Sobre os parâmetros M e ef_construction

(`M` é representado como `max_neighbors` nos parâmetros do ChromaDB.)

No HNSW, os hiperparâmetros `M` e `ef_construction` aumentam o consumo de memória RAM porque o algoritmo armazena um grafo de conexões entre vetores. O parâmetro `M` possui maior impacto, pois define quantos vizinhos cada vetor mantém em memória, enquanto `ef_construction` aumenta o custo e a complexidade da construção do índice.

Em comparação, uma busca K-Nearest Neighbors (KNN) exata geralmente consome menos RAM estruturalmente, pois armazena apenas os vetores, mas realiza buscas muito mais lentas por comparar a consulta com praticamente toda a base de dados.

---

# Sobre o ChromaDB

A função de embedding padrão do ChromaDB utiliza o modelo `Sentence Transformers all-MiniLM-L6-v2` para criar embeddings vetoriais automaticamente.

Neste projeto, o ChromaDB é responsável por:
- armazenar os embeddings;
- gerenciar o índice vetorial HNSW;
- realizar buscas semânticas por similaridade de cosseno;
- recuperar os documentos mais próximos semanticamente.

---

# Pipeline implementado

1. Inserção dos fragmentos técnicos de Direito Constitucional no banco vetorial.
2. Geração de embeddings automáticos via ChromaDB.
3. Criação explícita de índice HNSW.
4. Transformação da query usando HyDE.
5. Recuperação Top-10 via Similaridade de Cosseno.
6. Re-ranking com Cross-Encoder.
7. Seleção dos Top-3 documentos finais.

**Este arquivo README.md foi parcialmente gerado usando IA generativa.**