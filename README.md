# QuestGen

> A powerful document processing and intelligent question generation system powered by LLMs

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688)](https://fastapi.tiangolo.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13%2B-336791)](https://www.postgresql.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Database Migrations](#database-migrations)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**QuestGen** is an intelligent document processing platform that leverages Large Language Models (LLMs) to automatically generate questions and answers from uploaded documents. The system extracts text from various document formats (PDF, DOCX, TXT), chunks the content intelligently, and uses AI to generate comprehensive question sets with answers.

This backend service provides RESTful APIs for document management, text extraction, and intelligent content generation.

---

## Features

- 📄 **Multi-Format Document Support**: Process PDF, DOCX, and text files
- 🤖 **Intelligent Question Generation**: Leverage Gemini or Groq LLMs for question creation
- 💾 **Persistent Storage**: PostgreSQL database for reliable data management
- 🔄 **Async Processing**: Built with async/await for high performance
- 📋 **Project Management**: Organize documents and questions by project
- 🔀 **Flexible LLM Integration**: Switch between multiple LLM providers
- 🗄️ **Database Migrations**: Alembic for version-controlled schema changes
- 🐳 **Docker Support**: Ready-to-deploy containerized setup
- 📚 **Comprehensive API**: RESTful endpoints for all operations

---

## Tech Stack

### Backend
- **Framework**: FastAPI (async Python web framework)
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Async Driver**: asyncpg
- **Schema Management**: Alembic
- **LLM Integration**: LangChain, Google GenAI, Groq

### Key Dependencies
- `fastapi` - Web framework
- `sqlalchemy` - ORM
- `asyncpg` - Async PostgreSQL driver
- `alembic` - Database migrations
- `pydantic` - Data validation
- `langchain` - LLM framework
- `google-genai` - Google Gemini API
- `groq` - Groq API
- `pypdf` - PDF processing
- `python-docx` - Word document processing
- `uvicorn` - ASGI server

### Infrastructure
- **Containerization**: Docker & Docker Compose
- **Database**: PostgreSQL 17

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python**: 3.8 or higher
- **PostgreSQL**: 13 or higher
- **Docker & Docker Compose**: (optional, for containerized deployment)
- **Git**: For version control

### Required API Keys

- **Google Gemini API Key** (optional): For question generation using Gemini
- **Groq API Key** (optional): For question generation using Groq

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Mariam123Hamada/QuestGen.git
cd QuestGen
```

### 2. Create a Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

#### Option A: Using Docker Compose (Recommended)

```bash
docker compose up -d
```

This will start a PostgreSQL container configured with the environment variables.

#### Option B: Local PostgreSQL

Ensure PostgreSQL is running and accessible on your system.

---

## Configuration

### Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# Database Configuration
DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/questgen_db
POSTGRES_USER=questgen_user
POSTGRES_PASSWORD=your_secure_password
POSTGRES_DB=questgen_db
POSTGRES_PORT=5432

# LLM Configuration
LLM_PROVIDER=groq  # Options: 'groq' or 'gemini'
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=mixtral-8x7b-32768
GEMINI_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-pro
```

### Key Configuration Points

- **LLM_PROVIDER**: Choose your default LLM (`groq` or `gemini`)
- **DATABASE_URL**: Connection string for PostgreSQL with async driver
- **API Keys**: Obtain from respective provider dashboards

---

## Running the Application

### 1. Run Database Migrations

```bash
# Create new migration (if needed)
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head
```

### 2. Start the FastAPI Server

```bash
# Development server with auto-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Production server
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

The API will be available at `http://localhost:8000`

### 3. Access API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## Project Structure

```
QuestGen/
├── alembic/                    # Database migrations
│   ├── versions/              # Migration scripts
│   ├── env.py                 # Migration environment configuration
│   └── alembic.ini            # Migration settings
├── controllers/               # API controllers
│   └── constarins.py          # Validation constraints
├── db/                        # Database configuration
│   ├── base.py               # SQLAlchemy base model
│   ├── database.py           # Database engine setup
│   └── session.py            # Session factory
├── models/                    # SQLAlchemy ORM models
│   ├── answer.py             # Answer model
│   ├── document.py           # Document model
│   ├── project.py            # Project model
│   └── question.py           # Question model
├── repositories/              # Data access layer
│   ├── answer_repository.py
│   ├── document_repository.py
│   ├── project_repository.py
│   └── question_repository.py
├── routes/                    # API route handlers
│   └── upload.py             # Upload endpoints
├── schema/                    # Pydantic request/response schemas
│   ├── answer.py
│   ├── document.py
│   ├── project.py
│   └── question.py
├── services/                  # Business logic
│   ├── api_service/          # API-related services
│   │   └── upload_service.py
│   ├── db_service/           # Database services
│   │   ├── answer_service.py
│   │   ├── document_service.py
│   │   ├── project_service.py
│   │   └── question_service.py
│   ├── extractors/           # Document extraction services
│   │   ├── text_extraction_service.py
│   │   └── TypesFactory/
│   │       ├── base_extractor.py
│   │       ├── docs_extractor.py
│   │       ├── pdf_extractor.py
│   │       ├── text_extractor.py
│   │       └── extractor_factory.py
│   └── llm_service/          # LLM integration services
│       ├── chunk_service.py
│       └── generators/
│           ├── base_generator.py
│           ├── gemini_generator.py
│           ├── groq_generator.py
│           └── generator_factory.py
├── dependencies/              # Dependency injection
│   └── services.py
├── utils/                     # Utility functions
│   ├── config.py             # Configuration management
│   └── helper.py             # Helper functions
├── uploads/                   # Temporary file storage
├── main.py                   # FastAPI application entry point
├── requirements.txt          # Python dependencies
├── docker-compose.yaml       # Docker Compose configuration
├── alembic.ini              # Alembic configuration
├── LICENSE                  # License file
└── README.md                # This file
```

---

## API Documentation

### Core Endpoints

#### Health Check
```http
GET /
```

Response:
```json
{
  "Hello": "Hello World From the main route"
}
```

#### Upload Document
```http
POST /upload
```

Upload a document and trigger text extraction and question generation.

**Parameters:**
- `file` (multipart/form-data): Document file (PDF, DOCX, or TXT)
- `project_id` (optional): Associated project ID

**Response:**
```json
{
  "document_id": "uuid",
  "filename": "document.pdf",
  "status": "processing",
  "extracted_text_length": 5000
}
```

For complete API documentation, visit http://localhost:8000/docs

---

## Database Migrations

### Creating a Migration

To create a new database migration:

```bash
alembic revision --autogenerate -m "Add new column to questions table"
```

This creates a new migration file in `alembic/versions/`.

### Applying Migrations

```bash
# Apply all pending migrations
alembic upgrade head

# Revert to previous migration
alembic downgrade -1

# Show migration history
alembic history
```

### Migration Files

All migrations are version-controlled in `alembic/versions/`. Current migrations include:

- Initial table creation
- Column additions and updates
- Schema refinements

---

## Development Workflow

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Changes

- Add or modify code
- Run tests (if available)
- Follow code style guidelines

### 3. Commit and Push

```bash
git add .
git commit -m "Add your commit message"
git push origin feature/your-feature-name
```

### 4. Create a Pull Request

Submit a PR with a clear description of changes.

---

## Troubleshooting

### Database Connection Issues

If you encounter connection errors:

1. Verify PostgreSQL is running: `docker compose ps`
2. Check environment variables in `.env`
3. Ensure the database URL is correct: `postgresql+asyncpg://user:password@host:port/db`

### LLM API Issues

- Verify API keys are set correctly in `.env`
- Check API rate limits and quota
- Ensure network connectivity to API endpoints

### Port Already in Use

If port 8000 is in use:

```bash
uvicorn main:app --port 8001 --reload
```

---

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Support

For issues, questions, or suggestions, please open an issue on the repository.

---

## Author

**Mariam Abdelsalam**

Connect with me on LinkedIn: [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/mariam-abdelsalam-979843335)

---

**Happy Coding!🚀**