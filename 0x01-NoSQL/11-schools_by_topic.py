#!/usr/bin/env python3
"""
Module to find schools by
topic in a MongoDB collection.
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic.
    """
    return list(mongo_collection.find({"topics": topic}))
