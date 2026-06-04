Facebook_posts = [
    {
        'likes': 120,
        'shares': 50,
        'comments': 20
    },
    {
        'comments': 40
    },
    {
        'likes': 150,
        'shares': 60,
        'comments': 30
    },
    {
        'likes': 300
    },
    {
        'shares': 100,
        'comments': 50
    },
    {
        'likes': 180,
        'comments': 25
    },
    {
        'shares': 90,
        'comments': 35
    }
]

total_likes = 0
for post in Facebook_posts:
    try:
        total_likes += post['likes']
    except KeyError:
        pass
    
print(total_likes)