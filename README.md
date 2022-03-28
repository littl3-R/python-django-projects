
# Table of Contents

1.  [Intro](#orgb3a643b)
2.  [set-up the environment](#org914cf89)
    1.  [test it](#org1f4a3ae)
    2.  [installing some packages](#org4c5749b)
3.  [startproject](#orged01392)
4.  [More on the Django Template Language (DTL)](#org7452d35)
5.  [Building Static URLs Dynamically](#orge61b74e)
6.  [Circular Relations & Lazy Relations](#orgfdc4f22)



<a id="orgb3a643b"></a>

# Intro

Setting up the project

1.  download and install **python**
2.  create a **virtual environment**
3.  install **django**


<a id="org914cf89"></a>

# set-up the environment

    pyenv install --list
    # choose the python version
    pyenv install 3.10.2 # this install the python version
    pyenv virtualenv 3.10.2 udepython

then create a file **.python-version**
`~/udemy/.python-version`

    cat ../.python-version


<a id="org1f4a3ae"></a>

## test it

in the same path

    django-admin
    python --version


<a id="org4c5749b"></a>

## installing some packages

    pip install django black autopep8


<a id="orged01392"></a>

# startproject

    django-admin startproject mypage


<a id="org7452d35"></a>

# More on the Django Template Language (DTL)

In this course, we're going to use the DTL (Django Template Language)
a lot - for example also in the big course project (the "Blog"
project).

You also saw all the key features in this module already.

There are three important additions, which you'll see later, but
which I want to introduce right now already:

Accessing Dictionary Fields in Templates When accessing dictionary
data in a template, you DON'T use this syntax:

    {{ myDictionary['some_key'] }}

Instead, you use the dot notation - as if it were a regular Python
object:

    {{ myDictionary.some_key }}

This might look strange, but keep in mind, that the DTL is a
custom-made language. It looks like Python, but ultimately it is NOT
Python - it's a language parsed and executed by Django. Hence, its
syntax can deviate - just as it does here.

Again, you'll see this in action later in the course!

Calling Functions in Templates Calling functions in templates also
works differently than it does in Python.

Instead of calling it, you use functions like regular variables or
properties.

I.e., instead of:

    {{ result_from_a_function() }}

you would use

    {{ result_from_a_function }}


<a id="orge61b74e"></a>

# Building Static URLs Dynamically

Later in the course, we'll see an example for a static URL, that is
built dynamically.

What do I mean with that?

Imagine, that you want to build a static URL where some part of the
URL (e.g. the filename) is actually stored in a variable that's
exposed to the template.

So you might want to build the URL like this:

    {% static "my_path/to/" + the_file %}

Here, "the<sub>file</sub>" would be a variable holding the actual filename.

The above code would fail.

Instead, you can use the "add" filter provided by Django to
construct this path dynamically:

    {% static "my_path/to/"|add:the_file %}


<a id="orgfdc4f22"></a>

# Circular Relations & Lazy Relations

Sometimes, you might have two models that depend on each other -
i.e. you end up with a circular relationship.

Or you have a model that has a relation with itself.

Or you have a model that should have a relation with some built-in
model (i.e. built into Django) or a model defined in another
application.

Below, you find examples for all three cases that include Django's
solution for these kinds of "problems": Lazy relationships. You can
also check out the official docs in addition.

1.  Two models that have a circular relationship

    class Product(models.Model):
    # ... other fields ...
    last_buyer = models.ForeignKey('User')
    
    class User(models.Model):
    # ... other fields ...
    created_products = models.ManyToManyField('Product')

In this example, we have multiple relationships between the same two
models. Hence we might need to define them in both models. By using
the model name as a string instead of a direct reference, Django is
able to resolve such dependencies.

1.  Relation with the same model

    class User(models.Model):
    # ... other fields ...
    friends = models.ManyToManyField('self') 

The special self keyword (used as a string value) tells Django that
it should form a relationship with (other) instances of the same
model.

1.  Relationships with other apps and their models (built-in or custom apps)

    class Review(models.Model):
    # ... other fields ...
    product = models.ForeignKey('store.Product') # '<appname>.<modelname>'

You can reference models defined in other Django apps (no matter if
created by you, via python manage.py startapp <appname> or if it's a
built-in or third-party app) by using the app name and then the name
of the model inside the app.

