from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from  account.models import Profile
from .models import PersonalChat
def chat(request):

    template = 'chat.html'

    return render(request, template_name=template)




def room(request, room_name):


    return render(request, 'room.html', {'room_name': room_name})


def friend_list(request):

    friends = Profile.objects.all()

    context = {
        'friends': friends,
    }

    return render(request, 'chat/friends.html', context=context)



def get_or_create_partner(user1,user2):
    try:
        partner=PersonalChat.objects.get(user1=user1, user2=user2.user)
    except PersonalChat.DoesNotExist:
        try:

            partner=PersonalChat.objects.get(user1=user2.user, user2=user1)

        except PersonalChat.DoesNotExist:

            partner=PersonalChat(
                user1=user1,
                user2=user2.user
            )
            partner.save()
    return partner


@login_required
def personal_chat(request, id):

    user1 = request.user
    user2 = User.objects.get(id=id)
  
    print('user1.............',user1)
    print('user2.............',user2)
    friends = Profile.objects.all()
    profile = Profile.objects.get(user=request.user)

    partner = get_or_create_partner(user1,user2)

    if partner:
        context = {
            'chatgroup':id,
            'groups_participated':friends,
            'profile':profile,
        }
        
        return render(request, 'chat/room.html', context=context)