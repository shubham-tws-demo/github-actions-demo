from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    """Welcome page — the main route visitors see."""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>GitHub Actions Demo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                text-align: center;
            }
            h1 { font-size: 3rem; }
            p { font-size: 1.2rem; opacity: 0.9; }
        </style>
    </head>
    <body>
        <div>
            <h1>Deployed with GitHub Actions</h1>
        </div>
    </body>
    </html>
    """


@app.route("/health")
def health():
    """Health check endpoint — returns JSON status.

    Used by:
      - 9-deploy-ec2.yml to verify the container is running
      - Monitoring tools to check app availability
    """
    return jsonify({"status": "healthy", "app": "github-actions-demo"})

