# Another WSGI framework

Allow you to make small WSGI apps in a simple manner. 


# How to Install

You just need to download and install python3 if you already haven't: http://python.org .

Clone this repo:
```
git clone https://github.com/kheeva/otus_python_fs_dz3_wsgi
```

For simple testing you may use python's uwsgi server:
```
pip install uwsgi
```

# How to use
Customize your settings in config.py

Customize your data models (under construction).

Customize your view funcs.

Put your templates in teplates/ dir.

# Testing

```
uwsgi --http :9090 --wsgi-file controller.py
```

Connect via broser to http://127.0.0.1/your_urls

# Project Goals

The code is written for educational purposes. Training courses: otus.ru)
