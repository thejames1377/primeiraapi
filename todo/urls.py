from rest_framework import routers
from .views import todolistViewset, PessoaViewset

router = routers.DefaultRouter()
router.register(r'lista',todolistViewset)
router.register(r'pessoa',PessoaViewset)
urlpatterns = router.urls