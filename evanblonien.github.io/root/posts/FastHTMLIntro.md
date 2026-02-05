---
title: "FastHTML Tutorial" 
description: "How to use fastHTML as a beginner"
author: "Evan" 
date: "2026-01-14"
categories: ["Blog", "Getting Started", Intro]
image: "https://picsum.photos/400/200?random=11"
---

# Introduction 

FastHTML is a package that allows the user to write front end code only in python. This works by combining some of the front end framworks like Uvicorn and HTMX to bypass some of the complexity of creating a simple webpage. 

# How it should be used

FastHTML is not intended to be a replacement for front end coding, but rather for python users to easily create a working 'demo' version of their code that looks more visually appearing than the terminal

# Getting started

1. The first step is to install the required package. To do this, type into the terminal 
`uv pip install python-fasthtml`
1. (Optional) Fasthtml automatically uses PicoCSS, but there is a better looking package that can be installed called monsterUI. To install it type into the terminal 
`uv pip install python-fasthtml`

# Creating a basic webpage
Here is the most simple version of a webage using fasthtml

```
from fasthtml.common import *
rt, app = fast_app()
@rt('/')
def get(): 
    return(
        H1("hello world")
    )
serve() 
```

# What to do next
FastHtml, especially as a new concept, can be a bit difficult to understand initially and will require a lot of iterations and applications to get the hang of it. Some of the easiest/most useful projects to start off with are a blog. The best resource that I have come across so far has been the monsterUI documentations `https://monsterui.answer.ai/tutorial_app`

