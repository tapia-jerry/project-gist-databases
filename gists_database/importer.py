import requests
import json

def import_gists_to_database(db, username, commit=True):
    response = requests.get("https://api.github.com/users/{USERNAME}/gists".format(USERNAME=username))
    response.raise_for_status()
    gists_data = response.json()
    
    for gist in gists_data:
        gists_dict = {
            "github_id": gist['id'],
            "html_url": gist['html_url'],
            "git_pull_url": gist['git_pull_url'],
            "git_push_url": gist['git_push_url'],
            "commits_url": gist['commits_url'],
            "forks_url": gist['forks_url'],
            "public": gist['public'],
            "created_at": gist['created_at'],
            "updated_at": gist['updated_at'],
            "comments": gist['comments'],
            "comments_url": gist['comments_url']}
        db.execute("""
            INSERT INTO gists ("github_id", "html_url", "git_pull_url", "git_push_url", "commits_url", "forks_url", "public", "created_at", "updated_at", "comments", "comments_url") 
            VALUES (:github_id,:html_url,:git_pull_url,:git_push_url,:commits_url,:forks_url,:public,:created_at,:updated_at,:comments,:comments_url)
        """,gists_dict)
    if commit:
        db.commit()