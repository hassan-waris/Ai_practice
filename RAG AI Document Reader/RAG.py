#!/usr/bin/env python3

import streamlit as st
import pdfplumber
import faiss
import openai
import numpy as np
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

st.set_page_config(page_title="Legal Document Q&A")
st.title("Legal Document Q&A Assistant")

openai.api_key = st.secrets.get("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY")  # Removed for Github


uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file:
	with pdfplumber.open(uploaded_file) as pdf:
		text = ""
		for page in pdf.pages:
			content = page.extract_text()
			if content:
				text += content
				
	st.success("Document successfully loaded!")
	
	splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
	chunks = splitter.split_text(text)
	st.info(f"Document split into {len(chunks)} text chunks for processing.")
	
	st.write("Creating embeddings... (this may take a moment)")
	embed_model = OpenAIEmbeddings(model="text-embedding-3-small")
	
	# Generate embeddings for all chunks
	vectors = [embed_model.embed_query(chunk) for chunk in chunks]
	dim = len(vectors[0])
	
	# Create and populate FAISS index
	index = faiss.IndexFlatL2(dim)
	index.add(np.array(vectors).astype("float32"))
	
	st.success("Embeddings stored in FAISS index.")
	
	question = st.text_input("Ask a question about the uploaded document:")
	
	if question:
		st.write("Searching for relevant information...")
		q_vector = embed_model.embed_query(question)
		
		# Search top 3 relevant chunks
		D, I = index.search(np.array([q_vector]).astype("float32"), k=3)
		retrieved_chunks = [chunks[i] for i in I[0]]
		
		# Combine retrieved chunks as context
		context = "\n\n".join(retrieved_chunks)

		prompt = f"""
		You are a helpful legal assistant. Use the context below to answer the question.

		Context:
		{context}

		Question: {question}
		Answer:
		"""
		
		with st.spinner("Generating answer..."):
			response = openai.ChatCompletion.create(
				model="gpt-4-turbo",
				messages=[{"role": "user", "content": prompt}],
			)
			
		answer = response["choices"][0]["message"]["content"]
		

		st.subheader("Answer")
		st.write(answer)
		
		# Optional: show the top retrieved text snippets
		with st.expander("View retrieved text context"):
			st.write(context)
			