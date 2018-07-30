import requests

def import_gists_to_database(db, username, commit=True):
    try:
        ## get gists
        req = requests.get('https://api.github.com/users/{}/gists'.format(username))
        data = req.json()
    except:
        raise requests.HTTPError
    
    for gist in data:
        ## iterate over gists
        db.execute("INSERT INTO gists VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
        [ None, gist["id"], gist["html_url"],
        gist["git_pull_url"], gist["git_push_url"], gist["commits_url"],
        gist["forks_url"], gist["public"], gist["created_at"],
        gist["updated_at"], gist["comments"], gist["comments_url"] ])
