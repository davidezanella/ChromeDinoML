# Chrome Dino ML

This is a simple experiment that aims to create a Deep Learning model capable to play the chrome Dino game.

To program this project I took inspiration from other online repos and articles.
I'm quite proud of the result considering that, with some deeper knowledge, the model can be tuned better and the result could be much better.

In this project is used a Deep Q-learning Network.

With just an hour of training, the model is able to reach a score of 600 with 500 tries.
With a total of 700 tries, it reaches 3894 as the higher score.

Analyzing the results of this experiment I think that using an approach with generations and genetic algorithms the result could be better.


## How to use the project
Clone the repo and install the requirements

```
pip install -r requirements.txt
```

Start the training process
```
python main.py
```
By default, it uses chromium on Linux. If you're using another OS simply adjust the chromium location in the dino.py file.

