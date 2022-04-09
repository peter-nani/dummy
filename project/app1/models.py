from django.db import models

from datetime import datetime, timezone

# Create your models here.


class aci_logs(models.Model):
	aci_name = models.CharField(max_length=2000)
	Datetime = models.DateTimeField(default=datetime.now(timezone.utc))