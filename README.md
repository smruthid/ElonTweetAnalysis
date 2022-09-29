# Elon Tweet Analysis

---

## BACKGROUND

This is a multi-function jupyter lab notebook (stored as **sentiment_analyzer.ipynb**) that compares the sentiments of Elon Musk tweets versus stock market reactions from the individual stocks referenced in his tweets. Elon Musk, the richest man on Earth with over 107M followers on twitter, uses the platform to share his opinions, often controversial. In addition, Elon was charged with securities fraud by the SEC because of misleading tweets causing price fluctuations.

---

## PROJECT OVERVIEW

In this notebook we hope to answer the following questions:

* Does a correlation exist between Elons tweets and stock market reactions ?
* Is it possible to predict whether or not a stock with rise/fall/remain with the sentiment of his tweets? 
* Can we design a stock purchase method based on Elons tweets?

Bonus

* Do Elons tweets affect companies other than TSLA? (TEST: 'DOGE' + 'TWTR')
* Should we consider Elons tweet history on a certain company before investing?



---

## DATA SOURCES

**Datasets is provided by:**
* [Kaggle](https://www.kaggle.com/datasets/andradaolteanu/all-elon-musks-tweets)
* Yahoo Finance (yfinance)

**This project leverages python 3.7 with the following packages:**
* pandas
* scikit-learn
* yfinance
* hvplot


---

## INSTALLATION

1. Clone this repository by opening your terminal and entering the following commands:

```
  git clone https://github.com/smruthid/ElonTweetAnalysis.git
  cd ElonTweetAnalysis
```

2. After activating your preferred virtual env, install the required pre-requisites / libraries:

```
  pip install -r requirements.txt
```

3. Edit your .env file and populate the required credentials:

```
  MEANINGCLOUD_KEY=<insert your meaningcloud API key here>
  
  Obtain a key at [Meaningcloud](https://www.meaningcloud.com/developer/create-account)
  
```

## USAGE

This application runs as a Jupyter Notebook. Open your terminal, navigate to the folder you cloned from Github, and type:

```
  jupyter lab
```

---

## CONTRIBUTORS

[Smruthi Danda](https://github.com/smruthid)

[Ben Gunnels](https://github.com/miltiades-the-general)

[Greg Richardson](https://github.com/jgrichardson)

[Quianna Rolston](https://github.com/qrolston)

[Manisha Lal](https://github.com/ind-2004Manishalal)

[Zehra Vahidy](https://github.com/Zvahidy)



---

## License

The source code for the application is licensed under the MIT license, which you can find in the LICENSE file in this repo.

UC Berkeley Extension
Fintech Bootcamp '22