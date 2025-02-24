# **Deploying a Flask App on Render via GitHub**

## **Overview**
This guide explains how to deploy a **Flask application** to **Render** using **GitHub**. Render provides a **free hosting service** similar to **Heroku**, with **automatic deployments** whenever you push updates to GitHub.

---

## **Prerequisites**
Before deploying, ensure that you have:
- A **GitHub account** with your Flask app pushed to a repository  
- A **Render account** ([Sign Up Here](https://render.com))  
- A **requirements.txt** file listing all dependencies  
- Your Flask app’s main file (e.g., `app.py`)

---

## **Step 1: Prepare Your Flask Application**
Ensure your Flask app is structured like this:

```
/flask-app
│── app.py
│── requirements.txt
│── render.yaml (optional)
│── README.md
```

### **`app.py` (Main Flask Application)**
Your Flask app should be configured to listen on **0.0.0.0** and a dynamic port (`PORT` is assigned by Render):

```python
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Render! Your Flask App is Live!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render provides the PORT variable
    app.run(host='0.0.0.0', port=port)
```

---

### **`requirements.txt` (Dependencies)**
Create a `requirements.txt` file listing all dependencies:

```txt
flask
gunicorn
```

Render uses **Gunicorn** to run the Flask app efficiently in production.

---

### **`render.yaml` (Optional for Automated Deployments)**
If you want **Render to auto-deploy on GitHub updates**, create a `render.yaml` file:

```yaml
services:
  - type: web
    name: flask-app
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn -w 4 -b 0.0.0.0:$PORT app:app
    plan: free
```

---

## **Step 2: Push Your Flask App to GitHub**
Render deploys from **GitHub**, so push your project to a repository:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/your-username/flask-render-deploy.git
git push -u origin main
```

---

## **Step 3: Deploy to Render**
1. **Go to Render Dashboard** → [Render](https://dashboard.render.com/)  
2. **Click "New Web Service"**  
3. **Select "Connect a GitHub Repository"**  
4. **Find and select your Flask repository**  
5. **Configure the service:**
   - **Name:** `flask-app`
   - **Runtime:** `Python`
   - **Build Command:**  
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command:**  
     ```bash
     gunicorn -w 4 -b 0.0.0.0:$PORT app:app
     ```
   - **Instance Plan:** `Free`

6. Click **"Create Web Service"**  
7. Wait for the **deployment to complete**  

---

## **Step 4: Access Your Flask App**
Once deployed, Render provides a **public URL** like:

```
https://flask-app.onrender.com
```

Visit the URL to check if your app is running.

---

## **Step 5: Automate Future Deployments**
Whenever you update your Flask app in **GitHub**, push the changes:

```bash
git add .
git commit -m "Updated Flask app"
git push origin main
```

Render **automatically detects changes** and **redeploys** the updated app.
  

---

## **Conclusion**
 **Deploying Flask on Render is fast and free**—no need to configure EC2 or Heroku.  
 **GitHub integration makes updates automatic**.  
 **Gunicorn ensures production-ready performance**.  

