"""tripexpensetracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from tripexpensetracker.tripexpensetrackerapi.views.category_view import CategoryView
from tripexpensetracker.tripexpensetrackerapi.views.expense_category_view import ExpenseCategoryView
from tripexpensetracker.tripexpensetrackerapi.views.expense_view import ExpenseView
from tripexpensetracker.tripexpensetrackerapi.views.trip_view import TripView
from tripexpensetracker.tripexpensetrackerapi.views.user_view import UserView
from tripexpensetracker.tripexpensetrackerapi.views.user_auth import check_user, register_user


router = routers.DefaultRouter(trailing_slash=False)

router.register(r'users', UserView, 'user')
router.register(r'trips', TripView, 'trip')
router.register(r'expenses', ExpenseView, 'expense')
router.register(r'expensecategories', ExpenseCategoryView, 'expensecategory')
router.register(r'categories', CategoryView, 'category')

urlpatterns = [
    path('', include(router.urls)),
    # Authentication-related paths
    path('checkuser', check_user, name='check-user'),
    path('register', register_user, name='register-user'),
    path('trips/<int:pk>/add_expense', TripView.as_view({'post': 'add_trip_expense'}), name='trip-add-expense'),
    path('trips/<int:pk>/remove_trip_expense', TripView.as_view({'delete': 'remove_trip_expense'}), name='trip-remove-expense'),
]
