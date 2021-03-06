# Voix

## Introduction:

An anonymous platform for uplifting communities and promoting civic participation. Social media platforms hold great power in how our society defines itself, we believe that this can be taken a step further. Social media has often been criticized for promoting self-obsession, we believe that it can however be used for communal betterment. We utilized some basic web dev tools to develop a space where people can find points of congruity between different communities. Social/Civic issues are always in the minds of the general public and irrespective of their beliefs and interests these issues still take a toll on them and therefore, we came up with a social media platform that utilizes privacy enabled machine learning to recover ideas affecting communities and bring them to the top of our platform. These are then explored by sentiment analysis for gauging public views on said topic, which is then reported to local/civic authorities.

## What it does?

The idea utilizes the concept of Unsupervised Clustering and Differential Privacy to predict common topics discussed across the social media platform. The utilization of Privacy Enabled Machine Learning (Differential Privacy) ensures a level of anonymity for users, thereby protecting their identities while still giving them a voice. Once hot/trending topics are picked up in this manner, we utilize a ranking system to promote these posts, which is easily viewable in the trending tab. Herein people discuss these topics in-depth, giving reference materials and having detailed discussions. We utilize a sentiment analyzer here, to pick up views/thoughts which contain different perspectives over the topic under discussion and these are further grouped in for debates. The interaction-count and negative-positive feedback are used to gauge public views on said topic, which can then be reported to public/civic authorities.

## How we built it?

We used Streamlit for creating our site. While building we utilized the concept of abstraction and inheritance to create a simple to understand infrastructure for our site. Streamlit is one of the few untapped tools for python enthusiasts, that allows one to quickly build highly interactive web applications around their data, machine learning models, and pretty much anything. However, deviating from that, we instead used Flask and the python requests library to create ourselves an interactive social-media platform.  

We used the federated averaging algorithm and laplacian noise implementation for creating a differential privacy system. The two combined provided a backdrop for anonymizing the users of our site, while we used an interaction counter hosted on our server per post. These two became the backbone for creating the trending tab on our platform.

The use of sentiment analysis using natural language processing for gauging intent and public significance further aided us in providing only the best support on our platform. We used Feed Forward Neural Networks for this task. By aggregating common points for discussion, we look into developing a constructive debate setting to discuss social views. 

## Challenges we ran into?

Word Embeddings are memory intensive and we used `Effective Dimensionality Reduction for Word Embeddings - Vikas Raunak et al.` to reduce memory demand. In our utilization of the above library we also contributed to the open-source community by creating an executable Python3 version of it. 

## What we learned?

Some of the key take-aways from developing this project underline our newfound love for developing for a supportive community. Developing a project which brought people closer instead of further apart. We also learnt a lot about social-media spaces and how large social media platforms have generated them due to their recommendation algorithms, our idea to use an unbiased, crowdsourced retrieval system for supplying posts on the trending tab may improve on this considerably. 

## What???s next for Voix?

In our developments for this project, we focused on maintaining a scalable nature for our product. For future development of this project, we are looking forward to increasing user growth as well as adding moderation. A tie-up with local/civic authorities directly would further push forward the people???s voice.
