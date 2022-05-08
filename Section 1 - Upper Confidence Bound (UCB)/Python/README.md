# Upper Confidence Bound

## Definition

UCB is a deterministic algorithm for Reinforcement Learning that focuses on exploration and exploitation based on a confidence boundary that the algorithm assigns to each machine on each round of exploration. (A round is when a player pulls the arm of a machine).

It is used whenever we need to fulfil following goals :

  -  When an agent chooses an action that currently has the largest estimated value. The agent exploits its current knowledge by choosing the greedy action.
  - When the agent does not choose the largest estimated value and sacrifice immediate reward hoping to gain more information about the other actions. 
  - It allows the agent to improve its knowledge about each action. Hopefully, leading to a long-term benefit.
  - It allows the agent to choose the greedy action to try to get the most reward for short-term benefit. A pure greedy action selection can lead to sub-optimal behaviour.

Here agent learns the consequences of its actions through trial and error, rather than being explicitly told the correct action.

## Our Use Case

Here we are using a dataset containing detail of different types of Ads prepared by advertisement for selling a car and then we collected click through rate of the ads for lots of users. The cells of dataset contains if user clicks on the partiular Ad or not.
We try to train our model by performing UCB learning to predict whether a particular add is suitable for advertisement purpose or not and which one is the best one.

## Test Our Model

You can test our model by going to our Google Collab session and upload attached dataset in that session and run all cells to visualize the results.
Link to collab : [https://colab.research.google.com/drive/1LczUZeQAzASzzlkx5wHn1hw7qwc8hAdL?usp=sharing](https://colab.research.google.com/drive/1LczUZeQAzASzzlkx5wHn1hw7qwc8hAdL?usp=sharing)

## Results 

On running the Model you will see simillar results as shown below with our given dataset. If you wish to upload your own dataset you can rename and restructure that dataset as ours and upload it to session to view results.

### Test Result

<p align="center"><img src="/docs/img/ucb.png" alt="slr"></p>

## Contribute

You can directly create a PR through which you can tell us your intrest and contributing area.

