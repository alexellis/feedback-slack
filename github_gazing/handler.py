import requests
import json

def send_url(url, msg):
    try:
        r = requests.post(url, data=msg)
        print(url +" => " + str(r.status_code))
    except Exception as err:
        print(err)
    print msg

def build_summary(events, icon):
    msg = ""
    tally = {}

    user_list = {}

    for star in events:    
        repo_name = star["repo_name"]
        if not repo_name in tally:
            tally[repo_name] = 0
            user_list[repo_name] = []

        tally[repo_name] = tally[repo_name] + 1
        user_list[repo_name].append(star["user_name"])

    for repo in tally:
        msg = msg + ( (":" + icon + ":") * tally[repo] ) + " - " + repo  + "\n"
        msg = msg + "By: "+ " ".join(user_list[repo]) + "\n\n"

    return msg

def handle(req):
    msg = ""
    url = "http://gateway:8080/function/dockerbot"
    event = json.loads(req)

    # {"stars":[{"id":"5789016709","repo_name":"alexellis/faas","user_name":"nxnfufunezn","created_at":"2017-05-01T19:58:43Z"}],"forks":[{"id":"5789006050","repo_name":"alexellis/sshdkit","user_name":"zanetworker","created_at":"2017-05-01T19:57:04Z"}]}

    msg = msg + build_summary(event["stars"], "star")
    msg = msg + build_summary(event["forks"], "open_file_folder")

    req =  {"message": {"body":msg, "subject": ""}, "icon_emoji": ":stars:", "bot_name": "github_gazing bot" }

    send_url(url, json.dumps(req))
