
# Plant Disease Identifier

A microservices-based application to identify plant diseases based on uploaded images.

## Features
- Upload a plant image through the frontend.
- Backend identifies diseases and provides symptoms and treatments.
- Docker Compose orchestrates the services.

## Services
1. **Frontend**: HTML/JS app served via Nginx.
2. **Backend**: Flask API for processing and database interaction.
3. **Database**: PostgreSQL database with disease data.

## Setup Instructions
1. Ensure Docker and Docker Compose are installed.
2. Clone the repository or unzip the provided folder.
3. Navigate to the project directory.
4. Run `docker-compose up --build`.
5. Access the frontend at `http://localhost:8080`.
6. Upload a plant image to test the functionality.

## Notes
- The backend assumes the plant name is the file name (without extension).
- Preloaded plant disease data is included in the database.

## Endpoints
- `POST /identify`: Upload an image to identify plant disease.

## Cleanup
Run `docker-compose down` to stop and remove containers.

---
Developed by Ammara
