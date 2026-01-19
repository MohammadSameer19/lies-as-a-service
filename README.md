# 🤥 Lies as a Service (LaaS)

**Base URL:** `https://your-deployed-url.onrender.com`

Ever needed a creative excuse to escape a meeting, explain a missed deadline, or justify working from home? This API generates humorous, believable workplace lies and excuses for developers and professionals.

Built with FastAPI, rate limiting, and Docker support.

## 🚀 API Usage

**Method:** GET  
**Rate Limit:** 120 requests per minute per IP

### 🔄 Endpoints

#### Get a Random Lie
```bash
GET /api/lie
```

### 🔄 Example Request

```bash
curl https://your-deployed-url.onrender.com/api/lie
```

### ✅ Example Response

```json
{
  "lie": "I accidentally pushed to main and blamed it on a junior developer",
  "category": "tech"
}
```

#### Get a Lie by Category
```bash
GET /api/lie?category=tech
```

**Available Categories:**
- `sick` - Creative sick day excuses
- `meeting` - Reasons to skip meetings
- `deadline` - Explanations for missed deadlines
- `remote` - Justifications for remote work
- `technical` - Tech-related blockers and issues
- `manager` - Excuses for your manager
- `tech` - Developer lies and confessions
- `random` - Everyday lies people tell

**Example Request:**
```bash
curl https://your-deployed-url.onrender.com/api/lie?category=tech
```

#### Get All Categories
```bash
GET /api/categories
```

**Example Response:**
```json
{
  "categories": ["sick", "meeting", "deadline", "remote", "technical", "manager", "tech", "random"],
  "total": 8
}
```

#### Health Check
```bash
GET /health
```

Use it in apps, bots, landing pages, Slack integrations, or wherever you need a creative excuse!

## 🛠️ Installation & Setup

### Local Development

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd lies-as-a-service
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the server**
```bash
python main.py
```

The API will be available at `http://localhost:8000`

Interactive API docs at `http://localhost:8000/` (Swagger UI)

### 🐳 Docker Deployment

#### Using Docker
```bash
docker build -t lies-as-a-service .
docker run -p 8000:8000 lies-as-a-service
```

#### Using Docker Compose
```bash
docker-compose up -d
```

To stop:
```bash
docker-compose down
```

## 📁 Project Structure

```
lies-as-a-service/
├── .github/
│   └── workflows/
│       └── docker-build.yml      # CI/CD workflow
├── .devcontainer/
│   └── devcontainer.json         # GitHub Codespaces config
├── main.py                       # FastAPI application
├── responses.py                  # Lie database
├── requirements.txt              # Python dependencies
├── Dockerfile                    # Docker configuration
├── docker-compose.yml            # Docker Compose configuration
├── render.yaml                   # Render deployment config
├── .dockerignore                 # Docker ignore file
├── .gitignore                    # Git ignore file
├── LICENSE                       # MIT License
├── CONTRIBUTING.md               # Contribution guidelines
└── README.md                     # This file
```

## 🎯 Use Cases

- **Slack/Discord Bots**: Fun excuse generator commands
- **Team Humor**: Lighten up standup meetings
- **Excuse Generator Apps**: Build excuse-generating tools
- **Chatbots**: Add workplace humor to your bots
- **API Testing**: Practice API integration
- **Icebreakers**: Share funny excuses with your team
- **Satire Projects**: Workplace comedy applications

## 🌐 Deploy to Render

1. **Fork/Push this repository to GitHub**

2. **Create a new Web Service on Render:**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Render will auto-detect the `render.yaml` configuration

3. **Deploy:**
   - Click "Create Web Service"
   - Render will automatically build and deploy using Docker
   - Your API will be live at `https://your-app-name.onrender.com`

**Note:** Free tier on Render may spin down after inactivity. First request might take 30-60 seconds.

## 🔧 Configuration

### Change Port

**Local:**
```bash
uvicorn main:app --host 0.0.0.0 --port 3000
```

**Docker:**
```bash
docker run -p 3000:8000 -e PORT=8000 lies-as-a-service
```

### Rate Limiting

Default: 120 requests/minute per IP

To modify, edit the `@limiter.limit()` decorator in `main.py`:
```python
@limiter.limit("60/minute")  # Change to 60 requests per minute
```

## 📝 Adding More Lies

Edit the `LIES` dictionary in `main.py`:

```python
LIES = {
    "sick": [
        "Your new excuse here",
        # ... more excuses
    ],
    "tech": [
        "Your clever tech humor here",
        # ... more witty remarks
    ],
    # Add new category
    "your_category": [
        "Excuse 1",
        "Excuse 2",
    ]
}
```

## 🤝 Contributing

Feel free to:
- Add more workplace excuses to existing categories
- Create new excuse categories
- Improve the API
- Fix bugs
- Enhance documentation

## ⚓ GitHub Codespaces

Open this repo in GitHub Codespaces for instant development environment:
- Automatically configured with Python 3.11
- All dependencies pre-installed
- Port 8000 auto-forwarded
- Just open and run `python main.py`

## ⚠️ Disclaimer

This API is for **entertainment and humor purposes only**. All excuses are intentionally absurd and should not be used as actual excuses in professional settings. Use responsibly and at your own risk!

## 📄 License

MIT License - Use it however you want, just don't actually use these excuses at work!

## 👤 Author

Built with humor and FastAPI by developers who've heard (and used) every excuse in the book

---

**Remember:** These are jokes! Don't actually tell your manager that Mercury is in retrograde. 🤥
