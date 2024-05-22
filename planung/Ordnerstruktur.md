turnier_manager/
│
├── app/
│   ├── __init__.py
│   ├── extensions.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── event.py
│   │   ├── participant.py
│   │   ├── competition.py
│   │   ├── judge.py
│   │   └── result.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── main_routes.py
│   │   ├── event_routes.py
│   │   ├── participant_routes.py
│   │   └── result_routes.py
│   ├── static/
│   │   ├── css/
│   │   │   └── tailwind.css
│   │   ├── js/
│   │   │   └── flowbite.js
│   │   └── img/
│   ├── templates/
│   │   ├── main/
│   │   │   ├── index.html
│   │   │   ├── layout.html
│   │   └── events/
│   │       ├── event_list.html
│   │       ├── event_detail.html
│   │   └── participants/
│   │       ├── participant_list.html
│   │       ├── participant_detail.html
│   │   └── results/
│   │       ├── result_list.html
│   │       ├── result_detail.html
│   ├── data/
│       ├── migrations/
│       └── database.db
│
├── .env
├── .gitignore
├── config.py
├── requirements.txt
├── run.py
└── tailwind.config.js
