import requests
from flask import Flask
from mako.template import Template
from mako.lookup import TemplateLookup

app = Flask(__name__)
template_lookup = TemplateLookup(directories=['templates'])

@app.route("/starred_repos")
def get_starred_repos():
    get_starred_repos_template = template_lookup.get_template("get_user.mako")
    return get_starred_repos_template.render()

@app.route("/starred_repos/<username>")
def show_starred_repos(username):
    r = requests.get(f'https://api.github.com/users/{username}/starred')
    json_resp = r.json()
    repo_names= [
        {
            'name': repo['name'],
            'url': repo['html_url']
        }
        for repo in json_resp
    ]
    starred_repos_template = template_lookup.get_template("starred_repos.mako")
    return starred_repos_template.render(repos=repo_names, user=username)