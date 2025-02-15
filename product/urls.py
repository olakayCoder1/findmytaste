from django.urls import path

from product.views import ( 
    AddToFavoritesView,
    HotPickProductsView,
    OrderDetailView,
    OrderListCreateView,
    ProductBySystemCategoryView, 
    ProductByVendorCategoryView, 
    ProductDetailView, 
    SystemCategoryListView,
    UserFavoriteListView, 
    VendorDetailView
)


urlpatterns = [ 
    path('system-categories/', SystemCategoryListView.as_view(), name='system_categories'),
    path('hot-picks/', HotPickProductsView.as_view(), name='hot-pick-products'),
    path('product/system-category/<uuid:system_category_id>/', ProductBySystemCategoryView.as_view(), name='products_by_system_category'),
    path('product/<uuid:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('vendor/<uuid:vendor_id>/', VendorDetailView.as_view(), name='vendor_detail'),
    path('product/vendor-category/<uuid:vendor_category_id>/', ProductByVendorCategoryView.as_view(), name='products_by_vendor_category'),

    # Order Endpoints
    path('order/', OrderListCreateView.as_view(), name='create_list_order'),
    path('order/<uuid:order_id>/', OrderDetailView.as_view(), name='get_update_delete_order'),


    path('user/favorites/', UserFavoriteListView.as_view(), name='user_favorites_list'),
    path('user/favorites/<uuid:product_id>/', AddToFavoritesView.as_view(), name='add_to_favorites'),
]
