
from django.conf.urls import url
from django.contrib import admin
from Remote_User import views as remoteuser
from Service_Provider import views as serviceprovider
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', remoteuser.login, name="login"),
    url(r'^Register1/$', remoteuser.Register1),
    url(r'^Predict_CyberThreat_Type/$', remoteuser.Predict_CyberThreat_Type),
    url(r'^train_model/$', serviceprovider.train_model),
    url(r'^federated_aggregation/$', serviceprovider.federated_aggregation),
    url(r'^Download_Trained_DataSets/$', serviceprovider.Download_Trained_DataSets),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
