import requests
from flask import Flask
from mako.template import Template
from mako.lookup import TemplateLookup

app = Flask(__name__)
template_lookup = TemplateLookup(directories=['templates'])

@app.route("/starred_repos")
def get_starred_repos():
    get_starred_repos_template = Template(filename="templates/get_user.mako", lookup=template_lookup)
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
    starred_repos_template = Template(filename="templates/starred_repos.mako", lookup=template_lookup)
    return starred_repos_template.render(repos=repo_names, user=username)