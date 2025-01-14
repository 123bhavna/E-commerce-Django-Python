from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPasswordResetForm,MyPasswordChangeForm,MySetPasswordForm
from django.urls import path
from .views import add_to_wishlist, remove_from_wishlist

urlpatterns = [
  
    # path("",views.home),
    path('',views.ProductView.as_view(), name='home'),
    
    path('merchandise/', views.merchandise, name='merchandise'),
    path('merchandise/<slug:data>', views.merchandise, name='merchandisedata'),

    path('Women/', views.Women, name='Women'),
    path('Women/<slug:data>', views.Women, name='Womendata'),
    
    path('accessory/', views.accessory, name='accessory'),
    path('accessory/<slug:data>', views.accessory, name='accessorydata'),
    
    path('books/', views.books, name='books'),
    path('books/<slug:data>', views.books, name='booksdata'),
    
    path('stationary/', views.stationary, name='stationary'),
    path('stationary/<slug:data>', views.stationary, name='stationarydata'),

    path('electronics/', views.electronics, name='electronics'),
    path('electronics/<slug:data>/', views.electronics, name='electronicsdata'),
    
    # path('save-review/', views.save_review, name='ele'),
    
      
    path("about", views.AboutView.as_view(),name="about"),
    path("category/<slug:val>", views.CategoryView.as_view(),name="category"),

    path("product-detail/<int:pk>", views.ProductDetail.as_view(),name="product-detail"),

    path("product-detail1/<int:pk>", views.ProductDetail1.as_view(),name="product-detail1"),
    path("product-detail2/<int:pk>", views.ProductDetail2.as_view(),name="product-detail2"),
    path("product-detail3/<int:pk>", views.ProductDetail3.as_view(),name="product-detail3"),
    path("product-detail4/<int:pk>", views.ProductDetail4.as_view(),name="product-detail4"),
    path("product-detail5/<int:pk>", views.ProductDetail5.as_view(),name="product-detail5"),
    path("product-detail6/<int:pk>", views.ProductDetail6.as_view(),name="product-detail6"),
    
    path('save-review<int:pid>', views.save_review, name='save-review'),

    path("add-to-cart/", views.add_to_cart,name="add-to-cart"),
    path("cart/", views.show_cart,name="showcart"),
    path("reviewsuccess/", views.reviewsuccessView.as_view(),name="reviewsuccess"),
    path("checkout/", views.checkout.as_view(),name="checkout"),
    
    path("search/", views.search,name="search"),
    
    
    path("pluscart/", views.plus_cart),
    path("minuscart/", views.minus_cart),
    path("removecart/", views.remove_cart),
   
    
    
    path("FAQs/", views.FAQsView.as_view(), name="FAQs" ),
    path("terms/",views.termsView.as_view(), name="terms"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
 
 
 
    
    
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address/',views.address,name='address'),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(),name='updateAddress'),
    
    path('registration/', views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login'),
    
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone'),name='passwordchange'),   
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('logout/', auth_view.LogoutView.as_view(next_page='/'), name='logout'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetView.as_view(template_name='app/password_reset_done.html',form_class=MyPasswordResetForm),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetView.as_view(template_name='app/password_reset_confirm.html',form_class=MyPasswordResetForm),name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetView.as_view(template_name='app/password_reset_complete.html',form_class=MyPasswordResetForm),name='password_reset_complete'),
    path("add-to-wishlist/", views.add_to_wishlist,name="add-to-wishlist"),
    path("wishlist/", views.show_wishlist,name="showwishlist"),
   
    path("removewishlist/", views.remove_wishlist),
   
    path('add-to-wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:product_id>/', remove_from_wishlist, name='remove_from_wishlist'),
    path("removewishlist/", views.remove_wishlist),
 
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("registration/", views.CustomerRegistrationView.as_view(), name="customerregistration"),
    path("accounts/login/", auth_view.LoginView.as_view(template_name="app/login.html", authentication_form=LoginForm), name="login"),
    path("password-reset/", auth_view.PasswordResetView.as_view(template_name="app/password_reset.html", form_class=MyPasswordResetForm), name='password_reset'),   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
