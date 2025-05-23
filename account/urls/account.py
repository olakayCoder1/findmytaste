from django.urls import path
from account.views.account import (
    NotificationListView, PasswordChangeView, ProfileImageUploadView, 
    UserAddressUpdateView, UserDetailView,
    UpdateVenderBankAccount, VendorAddressUpdateView
)


urlpatterns = [ 
    path('', UserDetailView.as_view(), name='user-profile'),
    path('profile/', UserDetailView.as_view(), name='current-user-profile'),
    path('profile-image-upload', ProfileImageUploadView.as_view(), name='ProfileImageUploadView'),
    path('delivery-address', UserAddressUpdateView.as_view(), name='current-user-address'),
    path('password/change/', PasswordChangeView.as_view(), name='password-change'),
    path('notification', NotificationListView.as_view(), name='password-change'),
    path('bank-account', UpdateVenderBankAccount.as_view(), name='password-change'),
    path('vendor/update-address/', VendorAddressUpdateView.as_view(), name='update-vendor-address'),
]
