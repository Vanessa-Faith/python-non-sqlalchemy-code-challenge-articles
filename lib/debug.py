#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")
    
    # Create sample instances for testing
    author1 = Author("Carry Bradshaw")
    author2 = Author("Nathaniel Hawthorne")
    
    magazine1 = Magazine("Vogue", "Fashion")
    magazine2 = Magazine("AD", "Architecture")
    
    article1 = Article(author1, magazine1, "How to wear a tutu with style")
    article2 = Article(author1, magazine2, "2023 Eccentric Design Trends")
    article3 = author1.add_article(magazine2, "Carrara Marble is so 2020")
    
    print("\nSample data created!")
    print(f"Author 1: {author1.name}")
    print(f"Author 1 articles: {[a.title for a in author1.articles()]}")
    print(f"Author 1 magazines: {[m.name for m in author1.magazines()]}")
    print(f"Author 1 topic areas: {author1.topic_areas()}")
    
    print(f"\nMagazine 1: {magazine1.name}")
    print(f"Magazine 1 articles: {magazine1.article_titles()}")
    print(f"Magazine 1 contributors: {[a.name for a in magazine1.contributors()]}")

    # don't remove this line, it's for debugging!
    ipdb.set_trace()

