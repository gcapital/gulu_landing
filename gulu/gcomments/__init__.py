from gcomments.models import GComment
from gcomments.forms import GCommentForm

def get_model():
    return GComment
    
def get_form():
    return GCommentForm