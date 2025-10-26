# 📰 APROKO_BLOG

**APROKO_BLOG** is a social media blogging platform built with **Django** and **Django REST Framework (DRF)**.  
It provides a backend API for user authentication, profile management, blog posts, comments, and likes.  

This project can serve as a foundation for a capstone project or as the backend for a social blogging/social media application.

This project will have create an easy access to a firsthand information, ranging from entertainment news, fashion and lifestyle to mention but a few.
---

## 🚀 Features

- **User Authentication & JWT Tokens**  
  - User registration, login, refresh token  
  - JWT authentication (using SimpleJWT)

- **User Profiles**  
  - One-to-one `Profile` with avatar & bio  
  - Public profile view by username  
  - Update own profile

- **Blog Posts**  
  - Create, read, update, delete (CRUD) posts  
  - Search posts by title, content, or author  
  - Pagination support

- **Comments**  
  - Add comments to posts  
  - Retrieve comments for each post  
  - Edit/delete own comments

- **Likes**  
  - Clinch like/unlike on posts  
  - Count likes on posts  
  - See who liked a post

---

## 🛠️ Tech Stack

- **Backend**: Django 4.x, Django REST Framework  
- **Authentication**: JWT (djangorestframework-simplejwt)  
- **Database**: SQLite (default, can be swapped for PostgreSQL/MySQL)  
- **Media**: Django `ImageField` (requires Pillow)  
- **Deployment**: Works with Heroku, Render, or Docker (future setup)  

---

## 📂 Project Structure

