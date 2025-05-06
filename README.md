<!-- 🎬 Movie Clapperboard Emoji for visual flair -->
# 🎞️ RecSend

[![PyPI version](https://img.shields.io/pypi/v/recsend)](https://pypi.org/project/recsend/) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Struggling with curl’s endless flags and manual scripting? **RecSend** simplifies recommendation‑system testing into one human‑friendly config file and a single command. Simulate likes/dislikes (“swipes”), manage test users in Firebase, and fetch personalized movie suggestions — all from your terminal.

---

## 🚀 Features

- 🔄 **Swipe Simulation**  
  Send like/dislike events to your API to validate recommendation logic.  
- 🎯 **Fetch Recommendations**  
  Retrieve curated movie lists for any test user.  
- 👤 **Test-User Management**  
  Create or update Firebase test users on the fly.  
- 📁 **YAML / JSON Configs**  
  Define endpoint, method, headers, body, params, timeouts, retries, etc.  
- 🌈 **Colorized Output**  
  Use `-c` to pretty-print JSON with ANSI colors.  
- 📤 **Clean I/O**  
  Bodies → `stdout`; headers & status → `stderr` (ideal for shell scripting).

---

## 📦 Installation

Requires **Python 3.8+**

```bash
pip install recsend
```
**or**
```bash
pip3 install recsend
```
---
## 📄 Quickstart & Usage

### 1. Create a config file (YAML or JSON) under configs/, for example:
```yaml
# configs/recommend.yml
url: https://api.example.com/recommendations
method: GET
headers:
  Authorization: Bearer YOUR_API_TOKEN
params:
  user_id: test_user_123
timeout: 10   # seconds
retries: 2
```

### 2. Run any command:
```yaml
# Simulate a swipe
recsend swipe -f configs/swipe.yml

# Fetch recommendations
recsend recommend -f configs/recommend.yml

# Push or update a test user
recsend push-user -f configs/user.yml

# Enable colorized output
recsend recommend -f configs/recommend.yml -c

# Redirect body to file and metadata to log
recsend recommend -f configs/recommend.yml \
  > response.json 2> metadata.log
```
---
## 🧪 Sample Requests

Below are example YAML files for all common HTTP methods.  
Use them with any subcommand, for example:

```bash
recsend recommend -f configs/get_anime.yml       # GET example
recsend swipe     -f configs/create_todo.yml     # POST example
recsend swipe     -f configs/update_todo.yml     # PUT example
recsend swipe     -f configs/delete_todo.yml     # DELETE example

## 🤝 Contributing

1. Fork the repo
2. Branch: git checkout -b feature/your-feature-name
3. Commit: git commit -m "Add awesome feature"
4, Push: git push origin feature/your-feature-name
5. PR: Open a pull request and describe your changes
6. Please follow existing code style and add tests for new features.
```

### 1. GET (XML response)
```yaml
# configs/get_anime.yml
url: https://cdn.animenewsnetwork.com/encyclopedia/api.xml?anime=4658
method: GET

params:
  offset: 2
  limit: 100

headers:
  Accept: text/xml
  Accept-Language: en

timeout: 5   # seconds
```

```bash
recsend recommend -f configs/get_anime.yml
```

### 2. File Download
```yaml
# configs/download_pythonlearn.yml
url: http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf
method: GET
timeout: 10
```

```bash
recsend recommend -f configs/download_pythonlearn.yml > pythonlearn.pdf
```

### 3. POST (create)
```yaml
# configs/create_todo.yml
url: https://jsonplaceholder.typicode.com/todos/
method: POST

headers:
  Content-Type: application/json
  Authorization: Basic bXl1c2VybmFtZTpteXBhc3N3b3Jk

data:
  title: walk the dog
  completed: false

timeout: 5
```

```bash
recsend swipe -f configs/create_todo.yml
```


### 4. PUT (update)
```yaml
# configs/update_todo.yml
url: https://jsonplaceholder.typicode.com/todos/1
method: PUT

headers:
  Content-Type: application/json

data:
  title: walk the dog
  completed: true

timeout: 5
```

```bash
recsend swipe -f configs/update_todo.yml
```


### 5. DELETE
```yaml
# configs/delete_todo.yml
url: https://jsonplaceholder.typicode.com/todos/1
method: DELETE

timeout: 5
```

```bash
recsend swipe -f configs/delete_todo.yml
```


### Complete Template
```yaml
# configs/sample_request.yml

# REQUIRED
method: GET            # GET, OPTIONS, HEAD, POST, PUT, PATCH or DELETE
url: https://api.example.com/resource

# Optional URL parameters
params:
  page: 1
  per_page: 20

# Optional body for POST/PUT/PATCH
data:
  user:
    name: john
    age: 22
    hobbies:
      - running
      - reading

# OR raw JSON body
# data: |
#   {"user":{"name":"john","age":22,"hobbies":["running","reading"]}}

# Optional headers
headers:
  Content-Type: application/json
  Authorization: Bearer YOUR_TOKEN

# Optional cookies
cookies:
  session_id: abc123

# Request settings
timeout: 3.5          # seconds
allow_redirects: true
retries: 2

# SSL/TLS settings
verify: true          # or path to CA bundle
cert:                 # client certificate
  - path/to/client.crt
  - path/to/client.key

# Optional proxy settings
proxies:
  http:  http://10.0.0.1:3128
  https: https://10.0.0.1:1080
```

---

## 🛠️ Development Setup

Clone this repository and install the required packages:

```bash
git clone https://github.com/jaineelmodi11/recsend-developer-focused-CLI.git
cd recsend-developer-focused-CLI
pip3 install -r requirements.txt
```
---
## 📜 Meta
**Author: Jaineel Modi**

**Repository home: https://github.com/jaineelmodi11/recsend-developer-focused-CLI**

---
## 🤝 Contributing
1. Fork the repository
2. Create your feature branch
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch
   ```bash
   git push origin feature/your-feature-name
   ```
   
5. Open a Pull Request and describe your work
