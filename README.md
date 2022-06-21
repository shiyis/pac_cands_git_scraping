# pac-issue-git-scraping
This project scrapes all the PAC candidates in the FEC database their personal/campaign facebook profile. 


By running a github action workflow defined in [cands-policies.yml](.github/workflows/cands-policies.yml) workflow, we will be able to get the data of the candidate

Due to a massive ban of the scrapers and bots of facebook, the scraping project scrapes twitter instead by using a tweepy and an API key. 

sample out file [aaron_lee.csv](aaron_lee.csv)
