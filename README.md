# feedback-slack

Serverless FaaS functions for sending feedback from social media to Slack.

**What's here?**

* [forward_slack](./forward_slack/) - sends messages to a Slack webhook endpoint

* [github_gazing](./github_gazing/) - accepts incoming webhooks via the [Github Gazing project](https://github.com/alexellis/github_gazing) and forwards them to the Slack function

**How can I use it?**

* Deploy [FaaS](https://github.com/alexellis/faas) to your Swarm or K8s cluster

* Get the [FaaS CLI](https://github.com/alexellis/faas-cli) if you don't have it yet

* Get a webhook ID/token from Slack

* Create functions.yml via functions.example.yml and update with your webhook ID

* Build/deploy your functions

```
$ faas-cli -action build -f ./functions.yml
$ faas-cli -action push -f ./functions.yml
$ faas-cli -action deploy -f ./functions.yml
```
