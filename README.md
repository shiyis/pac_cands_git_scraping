# pac-issue-git-scraping
This project scrapes all the PAC candidates in the FEC database their **personal/campaign Twitter** timeline. 


By running a **github action** workflow defined in [cands-tw-feeds.yml](.github/workflows/cands-tw-feeds.yml) workflow, we will be able to get the data of the candidates.
#### Creating API key and secret
Oginally the project intended to scrape both facebook and twitter data. As of Jun 21st 2022, with a widespread ban of the scrapers and bots of facebook(due to security reasons), an upgrade in facebook's [Data Scraping Protocol](https://developers.facebook.com/docs/development/terms-and-policies/automated-data-collection/) and the easier usibility of twitter's [updated authentification API Auth V2](https://developer.twitter.com/en/docs/authentication/oauth-2-0), the scraping project has shifted its focus primarily in scraping Twitter data instead by using **tweepy (the Twitter package for Python) and an API key**. 

<img src="https://github.com/shiyis/pac-cands-git-scraping/blob/main/img/tw-api-interface.png" width="750" height="400">

And a huge thanks to this [medium article](https://dev.to/twitterdev/a-comprehensive-guide-for-using-the-twitter-api-v2-using-tweepy-in-python-15d9) that helps guide you through scraping data on tweeter using the tweepy package and their API key. Please refer to this article, if you have questions regarding how to set up an automation project in Twitter Developer platform.

Turns out, in order to scrape all the tweets of a particular candidate, I needed **elevated access** of the Twitter development API and account, so I went ahead and created an account and responded to their questions (including what you are using the data for and whether if it's affiliated with any gov entities etc). The approval speed was rather quick for me. It didn't take long as I responded in email in the morning, and 30 minutes later I got an email updating that my request has been approved. 

<img src="https://github.com/shiyis/pac-cands-git-scraping/blob/main/img/tw-ea-email.png" width="500" height="400">

#### Literature and references
Please also check out the **references and articles** I have gone over that are postentially pertaining to this research project. 

[endnote_references](endnote_references.txt)


#### Pulling data from Twitter
[twitter_data_pulling.ipynb](./twitter_data_pulling.ipynb) This jupyter notebook consists of the sample code that pulls data from a candidate's twitter account 

And here's the sample out file [christina_hagan.csv](./out.csv)
