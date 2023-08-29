"""Django models utilities"""

# Django
from django.db import models

class CRideModel(models.Model):
    """Comparte Ride base model.
    
    CRideModel acts as an abstract base class from which every
    other model in the porject will inherit. This class provides
    every table with the fallowing atributes:
        + create (Datetime): Store the datetime the object was create
        + create (Datetime): Store the last datetime the object was create
       
    """
    
    created = models.DateTimeField(
        'create at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was modified.'
    )

    class Meta:
        """Meta option"""

        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']
