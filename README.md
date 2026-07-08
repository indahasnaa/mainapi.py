# REST API Personal Profile & Music Playlist

A simple REST API built with **Python Flask** that displays a personal profile and a music playlist through both web pages and JSON API endpoints.

## Features

- Personal profile page
- Music playlist page
- REST API endpoint for personal information
- REST API endpoint for music playlist
- Simple HTML interface using Flask
- JSON responses using Flask `jsonify`

---

## Technologies Used

- Python 3
- Flask

---

## Project Structure

```
project/
│
├── app.py
├── README.md
└── requirements.txt
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/rest-api-profile.git
cd rest-api-profile
```

### 2. Create a virtual environment (optional)

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### 3. Install Flask

```bash
pip install flask
```

or

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python app.py
```

The application will run at:

```
http://localhost:1006
```

---

## Available Routes

### Home Page

```
GET /
```

Displays the homepage with navigation links.

---

### About Page

```
GET /about
```

Displays personal information.

---

### Playlist Page

```
GET /list
```

Displays a list of favorite songs.

---

### API - Personal Profile

```
GET /api/about
```

Example response:

```json
{
  "nama": "Indah Asna Fadila",
  "nim": "2311011008",
  "jurusan": "Teknik Elektro",
  "prodi": "Elektronika",
  "kampus": "Politeknik Negeri Padang",
  "asal": "Bukittinggi",
  "hobi": "Fotografi",
  "cita_cita": "Pengusaha"
}
```

---

### API - Music Playlist

```
GET /api/list
```

Example response:

```json
[
  {
    "judul": "Contoh Judul Lagu 1",
    "artis": "Artis A",
    "genre": "Pop"
  },
  {
    "judul": "Contoh Judul Lagu 2",
    "artis": "Artis B",
    "genre": "Indie"
  },
  {
    "judul": "Contoh Judul Lagu 3",
    "artis": "Artis C",
    "genre": "R&B"
  }
]
```

---

## Personal Information

| Field | Value |
|-------|-------|
| Name | Indah Asna Fadila |
| Student ID | 2311011008 |
| Department | Teknik Elektro |
| Study Program | Elektronika |
| University | Politeknik Negeri Padang |
| Origin | Bukittinggi |
| Hobby | Photography |
| Career Goal | Entrepreneur |

---

## Screenshot

You can add screenshots of:

- Home page
- About page
- Playlist page
- JSON response from `/api/about`
- JSON response from `/api/list`

---

## Future Improvements

- Add CRUD operations (Create, Read, Update, Delete)
- Store data in a database
- User authentication
- RESTful API documentation using Swagger
- Responsive frontend with Bootstrap

---

## License

This project is created for educational purposes.
