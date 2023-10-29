import streamlit as st
from utils import *


PINECONE_ENVIRONMENT="gcp-starter"
PINECONE_INDEX="chatbot"


# Creating Session State Variable
if 'HuggingFace_API_Key' not in st.session_state:
    st.session_state['HuggingFace_API_Key'] =''
if 'Pinecone_API_Key' not in st.session_state:
    st.session_state['Pinecone_API_Key'] =''
if 'Website_URL' not in st.session_state:
    st.session_state['Website_URL'] =''


#Frontend
st.title('AI Search Assistance For Website') 

# Sidebar to capture the API keys & website link
st.sidebar.title("Enter The Following Details")
st.session_state['HuggingFace_API_Key']= st.sidebar.text_input("Enter your HuggingFace API key?",type="password")
st.session_state['Pinecone_API_Key']= st.sidebar.text_input("Enter your Pinecone API key?",type="password")
st.session_state['Website_URL']= st.sidebar.text_input("Enter your website sitemap link?")


load_button = st.sidebar.button("Load data to Pinecone", key="load_button")

# pushing the data to Pinecone
if load_button:
    if all(st.session_state[key] for key in ['HuggingFace_API_Key', 'Pinecone_API_Key', 'Website_URL']):
        if is_valid_url(st.session_state['Website_URL']):
            try:
                # Fetch data from site
                site_data = fetch_website_data(st.session_state['Website_URL'])
                st.write("Data pull done...")

                # Split data into chunks
                data_chunks = split_data(site_data)
                st.write("Splitting data done...")

                # Creating embeddings instance
                embeddings = create_embeddings()
                st.write("Embeddings instance creation done...")

                # Push data to Pinecone
                push_to_pinecone(st.session_state['Pinecone_API_Key'], PINECONE_ENVIRONMENT, PINECONE_INDEX, embeddings, data_chunks)
                st.write("Pushing data to Pinecone done...")
                
                st.sidebar.success("Data pushed to Pinecone successfully!")
            except Exception as e:
                st.sidebar.error(f"An error occurred: {e}")
        else:
            st.sidebar.error("Invalid website URL!")
    else:
        st.sidebar.error("Please provide all required inputs!")



#Captures User Inputs reagrding search & number of search results
prompt = st.text_input('Please enter your query ',key="prompt")  
document_count = st.slider('No.Of links to return 🔗 - (0 LOW || 10 HIGH)', 0, 10, 5,step=1)

search = st.button("Search") 


if search:
    #Proceed only if API keys are provided
    if is_valid_url(st.session_state['Website_URL']):
        try:
            #Creating embeddings instance
            embeddings=create_embeddings()
            st.write("Embeddings instance creation done...")

            #Pull index data from Pinecone
            index=pull_from_pinecone(st.session_state['Pinecone_API_Key'],PINECONE_ENVIRONMENT,PINECONE_INDEX,embeddings)
            st.write("Pinecone index retrieval done...")

            #Fetch relavant documents from Pinecone index
            relavant_docs=get_similar_docs(index,prompt,document_count)
            #st.write(relavant_docs)

            #Displaying search results
            st.success("Please find the search results :")
    
            #Displaying search results in a user friendly manner
            st.write("These are the matching search results list....")
            for document in relavant_docs:
        
                st.write("👉**Result : "+ str(relavant_docs.index(document)+1)+"**")
                st.write("**Info**: "+document.page_content)
                st.write("**Link**: "+ document.metadata['source'])
                
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Invalid website URL!")       
