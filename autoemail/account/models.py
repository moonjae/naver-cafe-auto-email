from django.db import models
from functions.naver_cafe_crawler import Naver_Cafe_Crawler
# Create your models here.




class Cafe(models.Model):
    url = models.CharField(
        max_length=80,
        blank=True,
        null=True,
        unique=True,
    )


    def __str__(self):
        return self.url

class EmailManager(models.Manager):
    def crawl(self, url):
        Cafe_crawler = Naver_Cafe_Crawler()
        account_list =Cafe_crawler.scrape(url)
        Cafe.objects.update_or_create(
            url=url,
        )
        for account in account_list:
            self.update_or_create(
                account= account,
                defaults={
                    'cafe': Cafe.objects.get(url=url),
                }
            )




class Email_Address(models.Model):
    account = models.CharField(
        max_length=40,
        blank=True,
        null=True,
        unique=True,
    )
    cafe = models.ForeignKey(
        Cafe,
        on_delete=models.CASCADE
    )
    objects = EmailManager()


    def __str__(self):
        return self.account
