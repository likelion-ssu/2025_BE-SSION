from django.http import HttpResponse

def mainPage(request):
    return HttpResponse("""
        <h1>INSTAGRAM</h1>
        <ul>
            <li><a href="/user/">USER</a></li>
            <li><a href="/article/">ARTICLE</a></li>
            <li><a href="/following/">FOLLOWING</a></li>
        </ul>
    """)