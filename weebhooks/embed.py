class Embed:
    """
    An embed object that can be used in a webhook message.

    Params:

    `title` (str): Title of the embed.
    
    `description` (str): Description of the embed.

    `url` (str): The URL of the embed.

    `timestamp` (ISO8601 timestamp): The timestamp of the embed content.

    `color/colour` (int): The color code to use for the embed.
    """
    def __init__(self, **options):
        self.title = options.get("title", None)
        self.description = options.get("description", None)
        self.url = options.get("url", None)
        self.timestamp = options.get("timestamp", None)
        self.color = options.get("color", None) or options.get("colour", None)
        self.fields = list()
        self.footer = None
        self.image = None
        self.thumbnail = None
        self.video = None
        self.results = {
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "timestamp": self.timestamp,
            "color": self.color,
            "fields": self.fields,
            "footer": self.footer,
            "image": self.image,
            "thumbnail": self.thumbnail,
            "video": self.video
        }


    def add_field(self, name=None, value=None, inline=True):
        data = {
            "name": name,
            "value": value,
            "inline": inline
        }
        self.fields.append(data)
        return self

    def set_footer(self, text=None, icon_url=None):
        self.footer = {
            "text": text,
            "icon_url": icon_url
        }
        return self

    def set_author(self, **options):
        name = options.get("name", None)
        url = options.get("url", None)
        icon_url = options.get("icon_url", None)
        self.footer = {
            "text": name,
            "url": url,
            "icon_url": icon_url
        }

    def set_image(self, url, height=None, width=None):
        self.image = {
            "url": url,
            "height": height,
            "width": width
        }
        return self

    def set_thumbnail(self, url, height=None, width=None):
        self.thumbnail = {
            "url": url,
            "height": height,
            "width": width
        }
        return self

    def set_video(self, url, height=None, width=None):
        self.video = {
            "url": url,
            "height": height,
            "width": width
        }
        return self
