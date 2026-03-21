# Deployment Checklist

Complete this checklist before deploying to Render and Vercel.

## Pre-Deployment

### Code Quality
- [ ] All code is committed to GitHub
- [ ] No console errors in local development
- [ ] API endpoints tested locally
- [ ] Frontend components work correctly
- [ ] No sensitive data in configuration files
- [ ] .env files are in .gitignore

### Backend Preparation
- [ ] main.py uses environment variables
- [ ] requirements.txt includes all dependencies
- [ ] Procfile exists and is correct
- [ ] render.yaml exists and is correct
- [ ] CORS is configured for frontend URL
- [ ] Database connection string is set

### Frontend Preparation
- [ ] package.json includes all required packages
- [ ] Build scripts are working: `npm run build`
- [ ] .env.example is updated with correct API URL
- [ ] vercel.json is configured correctly
- [ ] API calls use REACT_APP_API_URL environment variable
- [ ] No hardcoded API URLs in code

## Render Backend Deployment

### Account & Repository
- [ ] Render account created
- [ ] GitHub repository connected to Render
- [ ] Repository is public or Render has access

### Service Configuration
- [ ] Web service created on Render
- [ ] Python 3.11 runtime selected
- [ ] Build command: `pip install -r backend/requirements.txt`
- [ ] Start command: `uvicorn main:app --host 0.0.0.0`

### Environment Variables
- [ ] FRONTEND_URL set to Vercel frontend URL
- [ ] DATABASE_URL configured
- [ ] All required variables added

### Deployment
- [ ] Initial deployment successful
- [ ] No build errors in logs
- [ ] Service is running (showing "Live")
- [ ] Health check endpoint accessible
- [ ] Copy backend URL for frontend configuration

## Vercel Frontend Deployment

### Account & Repository
- [ ] Vercel account created
- [ ] GitHub repository connected to Vercel
- [ ] Repository is public or Vercel has access

### Project Configuration
- [ ] Project name set
- [ ] Framework: React selected
- [ ] Root Directory: frontend
- [ ] Build Command: `npm run build`
- [ ] Output Directory: build

### Environment Variables
- [ ] REACT_APP_API_URL set to Render backend URL
- [ ] Environment variable added for production
- [ ] Environment variable added for preview deployments

### Deployment
- [ ] Initial deployment successful
- [ ] Build completed without errors
- [ ] Frontend loads without errors
- [ ] Copy frontend URL for backend configuration

## Post-Deployment Verification

### API Connectivity
- [ ] Backend API is accessible
- [ ] Frontend can reach backend API
- [ ] CORS errors are not present
- [ ] API documentation available at /docs

### Application Features
- [ ] Home page loads correctly
- [ ] Can view employee list
- [ ] Can create new employee
- [ ] Can delete employee
- [ ] Can mark attendance
- [ ] Can view attendance records
- [ ] Form validations working
- [ ] Error messages appear correctly

### Data Persistence
- [ ] Employee data persists after refresh
- [ ] Attendance data is saved
- [ ] Database operations complete correctly

### Performance & Monitoring
- [ ] Initial page load time is acceptable
- [ ] No console errors in browser
- [ ] Render logs show no errors
- [ ] Vercel deployments show as successful

## Monitoring & Maintenance

### Ongoing Tasks
- [ ] Set up log monitoring on Render
- [ ] Set up performance monitoring on Vercel
- [ ] Regular database backups planned
- [ ] Update dependencies periodically
- [ ] Monitor error rates
- [ ] Plan for database migration if needed

### Optional Enhancements
- [ ] Set up custom domain for backend
- [ ] Set up custom domain for frontend
- [ ] Implement authentication/authorization
- [ ] Add database backups
- [ ] Set up email notifications
- [ ] Implement rate limiting
- [ ] Add API authentication tokens

## Rollback Plan

If deployment fails:
- [ ] Check deployment logs for errors
- [ ] Verify environment variables are correct
- [ ] Test API endpoints with Postman/Insomnia
- [ ] Check GitHub repository for correct branch
- [ ] Review recent code changes
- [ ] Rollback to previous version if needed
- [ ] Contact platform support if stuck

## Deployment URLs

After successful deployment, save these URLs:

**Backend (Render)**:
```
https://your-backend-name.onrender.com
API Docs: https://your-backend-name.onrender.com/docs
```

**Frontend (Vercel)**:
```
https://your-frontend-name.vercel.app
```

---

**Deployment Date**: _______________
**Deployed By**: _______________
**Notes**: _____________________________________________________
