import streamlit as st

############## Initialize Agent ###############

# Set title 
st.title("Ask a question to an image ")
# Set header
st.header("Please upload an Image")
# Upload file
file = st.file_uploader("", type=["jpeg" , "jpg" , "png"])
if file:
    # display image
    st.image(file,use_column_width=True)
    # text input
    user_question = st.text_input("Ask a question about your Image")
    
############## compute agent response ###########
    # write agent response 
    if user_question and user_question != "":
        st.write("dummy response")
        
