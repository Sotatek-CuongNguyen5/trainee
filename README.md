# Image Text Processing API

This API allows you to insert text on images and manage text data. It provides endpoints to generate JWT tokens for authentication, insert text on images, manage text data, and display images using unique IDs.

## Table of Contents
- [Installation](#installation)
- [API Documentation](#api-documentation)
- [Authentication](#authentication)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. **Create a virtual environment and activate it**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory with the following content:
     ```
     SECRET_KEY=your_secret_key
     ALGORITHM=HS256
     HOST=0.0.0.0
     PORT=3000
     ```

5. **Run the application**:
   ```sh
   ./run.sh
   ```

## API Documentation

### Authentication

#### Generate Token

**Endpoint**: `/token`

**Method**: `POST`

**Request Body**:
- `username`: String (default: "admin")
- `password`: String (default: "admin")

**Response**:
- `access_token`: String
- `token_type`: String

### Image Text Processing

#### Insert Text on Image

**Endpoint**: `/insert_text_on_image/`

**Method**: `POST`

**Authentication**: Required

**Request Body**:
- `image`: File (required)
- `text`: String (required)
- `text_color`: String (optional, default: "black")
- `font_size_ratio`: Float (optional, default: 0.1)

**Response**:
- `base64_image`: String
- `image_url`: String

#### Insert Text on Image (Version 2)

**Endpoint**: `/insert_text_on_image_v2/`

**Method**: `POST`

**Authentication**: Required

**Request Body**:
- `image`: File (required)
- `text1`: String (required)
- `text2`: String (required)
- `text1_color`: String (optional, default: "green")
- `text2_color`: String (optional, default: "red")
- `font_size_ratio`: Float (optional, default: 0.1)

**Response**:
- `base64_image`: String
- `image_url`: String

### Text Management

#### Get Texts

**Endpoint**: `/texts/`

**Method**: `GET`

**Authentication**: Required

**Response**:
- List of texts

#### Check if Text Exists

**Endpoint**: `/text_exists/`

**Method**: `GET`

**Authentication**: Required

**Query Parameter**:
- `text`: String (required)

**Response**:
- `exists`: Boolean
- `text`: String

### Image Display

#### Display Image

**Endpoint**: `/images/{image_id}`

**Method**: `GET`

**Path Parameter**:
- `image_id`: String (required)

**Response**:
- Image file

## Authentication

All endpoints require JWT authentication. Include the JWT token in the Authorization header as a Bearer token.

Example:
```
Authorization: Bearer your_jwt_token
```

## Usage

1. **Generate a JWT token** by sending a POST request to `/token` with the default credentials (`username: admin`, `password: admin`).
2. **Use the generated token** to access the protected endpoints by including it in the `Authorization` header.
3. **Insert text on an image** by sending a POST request to `/insert_text_on_image/` or `/insert_text_on_image_v2/` with the required parameters.
4. **View the processed image** by accessing the URL provided in the response of the insert text API.

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.