# Serverless Image Processing

This project demonstrates a serverless architecture for image processing using Flask, PostgreSQL, AWS Lambda, and Docker. The application allows users to upload images, process them (resize and apply filters), and deploy them using AWS Lambda. Docker is used for local testing and development.

## Features
- Image upload
- Image processing (resize and filter)
- Serverless deployment with AWS Lambda
- Docker for local development and testing


## Setup and Installation

### Prerequisites
- Python 3.9+
- Docker
- Docker Compose
- AWS CLI
- AWS SAM CLI

### Virtual Environment Setup

1. **Create a Virtual Environment:**
    ```sh
    python -m venv venv
    ```

2. **Activate the Virtual Environment:**
    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```

3. **Install Dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Local Development

### Using Docker

1. **Build and Run the Docker Containers:**
    ```sh
    docker-compose up --build
    ```

2. **Access the Application:**
    Open your browser and go to `http://localhost:5000`.

### Without Docker

1. **Run the Application:**
    ```sh
    flask run
    ```

## Testing

1. **Run Tests:**
    ```sh
    python -m unittest discover -s tests
    ```

## Deployment

### AWS Lambda Deployment

1. **Ensure you have the AWS CLI and AWS SAM CLI installed and configured.**
2. **Deploy the application to AWS Lambda using AWS SAM CLI:**
    ```sh
    sam build
    sam deploy --guided
    ```

## File Descriptions

- `app/__init__.py`: Initializes the Flask application and sets up the database.
- `app/routes.py`: Contains the routes for image upload and processing.
- `app/models.py`: Defines the database models.
- `app/utils.py`: Contains utility functions for image processing.
- `tests/test_routes.py`: Contains unit tests for the routes.
- `tests/test_utils.py`: Contains unit tests for utility functions.
- `Dockerfile`: Dockerfile for building the Docker image.
- `docker-compose.yml`: Docker Compose file for setting up the development environment.
- `requirements.txt`: List of Python dependencies.
- `config.py`: Configuration file for the Flask application.
- `handler.py`: AWS Lambda handler for the application.
- `.gitignore`: Git ignore file.
- `README.md`: This readme file.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask
- PostgreSQL
- AWS Lambda
- Docker

## Contact

If you have any questions, feel free to contact me at [your-email@example.com].

