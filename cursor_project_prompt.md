# ReallyConnect — Cursor Project Context

## Project Overview
ReallyConnect is an **opt-in mentorship matching platform** designed for communities like ColorStack. It connects **mentors (volunteers)** with **mentees (students / early-career professionals)** in a structured, respectful way.

The goals of the platform are to:
- Help mentors give back **without being overwhelmed**
- Help mentees ask for help **without cold-DM anxiety**
- Use **Responsible AI** to improve communication, fairness, and safety

This is **NOT** a social network and **NOT** a replacement for LinkedIn. The product focuses on fixing one broken workflow: mentorship and guidance connections.

---

## Core Product Principles
- Mentors explicitly opt in and control their availability
- Mentees submit **structured requests**, not free-form DMs
- Matching prioritizes:
  1. Career / industry alignment
  2. Type of help offered vs. requested
  3. Availability and fairness limits
  4. Shared interests (secondary, humanizing factor)
- No infinite scrolling or swiping
- No contact information is shared until **both sides accept**

---

## Tech Stack (Locked In)

### Frontend
- React or Next.js

### Backend
- FastAPI (Python)

### Database & Auth
- Supabase (Postgres, Auth, Row Level Security)

### AI
- Used carefully with guardrails (request rewriting, safety checks)

Supabase is responsible for:
- Postgres database
- Authentication (JWTs)
- Row Level Security
- Optional file storage

FastAPI is responsible for:
- Business logic
- Matching logic
- Fairness constraints
- Responsible AI features

Auth flow:
1. Frontend authenticates via Supabase
2. Frontend receives a JWT
3. JWT is sent to FastAPI
4. FastAPI verifies the JWT and uses the Supabase **service role key** for database access

---

## Core MVP Features
1. User roles: Mentor, Mentee (or both)
2. Mentor profile:
   - Industry / role
   - Help types offered (resume review, mock interviews, career advice, social advice)
   - Max requests per week
   - Interests
3. Mentee profile:
   - Goals
   - Help needed
   - Background
   - Interests
4. Structured mentorship requests:
   - Help type
   - Short context
   - Key questions
5. Matching logic (rule-based and explainable)
6. Mentor inbox:
   - Accept / decline requests
7. Connection flow:
   - In-app chat **or** controlled contact exchange
8. Responsible AI feature:
   - AI-assisted request rewriter to improve tone and clarity
   - Must **not** fabricate experience or skills
   - Must show before/after and require user approval
9. Safety & fairness:
   - Weekly request caps
   - Soft warnings for inappropriate messages
   - Transparent match explanations

---

## Responsible AI Constraints (Very Important)
- AI assists users, it does **not** make decisions for them
- No hidden automation
- No deceptive rewriting
- No popularity-based ranking
- Always prioritize consent, privacy, and explainability

---

## Explicitly Out of Scope
- Social feeds
- Video calling
- Advanced ML recommendations
- Infinite swipe-based UIs
- Unstructured messaging systems

---

## Coding Expectations
- Keep code clean, readable, and modular
- Prefer simple, explicit logic over clever abstractions
- Clearly explain reasoning when implementing matching or AI features
- Ask before introducing major architectural changes

When unsure, default to:
**clarity > speed > complexity**

---

## Suggested First Tasks
- Define monorepo folder structure
- Design Supabase table schemas
- Create FastAPI app skeleton
- Implement Supabase JWT verification middleware
- Write initial rule-based matching logic
- Build API routes for mentorship requests

---

You are acting as a **senior engineer teammate** helping ship a clean, demo-ready MVP under hackathon constraints.
