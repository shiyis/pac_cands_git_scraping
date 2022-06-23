# pac-issue-git-scraping
This project scrapes all the PAC candidates in the FEC database their personal/campaign facebook profile. 


By running a github action workflow defined in [cands-tw-feeds.yml](.github/workflows/cands-tw-feeds.yml) workflow, we will be able to get the data of the candidate

As of Jun 21st 2022, Due to a massive ban of the scrapers and bots of facebook, the scraping project scrapes twitter instead by using a **tweepy and an API** key. 

I created a tweeter API and a script. The script is written in Python using the tweepy package. Please refer to the []() for the scraping script.
![tw-api-interface](img/tw-api-interface.png)


Please also check out the **references and articles** I have gone over that are postentially pertaining to this research project. 

[endnote_references](endnote_references.txt)

And a huge thanks to this [medium article](https://dev.to/twitterdev/a-comprehensive-guide-for-using-the-twitter-api-v2-using-tweepy-in-python-15d9) that helps guide you through scraping data on tweeter using the tweepy package and their API key.

Turns out, in order to scrape all the tweets of a particular candidate, I needed **elevated access** of the Twitter development API and account, so I went ahead and created an account and responded to their questions (including what you are using the data for and whether if it's affiliated with any gov entities etc). The approval speed was rather quick for me. It didn't take long as I responded in email in the morning, and 30 minutes later I got an email updating that my request has been approved. 

<img src="https://github.com/shiyis/pac-cands-git-scraping/blob/main/img/tw-ea-email.png" width="500" height="400">

sample out file [aaron_lee.csv](aaron_lee.csv)
