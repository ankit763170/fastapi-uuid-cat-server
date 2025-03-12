# FastAPI UUID Cat Server

This repository contains a FastAPI server that supports the following routes:

1. **GET /uuid**:  
   Generates and returns a unique version 4 UUID.

2. **GET /async-uuid**:  
   Generates and returns a unique version 4 UUID after a non-blocking delay of 3 seconds.

3. **GET /cat**:  
   Retrieves a random cat image from [cataas.com](https://cataas.com/cat) and returns it to the client.

## Requirements

- Python 3.9 or higher
- [Poetry](https://python-poetry.org/) for dependency management
- Docker (optional, for containerization)

## Getting Started

### Running Locally Using Poetry

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/backend-api-task-v2.git
   cd backend-api-task-v2
