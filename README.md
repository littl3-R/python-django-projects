
# Table of Contents

1.  [Intro](#orgbb52650)
2.  [set-up the environment](#org12f1833)
    1.  [test it](#orgf3a57dc)
    2.  [installing some packages](#org0d814ba)
3.  [startproject](#orgcb798c5)



<a id="orgbb52650"></a>

# Intro

Setting up the project

1.  download and install **python**
2.  create a **virtual environment**
3.  install **django**


<a id="org12f1833"></a>

# set-up the environment

    pyenv install --list
    # choose the python version
    pyenv install 3.10.2 # this install the python version
    pyenv virtualenv 3.10.2 udepython

then create a file **.python-version**
`~/udemy/.python-version`

    cat ../.python-version


<a id="orgf3a57dc"></a>

## test it

in the same path

    django-admin
    python --version


<a id="org0d814ba"></a>

## installing some packages

    pip install django black autopep8


<a id="orgcb798c5"></a>

# startproject

    django-admin startproject mypage

