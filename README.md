# Blog Title Generator API

## Overview
This project is a Django application that provides an API for generating creative blog titles based on the content provided by users. It utilizes the Groq API for natural language processing to suggest three potential titles. Additionally, the application demonstrates how to integrate FastAPI for handling requests.

## Features
- Accepts blog content via a POST request.
- Returns three suggested titles based on the input content.
- Built with Django for the web framework and integrated with the Groq API for NLP.
- Demonstrates how to use FastAPI as an alternative for API development.

## Technologies Used
- Django
- FastAPI
- LangChain
- Groq API
- Python

## Installation
```bash
pip install -r reuirements.txt
```

## FastAPI Implementation
The project also includes a FastAPI implementation for generating blog titles. This part can be run independently of the Django application.

Running the FastAPI Server
To run the FastAPI server, you need to use Uvicorn. Use the following command:

```bash
uvicorn main:app --reload
```

## Running the Django Server
To run the Django server, use the following command:

```bash
python manage.py runserver
```
## Using Postman
To use Postman for sending requests by using both FastAPI and Django:

- Open Postman.
- Set the request type to POST.
- Enter the URL for FastAPI server: http://127.0.0.1:8000/generate-titles/
- Enter the URL for Django server: http://127.0.0.1:8000/api/generate-titles/
- In the body, select "raw" and choose "JSON" from the dropdown. Enter your content:
```bash
{
  "content": "Your blog content here."
}
```
