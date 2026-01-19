# Lies as a Service (LaaS)

**Base URL:** `https://lies-as-a-service.onrender.com/lie`

**Example(Category-Wise):** `https://lies-as-a-service.onrender.com/lie?category=tech`

Ever needed a creative excuse to escape a meeting, explain a missed deadline, or justify working from home? This API generates humorous, believable workplace lies and excuses for developers and professionals.

Built with FastAPI, rate limiting, and Docker support.

## API Usage

**Method:** GET  
**Rate Limit:** 120 requests per minute per IP

### 🔄 Example Request

```bash
curl https://lies-as-a-service.onrender.com/lie
```

### ✅ Example Response

```json
{
  "lie": "I accidentally pushed to main and blamed it on a junior developer",
  "category": "tech"
}
```

Use it in apps, bots, landing pages, Slack integrations, or wherever you need a creative excuse!

## Endpoints

### Get a Random Lie
```bash
GET /lie
```

Returns a random lie from any category.

### Get a Lie by Category
```bash
GET /lie?category=tech
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

**Example:**
```bash
curl https://lies-as-a-service.onrender.com/lie?category=tech
```

### Get All Categories
```bash
GET /categories
```

**Response:**
```json
{
  "categories": ["sick", "meeting", "deadline", "remote", "technical", "manager", "tech", "random"],
  "total": 8
}
```

### Health Check
```bash
GET /health
```

## 🛠️ Self-Hosting

Want to run it yourself? It's lightweight and simple.

### 1. Clone this repository

```bash
git clone https://github.com/MohammadSameer19/lies-as-a-service
cd lies-as-a-service
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the server

```bash
python main.py
```

The API will be live at `http://localhost:8000`

You can also change the port using an environment variable:

```bash
uvicorn main:app --host 0.0.0.0 --port 3000
```

## 📁 Project Structure

```
lies-as-a-service/
├── main.py                       # FastAPI application
├── responses.py                  # Lie database
├── requirements.txt              # Python dependencies
├── Dockerfile                    # Docker configuration
├── docker-compose.yml            # Docker Compose
├── render.yaml                   # Render deployment config
├── .devcontainer/
│   └── devcontainer.json         # GitHub Codespaces config
├── .github/workflows/
│   └── docker-build.yml          # CI/CD workflow
├── LICENSE                       # MIT License
├── CONTRIBUTING.md               # Contribution guidelines
└── README.md                     # This file
```



## 🎯 Use Cases

- **Slack/Discord Bots**: Fun excuse generator commands
- **Team Humor**: Lighten up standup meetings
- **Chatbots**: Add workplace humor to your bots
- **API Testing**: Practice API integration
- **Icebreakers**: Share funny excuses with your team
- **Satire Projects**: Workplace comedy applications

## 📝 Adding More Lies

Edit the `LIES` dictionary in `responses.py`:

```python
LIES = {
    "sick": [
        "Your new excuse here",
        # ... more excuses
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

Check out [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## ⚓ Devcontainer

If you open this repo in GitHub Codespaces, it will automatically use `.devcontainer.json` to set up your environment. If you open it in VS Code, it will ask you if you want to reopen it in a container.


---

Want to use lies-as-a-service in your own project? Check the usage section in this README and start generating excuses like a pro.

## 👤 Author

Created with humor and FastAPI

## 📄 License

MIT — do whatever, just don't actually use these excuses at work.

---

**Remember:** These are jokes! Don't actually tell your manager that Mercury is in retrograde. 
