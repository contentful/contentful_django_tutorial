# Creating your own Contentful and Django Application

## Create your Django application

Create a Django application by running:

```bash
django-admin startproject YOUR_PROJECT_NAME
```

## Add Contentful to your project dependencies

On your project's `requirements.txt` add:

```
contentful
```

## Ways to include Contentful in your project:

### Contentful client within your views

Personally, I prefer initializing the Contentful Client within the `models.py` file, as you can see [here](./frontend/models.py). But this initialization
can be done wherever you think it's better for your understanding.

With the client now initialized, you can use it within your views, as you can see [here](./frontend/views.py).

For looking deeper into how to use the client, please refer to our [documentation](https://www.contentful.com/developers/docs/python/).

## How to use Contentful Entries in Templates

You can check how we use them in our example application [here](./frontend/templates/posts/all.html) and [here](./frontend/templates/posts/post.html).

## This is just the beggining

This is just a very simple tutorial to get things running, but every project has different needs, and we want to provide you
with the best solutions we can.

## Providing Feedback

If you want to provide feedback or improve this tutorial, feel free to submit a Pull Request.

