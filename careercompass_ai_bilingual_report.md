# CareerCompass AI — Bilingual Project Report  
# CareerCompass AI — Relatório Bilíngue do Projeto

---

## Table of Contents / Sumário

1. [English Version](#english-version)  
2. [Versão em Português](#versão-em-português)

---

# English Version

## 1. Project Name

**CareerCompass AI — IT Career Consultant Agent**

---

## 2. One-Sentence Pitch

**CareerCompass AI is a personal IT career consultant agent that helps new tech workers discover the right career path, understand their skill gaps, and build a personalized roadmap toward jobs that actually fit their interests, experience, and goals.**

---

## 3. Problem Statement

Many new people entering the IT market feel lost.

They apply to jobs on LinkedIn, Indeed, Glassdoor, and company websites, but these platforms often recommend jobs based mainly on resume keywords. This can mislead users into job paths that do not match their actual interests, goals, or current skill level.

Common problems include:

- Users may receive recommendations for jobs they are not truly interested in.
- Their resume may make them appear suitable for the wrong career path.
- They may not understand the difference between roles like Software Developer, Cybersecurity Analyst, QA Tester, Data Analyst, Cloud Support, DevOps, or IT Support.
- They may spend months applying to roles that are too advanced, unrelated, or poorly aligned.
- They may not know what skills they are missing.
- They may feel discouraged because they are applying without a clear direction.

The real pain point is not only finding jobs.

The real pain point is:

> **New tech workers do not know where they fit in the IT market.**

CareerCompass AI solves this by helping users understand their best career direction before they start applying blindly.

---

## 4. Unique Value Proposition

CareerCompass AI should not be presented as another job search app.

It should be presented as:

> **A career direction agent, not a job board.**

LinkedIn and Indeed ask:

> “What job do you want to search for?”

CareerCompass AI asks:

> “Who are you, what do you enjoy, what skills do you have, what kind of work fits you, and what path should you follow?”

Most job platforms match people to jobs based on the resume they already have. CareerCompass AI helps users understand:

- what career path fits them
- what jobs they should target first
- what skills they need to improve
- what projects they should build
- what resume direction they should follow
- what next steps are realistic

Strong positioning phrase:

> **LinkedIn shows what jobs exist. CareerCompass AI shows where you actually fit and how to get there.**

---

## 5. Target Audience

CareerCompass AI is designed for people entering or transitioning into the IT market.

Target users include:

- College students
- Recent graduates
- Bootcamp graduates
- Self-taught developers
- Career changers
- Junior developers
- Junior IT support candidates
- People with general tech skills but no clear direction

Typical user questions:

> “I studied programming, but I do not know if I should apply for developer, QA, cybersecurity, data analyst, or IT support roles.”

> “LinkedIn keeps recommending random jobs that do not match what I want.”

> “I do not know what skills I am missing.”

> “I do not know what project to build for my portfolio.”

> “I do not know if my resume is sending me in the wrong direction.”

CareerCompass AI answers these questions by acting as a personalized IT career consultant.

---

## 6. Product Concept

CareerCompass AI is an AI-powered IT career consultant agent for students, recent graduates, career changers, and early-career tech workers.

Instead of only reading a resume and recommending random job postings, the agent interviews the user, understands their background, preferences, strengths, weaknesses, and career goals, then recommends the most suitable IT career paths.

For each career path, it provides:

- match score
- explanation of why the path fits
- required skills
- missing skills
- beginner-friendly job titles
- recommended portfolio projects
- learning roadmap
- resume positioning advice
- job search strategy

The goal is to help users stop applying blindly and start moving toward a career path that actually makes sense.

---

## 7. AI Agent Structure

CareerCompass AI can be explained as a system of specialized agents working together.

---

### 7.1 Profile Understanding Agent

This agent learns about the user.

It asks about:

- education
- work experience
- technical skills
- projects
- certifications
- interests
- preferred work style
- confidence level
- career goals
- location
- preferred job type
- target timeline
- long-term goals

Example questions:

```text
Do you prefer building applications, solving security problems, analyzing data, helping users, or managing infrastructure?
```

```text
Do you enjoy coding every day, or would you prefer a mix of technical and communication work?
```

```text
Would you rather work on websites, cloud systems, databases, networks, security, testing, or data?
```

---

### 7.2 Career Path Matching Agent

This agent maps the user profile to possible IT career paths.

Possible paths include:

- Software Developer
- Web Developer
- Front-End Developer
- Back-End Developer
- Full-Stack Developer
- QA Tester
- Software Developer in Test
- Cybersecurity Analyst
- SOC Analyst
- IT Support Specialist
- Help Desk Analyst
- Cloud Support Associate
- DevOps Junior
- Data Analyst
- Business Analyst
- Database Administrator
- Mobile Developer
- Technical Support Engineer

Example output:

```text
Cybersecurity Analyst — 74% match

Why:
You have networking knowledge, security course experience, and interest in threat detection.

Missing:
SIEM, vulnerability scanning, Linux security, and incident response.

Best next step:
Build a small SOC home lab project.
```

---

### 7.3 Skill Gap Agent

This agent compares the user's current skills with the skills required for a chosen role.

Example:

```text
Target Path: Junior Cybersecurity Analyst

You already have:
- Basic networking
- SQL knowledge
- Web security basics
- Programming fundamentals

You need to improve:
- Linux commands
- SIEM tools
- Vulnerability scanning
- Incident response basics
- Security reporting
```

---

### 7.4 Roadmap Agent

This agent creates a step-by-step plan.

Example:

```text
30-Day Roadmap

Week 1:
- Learn basic SIEM concepts
- Complete a TryHackMe SOC Level 1 introduction
- Update resume summary toward cybersecurity

Week 2:
- Build a small log analysis project
- Practice Linux commands
- Add the project to GitHub

Week 3:
- Apply to 10 SOC/IT Support hybrid roles
- Create one LinkedIn post about the project

Week 4:
- Practice interview questions
- Improve resume keywords
- Follow up with recruiters
```

---

### 7.5 Job Strategy Agent

This agent gives realistic job search advice.

Example:

```text
Based on your profile, applying directly to Cybersecurity Analyst roles may be difficult right now.

A better entry strategy could be:
1. IT Support
2. Help Desk Analyst
3. SOC Analyst Intern
4. Junior Cybersecurity Analyst
```

This is valuable because many new tech workers target advanced roles without understanding the stepping-stone positions.

---

### 7.6 Resume Direction Agent

This agent checks whether the user's resume is pointing them toward the wrong role.

Example:

```text
Your resume currently looks more like a Web Developer resume.

If your goal is cybersecurity, you should highlight:
- security coursework
- Linux
- networking
- SQL injection/XSS knowledge
- security labs
- incident response projects
```

This is one of the strongest differentiators of the project.

---

## 8. Main MVP Features

For the hackathon, the MVP should be simple but powerful.

---

### Feature 1: Career Discovery Questionnaire

The user answers questions about:

- skills
- interests
- experience
- preferred work style
- career goals

---

### Feature 2: Resume/Profile Upload

The user can paste resume text or upload a PDF.

The agent extracts:

- skills
- education
- projects
- experience
- keywords
- possible current career direction

---

### Feature 3: Career Match Results

The app shows the top recommended IT career paths.

Example:

```text
Top Career Matches

1. Junior Full-Stack Developer — 86%
2. Software Developer in Test — 78%
3. Cybersecurity Analyst — 71%
```

Each result includes:

- why it matches
- what is missing
- difficulty level
- beginner job titles
- recommended projects

---

### Feature 4: Personalized Roadmap

The agent creates a 30-day or 90-day roadmap.

---

### Feature 5: Job Search Repositioning

The agent explains how the user should position themselves.

Example:

```text
Your current profile is too broad. For your first role, focus on Junior Full-Stack Developer and Software Developer in Test roles.
```

---

## 9. Key Differentiator: Career Misalignment Detector

The **Career Misalignment Detector** is one of the most unique features.

It detects when the user's resume, interests, and job search targets are pointing in different directions.

Example:

```text
Misalignment Detected

Your resume looks like: Web Developer
Your interest says: Cybersecurity
Your job search says: Data Analyst

This may confuse job platforms and recruiters.

Recommended focus:
For the next 30 days, target Software Developer in Test and Junior Web Developer roles while building cybersecurity portfolio projects.
```

This directly solves the problem that job platforms often make assumptions based on resume patterns and redirect people toward the wrong career direction.

---

## 10. Additional Feature: Career Path Simulator

The Career Path Simulator helps users compare different possible futures.

Example:

```text
If you choose Full-Stack Developer:
- Shortest path to employment
- Uses your current skills
- Needs a stronger portfolio
- Apply to junior web roles

If you choose Cybersecurity:
- Longer preparation time
- Needs security labs
- Start with IT Support or SOC Intern
- Strong long-term path

If you choose Data Analyst:
- Needs stronger Excel, Python data libraries, and Power BI/Tableau
- Build 2 dashboard projects
```

This helps users make better career decisions.

---

## 11. Suggested App Pages

### Page 1: Welcome

```text
Find your best IT career path.
Stop applying blindly. Get a personalized roadmap.
```

Button:

```text
Start Career Diagnosis
```

---

### Page 2: Career Questionnaire

Questions about interests, skills, goals, and preferred work style.

---

### Page 3: Resume Upload

The user can paste a resume or upload a file.

---

### Page 4: Career Match Dashboard

Shows recommended career paths with match scores.

---

### Page 5: Skill Gap Analysis

Shows:

- skills the user already has
- missing skills
- beginner-friendly roles
- difficulty level

---

### Page 6: Roadmap

Shows a 30-day or 90-day plan.

---

### Page 7: Action Center

Shows:

- update resume
- build project
- apply to roles
- practice interview
- improve skill

---

## 12. How This Fits the Hackathon Judging Criteria

---

### Criterion 1: Meaningful Real-World Problem

CareerCompass AI solves a real problem because many new IT workers are overwhelmed and misdirected when entering the market.

They may spend months applying to roles that do not match their skills, interests, or realistic entry path.

CareerCompass AI reduces confusion by helping them identify the right career direction, skill gaps, and next steps.

---

### Criterion 2: Creative, Delightful, and Forward-Thinking Experience

The experience is creative because it feels like talking to a real career consultant, not scrolling through a job board.

The agent gives a personalized career diagnosis, explains the user's best paths, and creates a roadmap.

The delightful moment is when the user sees:

> “This is the career path that fits you best, this is why, and this is exactly what to do next.”

---

### Criterion 3: Effective Use of AI Agents

The project uses AI agents thoughtfully because the system does more than chat.

It:

- interviews the user
- understands their profile
- analyzes their resume
- compares them to career paths
- detects skill gaps
- recommends job titles
- creates a roadmap
- gives resume direction
- remembers goals and preferences

That makes the project agentic because it coordinates multiple steps in a career planning workflow.

---

## 13. Live Demo Flow

A strong 3-minute demo could follow this structure.

---

### Scene 1: Problem

Show a new graduate saying:

```text
I studied Computer Programming, but I do not know if I should apply for Developer, QA, Cybersecurity, Data Analyst, or IT Support roles. LinkedIn keeps recommending random jobs.
```

---

### Scene 2: User Completes Career Profile

The app asks:

```text
What do you enjoy most?
- Building applications
- Solving security problems
- Working with data
- Helping users
- Testing software
- Managing cloud systems
```

Then asks:

```text
How confident are you in coding?
What projects have you built?
What kind of work environment do you prefer?
```

---

### Scene 3: Resume Analysis

User uploads or pastes a resume.

Agent says:

```text
I found skills in Java, Python, SQL, ASP.NET, React, PostgreSQL, Git, and cybersecurity coursework.
```

---

### Scene 4: Career Match Results

The dashboard shows:

```text
1. Full-Stack Developer — 84% match
2. Software Developer in Test — 79% match
3. Cybersecurity Analyst — 68% match
```

---

### Scene 5: Skill Gap + Roadmap

User clicks Cybersecurity Analyst.

Agent says:

```text
You are interested in cybersecurity, but your current resume is stronger for software development.

To move toward cybersecurity, you should build one SIEM/log analysis project, improve Linux, and apply to SOC Analyst Intern or IT Support roles first.
```

---

### Scene 6: Action Plan

Agent generates:

```text
30-Day Career Plan

Week 1: Fix resume direction
Week 2: Build portfolio project
Week 3: Apply to targeted jobs
Week 4: Practice interviews and follow-ups
```

---

### Scene 7: Final Message

End with:

```text
CareerCompass AI helps new IT workers stop applying blindly and start following a career path that actually fits.
```

---

## 14. Demo User Example

Use a fictional user like this:

```text
Name: Alex

Education:
Computer Programming diploma

Skills:
Java, Python, SQL, HTML, CSS, JavaScript, React, Git

Projects:
Inventory system, portfolio website, simple API

Interests:
Cybersecurity and software development

Problem:
Does not know whether to apply for developer, QA, cybersecurity, or IT support

Goal:
Get a first tech job within 6 months
```

Expected agent output:

```text
Best immediate path:
Junior Full-Stack Developer or Software Developer in Test

Secondary path:
Cybersecurity Analyst, but it requires extra preparation

Recommended strategy:
Apply now to software/testing roles while building cybersecurity projects on the side.
```

---

## 15. Example Agent Output

```text
Career Diagnosis Complete

Your strongest current path is Junior Full-Stack Developer.

Why:
You already have experience with JavaScript, React, ASP.NET, SQL, and Git. Your projects show application-building ability, which fits developer roles.

Your second strongest path is Software Developer in Test.

Why:
You have programming knowledge and can transition into testing automation by learning tools like Selenium, Playwright, JUnit, and API testing.

Your aspirational path is Cybersecurity Analyst.

Why:
You are interested in security, but your current profile needs more proof through projects like log analysis, vulnerability scanning, and incident response labs.

Recommended strategy:
Apply now to junior developer and QA automation roles while building one cybersecurity project to keep that path open.
```

---

## 16. Refined Project Description

```text
CareerCompass AI is an AI-powered IT career consultant agent designed for students, new graduates, career changers, and early-career tech workers who feel lost entering the technology job market.

Many job platforms recommend roles based mainly on resume keywords, which can mislead users into job paths that do not match their actual interests, goals, or realistic skill level. CareerCompass AI solves this by interviewing the user, analyzing their resume, identifying their strengths and preferences, detecting career misalignment, and recommending the best IT career paths.

The agent provides match scores for roles such as Software Developer, QA Tester, Cybersecurity Analyst, Data Analyst, IT Support, Cloud Support, and DevOps. For each path, it explains why the user fits, what skills are missing, what beginner job titles to search for, what portfolio projects to build, and what 30-day or 90-day roadmap to follow.

Unlike LinkedIn or Indeed, CareerCompass AI is not a job board. It is a career direction agent. It helps users stop applying blindly and start building a focused strategy toward a future role that actually fits them.
```

---

## 17. Master Prompt for the AI Agent

```text
You are CareerCompass AI, an expert IT career consultant agent.

Your goal is to help students, new graduates, career changers, and early-career tech workers discover the IT career path that best fits their skills, interests, experience, goals, and current market readiness.

You must not act like a generic chatbot or simply recommend jobs based on keywords. You must behave like a career consultant who diagnoses the user’s current situation, identifies career alignment or misalignment, explains realistic options, and creates a practical roadmap.

Your responsibilities:

1. Understand the user profile:
- education
- technical skills
- work experience
- projects
- certifications
- interests
- preferred work style
- location
- target timeline
- confidence level
- long-term goals

2. Analyze the user’s resume or profile:
- extract skills
- identify strongest career direction
- detect missing information
- identify whether the resume is too broad, unclear, or pointing toward the wrong role

3. Recommend IT career paths:
Consider paths such as:
- Software Developer
- Front-End Developer
- Back-End Developer
- Full-Stack Developer
- QA Tester
- Software Developer in Test
- Cybersecurity Analyst
- SOC Analyst
- IT Support Specialist
- Help Desk Analyst
- Cloud Support Associate
- DevOps Junior
- Data Analyst
- Business Analyst
- Database Administrator
- Mobile Developer
- Technical Support Engineer

For each recommended path, provide:
- match score from 0 to 100
- why the path fits
- what skills the user already has
- what skills are missing
- realistic entry-level job titles
- recommended portfolio projects
- estimated difficulty level
- next best action

4. Detect career misalignment:
Compare the user’s resume, interests, job search targets, and goals.
If they do not match, explain the misalignment clearly.

Example:
“Your resume currently looks like a web developer profile, but your stated interest is cybersecurity and your job search targets are data analyst roles. This could confuse job platforms and recruiters.”

5. Create a roadmap:
Generate a 30-day or 90-day roadmap with weekly steps.
The roadmap should include:
- skills to learn
- projects to build
- resume updates
- job titles to target
- networking actions
- interview preparation

6. Give realistic advice:
Be honest about whether a path is immediately reachable or aspirational.
Recommend stepping-stone roles when needed.

7. Keep the explanation simple:
Use clear language suitable for users who are new to the tech market.
Avoid unnecessary jargon.
Explain technical terms when needed.

8. Output format:
Always structure the response with:
- Career diagnosis summary
- Top recommended paths
- Skill gap analysis
- Career misalignment warning, if any
- Recommended roadmap
- Next 3 actions
```

---

## 18. Example Input for Testing

```text
User Profile:
I recently graduated from a Computer Programming program. I know Java, Python, SQL, HTML, CSS, JavaScript, React, ASP.NET Core, PostgreSQL, and Git. I built a smart inventory management system, a portfolio website, and a simple game project. I am interested in software development and cybersecurity, but I am not sure which career path is more realistic for my first job. I want to get a tech job within 6 months.

Resume Summary:
Computer Programming graduate with experience in full-stack development using ASP.NET Core, React, PostgreSQL, Java, Python, and SQL. Built academic projects involving inventory management, authentication, database integration, and web interfaces. Some coursework in cybersecurity, SQL injection, XSS, and network security.

Job Search Preference:
I have been applying to Junior Developer, Cybersecurity Analyst, Data Analyst, and IT Support roles.
```

Expected output:

```text
Career Diagnosis:
Your strongest immediate path is Junior Full-Stack Developer or Software Developer in Test. Your cybersecurity interest is valid, but it currently looks more like an aspirational path unless you build stronger security-specific projects.

Top Paths:
1. Junior Full-Stack Developer — 86%
2. Software Developer in Test — 80%
3. Cybersecurity Analyst/SOC Analyst — 68%

Misalignment:
Your resume is strongest for software development, but your job search is spread across too many directions. This may reduce your chances because each role expects different keywords and projects.

Recommended strategy:
Focus your resume and applications on Junior Developer and QA Automation roles for the next 30 days, while building one cybersecurity project to support your long-term cybersecurity goal.
```

---

## 19. 3-Minute Video Script

```text
Many new people entering the IT market feel lost. They apply to jobs on LinkedIn or Indeed, but those platforms often recommend roles based mostly on resume keywords. This can push users toward jobs that do not match their real interests, goals, or realistic skill level.

Our project is CareerCompass AI, an IT career consultant agent for students, new graduates, and career changers.

Instead of asking, “What job do you want?”, CareerCompass AI asks, “Where do you actually fit?”

The user starts by answering questions about their skills, projects, interests, and career goals. Then they upload or paste their resume.

The agent analyzes the profile and detects career alignment. In this example, the user is interested in cybersecurity, software development, and data analysis, but their resume is strongest for full-stack development.

CareerCompass AI recommends the top career paths, gives match scores, explains why each path fits, identifies missing skills, and suggests realistic entry-level job titles.

The most important feature is the Career Misalignment Detector. It shows when the user’s resume, interests, and job search targets are pointing in different directions.

Finally, the agent creates a personalized 30-day roadmap with skills to learn, projects to build, resume changes, and jobs to target.

CareerCompass AI is not another job board. It is a career direction agent that helps new IT workers stop applying blindly and start building a focused path toward their future.
```

---

## 20. Best Version to Present to Judges

```text
CareerCompass AI helps new IT workers find direction before they apply. Unlike job boards that match resumes to postings, our agent analyzes the person behind the resume: their skills, interests, goals, projects, and realistic market readiness. It detects career misalignment, recommends the best IT paths, and creates a personalized roadmap so users know exactly what to learn, build, and apply for next.
```

---

# Versão em Português

## 1. Nome do Projeto

**CareerCompass AI — Agente Consultor de Carreira em TI**

---

## 2. Frase Principal da Ideia

**CareerCompass AI é um agente pessoal de consultoria de carreira em TI que ajuda novos profissionais de tecnologia a descobrirem o caminho certo, entenderem suas lacunas de habilidades e criarem um roadmap personalizado para chegar em vagas que realmente combinam com seus interesses, experiência e objetivos.**

---

## 3. Declaração do Problema

Muitas pessoas novas entrando no mercado de TI se sentem perdidas.

Elas aplicam para vagas no LinkedIn, Indeed, Glassdoor e sites de empresas, mas essas plataformas geralmente recomendam cargos com base principalmente em palavras-chave do currículo. Isso pode direcionar usuários para caminhos que não combinam com seus interesses reais, objetivos ou nível atual de habilidade.

Problemas comuns incluem:

- O usuário pode receber recomendações de vagas que não são realmente do interesse dele.
- O currículo pode fazer a pessoa parecer adequada para uma área errada.
- A pessoa pode não saber a diferença entre cargos como Software Developer, Cybersecurity Analyst, QA Tester, Data Analyst, Cloud Support, DevOps ou IT Support.
- A pessoa pode passar meses aplicando para vagas muito avançadas, fora da área ou desalinhadas.
- A pessoa pode não saber quais habilidades estão faltando.
- A pessoa pode ficar desmotivada por aplicar sem direção clara.

O problema real não é apenas encontrar vagas.

O problema real é:

> **Novos profissionais de tecnologia não sabem exatamente onde se encaixam no mercado de TI.**

CareerCompass AI resolve isso ajudando os usuários a entenderem sua melhor direção de carreira antes de começarem a aplicar no escuro.

---

## 4. Proposta de Valor Única

CareerCompass AI não deve ser apresentado como mais um app de busca de emprego.

Ele deve ser apresentado como:

> **Um agente de direcionamento de carreira, não um job board.**

LinkedIn e Indeed perguntam:

> “Qual vaga você quer procurar?”

CareerCompass AI pergunta:

> “Quem é você, o que você gosta de fazer, quais habilidades você tem, que tipo de trabalho combina com você e qual caminho você deveria seguir?”

A maioria das plataformas conecta pessoas a vagas com base no currículo que elas já têm. CareerCompass AI ajuda os usuários a entenderem:

- qual carreira combina com eles
- quais cargos deveriam mirar primeiro
- quais habilidades precisam melhorar
- quais projetos deveriam construir
- como deveriam posicionar o currículo
- quais próximos passos são realistas

Frase forte de posicionamento:

> **LinkedIn mostra quais vagas existem. CareerCompass AI mostra onde você realmente se encaixa e como chegar lá.**

---

## 5. Público-Alvo

CareerCompass AI é feito para pessoas entrando ou migrando para o mercado de TI.

Usuários-alvo incluem:

- Estudantes universitários
- Recém-formados
- Pessoas que fizeram bootcamp
- Desenvolvedores autodidatas
- Pessoas mudando de carreira
- Desenvolvedores júnior
- Candidatos para IT Support
- Pessoas com habilidades gerais de tecnologia, mas sem direção clara

Perguntas típicas dos usuários:

> “Eu estudei programação, mas não sei se devo aplicar para developer, QA, cybersecurity, data analyst ou IT support.”

> “O LinkedIn fica me recomendando vagas aleatórias que não combinam comigo.”

> “Eu não sei quais habilidades estão faltando.”

> “Eu não sei que projeto fazer para o meu portfólio.”

> “Eu não sei se meu currículo está me empurrando para a direção errada.”

CareerCompass AI responde essas dúvidas atuando como um consultor de carreira em TI personalizado.

---

## 6. Conceito do Produto

CareerCompass AI é um agente com IA para consultoria de carreira em TI, criado para estudantes, recém-formados, pessoas mudando de carreira e profissionais iniciantes em tecnologia.

Em vez de apenas ler um currículo e recomendar vagas aleatórias, o agente entrevista o usuário, entende sua experiência, preferências, pontos fortes, pontos fracos e objetivos de carreira, e então recomenda os caminhos de TI mais adequados.

Para cada caminho de carreira, ele fornece:

- match score
- explicação do motivo
- habilidades necessárias
- habilidades faltando
- cargos iniciais recomendados
- projetos de portfólio recomendados
- roadmap de aprendizado
- orientação para posicionamento do currículo
- estratégia de busca de emprego

O objetivo é ajudar os usuários a pararem de aplicar “no escuro” e começarem a seguir um caminho profissional que realmente faça sentido.

---

## 7. Estrutura dos Agentes de IA

CareerCompass AI pode ser explicado como um sistema de agentes especializados trabalhando juntos.

---

### 7.1 Profile Understanding Agent

Esse agente entende quem é o usuário.

Ele pergunta sobre:

- educação
- experiência de trabalho
- habilidades técnicas
- projetos
- certificações
- interesses
- estilo de trabalho preferido
- nível de confiança
- objetivos de carreira
- localização
- tipo de vaga desejada
- prazo desejado
- objetivos de longo prazo

Exemplos de perguntas:

```text
Você prefere construir aplicações, resolver problemas de segurança, analisar dados, ajudar usuários ou gerenciar infraestrutura?
```

```text
Você gosta de programar todos os dias ou prefere um trabalho que mistura parte técnica com comunicação?
```

```text
Você prefere trabalhar com websites, cloud systems, databases, networks, security, testing ou data?
```

---

### 7.2 Career Path Matching Agent

Esse agente conecta o perfil do usuário com possíveis caminhos de carreira em TI.

Possíveis caminhos incluem:

- Software Developer
- Web Developer
- Front-End Developer
- Back-End Developer
- Full-Stack Developer
- QA Tester
- Software Developer in Test
- Cybersecurity Analyst
- SOC Analyst
- IT Support Specialist
- Help Desk Analyst
- Cloud Support Associate
- DevOps Junior
- Data Analyst
- Business Analyst
- Database Administrator
- Mobile Developer
- Technical Support Engineer

Exemplo de saída:

```text
Cybersecurity Analyst — 74% match

Por quê:
Você tem conhecimento de networking, experiência em matérias de security e interesse em threat detection.

Faltando:
SIEM, vulnerability scanning, Linux security e incident response.

Melhor próximo passo:
Construir um pequeno projeto de SOC home lab.
```

---

### 7.3 Skill Gap Agent

Esse agente compara as habilidades atuais do usuário com as habilidades necessárias para um cargo escolhido.

Exemplo:

```text
Caminho-alvo: Junior Cybersecurity Analyst

Você já tem:
- Basic networking
- SQL knowledge
- Web security basics
- Programming fundamentals

Você precisa melhorar:
- Linux commands
- SIEM tools
- Vulnerability scanning
- Incident response basics
- Security reporting
```

---

### 7.4 Roadmap Agent

Esse agente cria um plano passo a passo.

Exemplo:

```text
Roadmap de 30 dias

Semana 1:
- Aprender conceitos básicos de SIEM
- Completar uma introdução de SOC Level 1 no TryHackMe
- Atualizar o resume summary para cybersecurity

Semana 2:
- Construir um projeto simples de log analysis
- Praticar Linux commands
- Adicionar o projeto ao GitHub

Semana 3:
- Aplicar para 10 vagas de SOC/IT Support híbridas
- Criar um post no LinkedIn falando sobre o projeto

Semana 4:
- Praticar perguntas de entrevista
- Melhorar keywords do currículo
- Fazer follow-up com recruiters
```

---

### 7.5 Job Strategy Agent

Esse agente dá uma estratégia realista de busca de emprego.

Exemplo:

```text
Com base no seu perfil, aplicar diretamente para Cybersecurity Analyst pode ser difícil agora.

Uma estratégia melhor de entrada poderia ser:
1. IT Support
2. Help Desk Analyst
3. SOC Analyst Intern
4. Junior Cybersecurity Analyst
```

Isso é valioso porque muitos novos profissionais de tecnologia miram cargos avançados sem entender os cargos de transição.

---

### 7.6 Resume Direction Agent

Esse agente verifica se o currículo do usuário está apontando para o cargo errado.

Exemplo:

```text
Seu currículo atualmente parece mais um currículo de Web Developer.

Se seu objetivo é cybersecurity, você deveria destacar:
- security coursework
- Linux
- networking
- SQL injection/XSS knowledge
- security labs
- incident response projects
```

Esse é um dos maiores diferenciais do projeto.

---

## 8. Funcionalidades Principais do MVP

Para o hackathon, o MVP deve ser simples, mas forte.

---

### Feature 1: Career Discovery Questionnaire

O usuário responde perguntas sobre:

- habilidades
- interesses
- experiência
- estilo de trabalho preferido
- objetivos de carreira

---

### Feature 2: Upload ou Colagem do Currículo/Profile

O usuário pode colar o texto do currículo ou fazer upload de um PDF.

O agente extrai:

- skills
- educação
- projetos
- experiência
- keywords
- possível direção atual de carreira

---

### Feature 3: Career Match Results

O app mostra os principais caminhos de TI recomendados.

Exemplo:

```text
Top Career Matches

1. Junior Full-Stack Developer — 86%
2. Software Developer in Test — 78%
3. Cybersecurity Analyst — 71%
```

Cada resultado inclui:

- por que combina
- o que está faltando
- nível de dificuldade
- cargos iniciais recomendados
- projetos recomendados

---

### Feature 4: Roadmap Personalizado

O agente cria um roadmap de 30 ou 90 dias.

---

### Feature 5: Job Search Repositioning

O agente explica como o usuário deveria se posicionar.

Exemplo:

```text
Seu perfil atual está muito amplo. Para sua primeira vaga, foque em Junior Full-Stack Developer e Software Developer in Test.
```

---

## 9. Diferencial Principal: Career Misalignment Detector

O **Career Misalignment Detector** é uma das funcionalidades mais únicas.

Ele detecta quando o currículo, os interesses e os alvos de busca de emprego do usuário estão apontando em direções diferentes.

Exemplo:

```text
Misalignment Detected

Seu currículo parece apontar para: Web Developer
Seu interesse aponta para: Cybersecurity
Sua busca de emprego aponta para: Data Analyst

Isso pode confundir plataformas de emprego e recruiters.

Foco recomendado:
Nos próximos 30 dias, mire Software Developer in Test e Junior Web Developer enquanto constrói projetos de cybersecurity para o portfólio.
```

Isso resolve diretamente o problema de plataformas de emprego fazerem suposições com base no padrão do currículo e redirecionarem pessoas para uma direção de carreira errada.

---

## 10. Funcionalidade Adicional: Career Path Simulator

O Career Path Simulator ajuda os usuários a comparar futuros caminhos possíveis.

Exemplo:

```text
Se você escolher Full-Stack Developer:
- Caminho mais curto para empregabilidade
- Usa suas habilidades atuais
- Precisa de portfólio mais forte
- Aplique para vagas junior web

Se você escolher Cybersecurity:
- Tempo de preparação maior
- Precisa de security labs
- Comece com IT Support ou SOC Intern
- Bom caminho de longo prazo

Se você escolher Data Analyst:
- Precisa melhorar Excel, Python data libraries e Power BI/Tableau
- Construir 2 projetos de dashboard
```

Isso ajuda os usuários a tomarem melhores decisões de carreira.

---

## 11. Páginas/Telas Sugeridas do App

### Página 1: Welcome

```text
Find your best IT career path.
Stop applying blindly. Get a personalized roadmap.
```

Botão:

```text
Start Career Diagnosis
```

---

### Página 2: Career Questionnaire

Perguntas sobre interesses, habilidades, objetivos e estilo de trabalho preferido.

---

### Página 3: Resume Upload

O usuário pode colar um currículo ou fazer upload de arquivo.

---

### Página 4: Career Match Dashboard

Mostra caminhos de carreira recomendados com match scores.

---

### Página 5: Skill Gap Analysis

Mostra:

- habilidades que o usuário já tem
- habilidades faltando
- cargos iniciais recomendados
- nível de dificuldade

---

### Página 6: Roadmap

Mostra plano de 30 ou 90 dias.

---

### Página 7: Action Center

Mostra:

- atualizar currículo
- construir projeto
- aplicar para vagas
- praticar entrevista
- melhorar skill

---

## 12. Como Isso Se Encaixa nos Critérios do Hackathon

---

### Critério 1: Problema Real do Dia a Dia

CareerCompass AI resolve um problema real porque muitos novos profissionais de TI se sentem perdidos e mal direcionados quando entram no mercado.

Eles podem passar meses aplicando para vagas que não combinam com suas habilidades, interesses ou caminho realista de entrada.

CareerCompass AI reduz essa confusão ajudando o usuário a identificar a direção certa de carreira, lacunas de habilidades e próximos passos.

---

### Critério 2: Criatividade, Experiência Interessante e Visão de Futuro

A experiência é criativa porque parece uma conversa com um consultor de carreira real, não apenas navegar em um job board.

O agente entrega um diagnóstico personalizado de carreira, explica os melhores caminhos do usuário e cria um roadmap.

O momento mais marcante é quando o usuário vê:

> “Esse é o caminho de carreira que mais combina com você, esse é o motivo, e é exatamente isso que você deve fazer agora.”

---

### Critério 3: Uso Efetivo de AI Agents

O projeto usa agentes de IA de forma inteligente porque o sistema faz mais do que conversar.

Ele:

- entrevista o usuário
- entende o perfil
- analisa o currículo
- compara o usuário com caminhos de carreira
- detecta lacunas de habilidade
- recomenda cargos
- cria um roadmap
- orienta ajustes no currículo
- lembra objetivos e preferências

Isso torna o projeto agentic porque ele coordena várias etapas de um processo de planejamento de carreira.

---

## 13. Fluxo do Live Demo

Um bom demo de 3 minutos poderia seguir esta estrutura.

---

### Cena 1: Problema

Mostrar um recém-formado dizendo:

```text
Eu estudei Computer Programming, mas não sei se devo aplicar para Developer, QA, Cybersecurity, Data Analyst ou IT Support. O LinkedIn fica me recomendando vagas aleatórias.
```

---

### Cena 2: Usuário Completa o Career Profile

O app pergunta:

```text
O que você mais gosta?
- Construir aplicações
- Resolver problemas de segurança
- Trabalhar com dados
- Ajudar usuários
- Testar software
- Gerenciar cloud systems
```

Depois pergunta:

```text
Qual é seu nível de confiança em programação?
Quais projetos você já construiu?
Que tipo de ambiente de trabalho você prefere?
```

---

### Cena 3: Análise do Currículo

Usuário cola ou faz upload do currículo.

O agente responde:

```text
Encontrei habilidades em Java, Python, SQL, ASP.NET, React, PostgreSQL, Git e coursework em cybersecurity.
```

---

### Cena 4: Career Match Results

O dashboard mostra:

```text
1. Full-Stack Developer — 84% match
2. Software Developer in Test — 79% match
3. Cybersecurity Analyst — 68% match
```

---

### Cena 5: Skill Gap + Roadmap

Usuário clica em Cybersecurity Analyst.

O agente diz:

```text
Você tem interesse em cybersecurity, mas seu currículo atual é mais forte para software development.

Para se mover em direção à cybersecurity, você deveria construir um projeto de SIEM/log analysis, melhorar Linux e aplicar primeiro para SOC Analyst Intern ou IT Support.
```

---

### Cena 6: Plano de Ação

O agente gera:

```text
Plano de carreira de 30 dias

Semana 1: Ajustar a direção do currículo
Semana 2: Construir projeto de portfólio
Semana 3: Aplicar para vagas direcionadas
Semana 4: Praticar entrevistas e follow-ups
```

---

### Cena 7: Mensagem Final

Finalizar com:

```text
CareerCompass AI ajuda novos profissionais de TI a pararem de aplicar no escuro e começarem a seguir um caminho de carreira que realmente combina com eles.
```

---

## 14. Exemplo de Usuário para o Demo

Use um usuário fictício assim:

```text
Nome: Alex

Educação:
Computer Programming diploma

Skills:
Java, Python, SQL, HTML, CSS, JavaScript, React, Git

Projetos:
Inventory system, portfolio website, simple API

Interesses:
Cybersecurity e software development

Problema:
Não sabe se deve aplicar para developer, QA, cybersecurity ou IT support

Objetivo:
Conseguir a primeira vaga de tecnologia em até 6 meses
```

Saída esperada do agente:

```text
Melhor caminho imediato:
Junior Full-Stack Developer ou Software Developer in Test

Caminho secundário:
Cybersecurity Analyst, mas exige preparação extra

Estratégia recomendada:
Aplicar agora para software/testing roles enquanto constrói projetos de cybersecurity em paralelo.
```

---

## 15. Exemplo de Saída do Agente

```text
Career Diagnosis Complete

Seu caminho mais forte no momento é Junior Full-Stack Developer.

Por quê:
Você já tem experiência com JavaScript, React, ASP.NET, SQL e Git. Seus projetos mostram capacidade de construir aplicações, o que combina com vagas de developer.

Seu segundo caminho mais forte é Software Developer in Test.

Por quê:
Você tem conhecimento de programação e pode fazer transição para testing automation aprendendo ferramentas como Selenium, Playwright, JUnit e API testing.

Seu caminho aspiracional é Cybersecurity Analyst.

Por quê:
Você tem interesse em security, mas seu perfil atual precisa de mais provas através de projetos como log analysis, vulnerability scanning e incident response labs.

Estratégia recomendada:
Aplique agora para vagas de junior developer e QA automation enquanto constrói um projeto de cybersecurity para manter esse caminho aberto.
```

---

## 16. Descrição Refinada do Projeto

```text
CareerCompass AI é um agente de consultoria de carreira em TI com inteligência artificial, criado para estudantes, recém-formados, pessoas mudando de carreira e profissionais iniciantes que se sentem perdidos ao entrar no mercado de tecnologia.

Muitas plataformas de emprego recomendam vagas principalmente com base em palavras-chave do currículo, o que pode direcionar usuários para caminhos que não combinam com seus interesses reais, objetivos ou nível atual de habilidade. CareerCompass AI resolve isso entrevistando o usuário, analisando seu currículo, identificando pontos fortes e preferências, detectando desalinhamento de carreira e recomendando os melhores caminhos dentro de TI.

O agente fornece match scores para áreas como Software Developer, QA Tester, Cybersecurity Analyst, Data Analyst, IT Support, Cloud Support e DevOps. Para cada caminho, ele explica por que o usuário combina com aquela área, quais habilidades estão faltando, quais cargos iniciais procurar, quais projetos de portfólio construir e qual roadmap de 30 ou 90 dias seguir.

Diferente do LinkedIn ou Indeed, CareerCompass AI não é um job board. É um agente de direcionamento de carreira. Ele ajuda usuários a pararem de aplicar no escuro e começarem a construir uma estratégia focada para uma vaga futura que realmente combina com eles.
```

---

## 17. Master Prompt para o Agente de IA

```text
You are CareerCompass AI, an expert IT career consultant agent.

Your goal is to help students, new graduates, career changers, and early-career tech workers discover the IT career path that best fits their skills, interests, experience, goals, and current market readiness.

You must not act like a generic chatbot or simply recommend jobs based on keywords. You must behave like a career consultant who diagnoses the user’s current situation, identifies career alignment or misalignment, explains realistic options, and creates a practical roadmap.

Your responsibilities:

1. Understand the user profile:
- education
- technical skills
- work experience
- projects
- certifications
- interests
- preferred work style
- location
- target timeline
- confidence level
- long-term goals

2. Analyze the user’s resume or profile:
- extract skills
- identify strongest career direction
- detect missing information
- identify whether the resume is too broad, unclear, or pointing toward the wrong role

3. Recommend IT career paths:
Consider paths such as:
- Software Developer
- Front-End Developer
- Back-End Developer
- Full-Stack Developer
- QA Tester
- Software Developer in Test
- Cybersecurity Analyst
- SOC Analyst
- IT Support Specialist
- Help Desk Analyst
- Cloud Support Associate
- DevOps Junior
- Data Analyst
- Business Analyst
- Database Administrator
- Mobile Developer
- Technical Support Engineer

For each recommended path, provide:
- match score from 0 to 100
- why the path fits
- what skills the user already has
- what skills are missing
- realistic entry-level job titles
- recommended portfolio projects
- estimated difficulty level
- next best action

4. Detect career misalignment:
Compare the user’s resume, interests, job search targets, and goals.
If they do not match, explain the misalignment clearly.

Example:
“Your resume currently looks like a web developer profile, but your stated interest is cybersecurity and your job search targets are data analyst roles. This could confuse job platforms and recruiters.”

5. Create a roadmap:
Generate a 30-day or 90-day roadmap with weekly steps.
The roadmap should include:
- skills to learn
- projects to build
- resume updates
- job titles to target
- networking actions
- interview preparation

6. Give realistic advice:
Be honest about whether a path is immediately reachable or aspirational.
Recommend stepping-stone roles when needed.

7. Keep the explanation simple:
Use clear language suitable for users who are new to the tech market.
Avoid unnecessary jargon.
Explain technical terms when needed.

8. Output format:
Always structure the response with:
- Career diagnosis summary
- Top recommended paths
- Skill gap analysis
- Career misalignment warning, if any
- Recommended roadmap
- Next 3 actions
```

> Observação: Mesmo na versão em português do relatório, é recomendado manter o master prompt em inglês caso a equipe use APIs e ferramentas de IA em inglês.

---

## 18. Exemplo de Input para Teste

```text
User Profile:
I recently graduated from a Computer Programming program. I know Java, Python, SQL, HTML, CSS, JavaScript, React, ASP.NET Core, PostgreSQL, and Git. I built a smart inventory management system, a portfolio website, and a simple game project. I am interested in software development and cybersecurity, but I am not sure which career path is more realistic for my first job. I want to get a tech job within 6 months.

Resume Summary:
Computer Programming graduate with experience in full-stack development using ASP.NET Core, React, PostgreSQL, Java, Python, and SQL. Built academic projects involving inventory management, authentication, database integration, and web interfaces. Some coursework in cybersecurity, SQL injection, XSS, and network security.

Job Search Preference:
I have been applying to Junior Developer, Cybersecurity Analyst, Data Analyst, and IT Support roles.
```

Saída esperada:

```text
Career Diagnosis:
Your strongest immediate path is Junior Full-Stack Developer or Software Developer in Test. Your cybersecurity interest is valid, but it currently looks more like an aspirational path unless you build stronger security-specific projects.

Top Paths:
1. Junior Full-Stack Developer — 86%
2. Software Developer in Test — 80%
3. Cybersecurity Analyst/SOC Analyst — 68%

Misalignment:
Your resume is strongest for software development, but your job search is spread across too many directions. This may reduce your chances because each role expects different keywords and projects.

Recommended strategy:
Focus your resume and applications on Junior Developer and QA Automation roles for the next 30 days, while building one cybersecurity project to support your long-term cybersecurity goal.
```

---

## 19. Roteiro para Vídeo de 3 Minutos

```text
Muitas pessoas novas entrando no mercado de TI se sentem perdidas. Elas aplicam para vagas no LinkedIn ou Indeed, mas essas plataformas geralmente recomendam cargos com base principalmente em palavras-chave do currículo. Isso pode empurrar usuários para vagas que não combinam com seus interesses reais, objetivos ou nível real de habilidade.

Nosso projeto é CareerCompass AI, um agente consultor de carreira em TI para estudantes, recém-formados e pessoas mudando de carreira.

Em vez de perguntar “Que vaga você quer?”, CareerCompass AI pergunta “Onde você realmente se encaixa?”

O usuário começa respondendo perguntas sobre suas skills, projetos, interesses e objetivos de carreira. Depois, ele cola ou faz upload do currículo.

O agente analisa o perfil e detecta alinhamento de carreira. Neste exemplo, o usuário tem interesse em cybersecurity, software development e data analysis, mas o currículo dele é mais forte para full-stack development.

CareerCompass AI recomenda os principais caminhos de carreira, dá match scores, explica por que cada caminho combina, identifica habilidades faltantes e sugere cargos iniciais realistas.

A funcionalidade mais importante é o Career Misalignment Detector. Ele mostra quando o currículo, os interesses e os alvos de busca de emprego do usuário estão apontando em direções diferentes.

Por fim, o agente cria um roadmap personalizado de 30 dias com skills para aprender, projetos para construir, mudanças no currículo e vagas para mirar.

CareerCompass AI não é mais um job board. É um agente de direcionamento de carreira que ajuda novos profissionais de TI a pararem de aplicar no escuro e começarem a construir um caminho focado para o futuro.
```

---

## 20. Melhor Versão para Apresentar aos Jurados

```text
CareerCompass AI ajuda novos profissionais de TI a encontrarem direção antes de aplicar para vagas. Diferente de job boards que conectam currículos a vagas, nosso agente analisa a pessoa por trás do currículo: suas habilidades, interesses, objetivos, projetos e nível real de preparação para o mercado. Ele detecta desalinhamento de carreira, recomenda os melhores caminhos em TI e cria um roadmap personalizado para que o usuário saiba exatamente o que aprender, construir e aplicar em seguida.
```

---

# Final Note / Nota Final

This report can be used as a planning document for the team, a hackathon idea description, or a base for the project README.

Este relatório pode ser usado como documento de planejamento da equipe, descrição da ideia para o hackathon ou base para o README do projeto.
