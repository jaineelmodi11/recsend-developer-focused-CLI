<!-- 🎬 Movie Clapperboard Emoji for visual flair -->
# 🎞️ recsend

[![PyPI version](https://img.shields.io/pypi/v/recsend)](https://pypi.org/project/recsend/) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**recsend** is a simple, developer-focused CLI for testing movie recommendation backends via human-friendly YAML/JSON files.  
Simulate likes/dislikes (“swipes”), manage test users in Firebase, and fetch personalized movie suggestions — all from your terminal.

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


## 📄 Quickstart & Usage

### 1. Create a config file (YAML or JSON) under configs/, for example:
```bash
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
```bash
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

## 🧪 Testing
```bash
git clone https://github.com/jaineelmodi11/recsend-developer-focused-CLI.git
cd recsend-developer-focused-CLI
pip install -r requirements.txt
python -m unittest discover tests
```

## 🤝 Contributing

1. Fork the repo
2. Branch: git checkout -b feature/your-feature-name
3. Commit: git commit -m "Add awesome feature"
4, Push: git push origin feature/your-feature-name
5. PR: Open a pull request and describe your changes
6. Please follow existing code style and add tests for new features.



