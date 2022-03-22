
# Table of Contents

1.  [Intro](#org8bd0157)
2.  [set-up the environment](#org71887cb)
    1.  [test it](#orgb2f88b8)
    2.  [installing some packages](#orgc064ab5)
3.  [startproject](#org5a466dc)



<a id="org8bd0157"></a>

# Intro

Setting up the project

1.  installing **django**
2.  create a **virtual enviroment**
3.  download and install **python**

    python --version

    django-admin


<a id="org71887cb"></a>

# set-up the environment

    pyenv install --list
    # choose the python version
    pyenv install 3.10.2 # this install the python version
    pyenv virtualenv 3.10.2 udepython

then create a file **.python-version**
`~/udemy/.python-version`

    cat ../.python-version


<a id="orgb2f88b8"></a>

## test it

in the same path

    django-admin
    python --version


<a id="orgc064ab5"></a>

## installing some packages

    pip install django black autopep8


<a id="org5a466dc"></a>

# startproject

    django-admin startproject mypage

