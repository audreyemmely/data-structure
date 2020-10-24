class CsvModel:

    def __init__(self, csvRow):
        self.video_id = csvRow[0]
        self.trending_date = csvRow[1]
        self.title = csvRow[2]
        self.channel_title = csvRow[3]
        self.category_id = csvRow[4]
        self.publish_time = csvRow[5]
        self.tags = csvRow[6]
        self.views = csvRow[7]
        self.likes = csvRow[8]
        self.dislikes = csvRow[9]
        self.comment_count = csvRow[10]
        self.tumbnail_link = csvRow[11]
        self.comments_disabled = csvRow[12]
        self.rating_disabled = csvRow[13]
        self.video_error_or_removed = csvRow[14]
        self.description = csvRow[15]


    def __str__(self):
        return ('video_id: '+ self.video_id +' // trending_date: '+ self.trending_date +' // title: '+ self.title +
        ' // channel_title: '+ self.channel_title +' // publish_time: '+ self.publish_time + ' // views: '+ self.views +
        ' // likes: '+ self.likes +' // dislikes: '+ self.dislikes +'\n')