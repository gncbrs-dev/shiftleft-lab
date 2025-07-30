from flask import Flask, request

app = Flask(__name__)

# 🚨 Hardcoded secret (Semgrep + Gitleaks detect)
API_KEY = "sk_live_1234567890abcdef"

SECRET = "ghp_abcdef1234567890"


@app.route("/search")
def search():
    query = request.args.get("q")
    # 🚨 SQL injection (Semgrep detect)
    return f"SELECT * FROM users WHERE name = '{query}'"

@app.route("/")
def index():
    return "Hello insecure world!"

if __name__ == "__main__":
    app.run(debug=True)

