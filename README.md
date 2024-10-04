# Blog Title Generator API

## Overview
This project is a FastAPI application that provides an API for generating creative blog titles based on the content provided by users. It utilizes the Groq API for natural language processing to suggest three potential titles.

## Features
- Accepts blog content via a POST request.
- Returns three suggested titles based on the input content.
- Built with FastAPI for the web framework and integrated with the Groq API for NLP.

## Technologies Used
- FastAPI
- LangChain
- Groq API
- Python

## Create Virtual Environment
```bash
python -m venv myenv
```
"myenv" is the name of the virtual environment.

```bash
myenv\Scripts\activate
```

## Installation
Install the packages after activating the Virtual Environment.
```bash
pip install -r reuirements.txt
```

## FastAPI Implementation
The project includes a FastAPI implementation for generating blog titles. 

Running the FastAPI Server
To run the FastAPI server, you need to use Uvicorn. Use the following command:

```bash
uvicorn main:app --reload
```
## Using Postman for FastAPI
To use Postman for sending requests by using FastAPI:

- Open Postman.
- Set the request type to POST.
- Enter the URL for FastAPI server: http://127.0.0.1:8000/generate-titles/
- In the "body", select "form-data" and "content" in the Key and "Enter your blog content" in the Value.
