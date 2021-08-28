import requests


def download_image(url, file_path):
  r = requests.get(url, stream=True)

  if r.status_code == 200: #リクエストが成功した場合、画像ファイルを作成する処理を行う
    with open(file_path, "wb") as f: #対象のファイルを書き込み用かつバイナリモードで開く withを使用することで処理後に自動的にファイルのクローズも行う
      f.write(r.content) #テキストデータではなく画像データのため、content属性として書き込みを行う

def main():

  with open("ids.txt", "r") as f: #抽出するサムネイルのurlを記載しているids.txtを指定する
    lines = [x.strip() for x in f.readlines()]
    print(lines)

  for video_id in lines:
    url = "http://img.youtube.com/vi/{}/maxresdefault.jpg".format(video_id)

    download_image(url=url, file_path="images/thumbnails/{}.jpg".format(video_id))
    

main()