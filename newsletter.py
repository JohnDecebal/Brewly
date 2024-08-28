from app.models import ArticleSummary

def generate_newsletter():
    articles = ArticleSummary.query.order_by(ArticleSummary.created_at.desc()).limit(5).all()
    newsletter_content = "Today's Coffee News\n\n"
    for article in articles:
        newsletter_content += f"{article.title}\n{article.content}\nSource: {article.source}\n\n"
    return newsletter_content