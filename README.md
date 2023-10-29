# AI Search Assistance For Website

This project creates a web application to provide search assistance for websites. It fetches data from a given website, processes it, and enables a search feature to find relevant documents from the website.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7 or later.
- Streamlit.
- Pinecone.
- Sentence Transformers.
- langchain.
- Requests.
- asyncio.

### Installation

1. Clone the GitHub repository to your local machine:

   git clone <repository-url>

2. Navigate to the project directory:

   cd <repository-directory>

3. Install the required Python libraries:

   pip install streamlit pinecone-langchain sentence-transformers requests asyncio

## Usage

1. Run the Streamlit application:

   streamlit run app.py

2. Open your web browser and navigate to `localhost:8501` to access the application.

3. In the application, enter the required API keys and website URL, then click "Load data to Pinecone" to process the website data.

4. Enter a search query and specify the number of links to return, then click "Search" to retrieve and display relevant documents from the website.

5. You can use this sample sitemap for testing purposes
    https://www.grammarly.com/sitemap.xml

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.


Please replace `<repository-url>` and `<repository-directory>` with the actual URL and directory name of your GitHub repository. Note that the `pip install` command assumes that all the necessary libraries are available on PyPi, and the command to run the Streamlit app assumes your script is named `app.py`. Adjust these details to match your actual project setup.
