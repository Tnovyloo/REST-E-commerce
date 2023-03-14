from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils.functional import cached_property

from products.models import Product
from users.models import Address