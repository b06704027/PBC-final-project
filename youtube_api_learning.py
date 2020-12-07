from apiclient.discovery import build
import datetime as dt

api_key = "AIzaSyA7KHer89wcFm6wab12ZXnNGZm7AGsdHCU"
youtube = build('youtube', 'v3', developerKey=api_key)
# print(type(youtube))

# 轉成 RFC 3339 formatted date-time value 年-月-日T時:分:秒+(-)時區
start_time = dt.datetime(year=2020, month=12, day=1).strftime('%Y-%m-%dT%H:%M:%SZ')
end_time = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
# print(start_time, end_time)

# q代表搜尋的關鍵字(可以加上聯集跟差集) 其他可用參數: publishedAfter、order
req = youtube.search().list(part='snippet', q='2020 MAMA -BTS', type='video',
                            publishedAfter=start_time, publishedBefore=end_time, maxResults=50)
# print(type(req))
res = req.execute()
# print(res)
# print(res['items'][0])
list_items = sorted(res['items'], key=lambda x: x['snippet']['publishedAt'])
# for i in list_items:
#     print(i['snippet']['title'], i['snippet']['publishedAt'], i['id']['videoId'])

'''從channel中獲取所有影片'''


def get_channel_videos(channel_id):
    # get Uploads playlist id
    res = youtube.channels().list(id=channel_id,
                                  part='contentDetails').execute()
    # print(res)
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    videos = []
    next_page_token = None

    while True:
        res = youtube.playlistItems().list(playlistId=playlist_id, part='snippet',
                                           maxResults=50, pageToken=next_page_token).execute()
        # print(type(res))
        videos += res['items']
        next_page_token = res.get('nextPageToken')

        if next_page_token is None:
            break

    return videos


videos = get_channel_videos('UCtYjRhIDoaXqCTDyodYv6VQ')
# print(videos)
'''得到影片的統計資料'''


def get_videos_stats(video_ids):
    stats = []
    for i in range(0, len(video_ids), 50):  # 因為一次最多只能查五十個
        res = youtube.videos().list(id=','.join(video_ids[i:i + 50]),
                                    part='statistics').execute()
        # print(res['items'])
        stats += res['items']  # list += 是只有把裡面的值加進來
    # print(type(stats))
    return stats


video_ids = list(map(lambda x: x['snippet']['resourceId']['videoId'], videos))
# print(video_ids)
# print(len(video_ids))
stats = get_videos_stats(video_ids)
# print(stats)
most_disliked = sorted(stats, key=lambda x: int(x['statistics']['dislikeCount']), reverse=True)
for video in most_disliked:
    print(video['id'], video['statistics']['dislikeCount'])

