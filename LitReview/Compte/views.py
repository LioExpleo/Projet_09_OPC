from django.shortcuts import render




from django.http import HttpResponse




# Create your views here.
def hello_compte(request):
    #ticket=LitReview.Compte.models.Ticket

    return HttpResponse('<h1>Hello LitReview compte!</h1>')

'''
def createUser(request):
    userName = request.REQUEST.get('username', None)
    userPass = request.REQUEST.get('password', None)
    userMail = request.REQUEST.get('email', None)

    # TODO: check if already existed

    **user = User.objects.create_user(userName, userMail, userPass)**
    user.save()

    return render_to_response('home.html', context_instance=RequestContext(request))
'''
