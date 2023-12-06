from django import forms
from ArticlePage.models import Article, Subtitle
from MainPage.models import Category, Subcategory

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['category', 'department', 'main_message', 'target_audience', 'title', 'content', 'image']

class SubtitleForm(forms.ModelForm):
    class Meta:
        model = Subtitle
        fields = ['title', 'text', 'image']
        
class ArticleFilterForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True, empty_label="Vyberte kategóriu")
    article = forms.ModelChoiceField(queryset=Article.objects.none(), required=True, empty_label="Vyberte článok")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['article'].queryset = Article.objects.filter(category_id=category_id).order_by('title')
            except (ValueError, TypeError):
                pass
            