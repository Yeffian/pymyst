class Edit:
    def __init__(self, title, is_private, is_public, tags, pasties):
        self.title = title
        self.is_private = is_private
        self.is_public = is_public
        self.tags = tags

    def to_json(self):
        obj = {}

        if self.title is not None:
            obj['title'] = self.title
        
        if self.is_private is not None:
            obj['isPrivate'] = self.is_private
        
        if self.is_public is not None:
            obj['isPublic'] = self.is_public
        
        if self.tags is not None:
            obj['tags'] = self.tags

        return obj