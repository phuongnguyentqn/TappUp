"""
Base Model
"""
from django.db import models
from django.utils.timezone import now


class BaseModel(models.Model):
    """
    Base Model of Grasshopper Apps
    """
    id = models.BigAutoField(primary_key=True)
    created_date = models.DateTimeField(default=None)
    modified_date = models.DateTimeField(default=None)

    class Meta:
        abstract = True

    def save(self):
        """
        Override to generate create/update time on save
        """
        if not self.id:
            self.created_date = now()
        self.modified_date = now()
        return super().save()
