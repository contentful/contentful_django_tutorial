# Django Blog Demo

Simple Django and Contentful Application.
This application is for Demo purposes.

[Contentful](https://www.contentful.com) is a content management platform for web applications, mobile apps and connected devices.
It allows you to create, edit & manage content in the cloud and publish it anywhere via powerful API.
Contentful offers tools for managing editorial teams and enabling cooperation between organizations.

## Setup

* Install dependencies

```bash
pip install -r requirements.txt
```

* Run Server

```bash
python manage.py runserver
```

## Viewing Data

The project comes pre-loaded with a Read-Only Demo space.
You can view the content [here](http://localhost:8000)

## Using Custom Data

You can create your own Custom Data by following these steps:

> Ruby 1.9+ and Bundler are required for this step if you want to do it automatically.

* Install Contentful Bootstrap:

```bash
bundle install
```

* Create your space:

```bash
bundle exec contentful_bootstrap create_space django_demo -j bootstrap/template.json
```

After following the steps, the tool will provide you with a Space ID and Access Token. Then run the following commands replacing the values where they correspond:

```bash
export CTF_SPACE_ID=YOUR_SPACE_ID
export CTF_DELIVERY_KEY=YOUR_ACCESS_TOKEN
```

Then you can restart your application and use your own content.

To edit content, you can go to https://app.contentful.com and start editing.

## Tutorial

For a Tutorial on how to create your own Django Application using Contentful, you can read [here](./TUTORIAL.md)
