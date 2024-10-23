# Astron SD day 2024 Tamagotchi Edition

## 1. Context

The Astron Software Delivery Group has a new mascot: McFloofz. He is very needy and needs constant attention to his health. Therefore, this simple dashboard was created to play with him, feed him, and monitor his health. However, a secret stakeholder is not very fond of dogs. They want *you* to make the existing code less maintainable by making it *worse*. Follow steps 2 and 3 to start your journey thwarting the well being of McFloofz.


## 2. Setup

1. Clone this repo 
2. From the repo root, change directory to `sd_mascot`:
    - `cd sd_mascot`
3. Create a virtual env of your choosing, or let your favourite IDE do it for you:
    - `python3 -m venv .venv`
4. Activate the virtual env:
    - `source .venv/bin/activate`
5. Install dependencies: 
    - `pip install -r requirements.txt`
6. Run the server:
    - `python manage.py runserver`
7. Point your favourite browser to http://127.0.0.1:8000/
8. Run tests (if you wish):
    - `pytest`

## 3. Rules

* Before you start makes changing, create a branch name as follows: `branch-$teamname`
* Changes pushed to your branch will be analyzed with Sonarqube. Only Python code in the `pet` folder will be analyzed (HTML and CSS are excluded). Analysis results are visible [here](https://sonarcloud.io/project/overview?id=diggingforfire-github_sd-day-2024-tamagotchi-edition).
* For inspiration, [this ruleset with Python rules](https://sonarcloud.io/organizations/diggingforfire-github/rules?qprofile=AVzwrtCqgIkbjTX1x8Iv&activation=true) will be used for analysis. Try to implement as many rule violations as you can without breaking the existing tests. Gotta catch em all!
* All existing tests cannot be changed and they must pass. Beyond this, feel free to make any changes!
* Two examples to get you started:
    - 1: In `models.py` on line 64, change `100` to `100.0`. This will be produce the issue [Floating point numbers should not be tested for equality](https://sonarcloud.io/organizations/diggingforfire-github/rules?activation=true&open=python%3AS1244&q=floating&qprofile=AVzwrtCqgIkbjTX1x8Iv&tab=how_to_fix).
    - 2: In `views.py` on line 27, add `sd_mascot().feed()`. This will produce the issue [All code should be reachable](https://sonarcloud.io/organizations/diggingforfire-github/rules?activation=true&open=python%3AS1763&qprofile=AVzwrtCqgIkbjTX1x8Iv).