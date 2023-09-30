# Festival Wisher

The script checks the festival and sends email wishes to a group of users.

## Festivals are:-

- NewYear - [X]
- RepublicDay - [X]
- IndependenceDay - [X]
- GandhiJayanti - [X]
- Christmas - [X]

## How to run this script
###  Direct run

```bash 
python main.py
```

### Running with GitHub Actions

- Create an `actions.yml` file in the `.github/workflows` folder.

- Add the following script to actions.yml:
```bash
name: run main.py

on:
schedule:
    # - cron: '*/5 * * * *' # At every 5 minute
    # - cron: '0 8 * * *' # At every 8:00 AM
    # - cron: '29 2 * * *' # At Utc 02:29 AM is indian time  of 7:59 AM
    - cron: '30 18 * * *' # At UTC 06:30 PM, which corresponds to 12:00 AM Indian Time

jobs:
build:
    runs-on: ubuntu-latest
    steps:

    - name: checkout repo content
        uses: actions/checkout@v2 # checkout the repository content to github runner

    - name: setup python
        uses: actions/setup-python@v4
        with:
        python-version: '3.9' # install the python version needed
        
    - name: install python packages
        run: |
        python -m pip install --upgrade pip
        
    - name: execute py script # run main.py
        env:
        SENDER_EMAIL: ${{ secrets.SENDER_EMAIL }}
        PASSWORD: ${{ secrets.PASSWORD }}

        run: python main.py
```

- Add your `SENDER_EMAIL` and `PASSWORD` in the secrets of GitHub.
