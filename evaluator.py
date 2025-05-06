from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline

# Step 1: Load embeddings
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Step 2: Create ChromaDB vector store (store job criteria here)
job_criteria = ["5 years of Python experience", "Bachelor’s degree in CS"]
vector_store = Chroma.from_texts(job_criteria, embeddings, collection_name="job_criteria")

# Step 3: Define RAG pipeline
llm = HuggingFacePipeline.from_model_id(
    model_id="google/flan-t5-base",
    task="text2text-generation"
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vector_store.as_retriever(),
    return_source_documents=True
)

def evaluate_resume(resume_text):
    response = qa_chain({"query": f"Score this resume: {resume_text}"})
    return response["result"]