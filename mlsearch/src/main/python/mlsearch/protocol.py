class Protocol():
    """The Protocol for standard communication accross different api sources."""

    def __init__(self, kwargs):
        param_list = [
            
            # title -> paper_title, full_name, name
            # description -> paper_abstract, description

            # Paper with code
            'title',
            'paper_published', 'paper_url',
            'num_of_implementations', 'tasks',
            'paper_conference', 'repository_url',
            'repository_name', 'repository_framework',
            'repository_stars',
            
            # Github
            'description', 'private',
            'fork', 'updated_at',
            'stargazers_count', 'watchers_count',
            'language', 'forks_count',
            
            # Coursera
            'partners_v1', 'instructors_v1',
            
            # Source Flag
            'source'
        ]
        
        for param in kwargs:
            if param not in param_list:
                raise AttributeError('{} is not a valid parameter.'.format(param))
        
        self.title = kwargs.get('title', None)
        self.paper_published = kwargs.get('paper_published', None)
        self.paper_url = kwargs.get('paper_url', None)
        self.num_of_implementations = kwargs.get('num_of_implementations', None)
        self.tasks = kwargs.get('tasks', None)
        self.paper_conference = kwargs.get('paper_conference', None)
        self.repository_framework = kwargs.get('repository_framework', None)
        self.repository_stars = kwargs.get('repository_stars', None)
        self.description = kwargs.get('description', None)
        self.private = kwargs.get('private', None)
        self.fork = kwargs.get('fork', None)
        self.updated_at = kwargs.get('updated_at', None)
        self.stargazers_count = kwargs.get('stargazers', None)
        self.watchers_count = kwargs.get('watchers_count', None)
        self.language = kwargs.get('language', None)
        self.forks_count = kwargs.get('forks_count', None)
        self.partners_v1 = kwargs.get('partners_v1', None)
        self.instructors_v1 = kwargs.get('instructors_v1', None)
        self.source = kwargs.get('source', None)
    
    def to_JSON(self):
        """Transform the Protocol object to JSON object."""
        
        return self.__dict__
        
    def __repr__(self):
        return str(self.__dict__)