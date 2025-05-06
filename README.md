# recsend

**recsend** is a developer-focused CLI tool designed to interact with movie recommendation systems via structured YAML/JSON files. It allows developers and testers to simulate swipes, manage test users, and fetch personalized recommendations — all from the command line.

---

## 🚀 Features

- 🔄 Simulate user **swipes** (like/dislike) to test interaction behavior.
- 🎯 Get **movie recommendations** based on user profile or simulated activity.
- 🔐 Manage and push **test users to Firebase** for backend testing.
- 📁 Use simple **YAML or JSON files** to define request payloads.
- 🌈 Optional **colorized output** for improved readability.
- 📤 Clean output separation — responses to `stdout`, metadata to `stderr`.

---

## 📦 Installation

Make sure Python 3.8+ is installed.

```bash
pip install recsend
```

## 📄 Usage Examples

### 🔄 Simulate a Swipe

```bash
recsend swipe -f configs/swipe.yml
```

### 🎯 Fetch Recommendations
```bash
recsend recommend -f configs/recommend.yml
```

### 👤 Push a Test User to Firebase
```bash
recsend push-user -f configs/user.yml
```

### 🌈 Enable Colorized Output
```bash
recsend push-user -f configs/user.yml
```

### 🧪 Redirect Output and Headers
```bash
recsend recommend -f configs/recommend.yml > response.json 2> metadata.log
```


## 📁 Sample Configuration (recommend.yml)
```bash
# configs/recommend.yml
url: https://api.example.com/recommendations
method: GET

# HTTP headers
headers:
  Authorization: Bearer YOUR_API_TOKEN

# Query parameters
params:
  user_id: test_user_123

# Optional settings
timeout: 10       # seconds
retries: 2

```
