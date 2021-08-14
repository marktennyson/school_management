from django.db import models
from datetime import datetime
import typing as t

class Student(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)    
    standard = models.CharField(max_length=10, blank=False, null=False)
    roll_no = models.IntegerField(null=False, blank=False, unique=True)
    gender = models.CharField(max_length=1, blank=False, choices=(('M', 'Male'), ('F', 'Female')))
    dob = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now)
    is_active = models.BooleanField(default=True)
    
    def to_dict(self) -> t.Dict[str, t.Any]:
        return dict(
            id = self.pk,
            name = self.name,
            standerd = self.standard,
            roll_no = self.roll_no,
            gender = self.gender,
            dob = self.dob,
            created_at = self.created_at,
            is_active = self.is_active,
        )
    
    def __str__(self):
        return f"<{self.name}/{self.roll_no}>"