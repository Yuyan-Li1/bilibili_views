from bilibili_api import video

# put BVs in BV.txt
file = open('BV.txt', 'r')
while True:
    bv = file.readline()
    if not bv:
        break
    v = video.get_video_info(bvid=bv.rstrip())
    title = v['title']
    views = v['stat']['view']
    likes = v['stat']['like']
    comments = v['stat']['reply']
    print(f"Title: {title}")
    print(f"    Views: {views}")
    print(f"    Likes: {likes}")
    print(f"    Comments: {comments}")
