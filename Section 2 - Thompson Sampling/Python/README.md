# Thompson Sampling

## Definition

Thompson sampling is an algorithm for online decision problems where actions are taken sequentially in a manner that
must balance between exploiting what is known to maximize immediate performance and investing to accumulate
new information that may improve future performance. The
algorithm addresses a broad range of problems in a computationally efficient manner and is therefore enjoying wide
use.

Thompson Sampling (also sometimes referred to as the Bayesian Bandits algorithm) takes a slightly different approach; rather than just refining an estimate of the mean reward it extends this, to instead build up a probability model from the obtained rewards, and then samples from this to choose an action.

## Our Use Case

Here we are using a dataset containing detail of different types of Ads prepared by advertisement for selling a car and then we collected click through rate of the ads for lots of users. The cells of dataset contains if user clicks on the partiular Ad or not.
We try to train our model by performing UCB learning to predict whether a particular add is suitable for advertisement purpose or not and which one is the best one.

## Test Our Model

You can test our model by going to our Google Collab session and upload attached dataset in that session and run all cells to visualize the results.
Link to collab : [https://colab.research.google.com/drive/1ZYz8PWX2wf9oImdO0o3bZd_Bj_EwWIpn?usp=sharing](https://colab.research.google.com/drive/1ZYz8PWX2wf9oImdO0o3bZd_Bj_EwWIpn?usp=sharing)

## Results 

On running the Model you will see simillar results as shown below with our given dataset. If you wish to upload your own dataset you can rename and restructure that dataset as ours and upload it to session to view results.

### Test Result

<p align="center"><img src="/docs/img/sampline.png" alt="slr"></p>

## Contribute

You can directly create a PR through which you can tell us your intrest and contributing area.

