import requests


class Github:
    def __init__(self):
        self.api_url = "http://api.github.com"
        self.token = "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"

    def getUser(self, username):
        responce = requests.get(self.api_url + '/users/' + username)
        return responce.json()

    def getRepositories(self, username):
        responce = requests.get(self.api_url + '/users/' + username + '/repos')
        return responce.json()

    def createReppostory(self, name):
        responce=requests.post(self.api_url + '/user/repos?access_token=' + self.token, json={
             "id": 1296269,
             "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
             "name": name,
             "full_name": "octocat/Hello-World",
        })
        return responce.json()


github = Github()

while True:
    secim = input("1-Find User\n2-Get Repository\n3-Create Repository\n4-Exit\nSeçim : ")

    if secim == "4":
        break

    else:
        if secim == "1":
            username = input("username : ")
            result = github.getUser(username)
            print(f"name: {result['name']} public repos: {result['public_repos']} follower : {result['followers']}")

        elif secim == "2":

            username = input("username : ")
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name'])

        elif secim == "3":
            name=input("repostory nmae :")
            result=github.createReppostory(name)
            print(result)

        else:
            print("yanlış seçim")
