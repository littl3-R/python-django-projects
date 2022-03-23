
# Table of Contents

1.  [Intro](#orgf91c775)
2.  [set-up the environment](#org8133e44)
    1.  [test it](#org4182a33)
    2.  [installing some packages](#org4504ea4)
3.  [startproject](#orgceec2e7)
4.  [More on the Django Template Language (DTL)](#org5b8c2f8)
5.  [Building Static URLs Dynamically](#org49ebdbb)



<a id="orgf91c775"></a>

# Intro

Setting up the project

1.  download and install **python**
2.  create a **virtual environment**
3.  install **django**


<a id="org8133e44"></a>

# set-up the environment

    pyenv install --list
    # choose the python version
    pyenv install 3.10.2 # this install the python version
    pyenv virtualenv 3.10.2 udepython

then create a file **.python-version**
`~/udemy/.python-version`

    cat ../.python-version


<a id="org4182a33"></a>

## test it

in the same path

    django-admin
    python --version


<a id="org4504ea4"></a>

## installing some packages

    pip install django black autopep8


<a id="orgceec2e7"></a>

# startproject

    django-admin startproject mypage


<a id="org5b8c2f8"></a>

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


<a id="org49ebdbb"></a>

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

