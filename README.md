# Doc splitting estimator for the Openai embedding model

_under construction_

When applying Openai embedding model `text-embedding-ada-002` to any textual content and storage them in vector database, there is a rate limit on token per min (TPM) and response per min (RPM) on all openai models (See below for some examples). 

|Model|TPM|RPM|
|:---:|:--:|:--:|
|gpt-3.5-turbo|90,000|3,500|
|gpt-3.5-turbo-16k|180,000|3,500|
|gpt-4|10,000|200|
|text-embedding-ada-002|1,000,000|3,000|

To avoid to hit the rate limit to prevent the embedding operation stalling, here is a simple python code snippets to help estimate how many docs will reach the rate limit of the TPM by apply the binary search algorithm.

### Pre-requisite
1. Prepare your own documentation in the designated folder
2. Define your personal configuration and load the config file in the function below:
```python
def get_config_path():
    cwd = os.getcwd()
    return os.path.join(cwd, "<YOUR_JSON_CONFIG_FILE>")
```

### Start to use the codes
1. Set up your dev env
   ```shell
   python -m venv myvenv
   source myvenv/bin/activate
   ```
2. Install requirement libraries 
    ```shell
    pip install -r requirements.txt
    ```
3. Run the codes
   ```shell
   python estimator.py
   ```


