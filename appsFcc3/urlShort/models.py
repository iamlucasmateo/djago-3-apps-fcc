from django.db import models

class Url(models.Model):
    short = models.TextField()
    long = models.TextField()

    @classmethod
    def get_last_short_url(cls):
        return cls.objects.all().order_by("-short")[0].short
    
    @classmethod
    def shorten(cls, long_url):
        last = cls.get_last_short_url()
        if last[-1] == "z":
            new_url = last + "a"
        else:
            new_last_char = chr(ord(last[-1]) + 1)
            new_url = last[:-1] + new_last_char
        cls(None, new_url, long_url).save()
    
    @classmethod
    def long2short(cls, long_url):
        filter_object = cls.objects.filter(long=long_url)
        short_url = filter_object.values().get()["short"]
        return short_url
    
    @classmethod
    def short2long(cls, short_url):
        filter_object = cls.objects.filter(short=short_url)
        long_url = filter_object.values().get()["long"]
        return long_url

    def __str__(self):
        return f"URL. Short: {self.short}. Long: {self.long}"

