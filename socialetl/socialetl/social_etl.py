import logging
import os
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta
from typing import Callable, List, Tuple

import praw
import tweepy
from dotenv import load_dotenv
from metadata import log_metadata
from utils.db import DatabaseConnection

load_dotenv()

@dataclass
class RedditPostData:
    """Dataclass to hold reddit post data.

    Args:
        title (str): Title of the reddit post.
        score (int): Score of the reddit post.
        url (str): URL of the reddit post.
        comms_num (int): Number of comments on the reddit post.
        created (str): Datetime (string repr) of when the reddit
             post was created.
    """

    title: str
    score: int
    url: str
    comms_num: int
    created: str
    text: str

@dataclass
class TwitterTweetData:
    """Dataclass to hold twitter post data.

    Args:
        text (str): Text of the twitter post.
    """

    text: str

@dataclass
class SocialMediaData:
    """Dataclass to hold social media data.

    Args:
        id (str): ID of the social media post.
        text (str): Text of the social media post.
    """

    id: str
    source: str
    social_data: RedditPostData | TwitterTweetData
