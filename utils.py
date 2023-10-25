import os
import json

from langchain.document_loaders.csv_loader import CSVLoader

def get_config_path():
    cwd = os.getcwd()
    return os.path.join(cwd, "<YOUR_JSON_CONFIG_FILE>")

class ConfigLoader:

    def __init__(self):
        self.config_path = get_config_path()
        with open(self.config_path) as f:
            self.configs = json.loads(f.read())

    def load_embedding_config(self):
        openai_api_key = self.configs['openai']['api_key']
        openai_embedding_model = self.configs['openai']['embedding_model']
        max_token_per_min = self.configs['openai']["max_token_per_min"]
        token_range_bottom = self.configs['openai']["token_range_bottom"]
        token_range_top = self.configs['openai']["token_range_top"]
        encoding_name = self.configs['openai']['encoding_name']
        return openai_api_key, openai_embedding_model, max_token_per_min, \
            token_range_bottom, token_range_top, encoding_name
    
    def load_token_estiamtor_config(self):
        return self.configs["token_estimator"]['encoding_name']
    
    def load_data_config(self):
        return self.configs['data']['directory']
    
    def load_splitting_config(self):
        chunk_size = self.configs["splitting_parameters"]['chunk_size']
        chunk_overlap = self.configs["splitting_parameters"]['chunk_overlap']
        return chunk_size, chunk_overlap
    
class Configs(ConfigLoader):

    def __init__(self):
        super().__init__()
        self.OPENAI_API_KEY, self.OPENAI_EMBEDDING_MODEL, self.MAX_TOKEN_PER_MIN, \
            self.TOKEN_RANGE_BOTTOM, self.TOKEN_RANGE_TOP, self.ENCODING_NAME \
                = self.load_embedding_config()
        self.TOKEN_ESTIMATOR = self.load_token_estiamtor_config()
        self.DATA_DIRECTORY = self.load_data_config()
        self.CHUNK_SIZE, self.CHUNK_OVERLAP = self.load_splitting_config()

class DataLoader(Configs):

    def _init__(self):
        super().__init__()

    def load_csv(self):
        return CSVLoader(self.DATA_DIRECTORY)
    
    