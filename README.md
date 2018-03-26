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
  <img src="https://github.com/moonjae/naver-cafe-auto-email/blob/master/Usage_Screetshot_Img/search.png" width="600"/>
</p>
*Cafe Search View 
The search bar accepts an url of Naver Cafes and the url is used to scrape the IDs. Then, the view creates Account objects, using the Ids.


<p align="center">
  <img src="https://github.com/moonjae/naver-cafe-auto-email/blob/master/Usage_Screetshot_Img/email.png" width="600"/>
</p>
*Cafe List View 
This view contains both email send form and list of Naver Cafe urls. When all the components of the email sending for mis filled out, by clicking a submit button below each url, you can sned emails to members of a designated Cafe via SMTP. Clicking one of the hyperlinked url will redirect you to another view that shows the list of Naver IDs.





## Limitations 
* This application uses selenium module when scraping the Naver IDs so it takes quite a bit of time when attempting to scrape multiple post board pages. 






## Built With

* [Pycharm](https://www.jetbrains.com/pycharm/) 
* Django 





## Authors

* **Jae Hyun Moon** 


