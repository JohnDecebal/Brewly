from flask import Blueprint, jsonify
from .models import ArticleSummary

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify({"message": "Welcome to the Specialty Coffee Newsletter System"})

@main.route('/articles')
def get_articles():
    articles = ArticleSummary.query.order_by(ArticleSummary.created_at.desc()).limit(5).all()
    return jsonify([
        {
            "title": article.title,
            "content": article.content,
            "source": article.source,
            "url": article.url,
            "created_at": article.created_at.isoformat()
        } for article in articles
    ])