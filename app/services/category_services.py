from app.models.category import Category
from app import db

def create_category(name, description):
    category = Category(name=name, description=description)
    db.session.add(category)
    db.session.commit()
    return category

def get_categories():
    return Category.query.all()

def get_category_by_id(category_id):
    return Category.query.get(category_id)

def update_category(category_id, name=None, description=None):
    category = Category.query.get(category_id)
    if category:
        if name:
            category.name = name
        if description:
            category.description = description
        db.session.commit()
    return category

def get_topics_by_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return None
    return category.topics
