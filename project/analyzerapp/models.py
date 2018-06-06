from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=25)
    apariciones = models.IntegerField(blank=True,null=True)
    insert_date = models.DateField(auto_now_add=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.word+": "+str(self.apariciones)+" - "+str(self.insert_date)