import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("📄 Document question answering")
st.write(
    "Upload a document below and ask a question about it – GPT will answer! "
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
)

# Create an OpenAI client.
client = OpenAI(
    organization='org-afBVpclGmm1MWlPQ9jGi2B7g',
    project='proj_uWYBke7AJKPkQkLj3ZLRYGmn',
    api_key='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'
)

# Let the user upload a file via `st.file_uploader`.
uploaded_file = st.file_uploader(
    "Upload a document (.txt or .md)", type=("txt", "md")
)

# Ask the user for a question via `st.text_area`.
question = st.text_area(
    "Now ask a question about the document!",
    placeholder="Can you give me a short summary?",
    disabled=not uploaded_file,
)

if uploaded_file and question:

    # Process the uploaded file and question.
    document = uploaded_file.read().decode()
    messages = [
        {
            "role": "user",
            "content": f"Here's a document: {document} \n\n---\n\n {question}",
        }
    ]

    # Generate an answer using the OpenAI API.
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True,
    )

        # Stream the response to the app using `st.write_stream`.
    st.write_stream(stream)
