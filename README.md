# ikli

**ikli** is a fast, scalable URL shortener built with FastAPI and MongoDB. It features a sleek web interface and robust RESTful API for effortless link redirection, ensuring reliable and efficient URL management.

---

## Features

- **URL Shortening:** Quickly generate unique, short URLs.
- **Web Interface:** User-friendly form for entering URLs and receiving shortened links.
- **API Endpoints:** RESTful API for programmatic access to URL shortening and redirection.
- **NoSQL Backend:** Uses MongoDB for flexible, schema-less data storage.

---

## Tech Stack

- **Backend:** FastAPI
- **Database:** MongoDB (via Motor)
- **Templating:** Jinja2
- **Styling:** Bootstrap 5

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/drichorino/link-apex.git
   cd link-apex
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Linux/macOS:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Rename the `.env.template` file to `.env` in the project root. Modify the following content:
   ```
   MONGO_URL=mongodb://localhost:27017
   MONGO_DB=link_apex_db
   ```

5. **Ensure MongoDB is running locally:**

   Install MongoDB locally or run it via Docker:
   ```bash
   docker run --name mongodb -d -p 27017:27017 mongo:latest
   ```

---

## Usage

- **Run the Application:**
  ```bash
  uvicorn app.main:app --reload
  ```

- **Web Interface:**

  Open your browser and visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to shorten URLs using the form.

- **API Endpoints:**

  Access API endpoints under [http://127.0.0.1:8000/v1/api](http://127.0.0.1:8000/v1/api) for programmatic access.

- **Redirection:**

  Use the generated short URL (e.g., [http://127.0.0.1:8000/{short_code}](http://127.0.0.1:8000/{short_code})) to be redirected to the original URL.

---

## License

This project is open source and available under the [MIT License](LICENSE).
