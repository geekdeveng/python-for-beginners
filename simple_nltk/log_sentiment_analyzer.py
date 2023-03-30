"""
-author : geekdev
-desc : simple nltk
"""

import nltk

# vader -> download vocabulary list for use with SentimentIntensityAnalyzer.
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer


class SimpleNltk:
    """
    Simple Nltk
    """

    def __init__(self, keywords: tuple=tuple) -> None:
        """
        -desc           : init
        -param keywords : for sia analysis using keywords
        -return         : None
        """

        self.__keywords = keywords

    def get_sia_analysis(self, log_file: str=str) -> dict:
        """
        -desc           : Analysis results using vader -> SentimentIntensityAnalyzer.
                          Each line in the log file must be analyzed, and the compound value is the criterion for judgment.
        -param log_file : Log file path to read.
        -return         : Compound result count for all lines.
        """
        
        result: dict = {"negative_cnt": 0, "neutral_cnt": 0, "positive_cnt": 0}
        analyzer: SentimentIntensityAnalyzer = SentimentIntensityAnalyzer()

        with open(log_file, "r") as f:
            for line in f:
                line_result = analyzer.polarity_scores(line)
                if line_result["compound"] == 0:
                    result["neutral_cnt"] += 1
                elif line_result["compound"] > 0:
                    result["positive_cnt"] += 1
                elif line_result["compound"] < 0:
                    result["negative_cnt"] += 1

        return result
    
    def get_sia_analysis_using_keywords(self, log_file: str=str) -> dict:
        """
        -desc           : vader -> Analysis results using specific keywords in SentimentIntensityAnalyzer.
                          Each line in the log file matching the keywords must be analyzed, 
                          and the compound value is the criterion for judgment.
        -param log_file : Log file path to read.
        -return         : Compound result count for the line corresponding to the keyword among all lines.
        """
        
        result: dict = {"negative_cnt": 0, "neutral_cnt": 0, "positive_cnt": 0}
        analyzer: SentimentIntensityAnalyzer = SentimentIntensityAnalyzer()

        with open(log_file, "r") as f:
            for line in f:
                if any(keyword in line for keyword in self.__keywords):
                    line_result = analyzer.polarity_scores(line)
                    if line_result["compound"] == 0:
                        result["neutral_cnt"] += 1
                    elif line_result["compound"] > 0:
                        result["positive_cnt"] += 1
                    elif line_result["compound"] < 0:
                        result["negative_cnt"] += 1

        return result