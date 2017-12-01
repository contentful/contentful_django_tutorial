# Django Blog Demo

Simple Django and Contentful Application.
This application is for Demo purposes.

[Contentful](https://www.contentful.com) provides a content infrastructure for digital teams to power content in websites, apps, and devices. Unlike a CMS, Contentful was built to integrate with the modern software stack. It offers a central hub for structured content, powerful management and delivery APIs, and a customizable web app that enable developers and content creators to ship digital products faster.

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
