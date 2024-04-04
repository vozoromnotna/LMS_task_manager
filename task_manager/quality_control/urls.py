from django.urls import path, include
from .views import *

app_name = 'quality_control'

class_view = True

if class_view:
    urlpatterns = [
        path('', IndexView.as_view(), name="index"),
        path('bugs/', BugReportsListView.as_view(), name='bugs'),
        path('bugs/<int:bug_id>/', BugReportView.as_view(), name='bug_details'),
        path('bugs/add_bug_report/', BugReportCreateView.as_view(), name='bug_add'),
        path('bugs/<int:bug_id>/update/', BugReportUpdateView.as_view(), name='bug_update'),
        path('bugs/<int:bug_id>/delete/', BugReportDeleteView.as_view(), name='bug_delete' ),
        
        
        path('features/', FeatureRequestsListView.as_view(), name='features'),
        path('features/<int:feature_id>/', FeatureRequestView.as_view(), name='feature_details'),
        path('features/add_feature_request', FeatureRequestCreateView.as_view(), name='feature_add'),
        path('features/<int:feature_id>/update/', FeatureRequestUpdateView.as_view(), name='feature_update'),
        path('features/<int:feature_id>/delete/', FeatureRequestDeleteView.as_view(), name='feature_delete'),
    ]
else:
    urlpatterns = [
        path('', index , name="index"),
        
        path('bugs/', bugs, name='bugs'),
        path('bugs/<int:bug_id>/', bug_details, name='bug_details'),
        path('bugs/add_bug_report/', bug_add, name='bug_add'),
        path('bugs/<int:bug_id>/update/', bug_update, name='bug_update'),
        path('bugs/<int:bug_id>/delete/', bug_delete, name='bug_delete' ),
        
        path('features/', features, name='features'),
        path('features/<int:feature_id>/', feature_details, name='feature_details'),
        path('features/add_feature_request', feature_add, name='feature_add'),
        path('features/<int:feature_id>/update/', feature_update, name='feature_update'),
        path('features/<int:feature_id>/delete/', feature_delete, name='feature_delete'),
    ]
 