from simple_image_download import simple_image_download as sid

response = sid.simple_image_download

response().download('bear', 5)
print(response().urls('bear', 5))
