from llm_document import gerar_documento_hipotetico
from collection_config import collection

collection.add(
    ids=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", 
         "11", "12", "13", "14", "15", "16", "17", "18", "19", 
         "20", "21", "22", "23", "24", "25"],
    documents=[
        "A Constituição Federal estabelece que a separação dos poderes constitui cláusula pétrea, vedando propostas de emenda constitucional tendentes à sua abolição.",
        "O controle concentrado de constitucionalidade pode ser exercido pelo Supremo Tribunal Federal mediante ação direta de inconstitucionalidade.",
        "Os direitos e garantias fundamentais possuem aplicabilidade imediata, conforme disposto no artigo 5º da Constituição.",
        "A intervenção federal nos estados somente poderá ocorrer nas hipóteses taxativamente previstas pela Constituição Federal.",
        "O mandado de segurança é cabível para proteger direito líquido e certo não amparado por habeas corpus ou habeas data.",
        "A competência legislativa concorrente permite à União editar normas gerais e aos estados suplementá-las.",
        "O princípio federativo assegura autonomia política, administrativa e financeira aos entes federativos.",
        "A ação declaratória de constitucionalidade exige demonstração de controvérsia judicial relevante sobre a norma impugnada.",
        "Os tratados internacionais de direitos humanos aprovados em rito qualificado possuem equivalência às emendas constitucionais.",
        "A administração pública deve obedecer aos princípios da legalidade, impessoalidade, moralidade, publicidade e eficiência.",
        "O poder constituinte originário caracteriza-se por ser inicial, ilimitado juridicamente e autônomo.",
        "O habeas data destina-se ao conhecimento ou retificação de informações relativas à pessoa do impetrante constantes em bancos de dados públicos.",
        "A soberania popular é exercida pelo sufrágio universal e pelo voto direto e secreto, com valor igual para todos.",
        "O controle difuso de constitucionalidade permite que qualquer juiz ou tribunal afaste a aplicação de norma incompatível com a Constituição.",
        "A iniciativa de lei complementar sobre organização do Ministério Público da União é privativa do Procurador-Geral da República.",
        "O estado de defesa pode ser decretado pelo Presidente da República para preservar ou restabelecer a ordem pública ameaçada.",
        "As comissões parlamentares de inquérito possuem poderes de investigação próprios das autoridades judiciais.",
        "A competência para julgar o Presidente da República nos crimes de responsabilidade pertence ao Senado Federal.",
        "O princípio da dignidade da pessoa humana constitui fundamento da República Federativa do Brasil.",
        "A arguição de descumprimento de preceito fundamental destina-se a evitar ou reparar lesão a preceito fundamental decorrente de ato do poder público.",
        "O processo legislativo constitucional compreende iniciativa, discussão, votação, sanção, veto e promulgação.",
        "A imunidade parlamentar material protege deputados e senadores por opiniões, palavras e votos no exercício do mandato.",
        "A desapropriação por necessidade pública depende de prévia e justa indenização em dinheiro, salvo exceções constitucionais.",
        "O princípio da proporcionalidade é utilizado na interpretação constitucional para solução de conflitos entre direitos fundamentais.",
        "A competência originária do Supremo Tribunal Federal inclui o julgamento de ações contra atos do Congresso Nacional em determinadas hipóteses."
    ],
    metadatas=[{"tema": "direito constitucional"}] * 25
)

print("== Collection do chromadb: ==")
print(collection.get())

documento_hyde = gerar_documento_hipotetico(
    "quais são os direitos fundamentais?"
)

print("== Documento gerado por LLM: ==")
print(documento_hyde)

results = collection.query(
    query_texts=[documento_hyde],
    n_results=10
)

print("== Resultados da consulta: ==")
print(results)