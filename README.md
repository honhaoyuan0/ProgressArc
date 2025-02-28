# ProgressArc  

## Overview  
ProgressArc is a **customizable hierarchy diagram tool** designed to help users **track project progress, organize study revisions, and visualize structures** in a clear, structured format. Whether you're managing a software development roadmap, tracking revision progress for exams, or presenting a structured workflow, ProgressArc provides an intuitive way to map out dependencies and milestones.  

## Features  
✅ **Customizable Hierarchy Diagram** – Easily create and modify diagrams for project tracking, study plans, and structured presentations.  
✅ **Microservices Architecture** – Backend services are decoupled into separate **Flask** microservices, enhancing scalability and maintainability.  
✅ **User Authentication & API Services** – Secure login, registration, and API endpoints managed independently.  
✅ **MongoDB Database** – Ensures fast and flexible data storage for structured and unstructured data.  
✅ **Vue3 Frontend** – A responsive and interactive UI, leveraging Vue3 for dynamic data visualization.  
✅ **Multi-Use Case** – Can be used for personal study tracking, team project planning, or as a **visual aid** for structured presentations.  

## Tech Stack  
- **Backend**: Python (Flask)  
- **Frontend**: Vue3  
- **Database**: MongoDB  
- **Architecture**: Microservices (Flask applications for login, registration, API calls)  

## Inspiration  
ProgressArc was inspired by my experience working with **Kubernetes microservices architecture** during the **NUS Summer Workshop** in 2024. The goal was to build a flexible and scalable project-tracking tool that could be used across different domains.  

## Project Setup  

### Frontend  
```sh
npm install
npm run dev
```  

### Backend  

1. In the `backend` directory, create and activate a virtual environment:  

   - Windows:  
     ```sh
     python -m venv .venv
     .venv/Scripts/activate
     ```  
   - MacOS/Linux:  
     ```sh
     python -m venv .venv
     source .venv/bin/activate
     ```  

2. Install dependencies:  
   ```sh
   pip install -r requirements.txt
   ```  

3. Configure environment variables in `.env`:  
   ```
   MONGO_URI=<SECRET>
   FLASK_SECRET_KEY=<SECRET>
   ```  

4. Run the microservices (multiple terminals needed):  
   ```sh
   flask --app auth_service/auth.py --debug run
   flask --app project_service/project.py --debug run -p 5001
   ```  
   - Authentication service starts at **port 5000**  
   - Project service starts at **port 5001**  

---