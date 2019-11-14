from mlsearch.config import Config
from mlsearch.protocol import Protocol
from github import Github
import json
# import scholarly

try:
    from botocore.vendored import requests
    from botocore.vendored.requests.auth import HTTPBasicAuth
except ModuleNotFoundError:
    import requests
    from requests.auth import HTTPBasicAuth


class APIRequest():
    """For handling the different Valid API requests."""

    def __init__(self, source, query, init_idx, count):
        """
        Initialization for the class.

        :param  source:     The API request destination.
        :param  query:      The query for searching.
        :param  init_idx:   The initial pagination index.
        :param  count:      The number of records to be fetched.
        """

        self.params = {'query':query, 'init_idx':init_idx, 
                            'count':count, 'source': source}
        self.params_model = {'query':str, 'init_idx':int, 
                                  'count':int}
        # Load the configuration file
        self._config = Config
        # Validate Params
        self._validate_params()
        # Response data
        self.data = {'response_code': 201, 'content': None}

    @property
    def github_acc_token(self):
        return self._config.GITHUB_ACC_TOKEN

    @github_acc_token.setter
    def github_acc_token(self, access_token):
        if access_token:
            self._config.GITHUB_ACC_TOKEN = access_token


    @property
    def pwc_auth_info(self):
        return (self._config.PWC_USER_NAME, self._config.PWC_PASSWORD)

    @pwc_auth_info.setter
    def pwc_auth_info(self, auth_info: "tuple(user_name, password)"):
        assert isinstance(auth_info, tuple), \
           f"Invalid type for auth_info. Expected tuple but got {type(auth_info)}." 
        if len(auth_info) == 2:
            assert isinstance(auth_info[0], str), \
                f"Invalid type for user_name. Expected str but got {type(auth_info[0])}."
            assert isinstance(auth_info[1], str), \
                f"Invalid type for password. Expected str but got {type(auth_info[1])}."
            self._config.PWC_USER_NAME = auth_info[0]
            self._config.PWC_PASSWORD = auth_info[1]
        else:
            raise AttributeError(f"Expected tuple with length 2 but got {len(auth_info)}.")

    def _validate_params(self):
        """Validate user input data."""

        for item, typ in self.params_model.items():
            if item in self.params.keys():
                if not typ == type(self.params[item]):
                    raise TypeError(
                        f'Invalid type for {item}. {typ} is expected but ' 
                        f'{type(self.params[item])} is given.')

        if self.params['source'] not in self._config.VALID_API_SOURCE:
            raise ValueError(
                f"Invalid value for {self.params['source']}. "
                f"Expected values are {self._config.VALID_API_SOURCE}")
                
    def _fetch_github(self) -> [Protocol]:
        """Fetch Github Repository"""

        github = Github(self._config.GITHUB_ACC_TOKEN)
        query = '+'.join([self.params['query'], self._config.GITHUB_URL])
        responses = github.search_repositories(query, 'stars', 'desc')
        results = []

        for response in responses[
            self.params['init_idx']:self.params['init_idx'] + \
            self.params['count']]:

            data = {
                'repository_url' : response.clone_url.replace('.git', ''),
                'title' : response.name,
                'description' : response.description,
                'private' : response.private,
                'fork' : response.fork,
                'updated_at' : response.updated_at.strftime("%Y%m%dT%H:%M:%S"),
                'stargazers_count' : response.stargazers_count,
                'watchers_count' : response.watchers_count,
                'language' : response.language,
                'forks_count' : response.forks_count,
                'source' : self.params.get('source', '')
            }
            results.append(Protocol(data))
            
            self.data['response_code'] = 200
            self.data['content'] = [proto.to_JSON() for proto in results]

    def _fetch_paperwithcode(self) -> [Protocol]:
        """Fetch Paper with Code Repository"""

        results = []
        url = f"{self._config.PWC_URL}{self.params['query']}"
        query_result = requests.get(url,
                                    auth=HTTPBasicAuth(self._config.PWC_USER_NAME,
                                    self._config.PWC_PASSWORD))

        if query_result.status_code == 200:
            content = json.loads(query_result.content)
            content = content[self.params['init_idx']:self.params['init_idx'] + \
                                self.params['count']]

            for item in content:
                data = {
                    'title': item.get('paper_title', None),
                    'description': item.get('paper_abstract', None),
                    'paper_url': item.get('paper_url', None),
                    'num_of_implementations': item.get('num_of_implementations', None),
                    'tasks': item.get('tasks', None),
                    'paper_conference': item.get('paper_conference', None),
                    'repository_url': item.get('repository_url', None),
                    'repository_name': item.get('repository_name', None),
                    'repository_framework': item.get('repository_framework', None),
                    'repository_stars': item.get('repository_stars', None),
                    'paper_published': item.get('paper_published', None),
                    'source': self.params.get('source', '')
                }
                results.append(Protocol(data))

            self.data['content'] = [proto.to_JSON() for proto in results]

        self.data['response_code'] = query_result.status_code
        
    def fetch_data(self) -> json:
        """Fetch the data from designated API source."""

        try:
            if self.params.get('source', '') == 'paperwithcode':
                self._fetch_paperwithcode()

            if self.params.get('source', '') == 'github':
                responses = self._fetch_github()

            # TODO: Implement the function for Coursera. However, this function
            # may be handled by the backend server.
            if self.params.get('source', '') == 'coursera':
                pass

        except Exception as ex:
            self.data['response_code'] = 500
            self.data['content'] = str(ex)

        return self.data