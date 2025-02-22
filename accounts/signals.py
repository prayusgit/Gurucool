from django.db.models.signals import post_save
from django.contrib.auth.models import Group, User


def create_student(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.filter(name='student')
        if group.exists():
            group = group.first()
            instance.groups.add(group)


post_save.connect(create_student, sender=User)
