# naver-cafe-auto-email

Naver is currently the biggest search engine in South Korea. Naver Cafe platform is a platform that allows its members to share common ideas by posting their thoughts. 
This Django web application scrapes Naver IDs of members registered for a certain Cafe and sends emails to the members. 

## Prerequisites 
```
pip install requirements.txt
```

## Instructions

*Set .secrets folder at the same level as account and config folders
*Add secrets.json file to the folder 
*The json file should resemble something like below

```
{
  "SECRET_KEY": "**************************************'"
}
```

## Usage 
<p align="center">
  <img src="https://github.com/moonjae/naver-cafe-auto-email/blob/master/Usage_Screetshot_Img/search.png" width="350"/>
  <img src="https://github.com/moonjae/naver-cafe-auto-email/blob/master/Usage_Screetshot_Img/email.png" width="350"/>
</p>



## Limitations 
* This application uses selenium module when scraping the Naver IDs so it takes quite a bit of time when attempting to scrape multiple post board pages. 






## Built With

* [Pycharm](https://www.jetbrains.com/pycharm/) 
* Django 





## Authors

* **Jae Hyun Moon** 


