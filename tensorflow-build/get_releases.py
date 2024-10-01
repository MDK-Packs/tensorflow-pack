
import requests
from datetime import datetime

def get_release_history():
    url = f"https://api.github.com/repos/MDK-PACKS/tensorflow-pack/releases"
    releases = []
    page = 1
    
    while True:
        response = requests.get(f"{url}?page={page}&per_page=100")
        if response.status_code == 200:
            page_releases = response.json()
            if not page_releases:
                break
            releases.extend(page_releases)
            page += 1
        else:
            print(f"Error fetching releases: {response.status_code}")
            break
    
    return releases

release_history = get_release_history()

for release in release_history:
    if 'nightly' in release['tag_name']:
        continue
    formatted_date = datetime.strptime(release['published_at'], "%Y-%m-%dT%H:%M:%SZ").date().strftime("%Y-%m-%d")
    print(
            "<release version=\""+release['tag_name']+"\" url=\"https://github.com/MDK-Packs/tensorflow-pack/releases/download/"
            +release['tag_name']+"/tensorflow.tensorflow-lite-micro."+release['tag_name']+".pack\" date=\""+formatted_date+"\">"
            +release['body'] + "</release>"
    )
