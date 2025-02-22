from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Your Full Name"  # Replace with your full name
    username = os.getenv("USER") or os.getenv("USERNAME") or os.getlogin() or "Unknown"

    # Convert UTC to IST (Indian Standard Time)
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)

    # Get the top command output (first 10 lines)
    top_output = subprocess.getoutput("top -b -n 1 | head -10")

    # HTML Output
    html_content = f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time.strftime("%Y-%m-%d %H:%M:%S")}</p>
    <pre>{top_output}</pre>
    """
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
