#!/usr/bin/env python
# coding: utf8
import sys
import re
import os
from stopword_list import stopwords


class TextCleaner:
    punc = '''!()-[]{.};:'"\,<>/?@#$%^&*_~`|’“”…—–'''
    # removed_plus = stopwords

    @classmethod
    def run(cls, text: str) -> list:
        """
            run textCleaner for input string
        Args:
            text (str): input string
        Returns:
            list: token list
        """
        return cls.tokenize(cls.normlize(text))

    @classmethod
    def tokenize(cls, text: str) -> list:
        """
            tokenize, delete eng stopwords
        Args:
            text (str): input string
        Returns:
            list: tokens
        """
        # stop_words = cls.removed_plus
        stop_words = list()
        tokens = text.split()
        return [token.strip() for token in tokens if token.strip() and token.strip() not in stop_words]

    @classmethod
    def normlize(cls, text: str) -> str:
        """
            lower, delete numbers, delete punc, strip
        Args:
            text (str): input string
        Returns:
            str: normlized string
        """
        text = text.lower()
        text = re.sub(r"\d+", '', text)

        for each in cls.punc:
            text = text.replace(each, " ")

        text.strip()

        return text


if __name__ == "__main__":
    """
    mapper
    """

    text_cleaner = TextCleaner()

    for line in sys.stdin:
        words = text_cleaner.run(line)
        for word in words:
            print('%s\t%s' % (word, 1))