import re

class FraudKeywordDetector:
    def __init__(self):
        self.keyword_categories = {
            "Fraud": {
                "keywords": ["fraud", "embezzlement", "kickback", "forgery", "deception"],
                "color": "FFB6C1"  # Light Red
            },
            "Bribery": {
                "keywords": ["bribe", "bribery", "inducement", "payoff", "gratuity"],
                "color": "FFD580"  # Light Orange
            },
            "Compliance Violation": {
                "keywords": ["non-compliance", "violation", "penalty", "illegal", "non-adherence"],
                "color": "FFFF99"  # Light Yellow
            },
            "Contract Risk": {
                "keywords": ["breach", "termination", "lawsuit", "dispute", "settlement"],
                "color": "ADD8E6"  # Light Blue
            },
            "Financial Misconduct": {
                "keywords": ["misstatement", "false reporting", "concealment", "manipulation", "misrepresentation"],
                "color": "90EE90"  # Light Green
            },
            "Money Laundering": {
                "keywords": ["laundering", "shell company", "offshore account", "illicit transfer"],
                "color": "B2DFDB"  # Light Teal
            },
            "Corruption": {
                "keywords": ["corruption", "collusion", "favoritism", "nepotism"],
                "color": "E1BEE7"  # Light Violet
            }
        }

    def get_keywords_and_colors(self, selected_categories):
        keywords_colors = {}
        for category in selected_categories:
            data = self.keyword_categories.get(category)
            if data:
                for keyword in data["keywords"]:
                    keywords_colors[keyword.lower()] = data["color"]
        return keywords_colors
