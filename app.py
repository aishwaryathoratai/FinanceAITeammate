import time
import streamlit as st
from graph import graph

st.set_page_config(
    page_title="Enterprise Finance AI",
    layout="wide"
)
st.title("Enterprise Finance AI Teammate")
st.markdown(
    """
Ask questions related to:

- 💰 Finance
- 📄 Company Policies
- 🛠 IT Support

The Supervisor Agent automatically routes your question
to the appropriate expert agent.
"""
)
question = st.text_area(
    "Ask your question",
    height=120,
    placeholder="Example: How can I claim travel reimbursement?"
)

# Submit Button

if st.button("Generate Answer", use_container_width=True):

    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            start = time.time()
            result = graph.invoke(
                {
                    "question": question
                }

            )
            end = time.time()

        st.subheader("Selected Agent")
        st.success(result["route"].capitalize())
        st.subheader("Answer")
        st.write(result["answer"])
        st.subheader("Sources")
        if result["sources"]:
            for source in result["sources"]:
                st.write(f"• {source}")
        else:
            st.info("No source available.")
        st.subheader("Response Time")

        st.write(f"{end-start:.2f} seconds")