from utils import SCORES_TEMPLATE
from flask import render_template
from score import Score


class MainScores:

    @staticmethod
    def score_server():
        score = Score(None).get_scores_dict()
        return render_template(SCORES_TEMPLATE, scores=score)




