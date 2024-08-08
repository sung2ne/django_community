from django import forms
from django.utils.safestring import SafeString
from board.models import Board

# 등록
class CreateForm(forms.ModelForm):
    """
    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            
    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='mb-3'>"))
    """
    
    class Meta:
        model = Board
        fields = ["title", "content"]
        labels = {
            "title": "제목",
            "content": "내용",
        }