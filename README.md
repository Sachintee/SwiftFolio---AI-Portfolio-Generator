# SwiftFolio - Dynamic Portfolio Generator

SwiftFolio is a full-stack web application that generates and manages dynamic portfolios from your resume, GitHub, LeetCode, and HackerRank data.

## What's New

- Portfolio editing for bio, about, skills, and projects
- Portfolio translation with multi-language support
- Resume download from the generated portfolio page
- HTML export for a full portfolio report
- Demo portfolio flow that loads the latest created portfolio
- Stable export payloads for downstream use

## Features

- 📄 **Resume Upload** - Upload your PDF resume and let the backend extract skills, experience, and education
- 🖥️ **GitHub Integration** - Showcase repositories, contributions, and coding activity
- 🏆 **Coding Stats** - Display LeetCode and HackerRank problem-solving stats
- 🤖 **AI Generation** - Generate portfolio copy such as about text, bio, and project descriptions
- ✏️ **Portfolio Editing** - Update bio, about, skills, projects, and language after generation
- 🌍 **Translation** - Translate portfolio content into many supported languages
- ⬇️ **Resume Download** - Download the original uploaded resume from the portfolio page
- 📦 **Export** - Export the full portfolio as an HTML report
- 🔄 **Dynamic Updates** - Refresh portfolio data when connected accounts change

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | FastAPI (Python) |
| Frontend | Next.js 14 (React) + TypeScript |
| Database | MongoDB |
| Styling | Tailwind CSS |
| Deployment | Docker |

## Quick Start

### Prerequisites

- Docker & Docker Compose
- Node.js 20+ (for local development)
- Python 3.11+ (for local backend development)
- MongoDB (local or Atlas)

### Using Docker Compose

1. Clone the repository
2. Create `.env` file from `.env.example`:

```env
# Backend
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=swiftfolio
OPENAI_API_KEY=sk-your-api-key-here
GITHUB_TOKEN=ghp_your_token_here
```

3. Run the application:

```bash
docker-compose up --build -d
```

4. Access the application:
   - Frontend:http://localhost:3000 
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

### Local Development

#### Backend

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload
```

#### Frontend

```bash
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

## API Endpoints

### Generate Portfolio
```bash
POST /api/portfolio/generate
{
  "username": "yourname",
  "resume": "base64_encoded_pdf",  // optional
  "github_username": "yourgithub",  // optional
  "leetcode_username": "yourleetcode",  // optional
  "hackerrank_username": "yourhackerrank"  // optional
}
```

### Get Portfolio
```bash
GET /api/portfolio/{username}
```

### Latest Portfolio
```bash
GET /api/portfolio/latest
```

### Available Languages
```bash
GET /api/portfolio/languages/available
```

### Edit Portfolio
```bash
PATCH /api/portfolio/{username}/edit
```

### Translate Portfolio
```bash
POST /api/portfolio/{username}/translate/{language}
```

### Download Resume
```bash
GET /api/portfolio/{username}/resume/download
```

### Export HTML
```bash
GET /api/portfolio/{username}/export/html
```

### Refresh Portfolio
```bash
POST /api/portfolio/{username}/refresh
```

### Update or Delete Portfolio
```bash
PUT /api/portfolio/{username}
DELETE /api/portfolio/{username}
```

## Project Structure

```
SwiftFolio/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI app entry
│   │   ├── config.py        # Configuration
│   │   ├── database.py      # MongoDB connection
│   │   ├── models/          # Pydantic models
│   │   ├── routers/         # API endpoints
│   │   └── services/        # Business logic
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── app/             # Next.js pages
│   │   ├── components/      # React components
│   │   └── lib/             # Utilities
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## License

MIT License - feel free to use this for your own projects!

