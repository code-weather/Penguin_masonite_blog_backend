"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog

class BlogTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
    def run(self):
        Blog.create({"subject": "Food diet", "details": "Eating diet"})
        Blog.create({"subject": "Exercise", "details": "Staying physical"})
        Blog.create({"subject": "Lifestyle", "details": "Living your life"})