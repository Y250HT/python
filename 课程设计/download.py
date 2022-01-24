import requests
def download(src):
    img_resp = requests.get(src)
    img_name = src.split("/")[-1]
    with open(img_name, mode="wb") as f:
        f.write(img_resp.content)