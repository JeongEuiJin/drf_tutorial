from django.contrib.auth import get_user_model
from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

User = get_user_model()

class Snippet(models.Model):
    owner = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    highlighted = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        # linenos = self.linenos and 'table' or False
        linenos = 'table' if self.linenos else False
        options = {'title':self.title} if self.title else {}
        formatter = HtmlFormatter(
            style = self.style,
            linenos=linenos,
            full=True,
            **options,
        )
        self.highlighted = highlight(self.code , lexer, formatter)
        super().save(*args,**kwargs)