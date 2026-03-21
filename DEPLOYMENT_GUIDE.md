# HRMS Deployment Guide

This guide explains how to deploy the HRMS application on **Render** (backend) and **Vercel** (frontend).

## Backend Deployment (Render)

### Prerequisites
- Render account (https://render.com)
- GitHub repository with your HRMS project

### Step 1: Prepare Your Repository
1. Push your project to GitHub
2. Make sure the following files are in your repository:
   - `Procfile` - in the root directory
   - `render.yaml` - in the root directory  
   - `backend/requirements.txt` - with all Python dependencies
   - `backend/main.py` - FastAPI application

### Step 2: Deploy Backend on Render
1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **New +** → **Web Service**
3. Connect your GitHub repository
4. Fill in the following details:
   - **Name**: `hrms-backend` (or any name)
   - **Runtime**: Python 3.11
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0`
   - **Plan**: Free tier (or upgrade as needed)

5. Click **Deploy Web Service**
6. Once deployed, copy your backend URL (e.g., `https://hrms-backend.onrender.com`)

### Step 3: Configure Environment Variables on Render
1. In the Render dashboard, go to your web service
2. Click on **Environment**
3. Add the following variables:
   ```
   FRONTEND_URL=https://your-vercel-frontend-url.vercel.app
   ```
4. Click **Save** to redeploy

---

## Frontend Deployment (Vercel)

### Prerequisites
- Vercel account (https://vercel.com)
- GitHub repository with your HRMS project

### Step 1: Prepare Your Frontend
1. Ensure your frontend has:
   - `frontend/package.json` with build scripts
   - `frontend/vercel.json` - deployment configuration
   - `frontend/.env.example` - environment variable template

2. Update `frontend/package.json` if needed to include `@react-scripts`:
   ```json
   "dependencies": {
     "react": "^18.2.0",
     "react-dom": "^18.2.0",
     "react-scripts": "^5.0.1",
     "axios": "^1.6.2",
     "react-router-dom": "^6.20.1"
   }
   ```

### Step 2: Deploy Frontend on Vercel
1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click **Add New** → **Project**
3. Import your GitHub repository
4. Configure the project:
   - **Framework**: React
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `build`

5. Click **Deploy**

### Step 3: Configure Environment Variables on Vercel
1. After deployment, go to your project settings
2. Click on **Environment Variables**
3. Add the following:
   ```
   REACT_APP_API_URL=https://your-render-backend-url.onrender.com
   ```
4. Redeploy the project to apply environment variables
   - Click **Deployments** → **Redeploy** → Confirm

---

## Environment Variables Summary

### Backend (.env)
```
DATABASE_URL=sqlite:///./hrms.db          # or your PostgreSQL URL
FRONTEND_URL=https://your-frontend-url    # Your Vercel frontend URL
```

### Frontend (.env.production)
```
REACT_APP_API_URL=https://your-backend-url  # Your Render backend URL
```

---

## Post-Deployment Checklist

- [ ] Backend API is accessible at `https://your-backend-url/docs`
- [ ] Frontend loads without CORS errors
- [ ] API calls from frontend work correctly
- [ ] Database operations are functional
- [ ] Employee management features work
- [ ] Attendance management features work
- [ ] Both services update in real-time without refresh

---

## Troubleshooting

### CORS Errors
If you see CORS errors in the browser console:
1. Check the `FRONTEND_URL` environment variable on Render
2. Check the `REACT_APP_API_URL` in Vercel environment variables
3. Both must match the actual deployed URLs

### Database Issues
- SQLite works locally but may have limitations on serverless platforms
- Consider using PostgreSQL for production: `postgresql://user:password@host:port/dbname`

### 404 on Frontend Routes
- Ensure `vercel.json` is configured with proper routing for React

### Slow Initial Load
- Free tier services on both platforms have cold starts
- Upgrade to paid tiers for better performance

---

## Database Migration (Optional for Production)

To use PostgreSQL instead of SQLite:

1. Create a PostgreSQL database
2. Update the DATABASE_URL:
   ```
   postgresql://username:password@hostname:5432/dbname
   ```
3. On Render, add this to Environment Variables
4. Redeploy backend

---

## Next Steps
- Monitor logs on both Render and Vercel dashboards
- Set up alerting for errors
- Consider adding authentication for API endpoints
- Implement logging and analytics
