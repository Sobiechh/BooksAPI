from rest_framework import routers

from .views import BookViewset, AuthorViewset, IsbnViewset

router = routers.DefaultRouter()
router.register(r"books", BookViewset)
router.register(r"authors", AuthorViewset)
router.register(r"isbns", IsbnViewset)
