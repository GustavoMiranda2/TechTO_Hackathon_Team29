from __future__ import annotations

ROADMAPS = {
    "frontend": {
        "title": "Frontend Developer",
        "roadmap_url": "https://roadmap.sh/frontend",
        "summary": "Builds the part of products people see and touch in the browser.",
        "skills": [
            "HTML", "CSS", "JavaScript", "Git", "TypeScript", "React",
            "State management", "Tailwind / CSS frameworks", "Web APIs / fetch",
            "Testing (Jest / Playwright)", "Build tools (Vite)", "Accessibility",
            "Performance basics",
        ],
    },
    "backend": {
        "title": "Backend Developer",
        "roadmap_url": "https://roadmap.sh/backend",
        "summary": "Builds the logic, data, and APIs that power applications behind the scenes.",
        "skills": [
            "A language (Python / Java / Node)", "Git", "REST APIs", "SQL databases",
            "ORMs", "Authentication / authorization", "Caching", "Message queues",
            "Docker", "Testing", "API security", "Logging & monitoring",
        ],
    },
    "fullstack": {
        "title": "Full-Stack Developer",
        "roadmap_url": "https://roadmap.sh/full-stack",
        "summary": "Comfortable across frontend and backend; ships features end to end.",
        "skills": [
            "HTML", "CSS", "JavaScript", "TypeScript", "React", "A backend language",
            "REST APIs", "SQL databases", "Git", "Authentication", "Docker",
            "Deployment / hosting", "Testing",
        ],
    },
    "devops": {
        "title": "DevOps / Platform Engineer",
        "roadmap_url": "https://roadmap.sh/devops",
        "summary": "Automates how software is built, shipped, and runs reliably in production.",
        "skills": [
            "Linux", "Networking basics", "A scripting language", "Git",
            "CI/CD pipelines", "Docker", "Kubernetes", "Cloud (AWS/GCP/Azure)",
            "Infrastructure as Code (Terraform)", "Monitoring & logging",
            "Shell scripting",
        ],
    },
    "cybersecurity": {
        "title": "Cybersecurity Analyst",
        "roadmap_url": "https://roadmap.sh/cyber-security",
        "summary": "Defends systems: detects threats, investigates incidents, hardens infrastructure.",
        "skills": [
            "Networking fundamentals", "Linux", "Operating system basics",
            "Security concepts (CIA triad)", "Web security (XSS, SQLi)",
            "SIEM tools", "Vulnerability scanning", "Incident response",
            "Log analysis", "Scripting (Python/Bash)", "Security reporting",
        ],
    },
    "qa": {
        "title": "QA / Software Developer in Test",
        "roadmap_url": "https://roadmap.sh/qa",
        "summary": "Ensures software works; automates tests so bugs are caught before users see them.",
        "skills": [
            "Testing fundamentals", "A programming language", "Manual test design",
            "Selenium / Playwright", "API testing (Postman)", "Test automation frameworks",
            "CI integration", "Git", "Bug reporting", "Performance testing basics",
        ],
    },
    "data": {
        "title": "Data Analyst",
        "roadmap_url": "https://roadmap.sh/data-analyst",
        "summary": "Turns raw data into insights that drive decisions.",
        "skills": [
            "SQL", "Excel / spreadsheets", "Python (pandas)", "Data cleaning",
            "Statistics basics", "Data visualization", "Power BI / Tableau",
            "Storytelling with data", "Dashboards", "Basic ETL",
        ],
    },
    "mobile": {
        "title": "Mobile Developer",
        "roadmap_url": "https://roadmap.sh/android",
        "summary": "Builds the apps people carry in their pockets, on iOS or Android.",
        "skills": [
            "A mobile language (Kotlin/Swift/Dart)", "UI fundamentals", "Git",
            "REST APIs", "Local storage", "State management", "App lifecycle",
            "Push notifications", "Publishing to stores", "Testing",
        ],
    },
}


def list_paths_for_prompt() -> str:
    lines = []
    for key, p in ROADMAPS.items():
        lines.append(f'- "{key}" - {p["title"]}: {p["summary"]}')
    return "\n".join(lines)


def get_roadmap(key: str) -> dict | None:
    return ROADMAPS.get(key)
