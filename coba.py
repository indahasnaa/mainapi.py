from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

data_diri = {
    "nama": "Indah Asna Fadila",
    "nim": "2311011008",
    "jurusan": "Teknik Elektro",
    "prodi": "Elektronika",
    "kampus": "Politeknik Negeri Padang",
    "asal": "Bukittinggi",
    "hobi": "Fotografi",
    "cita_cita": "Pengusaha"
}

playlist_musik = [
    {"judul": "Contoh Judul Lagu 1", "artis": "Artis A", "genre": "Pop"},
    {"judul": "Contoh Judul Lagu 2", "artis": "Artis B", "genre": "Indie"},
    {"judul": "Contoh Judul Lagu 3", "artis": "Artis C", "genre": "R&B"},
]

BASE_STYLE = """
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
        font-family: 'Poppins', sans-serif;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 40px 20px;
        background:
            linear-gradient(rgba(10, 15, 20, 0.55), rgba(10, 15, 20, 0.65)),
            url('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1600&q=80');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        color: #f5f5f5;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
        max-width: 480px;
        width: 100%;
    }
    h1 {
        font-weight: 700;
        font-size: 22px;
        margin-bottom: 8px;
        background: linear-gradient(90deg, #7fffd4, #00d4ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    p.subtitle { font-weight: 300; font-size: 14px; color: #e0e0e0; margin-bottom: 25px; }
    .nav { display: flex; justify-content: center; gap: 15px; margin-top: 25px; flex-wrap: wrap; }
    .nav a {
        color: #fff; text-decoration: none; font-size: 14px; font-weight: 500;
        padding: 10px 20px; border-radius: 30px; border: 1px solid rgba(255,255,255,0.25);
        background: rgba(255,255,255,0.08); transition: 0.3s;
    }
    .nav a i { margin-right: 6px; }
    .nav a:hover {
        background: linear-gradient(90deg, #00d4ff, #2ecc71);
        border-color: transparent; transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(0, 212, 255, 0.4);
    }
    .item {
        text-align: left;
        background: rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 14px 18px;
        margin-bottom: 10px;
        border-left: 3px solid #7fffd4;
    }
    .item .judul { font-weight: 500; font-size: 15px; }
    .item .artis { font-size: 12px; color: #d8d8d8; }
    .info-row { text-align: left; margin: 10px 0; font-size: 14px; }
    .info-row span { color: #7fffd4; font-weight: 500; }
</style>
"""

@app.route("/")
def home():
    html = f"""
    <!DOCTYPE html><html lang="id"><head><meta charset="UTF-8">
    <title>REST API - Indah Asna Fadila</title>{BASE_STYLE}</head>
    <body>
        <div class="card">
            <i class="fa-solid fa-code" style="font-size:40px;color:#7fffd4;margin-bottom:15px;"></i>
            <h1>REST API by Indah Asna Fadila</h1>
            <p class="subtitle">Politeknik Negeri Padang &bull; Teknik Elektro</p>
            <div class="nav">
                <a href="/about"><i class="fa-solid fa-user"></i>About</a>
                <a href="/list"><i class="fa-solid fa-music"></i>Playlist</a>
            </div>
        </div>
    </body></html>
    """
    return render_template_string(html)

@app.route("/about")
def about():
    rows = "".join(f'<div class="info-row"><span>{k.replace("_"," ").title()}:</span> {v}</div>' for k, v in data_diri.items())
    html = f"""
    <!DOCTYPE html><html lang="id"><head><meta charset="UTF-8">
    <title>About - Indah Asna Fadila</title>{BASE_STYLE}</head>
    <body>
        <div class="card">
            <i class="fa-solid fa-user" style="font-size:36px;color:#7fffd4;margin-bottom:15px;"></i>
            <h1>Tentang Saya</h1>
            {rows}
            <div class="nav">
                <a href="/"><i class="fa-solid fa-house"></i>Home</a>
                <a href="/list"><i class="fa-solid fa-music"></i>Playlist</a>
            </div>
        </div>
    </body></html>
    """
    return render_template_string(html)

@app.route("/list")
def list_page():
    items = "".join(
        f'<div class="item"><div class="judul">{p["judul"]}</div><div class="artis">{p["artis"]} &bull; {p["genre"]}</div></div>'
        for p in playlist_musik
    )
    html = f"""
    <!DOCTYPE html><html lang="id"><head><meta charset="UTF-8">
    <title>Playlist - Indah Asna Fadila</title>{BASE_STYLE}</head>
    <body>
        <div class="card">
            <i class="fa-solid fa-music" style="font-size:36px;color:#7fffd4;margin-bottom:15px;"></i>
            <h1>Playlist Musik</h1>
            <p class="subtitle">Lagu favorit</p>
            {items}
            <div class="nav">
                <a href="/"><i class="fa-solid fa-house"></i>Home</a>
                <a href="/about"><i class="fa-solid fa-user"></i>About</a>
            </div>
        </div>
    </body></html>
    """
    return render_template_string(html)

@app.route("/api/about")
def api_about():
    return jsonify(data_diri)

@app.route("/api/list")
def api_list():
    return jsonify(playlist_musik)

if __name__ == "__main__":
    app.run(port=1006, debug=True)