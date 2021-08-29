import requests


def download_image(url, file_path):
  r = requests.get(url, stream=True)

  if r.status_code == 200: #リクエストが成功した場合、画像ファイルを作成する処理を行う
    with open(file_path, "wb") as f: #対象のファイルを書き込み用かつバイナリモードで開く withを使用することで処理後に自動的にファイルのクローズも行う
      f.write(r.content) #テキストデータではなく画像データのため、content属性として書き込みを行う

def main():

  with open("ids.txt", "r") as f: #ids.txtを読み込み用で開く withを使用することで処理後に自動的にファイルのクローズも行う
    lines = [x.strip() for x in f.readlines()] #ids.txtから1行づつ取り出し、空白を削除したのち"lines"に配列として代入していく
    print(lines)

  for video_id in lines:
    url = "http://img.youtube.com/vi/{}/maxresdefault.jpg".format(video_id)

    download_image(url=url, file_path="images/thumbnails/{}.jpg".format(video_id))


main()