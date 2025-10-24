"""
URL configuration for KanithaProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# ใน KanithaProject/urls.py
# KanithaProject/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.shortcuts import redirect

# **สำคัญ: นำเข้า view ฟังก์ชันที่ใช้ในไฟล์นี้โดยตรง**
from student_data.views import user_login, user_register, user_logout 

urlpatterns = [
    # --------------------------------------------------------
    # 1. ROOT PATH & AUTHENTICATION
    # --------------------------------------------------------
    # หน้าหลัก / ให้ redirect ไปหน้า Login
    path('', lambda request: redirect('login'), name='root'), 
    
    # Authentication (ใช้ฟังก์ชันที่ import ตรงๆ)
    path('login/', user_login, name='login'),      
    path('register/', user_register, name='register'), 
    path('logout/', user_logout, name='logout'),    
    
    # --------------------------------------------------------
    # 2. APPLICATION & ADMIN
    # --------------------------------------------------------
    path('admin/', admin.site.urls),
    
    # --- รองรับพิมพ์ผิด common typos: 'datal' → redirect ไปยัง 'data' ---
    path('datal/login/', RedirectView.as_view(url='/data/login/', permanent=False)),
    path('datal/register/', RedirectView.as_view(url='/data/register/', permanent=False)),
    path('datal/logout/', RedirectView.as_view(url='/data/logout/', permanent=False)),
    path('datal/', RedirectView.as_view(url='/data/', permanent=False)),
    # --- end typo redirects ---

    # ให้รองรับ /user/ และ /user/login/ โดย redirect ไปยังหน้าใน app student_data
    path('user/', RedirectView.as_view(url='/data/profile/', permanent=False)),
    path('user/login/', RedirectView.as_view(url='/data/login/', permanent=False)),
    
    # นำเข้า URL ทั้งหมดจาก student_data (ทั้ง Frontend และ API)
    # ทำให้ URL ทั้งหมดเริ่มต้นด้วย /data/
    path('data/', include('student_data.urls')), 
]