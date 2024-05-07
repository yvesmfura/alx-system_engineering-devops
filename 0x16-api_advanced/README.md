# 0x16. API Advanced

## Description
This repository contains solutions to various tasks related to working with APIs, specifically focusing on the Reddit API. The tasks involve querying the Reddit API, parsing JSON responses, handling pagination, and performing operations such as counting occurrences of keywords in article titles.

## Background Context
API-related questions are common in technical interviews, making it essential to be comfortable with making API calls and parsing responses. The Reddit API offers a rich source of data and endpoints for practice, allowing individuals to gain familiarity with working with APIs.

## Resources
- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [Query String](https://en.wikipedia.org/wiki/Query_string)

## Learning Objectives
By completing the tasks in this project, participants are expected to achieve the following learning objectives:
- Understand how to read API documentation to find relevant endpoints
- Learn how to use an API with pagination to handle large datasets
- Gain experience in parsing JSON responses from an API
- Develop the ability to make recursive API calls for fetching multiple pages of data
- Learn how to sort a dictionary by value


## Requirements
### General
- Allowed editors: vi, vim, emacs
- All files should be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
- Files should end with a new line
- The first line of all files should be `#!/usr/bin/python3`
- Imported libraries should be organized alphabetically
- A `README.md` file at the root of the project folder is mandatory
- Code should adhere to the PEP 8 style guide
- All files must be executable
- File lengths will be tested using `wc`
- All modules should include documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- Requests module should be used for sending HTTP requests to the Reddit API

## Tasks
### 0. How many subs?
Write a function that queries the Reddit API and returns the number of subscribers for a given subreddit. If an invalid subreddit is provided, the function should return 0.

### 1. Top Ten
Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

### 2. Recurse it!
Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.

### 3. Count it!
Write a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.

---
