from django.db import models

# Create your models here.


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True,
                               on_delete=models.CASCADE,
                               null=True)
    parent_menu = models.ForeignKey('Menu',
                               on_delete=models.CASCADE)
    scr = models.CharField(max_length=300, blank=True)

    def __str__(self):
        if self.parent:
            return f"{self.parent_menu.name}-{self.parent.name}-{self.name}"
        else:
            return f"{self.parent_menu.name}-{self.name}"

    def save(self, *args, **kwargs):
        if self.parent:
            self.scr = f"{self.parent.scr}/{self.name}"
        else:
            self.scr = f"{self.parent_menu}/{self.name}"
        return super(MenuItem, self).save(*args, **kwargs)

    def create(self, *args, **kwargs):
        return super(MenuItem, self).save(*args, **kwargs)

class Menu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

