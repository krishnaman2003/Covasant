"""
Question-16:
Sharing of content 
@app.route("/updatefortoday", methods=['GET','POST'])#http://localhost:5000/updatefortoday
@app.route("/share", methods=['GET'])#http://localhost:5000/share
@app.route("/clearnotepadtxt", methods=['GET'])#http://localhost:5000/clearnotepadtxt
"""

from flask import Flask, request
import os

app = Flask(__name__)
NOTEPAD_FILE = os.path.join(app.root_path, "notepad.txt")

@app.route("/updatefortoday", methods=['GET', 'POST'])
def update_notepad():
    if request.method == 'POST':
        content = request.form.get('content', '')
        with open(NOTEPAD_FILE, 'w') as f:
            f.write(content)
        return "Notepad updated. <a href='/share'>View Notepad</a>"
    else:
        return """
        <html><head><title>Update Notepad</title></head>
        <body>
            <h2>Update Today's Notepad</h2>
            <form method="post">
                <textarea name="content" rows="10" cols="50"></textarea><br><br>
                <input type="submit" value="Update Notepad">
            </form>
        </body></html>
        """

@app.route("/share", methods=['GET'])
def share_notepad():
    content = "Notepad is empty or file not found."
    if os.path.exists(NOTEPAD_FILE):
         with open(NOTEPAD_FILE, 'r') as f:
            file_content = f.read()
            if file_content.strip():
                 content = file_content
            else:
                 content = "Notepad is currently empty."
    return f"""
    <html><head><title>Shared Notepad</title></head>
    <body>
        <h2>Current Notepad Content</h2>
        <pre>{content}</pre>
        <br>
        <a href="/updatefortoday">Update Notepad</a>
        <br>
        <a href="/clearnotepadtxt">Clear Notepad</a>
    </body></html>
    """

@app.route("/clearnotepadtxt", methods=['GET'])
def clear_notepad():
    with open(NOTEPAD_FILE, 'w') as f:
        pass 
    return "Notepad cleared. <a href='/share'>View Notepad</a>"

if __name__ == '__main__':
    app.run()
